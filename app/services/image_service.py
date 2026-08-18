import os
from PIL import Image, ImageOps
import io

class ImageService:
    _session = None

    @classmethod
    def _get_session(cls):
        if cls._session is None:
            from rembg import new_session
            cls._session = new_session("isnet-general-use")
        return cls._session

    @staticmethod
    def remove_background(input_path, output_path):
        """
        Removes background with 'Balanced Elite' configuration.
        Initializes the engine on-demand for fast app startup.
        """
        from rembg import remove
        with open(input_path, 'rb') as i:
            input_data = i.read()
            # Balanced parameters to avoid eating into dark letters
            output_data = remove(
                input_data, 
                session=ImageService._get_session(),
                alpha_matting=True,
                alpha_matting_foreground_threshold=150,
                alpha_matting_background_threshold=20,
                alpha_matting_erode_size=5
            )
            with open(output_path, 'wb') as o:
                o.write(output_data)
        return output_path

    @staticmethod
    def generate_ico(input_path, output_path, sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]):
        """
        Generates a multi-resolution ICO file including 128x128.
        """
        img = Image.open(input_path)
        img.save(output_path, format='ICO', sizes=sizes)
        return output_path

    @staticmethod
    def crop_to_square(img):
        """
        Crops an image to a 1:1 aspect ratio, centered.
        """
        width, height = img.size
        if width == height:
            return img
        
        new_size = min(width, height)
        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2
        
        return img.crop((left, top, right, bottom))

    @staticmethod
    def trim_and_resize_to_fill(img, target_size=512, padding=0.05):
        """
        Trims transparency and resizes the drawing to fill the target_size square,
        leaving a small relative padding.
        """
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        bbox = img.getbbox()
        if not bbox:
            # Return a blank square if no drawing found
            return Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
            
        img_trimmed = img.crop(bbox)
        w, h = img_trimmed.size
        
        # Calculate scale to fit in (target_size * (1 - padding*2))
        max_dim = target_size * (1 - (padding * 2))
        scale = max_dim / max(w, h)
        
        new_w = int(w * scale)
        new_h = int(h * scale)
        
        img_resized = img_trimmed.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Create final canvas
        final_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
        paste_x = (target_size - new_w) // 2
        paste_y = (target_size - new_h) // 2
        
        final_img.paste(img_resized, (paste_x, paste_y), mask=img_resized)
        
        return final_img

    @staticmethod
    def generate_installer_bmps(input_path, project_paths):
        """
        Generates required BMPs for Inno Setup, NSIS, and WiX.
        """
        img = Image.open(input_path)
        if img.mode == 'RGBA':
            # Create a white background for BMPs as they don't support transparency well in these contexts
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background

        # Specs mapping: (width, height, path_key, filename)
        specs = [
            # Inno Setup
            (164, 314, "installers_inno", "wizard-image.bmp"),
            (58, 58, "installers_inno", "small-image.bmp"),
            # NSIS
            (164, 314, "installers_nsis", "welcome.bmp"),
            (150, 57, "installers_nsis", "header.bmp"),
            # WiX
            (493, 312, "installers_wix", "dialog.bmp"),
            (493, 58, "installers_wix", "banner.bmp")
        ]

        for w, h, path_key, filename in specs:
            target_path = os.path.join(project_paths[path_key], filename)
            
            # Use fit to avoid distortion, padding with white if necessary
            resized = ImageOps.pad(img, (w, h), color=(255, 255, 255), centering=(0.5, 0.5))
            
            # Save as 24-bit BMP
            resized.convert("RGB").save(target_path, "BMP")

    @staticmethod
    def save_base_logo(image_bytes, output_path):
        """
        Saves raw image bytes from API to a file.
        """
        img = Image.open(io.BytesIO(image_bytes))
        img.save(output_path, "PNG")
        return output_path

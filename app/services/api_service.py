import requests
from openai import OpenAI
import os

class APIService:
    def __init__(self, api_key, provider="grok"):
        self.client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
        self.image_model = "grok-imagine-image"
        self.text_model = "grok-2-1212" # Using grok-2-1212 for more stability

    def generate_text(self, system_prompt, user_prompt):
        """
        Generates text using Grok (useful for creating the branding concept).
        """
        response = self.client.chat.completions.create(
            model=self.text_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content

    def generate_image(self, prompt):
        """
        Calls Grok Imagine to generate an image.
        """
        # Grok requirements: 
        # - model: grok-imagine-image
        # - quality: low, medium, high
        # - size: NOT SUPPORTED as an argument
        params = {
            "model": self.image_model,
            "prompt": prompt,
            "quality": "medium",
            "n": 1,
        }

        response = self.client.images.generate(**params)
        
        image_url = response.data[0].url
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            return img_response.content
        else:
            raise Exception(f"Failed to download image: {img_response.status_code}")

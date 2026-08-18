# 03_04: Matemáticas y Algoritmos Clave - ABL Suit Favicon

## 📐 Algoritmo `trim_and_resize_to_fill`

```python
def trim_and_resize_to_fill(img, target_size=512, padding=0.05):
    # 1. Obtener Bounding Box de la zona no transparente (alpha > 0)
    bbox = img.getbbox()
    img_trimmed = img.crop(bbox)
    w, h = img_trimmed.size
    
    # 2. Calcular escala conservando aspecto
    max_dim = target_size * (1 - (padding * 2)) # 512 * 0.90 = 460.8px
    scale = max_dim / max(w, h)
    
    new_w = int(w * scale)
    new_h = int(h * scale)
    
    # 3. Redimensionar con filtro Lanczos antialias
    img_resized = img_trimmed.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # 4. Centrar en lienzo final de 512x512
    final_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
    paste_x = (target_size - new_w) // 2
    paste_y = (target_size - new_h) // 2
    final_img.paste(img_resized, (paste_x, paste_y), mask=img_resized)
    return final_img
```

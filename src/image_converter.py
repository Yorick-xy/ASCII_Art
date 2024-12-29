from PIL import Image, ImageDraw, ImageFont
from tkinter import messagebox

ASCII_CHARS = " .:-=+*#%@"

def resize_image(image, new_width=100):
    """Redimensionne l'image tout en maintenant le ratio largeur/hauteur"""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Ajustement pour l'affichage ASCII
    return image.resize((new_width, new_height))

def grayscale(image):
    """Convertit l'image en niveaux de gris"""
    return image.convert("L")

def pixels_to_ascii(image):
    """Convertit chaque pixel en un caractère ASCII basé sur sa luminosité"""
    pixels = image.getdata()
    interval = 256 // len(ASCII_CHARS)
    ascii_str = "".join([ASCII_CHARS[min(pixel // interval, len(ASCII_CHARS) - 1)] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Transforme une image en art ASCII"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'ouvrir l'image : {e}")
        return None

    image = resize_image(image, new_width)
    image = grayscale(image)
    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_image = "\n".join([ascii_str[i:i + new_width] for i in range(0, pixel_count, new_width)])
    return ascii_image
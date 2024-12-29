import tkinter as tk
from tkinter import filedialog, messagebox
from src.image_converter import image_to_ascii

def browse_image():
    """Ouvre une boîte de dialogue pour sélectionner une image"""
    global image_path
    image_path = filedialog.askopenfilename(
        title="Sélectionnez une image",
        filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.tiff *.gif"), ("Tous les fichiers", "*.*")]
    )
    if image_path:
        image_label.config(text=f"Image sélectionnée : {image_path}")
    else:
        image_label.config(text="Aucune image sélectionnée.")

def generate_ascii():
    """Génère l'ASCII à partir de l'image sélectionnée"""
    if not image_path:
        messagebox.showerror("Erreur", "Veuillez sélectionner une image.")
        return

    try:
        new_width = int(width_entry.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une largeur valide.")
        return

    ascii_art = image_to_ascii(image_path, new_width)
    if ascii_art:
        ascii_text.delete(1.0, tk.END)
        ascii_text.insert(tk.END, ascii_art)

def create_gui():
    """Crée l'interface graphique"""
    root = tk.Tk()
    root.title("Convertisseur Image en ASCII")

    # Variables globales
    global image_path
    image_path = ""

    # Bouton pour sélectionner une image
    browse_button = tk.Button(root, text="Choisir une image", command=browse_image)
    browse_button.pack(pady=10)

    # Label pour afficher le chemin de l'image sélectionnée
    global image_label
    image_label = tk.Label(root, text="Aucune image sélectionnée.", wraplength=400, justify="center")
    image_label.pack(pady=5)

    # Champ pour entrer la largeur
    width_frame = tk.Frame(root)
    width_frame.pack(pady=10)

    width_label = tk.Label(width_frame, text="Largeur :")
    width_label.pack(side="left", padx=5)

    global width_entry
    width_entry = tk.Entry(width_frame, width=10)
    width_entry.insert(0, "200")  # Largeur par défaut
    width_entry.pack(side="left", padx=5)

    # Bouton pour générer l'ASCII
    generate_button = tk.Button(root, text="Générer l'ASCII", command=generate_ascii)
    generate_button.pack(pady=10)

    # Zone de texte pour afficher l'art ASCII, inversée (fond noir, texte blanc)
    global ascii_text
    ascii_text = tk.Text(root, wrap="none", bg="black", fg="white")
    ascii_text.pack(fill="both", expand=True, padx=10, pady=10)

    return root
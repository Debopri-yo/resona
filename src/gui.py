import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from api_fetcher import fetch_artist_info

def display_artist_info():
    artist_name = entry.get().strip()

    if not artist_name:
        bio_text.delete("1.0", tk.END)
        bio_text.insert(tk.END, "Please enter an artist name.")
        image_label.config(image='', text="")
        return

    info = fetch_artist_info(artist_name)

    # Clear previous content first
    bio_text.delete("1.0", tk.END)
    image_label.config(image='', text="")

    if info:
        bio_text.insert(tk.END, info['bio'])

        PLACEHOLDER_URL = "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png"

        # Make sure the image URL is not empty, None, or placeholder
        if info['image_url'] and info['image_url'].strip() != "" and info['image_url'] != PLACEHOLDER_URL:
            print("Image URL:", info['image_url'])
            try:
                img_data = requests.get(info['image_url']).content
                img = Image.open(BytesIO(img_data))
                img = img.resize((300, 300))
                photo = ImageTk.PhotoImage(img)

                image_label.config(image=photo)
                image_label.image = photo
            except Exception as e:
                print(f"Error loading image: {e}")
                bio_text.insert(tk.END, "\n[Image could not be loaded]")
        else:
            bio_text.insert(tk.END, "\n[No artist image available]")
    else:
        bio_text.insert(tk.END, "Could not retrieve artist info. Try a different name.")

# ✅ Define root BEFORE mainloop
root = tk.Tk()
root.title("Resona - Artist Info")
root.geometry("600x600")

# Input
entry = ttk.Entry(root, width=40)
entry.pack(pady=10)

btn = ttk.Button(root, text="Fetch Info", command=display_artist_info)
btn.pack()

# Image
image_label = ttk.Label(root)
image_label.pack(pady=10)

# Bio
bio_text = tk.Text(root, height=10, wrap='word')
bio_text.pack(pady=10, fill='both', expand=True)

print("Launching GUI...")
root.mainloop()


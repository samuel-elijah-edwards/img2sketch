import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageSketchConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Sketch Converter")

        self.original_image_label = tk.Label(root, text="Original Image")
        self.original_image_label.pack(pady=10)

        self.sketch_image_label = tk.Label(root, text="Sketch Image")
        self.sketch_image_label.pack(pady=10)

        self.label_selected_image = tk.Label(root, text="Selected Image:")
        self.label_selected_image.pack(pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, state="readonly", width=40)
        self.entry.pack(pady=5)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.process_button = tk.Button(root, text="Process Image", command=self.process_image)
        self.process_button.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_image)
        self.clear_button.pack(pady=10)

        self.original_photo = None
        self.sketch_photo = None

    def browse_file(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            self.entry_var.set(file_path)
            self.load_original_image(file_path)
        else:
            print("No file selected.")

    def load_original_image(self, image_path):
        original_image = Image.open(image_path)
        original_image.thumbnail((300, 300))
        self.original_photo = ImageTk.PhotoImage(original_image)
        self.original_image_label.config(image=self.original_photo)
        self.original_image_label.image = self.original_photo

    def process_image(self):
        image_path = self.entry_var.get()

        if image_path:
            image_type = Image.open(image_path).format
            image = cv2.imread(image_path)

            gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            inverted = 255 - gray_image
            blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
            invertedBlur = 255 - blurred
            pencilsketch = cv2.divide(gray_image, invertedBlur, scale=256.0)

            # Specify the file extension in the output path
            output_path = "assets/sketch." + image_type.lower()
            cv2.imwrite(output_path, pencilsketch)
            print(f"Sketch saved to {output_path}")

            self.load_sketch_image(output_path)
        else:
            print("No file selected.")

    def load_sketch_image(self, sketch_path):
        sketch_image = Image.open(sketch_path)
        sketch_image.thumbnail((300, 300))
        self.sketch_photo = ImageTk.PhotoImage(sketch_image)
        self.sketch_image_label.config(image=self.sketch_photo)
        self.sketch_image_label.image = self.sketch_photo

    def clear_image(self):
        self.entry_var.set("")
        self.original_image_label.config(image="")
        self.sketch_image_label.config(image="")
        print("Cleared the selected image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSketchConverter(root)
    root.mainloop()

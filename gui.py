import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Crop Maturity Prediction")
        self.master.geometry("500x550")

        # Create a button to open the file dialog
        self.button = tk.Button(self.master, text="Select Image", command=self.open_file)
        self.button.pack()

        # Create a canvas to display the selected image
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        # Create a Checkbutton to toggle the prediction
        self.checkbutton_var = tk.BooleanVar()
        self.checkbutton = tk.Checkbutton(self.master, text="Predict maturity", variable=self.checkbutton_var)
        self.checkbutton.pack()

        # Create a Submit button to analyze the selected image
        self.submit_button = tk.Button(self.master, text="Submit", command=self.analyze_image)
        self.submit_button.pack()

        # Create a label to display the prediction result
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

        image = Image.open(file_path)
        image = image.resize((400, 400))

        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def analyze_image(self):
        if self.checkbutton_var.get():
          
            self.result_label.configure(text="Analyzing...")
            self.master.after(6000, self.show_result)
            
            print("readuy")
            

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

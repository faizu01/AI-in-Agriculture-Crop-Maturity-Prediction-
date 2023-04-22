import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np

# Loading the PreTrained model from the dataset 
model = tf.keras.models.load_model('crop_model.h5')

def analyze_image():
    # Loading  image and preprocess it
    image = Image.open(file_path)
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Use the model to predict the crop maturity
    prediction = model.predict(image)[0]
    if prediction[0] > prediction[1]:
        maturity = 'Ready to Harvest'
    else:
        maturity = 'Not Ready to Harvest'

    # Update the GUI with the prediction result
    result_label.config(text=maturity)

def select_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# Create the GUI window
root = tk.Tk()
root.title('Crop Maturity Predictor')

select_button = tk.Button(root, text='Select Image', command=select_image)
select_button.pack()

analyze_button = tk.Button(root, text='Analyze', command=analyze_image, bg='red', fg='white')
analyze_button.pack()

image_label = tk.Label(root)
image_label.pack()

result_label = tk.Label(root, font=('Arial', 18))
result_label.pack()

# Start the GUI
root.mainloop()

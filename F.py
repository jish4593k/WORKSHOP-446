import os
import random
from fpdf import FPDF
from PIL import Image

ist
def is_directory_valid(chat_id):
    directory_path = f"./images/{chat_id}"
    if os.path.exists(directory_path) and any(file.endswith(".jpg") for file in os.listdir(directory_path)):
        return True
    else:
        return False


def create_pdf(chat_id, pdf_name):
    image_path = f"./is/{chat_id}/"
    image_files = [file for file in os.listdir(image_path) if file.endswith(".jpg")]

    pdf = FPDF()
    
    for i, image_file in enumerate(image_files):
        if i >= 15:
            break
        
        image = Image.open(os.path.join(image_path, image_file))
        pdf.add_page()
        pdf.image(os.path.join(image_path, image_file), x=10, y=10, w=190)
    
    pdf.output(pdf_name)


    os.remove(pdf_name)


chat_id = "ehat"
pdf_name = f"{chat_id}_document.pdf"

if is_directory_valid(chat_id):
    create_pdf(chat_id, pdf_name)
    print(f"PDF created successfully: {pdf_name}")
 
else:
    print("No valid images found in the directory.")

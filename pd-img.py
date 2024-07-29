import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def images_to_pdf(folder_path, output_filename):
    images = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()  # Ensure images are sorted in alphabetical order
    
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter

    for image_name in images:
        img_path = os.path.join(folder_path, image_name)
        img = Image.open(img_path)
        img_width, img_height = img.size
        aspect_ratio = img_height / img_width

        # Calculate the height of the image to fit the page width
        img_height_new = height
        img_width_new = img_width * (img_height_new / img_height)

        if img_width_new > width:
            img_width_new = width
            img_height_new = img_width_new * aspect_ratio

        c.drawImage(img_path, 0, 0, width=img_width_new, height=img_height_new)
        c.showPage()

    c.save()

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing images: ")
    output_filename = "output.pdf"
    images_to_pdf(folder_path, output_filename)
    print("PDF generated successfully!")


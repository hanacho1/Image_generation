from PIL import Image
import os

def resize_images(input_dir, output_dir, size=(512, 512)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_dir, filename))
            img = img.resize(size, Image.ANTIALIAS)
            img.save(os.path.join(output_dir, filename))

resize_images('/workspace/stylegan2/cat_dataset/cats/', '/workspace/stylegan2/cat_dataset/resize/')

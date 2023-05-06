import os
import random
from PIL import Image

input_folder = r""

print("|---------------------|")
print("|  to .png converter  |")
print("|     by luka beg     |")
print("|      (c) 2023       |")
print("|---------------------|")
input_folder = input("Input folder: ").strip('"')
input_folder = os.path.normpath(input_folder)
print("\n==============================================================================\n\n")

#Create starting output folder
randomnumber = random.randint(0, 2147483646)
output_folder = "png_" + str(randomnumber)
if '"' in output_folder:
    output_folder = output_folder.replace('"', '')
os.makedirs(output_folder, exist_ok=True)

num_files = 0

#Loop through the directory for the progress number
for root, dirs, files in os.walk(input_folder):
    for f in files:
        if f.lower().endswith((".tiff", ".tif", ".jpg", ".jpeg", ".bmp", ".png")):
            num_files += 1

count = 0

#Loop through all directories and subdirectories to convert them to .png
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith((".tiff", ".tif", ".jpg", ".jpeg", ".bmp", ".png")):
            count += 1
            percentage = round((count / num_files) * 100)
            progress = f"{count}/{num_files} - {percentage}% | {filename}"
            print(f"Conversion {progress}")
            input_subfolder = os.path.relpath(root, input_folder)
            output_subfolder = os.path.join(output_folder, input_subfolder)
            os.makedirs(output_subfolder, exist_ok=True)
            image = Image.open(os.path.join(root, filename))
            image.save(os.path.join(output_subfolder, os.path.splitext(filename)[0] + ".png"))

print("\n==============================================================================\nSuccessfully saved",count,"image files to",output_folder,"\n==============================================================================")
input("Press enter to exit...")

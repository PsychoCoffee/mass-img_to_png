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

randomnumber = random.randint(0, 2147483646)
output_folder = "png_" + str(randomnumber)
if '"' in output_folder:
    output_folder = output_folder.replace('"', '')
os.makedirs(output_folder, exist_ok=True)

# Count number of image files
num_files = sum(1 for f in os.listdir(input_folder) if f.lower().endswith((".tiff", ".tif", ".jpg", ".jpeg", ".bmp", ".png")))

# Counter for image files
count = 0

for filename in os.listdir(input_folder):
    a = filename.lower()
    if a.endswith(".tiff") or a.endswith(".tif") or a.endswith(".jpg") or a.endswith(".jpeg") or a.endswith(".bmp") or a.endswith(".png"):
        count += 1
        percentage = round((count / num_files) * 100)
        progress = f"{count}/{num_files} - {percentage}% | {filename}"
        print(f"Conversion {progress}")
        image = Image.open(os.path.join(input_folder, filename))
        image.save(os.path.join(output_folder, os.path.splitext(filename)[0] + ".png"))

# Print message when done
print("\n==============================================================================\nSuccessfully saved",count,"image files to",output_folder,"\n==============================================================================")
input("Press enter to exit...")


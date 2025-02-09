import os
import pytesseract
from PIL import Image
import glob

image_folder = r'C:\Users\ASUS\Desktop\images_waited'

output_folder = r'C:\Users\ASUS\Desktop\result for images'
os.makedirs(output_folder, exist_ok=True)

image_files = glob.glob(os.path.join(image_folder, '*.*'))
image_files = [f for f in image_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

for image_file in image_files:
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image, lang='eng')
    base_name = os.path.basename(image_file)
    output_file = os.path.join(output_folder, os.path.splitext(base_name)[0] + '.txt')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f' 把{image_file} 提取到到 {output_file}')

print('完毕')


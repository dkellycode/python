import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image
# from PIL.ExifTags import Base, TAGS


def basicesizer():
    """Basic resizing tool for square images."""
    target_img = Image.open(fd.askopenfilename())

    imgwidth = target_img.size[0]
    imgheight = target_img.size[1]
    print(f'img_width = {imgwidth}')
    print(f'img_height = {imgheight}')

    if imgheight == imgwidth:
        new_pxl_val  = int(input("Enter the new pixel value: "))
    else:
        print("Image not square, please use advanced image rescaler")
        exit()
        
    target_img.resize((new_pxl_val, new_pxl_val)).save("/Users/d3ops/Documents/resized_img.jpg", "JPEG")


def advancedsizer():
    """Advanced resizing tool for non-square images."""
    target_img = Image.open(fd.askopenfilename())
    imgwidth = target_img.size[0]
    imgheight = target_img.size[1]
    print(f'img_width = {imgwidth}')
    print(f'img_height = {imgheight}')

    if imgheight == imgwidth:
        new_pxl_val  = int(input("Enter the new pixel value: "))
        target_img.resize((new_pxl_val, new_pxl_val)).save("/Users/d3ops/Documents/resized_img.jpg", "JPEG")
    else:
        new_pxl_val = int(input("Enter the maximum pixel value for the longest axis: "))
        # maxparam = max(imgheight, imgwidth)
        newratio = new_pxl_val/max(imgheight, imgwidth)
        resize_img = target_img.resize((int(imgwidth * newratio), int(imgheight * newratio)), Image.Resampling.LANCZOS).convert("RGBA")

        new_image = Image.new("RGBA", (new_pxl_val, new_pxl_val), (0, 0, 0, 0))
        x = (new_pxl_val - resize_img.width) // 2
        y = (new_pxl_val - resize_img.height) // 2
        new_image.paste(resize_img, (x, y))
        save_format = str(input("Enter the image format (e.g., JPEG, PNG): ")).replace("jpg","jpeg")
        if save_format.upper() == 'JPEG' or save_format.upper() == 'JPG':
            new_image = new_image.convert('RGB')
        # new_image.save("/Users/d3ops/Documents/resized_img.png", "PNG")
        new_image.save('/Users/d3ops/Documents/resized_img.'+f'{save_format.lower()}', f'{save_format.upper()}')


def main():
    root = tk.Tk()
    root.title("Image Resizer Tool")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 300
    window_height = 150
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(root, text="Select a function to run:")
    label.pack(pady=10)

    def run_basic():
        root.destroy()
        basicesizer()

    def run_advanced():
        root.destroy()
        advancedsizer()

    basic_button = tk.Button(root, text="Basic Resizer", command=run_basic, background="#ff6600")
    basic_button.pack(pady=5)

    advanced_button = tk.Button(root, text="Advanced Resizer", command=run_advanced)
    advanced_button.pack(pady=5)

    root.mainloop()

main()

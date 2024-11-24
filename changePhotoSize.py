import glob
from moviepy.editor import *
from PIL import Image

# read phto file
#image_files = ["GLU_4826.jpg","GLU_4828.jpg"]
image_files = glob.glob("./Images/*.jpg")

# resize photo to 2992 * 2000 and rename image file
for i in range(len(image_files)):
    im = Image.open(image_files[i])
    im_resized = im.resize((2992, 2000))
    file_name = image_files[i].split("\\")[-1]
    im_resized.save(f"./Images/RESIZE_{file_name}")

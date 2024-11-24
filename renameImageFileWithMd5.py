
import os
import hashlib
import glob

def get_md5(file_path):
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


# read phto file
#image_files = ["GLU_4826.jpg","GLU_4828.jpg"]
image_files = glob.glob("./Images/BOY*.JPG")

# according the photo content to rename image file with md5
for i in range(len(image_files)):
    md5 = get_md5(image_files[i])
    fileName = "BOY_"+md5 + ".jpg" 
    os.rename(image_files[i], fileName)
    print(image_files[i] + " -> " + fileName)
    #image_files[i] = fileName
    #print(image_files[i])
    print("")

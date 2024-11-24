
import os
import hashlib
import glob
import datetime
import exifread

def get_md5(file_path):
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def get_photo_taken_time(photo_path): 
    with open(photo_path, 'rb') as photo: 
        tags = exifread.process_file(photo) 
        taken_time = tags.get('EXIF DateTimeOriginal') 

        if taken_time is None:
            # Get the creation time of the image file
            creation_time = os.path.getctime(photo_path)
            formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime('%Y%m%d%H%M')
            return formatted_time
        # format yyyyMMddHHmm 
        taken_time = str(taken_time).replace(":", "").replace(" ", "")
        return taken_time

# read phto file
#image_files = ["GLU_4826.jpg","GLU_4828.jpg"]
image_files = glob.glob("./Images/*.JPG")

# according the photo content to rename image file with md5
for i in range(len(image_files)):
    # Get the original file name without path and extension 
    file_name = image_files[i].split("\\")[-1]
    file_name = file_name.split(".")[0]

    # continue for next file
    # continue


    # Get the md5 of the image file
    md5 = get_md5(image_files[i])

    # 抓取照片拍攝時間 (EXIF)
    formatted_time = get_photo_taken_time(image_files[i])

    # Create the new file name
    fileName = file_name + "_" + formatted_time+"_"+ md5 + ".JPG"
    os.rename(image_files[i], fileName)
    print(image_files[i] + " -> " + fileName)
    #image_files[i] = fileName
    #print(image_files[i])
    print("")

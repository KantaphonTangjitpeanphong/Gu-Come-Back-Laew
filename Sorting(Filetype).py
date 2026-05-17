import os 
import shutil 

directory = "/Users/kantaphontangjitpeanphong/Desktop/100MSDCF"
files = os.listdir("/Users/kantaphontangjitpeanphong/Desktop/100MSDCF")
print(files)
os.makedirs("/Users/kantaphontangjitpeanphong/Desktop/100MSDCF/Raw")
os.makedirs("/Users/kantaphontangjitpeanphong/Desktop/100MSDCF/Jpg")
for i in range(len(files)):
    print(i)
    if "ARW" in files[i]:
        shutil.move(f"/Users/kantaphontangjitpeanphong/Desktop/100MSDCF{files[i]}",f"/Users/kantaphontangjitpeanphong/Desktop/100MSDCF/Raw{files[i]}")
        print(f"moved {files[i]} to raw")
    elif "JPG" in files[i]:
        shutil.move(f"/Users/kantaphontangjitpeanphong/Desktop/100MSDCF{files[i]}",f"/Users/kantaphontangjitpeanphong/Desktop/100MSDCF/Jpg{files[i]}")   
        print(f"moved {files[i]} to Jpg")
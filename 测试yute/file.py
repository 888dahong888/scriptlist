import os
import shutil
os.chdir(r"\..\")
formats ={
    "音频":[".mp3",".wav"],
    "视频":[".mp3",".avi",".mov"],
    "图片":[".jpeg",".jpg",".png","gif","bmp"],
    "文档":[".txt",".pdf",".doc",".docx"],
    "程序":[".exe",".msi"],
    "压缩":[".zip",".rar"],
}

for f in os.listdir():
    ext=os.path.splitext(f)[-1].lower()
    for d.exts in formats.items:
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(f,"{0}/{1}".format(d,f))
         
print("success") 
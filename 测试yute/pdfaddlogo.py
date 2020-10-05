#pymupdf
import fitz
#添加水印
def add_watermark(input_file,output_file,img_file):
    rec=fitz.Rect(450,20,550,50)
    f=fitz.open(input_file)
    for page in f:
        page.insertImage(rec,img_file)
    f.save(output_file)

from moviepy.editor import VideoFileClip
def mp4_to_gif(video,gif):
    clip=VideoFileClip(video).subclip(5,10)
    clip.write_gif(gif)
#添加密码
from PyPDF2 import PdfFileReader,PdfFileWriter
def encrypt(input_file,output_file,password="123456"):
    reader = PdfFileReader(input_file)
    writer=PdfFileWriter()
    for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))
    writer.encrypt(user_pwd=password,owner_pwd=None,use_128bit=True)
    with open(output_file,'wb') as f:
        writer.writer(f)

#合并
from PyPDF2 import PdfFileMerger
def merger(output,files):
    m=PdfFileMerger()
    for file in files:
        m.append(file)
    with open(output,'wb') as f:
        m.writer(f)
        
#分割
from PyPDF2 import PdfFileReader,PdfFileWriter
def pdf_splitter(file):
    pdf=PdfFileReader(file)
    writer=PdfFileWriter()
    for i in range(10):
        writer.addPage(pdf.getPage(i))
    with open('1223.pdf','wb') as f:
        writer.writer(f)
    print("success")
if __name__ == '__main__':
    add_Watermark('django.pdf', 'watermark.pdf','logo.png')
    mp4_to_gif('123.mp4','123.gif')

    files=['1.pdf','2.pdf','3.pdf']
    merger('output.pdf',files)
    
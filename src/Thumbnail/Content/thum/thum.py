from moviepy.editor import *
from mutagen import File
from PIL import Image

def ImageResizer(path):
    img = Image.open(path)
    new_img = img.resize((200,200))
    filename, format = path.split('.')
    print(filename, format)
    last = filename.split("/")
    newpath = last[-1]+"_resized."+format
    print(newpath)
    new_img.save(newpath, format, optimize=True)

def GetImageThumbnail(path):
    print()
    ImageResizer(path)
    return
def GetVideoThumbnail(path, time=1.0):
    try:
        clip = VideoFileClip(path)
        clip.save_frame("thumbnail.png", time)
        return_path = "thumbnail.png"
    except :
        return_path = "Thumbnailvideo.png"
    return return_path


def GetAudioThumbnail(path):
    try:
        file = File(path)
        artwork = file.tags['APIC:'].data
        with open('thumbnail.jpg', 'wb') as img:
            img.write(artwork)
        return_path = "audio.jpg"
    except:
        return_path = "Thumbnailaudio.png"
    return return_path


def GetTextThumbnail(path, time=1.0):
    return_path = "Thumbnailtext.png"
    return path_path

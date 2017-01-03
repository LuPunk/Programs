import os

path = "C:\\Users\\Luca\\Downloads"
dot = 0
os.chdir(path)
files = os.listdir(path)

def mover(file):
    torrent = [".torrent"]
    pic = [".jpg", ".jpeg", ".gif", ".png"]
    music = [".mp3", ".flac", ".wav", ".ogg"]
    pdf = ".pdf"
    exe = [".exe", ".msi"]

    dot = file.rfind(".")

    if file[dot:] in torrent:
        os.rename(path + "\\" + file, path + "\Torrents\\" + file)
    elif file[dot:] in pic:
        os.rename(path + "\\" + file, path + "\Images\\" + file)
    elif file[dot:] in music:
        os.rename(path + "\\" + file, path + "\Music\\" + file)
    elif file[dot:] in pdf:
        os.rename(path + "\\" + file, path + "\PDFs\\" + file)
    elif file[dot:] in exe:
        os.rename(path + "\\" + file, path + "\Executables\\" + file)
    else:
        path_ok = False
        while path_ok == False:
            print("Where should I place this file?: {}".format(file))
            alt_path = input("Folder: ")
            if os.path.exists(path + "\\{}".format(alt_path)):
                os.rename(path + "\\" + file, path + "\{}\\".format(alt_path) + file)
                path_ok = True

    return None

for check in files:
    if "." in check and check[0] != ".":
        mover(check)

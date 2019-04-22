''' File collections module''' 
import os
import argparse
from glob import glob

from helper import IMAGE_FILES, MUSIC_FILES, VIDEO_FILES, EBOOK_FILES

def get_files(path, filetypes):
    files = []
    for filetype in filetypes:
        files.extend([y for x in os.walk(path) for y in glob(os.path.join(x[0], filetype))])
    return files

def get_image_files(path):
    return get_files(path, ["*."+x for x in IMAGE_FILES])

def get_music_files(path):
    return get_files(path, ["*."+x for x in MUSIC_FILES])

def get_ebook_files(path):
    return get_files(path, ["*."+x for x in EBOOK_FILES])

def get_video_files(path):
    return get_files(path, ["*."+x for x in VIDEO_FILES])


if __name__=='__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = True,
        help = "Path to the folder to be scanned")
    ap.add_argument("-t", "--filetypes", required = False,
        help = "list of filetypes to scan(separated by comma")
    args = vars(ap.parse_args())

    folder_path =  args["path"]
    file_types  =  args["filetypes"].split(",")

    for i in get_music_files(folder_path):
        print(i)


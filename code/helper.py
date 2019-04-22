import os

mapping = {
        'Artist'        :'artist',
        'Album'         :'album',
        'Album Artist'  :'album_artist',
        'Title'         :'title',
        'Track'         :'track_num',
        'Genre'         :'genre',
        'Composer'      :'composer',
        'Year'          :'best_release_date',
        'Disc Number'   :'disc_num',
        'Play count'    :'play_count',
    }

# tinytag mappings
mapping_tt = {
        'Artist'        :'artist',
        'Album'         :'album',
        'Album Artist'  :'albumartist',
        'Title'         :'title',
        'Track'         :'track',
        'Track Total'   :'track_total',
        'Genre'         :'genre',
        'Composer'      :'composer',
        'Year'          :'year',
        'Disc'          :'disc',
        'Disc Total'    :'disc_total',
        'Samplerate'    :'samplerate',
        'Duration'      :'duration',
        'Filesize'      :'filesize',
        'Comment'       :'comment',
    }

IMAGE_FILES = ["jpg","jpeg", "png"]
MUSIC_FILES = ["mp3","m4a", "m4b", "aac","wav"]
EBOOK_FILES = ["epub","mobi", "pdf"]
VIDEO_FILES = ["mp4","avi", "mov"]

def verify_exists(filepath):
    if not os.path.exists(filepath):
        raise Exception("File does not exist: {}".format(filepath))
    elif not os.path.isfile(filepath):
        raise Exception("This is not a file: {}".format(filepath))
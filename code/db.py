from peewee import *
from pathlib import Path
import datetime

from id3 import get_id3_tags_tt

TYPES = ['b','m','v', 'i']

from helper import verify_exists
from helper import IMAGE_FILES, MUSIC_FILES, VIDEO_FILES, EBOOK_FILES

db_path = Path.cwd().joinpath('db')
os.mkdirs(db_path)
db = SqliteDatabase(db_path.joinpath('my_database.db'))

class BaseModel(Model):
    class Meta:
        database = db

# class Ebook(BaseModel):
#     path   = CharField(unique=True)
#     name   = CharField()
#     added  = DateTimeField(default=datetime.datetime.now)
#     parsed =  BooleanField(default=False)
class LibraryPath(BaseModel):
    path        = CharField(unique=True)
    libtype     = CharField()
    added       = DateTimeField(default=datetime.datetime.now)
    parsed      = BooleanField(default=False)

class Music(BaseModel):
    path   = CharField(unique=True)
    title   = CharField()
    added  = DateTimeField(default=datetime.datetime.now)
    parsed =  BooleanField(default=False)
    title   = CharField()
    artist   = CharField()
    album   = CharField()
    track   = CharField()
    track_total   = CharField()
    genre   = CharField()
    composer   = CharField()
    year   = CharField()
    disc   = CharField()
    disc_total   = CharField()
    samplerate   = CharField()
    duration   = CharField()
    filesize   = CharField()
    comment   = CharField()

# class Video(BaseModel):
#     path   = CharField(unique=True)
#     name   = CharField()
#     added  = DateTimeField(default=datetime.datetime.now)
#     parsed =  BooleanField(default=False)

# class Image(BaseModel):
#     path = CharField(unique=True)
#     name = CharField()
#     added = DateTimeField(default=datetime.datetime.now)
#     parsed =  BooleanField(default=False)

def get_music_object(filepath):
    verify_exists(filepath)
    tags = get_id3_tags_tt(filepath)
    music = Music(path=filepath)
    for i in mapping_tt.keys():
        setattr(music,mapping_tt[i], unicode(tags.get(i,"")), "utf-8")
    music.parsed = True
    return music

def firstrun():
    db.connect()
    db.create_tables([LibraryPath, Ebook, Music, Video, Image])

def save_to_db(filepath, typ):
    if typ not in TYPES:
        raise Exception("Invalid file type: {}".format(typ))
    if typ == 'm':
        obj = get_music_object(file_path)
    elif typ == 'e':
        obj = get_book_object(file_path)
    elif typ == 'v':
        obj = get_video_object(file_path)
    elif typ == 'i':
        obj = get_image_object(file_path)
    
    obj.save()
    return true

if __name__=='__main__':
    firstrun()
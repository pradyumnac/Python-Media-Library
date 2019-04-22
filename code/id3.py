import os
import eyed3
from tinytag import TinyTag
import argparse

from helper import verify_exists
from helper import IMAGE_FILES, MUSIC_FILES, VIDEO_FILES, EBOOK_FILES

def get_id3_tags_tt(filepath, tag_name = 'all'):
    # tinytag version
    tags = {}
    verify_exists(filepath)
    
    tag = TinyTag.get(filepath)
    for i in mapping_tt.keys():
        tags[i] = getattr(tag, mapping_tt[i])

    tags['Duration'] = int(tags['Duration'])
    if tag_name == 'all':
        return tags
    else:
        assert tag_name in mapping_tt.keys()
        tags[tag_name]

def get_id3_tags(filepath, tag_name = 'all'):
    tags = {}
    verify_exists(filepath)
    
    audiofile = eyed3.load(filepath)
    for i in mapping.keys():
        tags[i] = getattr(audiofile.tag, mapping[i])

    tags['Genre'] = tags['Genre'].name
    if tag_name == 'all':
        return tags
    else:
        assert tag_name in mapping.keys()
        tags[tag_name]

def set_id3_tags(filepath, tags):
    verify_exists(filepath)
    audiofile = eyed3.load(filepath)

    assert type(tags) == type({})
    for i in tags.keys():
        if i in mapping:
            setattr(audiofile.tag, mapping[i], unicode(tags.get(i,''), "utf-8"))
        else:
            print("Skipping tag: {}".format(i))

    audiofile.tag.save()


if __name__=='__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required = True,
        help = "path to the music file")
    action = ap.add_mutually_exclusive_group(required=True)
    action.add_argument('--get', action="store_true", default=False, help='Gets ID3 tag')
    action.add_argument('--set', action="store_true", default=False, help='Sets ID3 tag')
    ap.add_argument("-t", "--tagname", required = False, default='all', help = "Name of the ID3 tag")
    ap.add_argument("-v", "--value", required = False, help = "Value of the ID3 tag (Only for option set)")
    
    
    args = vars(ap.parse_args())

    file_path =  args["file"]
    print(get_id3_tags_tt(file_path))




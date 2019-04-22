import argparse
import PIL.Image
from PIL.ExifTags import TAGS


def get_exif_tags(image_path):
    img = PIL.Image.open(image_path)
    # exif = {
    #     PIL.ExifTags.TAGS[k]: v
    #     for k, v in img._getexif().items()
    #     if k in PIL.ExifTags.TAGS
    # }
    img.verify()
    exif = img._getexif()
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled


if __name__=='__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True,
        help = "Path to the image to be scanned")
    args = vars(ap.parse_args())

    image_path =  args["image"]
    tags = get_exif_tags(image_path)
    # print(tags)
    for tag in tags:
        print("{} => {}".format(tag, tags[tag]))
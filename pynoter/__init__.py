from fcn import conv_raw
import argparse
import os

# make argument parser for powerpoint and methods to be called
# on the powerpoint
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required=True, help='path to ppt')
ap.add_argument('-t', '--title', required=False, help='title new doc')
ap.add_argument('-ft', '--filetype', required=True, help='specify type of file')

args = vars(ap.parse_args())

path = str(args['path'])
title = str(args['title'])
filetype = str(args['filetype'])


# call each method depending on the boolean value attributed
def main():
    myppt = conv_raw.Powerpoint(path, title, filetype)
    myppt.slide_note()
    myppt.note_file()

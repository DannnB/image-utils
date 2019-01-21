#!/usr/bin/python
# Author: DanB
# Wokrs on Windows, needs testing on mac and linux

from PIL import Image
import os
import sys

import tkinter
from tkinter import filedialog

# hide the anoying default tk window that opens along with the directory dialog
root = tkinter.Tk()
root.withdraw()

def init():
  # get path and optimise image
  resize()
  # print('Running...')

def selectDir():
  # get selected path from user
  path_selected = filedialog.askdirectory(
      parent=root, initialdir="/web/python/utilscripts/images",  title='Please select a directory') + '/'
  return path_selected

def resize():
  path_selected = selectDir()

  dirs = os.listdir(path_selected)

  save_directory_name = 'optimized'
  save_directory = path_selected + '/' + save_directory_name + '/'
  
  for item in dirs:

    if os.path.isfile(path_selected + '/' + item):
      # split the filename and extention
      name, ext = os.path.splitext(item)
      if ext == '.jpg':

        # path of the image in the selected folder to be looped
        img_path = path_selected+item

        # open image
        im = Image.open(img_path)


        ## set the max image size in ether width or height
        size = (800, 800)
        im.thumbnail(size, Image.ANTIALIAS)

        ## Save the image ##
        # create output folder if it dosn't exist
        if not os.path.exists(save_directory):
          os.makedirs(save_directory)

        # create output file path and name
        output = path_selected + save_directory_name + '/' + name + ext

        # save the image to the save_directory_name folder
        # TODO: use directory dialog to get output folder
        im.save(output, 'JPEG', quality=100)

init()
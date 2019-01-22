#!/usr/bin/python
# Author: DanB
# Wokrs on Windows, needs testing on mac and linux

from PIL import Image
import os
import sys

import tkinter
from tkinter import *
from tkinter import filedialog

# hide the anoying default tk window that opens along with the directory dialog
# root = tkinter.Tk()
# root.withdraw()

root = tkinter.Tk()

# vars
global folder_path_input
global folder_list 
folder_list = ["test"]
folder_path_input = ''

def init():
  # get path and optimise image
  #resize(selectDir())
  main()
  # print('Running...')

def main():
  # window settings
  mainWindowSettings()
  # render main view
  mainWindow()
  
  #launch application
  root.mainloop()


def mainWindowSettings():
  # window settings
  root.title("Batch Image Optimisation Tool v0.1")
  root.geometry("300x300")
  # window.wm_iconbitmap('name.ico')

def browse_button():
  print('button clicked')
  filename = filedialog.askdirectory(
      parent=root, initialdir="/web/python/utilscripts/images",  title='Please select a directory')
  folder_path_input = filename
  print('#############')
  print(filename)
  print('#############')

def list_files_button():
  dirs = os.listdir(folder_path_input)

  for item in dirs:
    folder_list.append(item)

  print('#############')
  print(dirs)
  print('#############')

def mainWindow():
  # label
  lbl1 = Label(root, text='Please select a directory')
  label_path = Label(root, textvariable=folder_path_input)
  label_list = Label(root, textvariable=folder_list)

  #button
  button2 = Button(text="Browse", command=browse_button)
  btn_list_files = Button(text="list files", command=list_files_button)
  
  # layout
  lbl1.grid(row=0, column=1)
  button2.grid(row=0, column=3)
  label_path.grid(row=1, column=1)
  label_list.grid(row=2, column=3)
  btn_list_files.grid(row=2, column=1)
  














def selectDir():
  # get selected path from user
  path_selected = filedialog.askdirectory(
      parent=root, initialdir="/web/python/utilscripts/images",  title='Please select a directory') + '/'
  return path_selected

def resize(path_location):
  path_selected = path_location

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

        ####################
        ## Save the image ##
        ####################
        # create output folder if it dosn't exist
        if not os.path.exists(save_directory):
          os.makedirs(save_directory)

        # create output file path and name
        output = path_selected + save_directory_name + '/' + name + ext

        # save the image to the save_directory_name folder
        # TODO: use directory dialog to get output folder
        im.save(output, 'JPEG', quality=100)

init()

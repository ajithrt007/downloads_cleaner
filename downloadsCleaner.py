import os
import shutil
import datetime;

no_files_cleaned = 0
files_dict = {}

# def make_directories(folder_organization):
#    for primary_folder in folder_organization:

def move_file(file_name, file_type, primary_folder, *args):
   global no_files_cleaned
   files_in_dir = []
   destination_path = os.path.join(dir_path, primary_folder)

   if len(args) != 0:
      for subfolder in args:
         destination_path = os.path.join(destination_path, subfolder)

   files_in_dir = os.listdir(destination_path)

   if file_name not in files_in_dir:
      shutil.move(os.path.join(dir_path,file_name), destination_path)

   else:
      index_of_dot = file_name.index('.')
      new_file_name = file_name[:index_of_dot] + '_' + str(datetime.datetime.now()).replace(" ", "_").replace(":", "-") + file_type
      shutil.move(os.path.join(dir_path, file_name), os.path.join(destination_path, new_file_name))

   no_files_cleaned += 1

def classify(file_type, file_name):
   global no_files_cleaned

   if file_type == '.svg' or file_type == '.eps' or file_type == '.ai' or file_type == '.psd':
      move_file(file_name,file_type, 'Image', 'svg') #moved to svg folder inside Image folder

   elif file_type == '.png':
      move_file(file_name,file_type, 'Image', 'png') #moved to png folder inside Image folder

   elif file_type == '.jpg' or file_type == '.jpeg' or file_type == '.JPG':
      move_file(file_name,file_type, 'Image', 'jpg') #moved to jpg folder inside Image folder

   elif file_type == '.webp' or file_type == '.jfif' or file_type == '.gif':
      move_file(file_name,file_type, 'Image') #moved to  Image folder

   elif file_type == '.pdf' or file_type == '.PDF':
      move_file(file_name,file_type, 'Documents','pdf') #moved to pdf folder inside Documents folder

   elif file_type == '.csv' or file_type == '.xlsx' or file_type == '.xls':
      move_file(file_name,file_type, 'Documents','excel') #moved to excel folder inside Documents folder

   elif file_type == '.pptx':
      move_file(file_name,file_type, 'Documents','slides') #moved to slides folder inside Documents folder

   elif file_type == '.docx' or file_type == '.doc':
      move_file(file_name,file_type, 'Documents','word') #moved to word folder inside Documents folder
      
   elif file_type == '.txt':
      move_file(file_name,file_type, 'Documents','text') #moved to text folder inside Documents folder

   elif file_type == '.zip' or file_type == '.rar':
      move_file(file_name,file_type, 'ZIP') #moved to ZIP folder

   elif file_type == '.ipynb' or file_type == '.json' or file_type == '.js' or file_type == '.css' or file_type == '.html' or file_type == '.c' or file_type == '.y':
      move_file(file_name,file_type, 'Code') #moved to Code folder
      
   elif file_type == '.exe' or file_type == '.msi':
      move_file(file_name,file_type, 'EXE') #moved to EXE folder
      
   elif file_type == '.mp4' or file_type == '.mkv' or file_type == '.m4v':
      move_file(file_name,file_type, 'Media','Video') #moved to Video folder inside Media folder

   elif file_type == '.mp3':
      move_file(file_name,file_type, 'Media','Audio') #moved to Audio folder inside Media folder


def clean_directory(dir_path):
   for file in os.listdir(dir_path):
      file_type =  os.path.splitext(file)[1]
      classify(file_type,file)

if __name__ == '__main__':
   dir_path = 'D:\\Downloads' #Your downloads destination here   
   folder_organization={
      'Fonts': [],
      'Documents': ['pdf','text','word','slides','excel'],
      'Image': ['jpg','png','svg'],
      'EXE':[],
      'ZIP':[],
      'Media':['Audio','Video'],
      'Code':[]
   }
   # make_directories(folder_organization)
   clean_directory(dir_path)
   print("Downloads is Cleaned !![{0} files moved]".format(no_files_cleaned))
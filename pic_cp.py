import os 
import shutil
from glob import glob

src_dir = 'G:\Photos\ShaftImages'
dest_dir = 'G:\Photos\Pixiv_Image_Collection'

init_pic_sort_index = 41
str_init_pic_sort_index = str(init_pic_sort_index)
folder_index = 1

init_dest_folder_name = 'Pixiv_Images_' + '0' + str_init_pic_sort_index
init_dest_folder_path = dest_dir + '\\' + init_dest_folder_name


src_file_list = os.listdir(src_dir)
num_src_file = len(src_file_list)
print(f'{num_src_file} files in {src_dir}')

init_dest_folder_list = os.listdir(init_dest_folder_path)


#find initial folder and number of files in it
if not os.path.exists(init_dest_folder_path):
    os.mkdir(init_dest_folder_path)
    print('Directory created')
    print(f'folder {init_dest_folder_path} created')
else:
    num_init_dest_folder_list = len(init_dest_folder_list)
    print('Directory exists')
    print(f'folder {init_dest_folder_path} has {num_init_dest_folder_list} files')

#begin copy files 
for index, item in enumerate(src_file_list):
#initial folder, copy files limited to 100 - existing_files
    if index < 100 - num_init_dest_folder_list:
        shutil.copy(src_dir + '\\' + item, init_dest_folder_path)
    else:
#create new folder and copy files 
        new_dest_folder_path = dest_dir + '\\' + 'Pixiv_Images_' + '0' + str(init_pic_sort_index + folder_index)
        if not os.path.exists(new_dest_folder_path):
            os.mkdir(dest_dir + '\\' + 'Pixiv_Images_' + '0' + str(init_pic_sort_index + folder_index))
            print(f'Directory created {init_pic_sort_index + folder_index}')
    
        shutil.copy(src_dir + '\\' + item, new_dest_folder_path)
#folder index increment
        if (index - 100 + num_init_dest_folder_list + 1)%100 == 0:
            folder_index = folder_index + 1
            


 






    

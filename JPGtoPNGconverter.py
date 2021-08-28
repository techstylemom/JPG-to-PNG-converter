import sys
import os
from PIL import Image

#grab the 1st and 2nd argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

#check if new folder exist, if not create it
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#loop through pokedex and convert each image to png
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.thumbnail((200, 200))
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')

#save to new folder
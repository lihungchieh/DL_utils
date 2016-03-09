import numpy as np 
import cv2 
from os import listdir
from os.path import join, isfile
import imutils
import sys

if len(sys.argv) != 3:
	print "Usage: python data_augment.py source_dir target_dir"
	sys.exit()

path = sys.args[1]
store_path = sys.args[2]

dim = (128, 128)

f_list = [f for f in listdir(path) if isfile(join(path, f)) and 
	(f[-3:] == 'png' or f[-3:] == 'jpg' or f[-3:] == 'bmp')]

def rotate_img(img, file_name, store_path, iter_count = 1):
	img_left_five = imutils.rotate(img, 3)
	img_left_five = cv2.resize(img_left_five, dim, interpolation=cv2.INTER_AREA)
	iter_count += 1
	cv2.imwrite(join(store_path, file_name + '_' + str(iter_count)) + '.jpg', img_left_five)

	img_right_five = imutils.rotate(img, 358)
	img_right_five = cv2.resize(img_right_five, dim, interpolation=cv2.INTER_AREA)
	iter_count += 1
	cv2.imwrite(join(store_path, file_name + '_' + str(iter_count) + '.jpg'), img_right_five)

	img_left_ten = imutils.rotate(img, 10)
	img_left_ten = cv2.resize(img_left_ten, dim, interpolation=cv2.INTER_AREA)
	iter_count += 1
	cv2.imwrite(join(store_path, file_name + '_' + str(iter_count)) + '.jpg', img_left_ten)

	img_right_ten = imutils.rotate(img, 350) 
	img_right_ten = cv2.resize(img_right_ten, dim, interpolation=cv2.INTER_AREA)
	iter_count += 1
	cv2.imwrite(join(store_path, file_name + '_' + str(iter_count)) + '.jpg', img_right_ten)

count = 0
print "The count of images before argument"
print len(f_list)

for file_name in f_list:
	img = cv2.imread(join(path, file_name))
	f = file_name[:-4]
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite(join(store_path, f + '_0.jpg'), resized)
	count += 1
	change the color in R, G, B channel respectively, then rotated the data in 5, 10 degree respectly
	img_flip = cv2.flip(resized, 1)
	cv2.imwrite(join(store_path, f + '_1.jpg'), img_flip)

	M = np.ones(resized.shape, dtype='uint8') * 5
	img_add = cv2.add(resized, M)
	cv2.imwrite(join(store_path, f + '_2.jpg'), img_add)
	count +=1

	img_sub = cv2.subtract(resized, M)
	cv2.imwrite(join(store_path, f + '_3.jpg'), img_sub)
	count += 1

	flip_add = cv2.add(img_flip, M)
	cv2.imwrite(join(store_path, f + '_4.jpg'), flip_add)
	count += 1

	flip_sub = cv2.subtract(img_flip, M)
	cv2.imwrite(join(store_path, f + '_5.jpg'), flip_sub)
	count += 1

	# rotated the images above to argument 
	rotate_img(img, f, store_path, 5)
	count += 4
	rotate_img(img_flip, f, store_path, 9)
	count += 4
	rotate_img(img_add, f, store_path, 13)
	count += 4
	rotate_img(img_sub, f, store_path, 17)
	count += 4
	rotate_img(flip_add, f, store_path, 21)
	count += 4
	rotate_img(flip_sub, f, store_path, 25)
	count += 4

print "Resized and argumented images number"
print count



import os
from imutils import paths

BASE_IMG = os.path.join(os.getcwd(), 'images')

dir_paths = [os.path.join('images', dir) for dir in os.listdir(BASE_IMG)]

for dir_path in dir_paths:
    os.rename(dir_path, dir_path.replace(' ', '_'))

for dir_path in dir_paths:
    print(dir_path)
    i = 0
    imgs = paths.list_images(dir_path)
    for img in imgs:
        print(img)
        fname = img.split('\\')
        os.rename(img, os.path.join(fname[0], fname[1], f'{i:04d}.jpg'))
        i += 1
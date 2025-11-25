
import os

# To be able to run the file more often
# you have to remove the 'thumbnails' directory:
import shutil
shutil.rmtree('thumbnails')

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())  # ['large', 'medium', 'small']

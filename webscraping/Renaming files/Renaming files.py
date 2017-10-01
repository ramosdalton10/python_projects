import os

# PROGRAM TO CHANGE THE NAMES OF FILES

os.chdir('/root/Downloads/Fotos from germany/')  # change the path
zet = []
print os.getcwd()  # prints the current working directory path
i = 1
for path in os.listdir('/root/Downloads/Fotos from germany/'):
    need, out, go = path.split('jpg')
    new_name = need + '_' + str(i) + '.jpg'
    i += 1
    # os.rename(path, new_name)

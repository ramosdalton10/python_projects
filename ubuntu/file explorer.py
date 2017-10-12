import os


for root , dir, file in os.walk('/home/goku'):
    # if x == 'French':
    print root
    print dir
    print file
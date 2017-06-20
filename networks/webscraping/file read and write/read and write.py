import requests , re , urllib

with open('test_file.txt','r+') as f:
    f.write('this is a test charactor from the start')
with open('test_file.txt', 'r+') as f:
    print f.read()
urllib.urlretrieve('http://www.wou.edu/~rrogers/Germany/Stuttgart%204-18-07/n51700059_30302168_377.jpg','n51700059_30302168_377.jpg')
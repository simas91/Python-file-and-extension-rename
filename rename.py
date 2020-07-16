import shutil, os, re

# renames ALL files and changes their extension in given folder

# checks if file name contains illegal character
def fileNaming(data):
    re1 = re.compile(r'[\\/:*?"<>|]') # illegal naming characters
    if re1.search(data):
        print(r'name can\'t contain following characters: \/:*?"<>|')
        return False
    return True

# asking directory of files
folder = ''

while not os.path.isdir(folder):
    folder = input(r'enter full destination of the folder (etc: C:\Users\me\folder): ')

# asking for prefix and/or suffix options
answer = 'x' # option to add suffix or prefix
naming = ''  # naming for suffix/prefix
checkNaming = False

while answer != '' and answer != 'p' and answer != 's':
    answer = input('do you want to add extra naming as suffix(s) or prefix(p)? leave empty if not: ')

if answer != '': 
    while not checkNaming:
        if answer == 's':
            naming = input('add suffix: ')
        else:
            naming = input('add prefix: ')
        checkNaming = fileNaming(naming)

# setting file extension
fileExtension = input('set file extension: ')

# renaming all files in cwd
fileList = os.listdir(folder) # list of all files in directory

count = input('file naming count starts from: ') 
while not count.isdigit():
    count = input('file naming count starts from: ')

for file in fileList: # renames all files
    if answer == 'p' :
        shutil.move(folder + '\\' + file, folder + '\\' + naming + ' ' + str(count) + '.' + fileExtension)
    elif answer == 's':
        shutil.move(folder + '\\' + file, folder + '\\'+ str(count) + ' ' + naming + '.' + fileExtension)
    else:
        shutil.move(folder + '\\' + file, folder + '\\'+ str(count) + '.' + fileExtension)
    count = int(count) + 1

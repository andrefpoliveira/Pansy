# PPM -> Pansy Package Manager
import requests
import os
import sys

packages = ['math']

print("Pansy v0.5a → Installing {}...".format(sys.argv[1]))

try:
    if os.path.isdir("./pansy_modules") == True:
        if sys.argv[1] in packages:
            url = 'https://centeltech.com/modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1])
            txt = url[42:-1]+url[-1]
            myfile = requests.get(url)
            os.mkdir("./pansy_modules/{}".format(sys.argv[1]))
            open('./pansy_modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1]), 'wb').write(myfile.content)
            base = os.path.splitext('./pansy_modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1]))[0]
            os.rename('./pansy_modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1]), base + ".pansy")
            print("Done!")
        else:
            print("Check Failed: No module named {}. Check your spelling and try again.".format(sys.argv[1]))
    else:
        if sys.argv[1] in packages:
            os.mkdir('./pansy_modules')
            url = 'https://centeltech.com/modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1])
            txt = url[42:-1]+url[-1]
            myfile = requests.get(url)
            os.mkdir("./pansy_modules/{}".format(sys.argv[1]))
            open('./pansy_modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1]), 'wb').write(myfile.content)
            base = os.path.splitext('./pansy_modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1]))[0]
            os.rename('./pansy_modules/{}/{}.txt'.format(sys.argv[1], sys.argv[1]), base + ".pansy")
            print("Done!")
        else:
            print("Check Failed: No module named {}. Check your spelling and try again.".format(sys.argv[1]))
except FileExistsError:
  print("FileError → Cannot create file/folder as it already exists. Try deleting the file/folder and try again!")

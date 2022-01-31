from os.path import splitext
from os import walk, rename
import easygui as eg

path = eg.diropenbox()
fileExt = list(input("File extentions (write comma seperated): ").split(","))
start = int(input("Min number for naming: "))
step = int(input("Step number for naming: "))
try:
    _, _, filenames = next(walk(path))
    print(filenames)
    for f in filenames:
        oldName, ext = splitext(f)
        if ext[1:] in fileExt:
            rename(path + '/' + f, path + '/' + str(start) + ext)
            start += step


except Exception as e:
    print("Error:", e)

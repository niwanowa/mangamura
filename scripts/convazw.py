import os,sys,subprocess,shutil

path = os.getcwd()

files = os.listdir(path)
target = [f for f in files if 'azw' in f]

print(target)

subprocess.run("ebook-convert.exe {} tmp.zip".format(target[0]), shell=True)

print()

shutil.unpack_archive('tmp.zip', 'tmp')

subprocess.run("azw32jpeg.py", shell=True, cwd=r'./tmp')
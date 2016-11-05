#!usr/bin/python

from defs import ManagePath
import os, shutil

dir_files = ManagePath.gettargetfilesdir()
dir_prj = ManagePath.getprjdir()
dir_output = os.path.join(dir_prj, 'output')

for dirr, dirnames, filenames in os.walk(dir_files):
    for filename in filenames:
        if len(filename.split('.')) == 1:
            src = os.path.join(dir_files, filename)
            dst = os.path.join(dir_output, filename)
            if os.path.isfile(src):
                shutil.copy(src, dst)
            if os.path.isfile(dst):
                print(filename + '复制成功')
            else:
                print(filename + '复制失败')

for dirr, dirnames, filenames in os.walk(dir_output):
    for filename in filenames:
        if len(filename.split('.')) == 1:
            newfilename = filename + '.png'
            newfilepath = os.path.join(dir_output, newfilename)
            os.rename(os.path.join(dir_output, filename), newfilepath)
            if(os.path.isfile(newfilepath)):
                print(filename + '重命名成功')
            else:
                print(filename + '重命名失败')
                


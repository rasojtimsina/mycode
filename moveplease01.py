#!/usr/bin/env python3

import shutil
import os

#the code below will force python to run in the following specified directory.
os.chdir('/home/student/mycode/')

#the following code will move file or folder from the source to the destination

shutil.move('raynor.obj', 'ceph_storage/')

#if in case thre are files or folder with the same name in destination the command below will prevent that

xname = input('What is the new name for kerrigan.obj? ')

# The following line will rename a file

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)




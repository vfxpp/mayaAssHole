# -*- coding: utf-8 -*-
#author:Oliver
#get maya file out ass file incloud all arnold lights

"""
a simple script to render ass file from maya

usage: python outass.py /path/to/mayafile

"""

import sys
import os
import subprocess

#get the command flag
mayafile = sys.argv[1]

#where mel script
mel = 'D:/WriteAss/outass.mel'

#
#basename = os.path.basename(sys.argv[1]) 

#run maya and run mel and out ass file
fopen = subprocess.Popen("C:/Program Files/Autodesk/Maya2014/bin/mayabatch.exe -file {0} -script {1}".format(mayafile,mel))
fopen.wait()

#print(fopen.stdout.read())
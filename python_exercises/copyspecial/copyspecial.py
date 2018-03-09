#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  filenames = []
  s = [os.path.abspath(os.path.join(dir,filename)) for filename in os.listdir(dir) if re.search(r'__\w+__',filename)]
  return s

def copy_to(paths, dir):
  print 'copying files from ' + os.path.abspath(paths) + ' to ' + os.path.abspath(dir)
  filenames = get_special_paths(paths)
  for filename in filenames:
    shutil.copy(filename,dir)

def zip_to(paths,zippath):
  print 'zipping files in ' + os.path.abspath(paths) + ' copy zip to ' + os.path.abspath(zippath)
  filenames = get_special_paths(paths)
  unixfiles = ''
  
  for filename in filenames:
    unixfiles = unixfiles + ' ' + filename

  cmd = 'zip '+ os.path.join(os.path.abspath(zippath),'zipfies.zip')+unixfiles
  print 'about to execute: ' + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  print output



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[0]
    del args[0]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[0]
    del args[0]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  if todir == '--todir':
    copy_to(args[1],args[0])
  elif tozip == '--tozip':
    zip_to(args[1],args[0])
  else:
    filenames = get_special_paths(args[0])
    print filenames

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
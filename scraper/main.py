import os
import sys

# Import by relative path
cwd = os.getcwd()
sys.path.append(cwd + "/data/")
sys.path.append(cwd + "/gui/")
sys.path.append(cwd + "/scraper/")

import gui_main

if __name__ == '__main__':
   gui_main.Main_Window()

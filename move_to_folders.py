import datetime
import pathlib
import os

mypath =r'C:\Users\admin\Pictures\90_deg_consolidated'

# from pathlib import Path
# nameTimeDict = {}

# for path in Path(mypath).iterdir():
#     info = path.stat()  
#     intdate = int(info.st_mtime)
#     nameTimeDict[path.name] = datetime.datetime.fromtimestamp( intdate )
    
os.chdir(mypath)
print("Current Working Directory " , os.getcwd())

#for i in range(1,97):
 #   if not os.path.exists(str(i)):
  #      os.makedirs(str(i))
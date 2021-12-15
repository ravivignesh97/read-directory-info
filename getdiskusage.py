#!/usr/bin/python3
import argparse
import json
import logging
import os
import glob
import subprocess

logging.basicConfig(level=logging.INFO)

def check_valid_folder_path(folderpath):
    if folderpath.startswith("/") and '.' not in folderpath and len(folderpath) > 1:
        return True
    else:
        return False

def is_mount_path(folderpath):
    ismount = os.path.ismount(folderpath)
    return ismount

def getdisksizeinfo(folderpath):
    """ returns disk usage as folder list  """
    try:
        if check_valid_folder_path(folderpath):
            output = {"files":[]}
            for name in glob.glob(folderpath+"/*", recursive=False):
                size = subprocess.check_output(['du','-s', name]).split()[0].decode('utf-8')
                output['files'].append({name : size})
            if is_mount_path(folderpath):
                output['mount']=True
            else:
                output['mount']=False
            return output
        else:
            return None
    except Exception as e:
        print("Error: "+str(e))
        return { "error" : str(e)}

parser  = argparse.ArgumentParser('''
script returns disk usage as folder list  

Example usage: 
python3 getdiskusage.py /data

''')
parser.add_argument('folderpath',type = str,  help="provide the folderpath")

if __name__ == '__main__':
    try:
        args = parser.parse_args()
        print("\n")
        print("-----------Input request information-------")
        print("Mount Path: "+str(args.folderpath))
        folderpath = args.folderpath
        if check_valid_folder_path(folderpath):
            pass
        else:
            print("Invalid folderpath")
            exit()
        response=getdisksizeinfo(folderpath)
        if "files" in response:
            print(json.dumps(response, indent=4))
        else:
            print(response)
        print("------Script completed--------")
        print("\n\n")
    except Exception as e:
        print(e)
        




    


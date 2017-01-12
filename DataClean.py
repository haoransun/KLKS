## AddDSG
#tricky for index -4 of each line, why?
"""
Auther:Haoran
This is used to add observer type obesever type "DSG" to 3rd line 
in each .dat files.
To use it,pull it to the dir with .dat files and run in python 3

update: also can take the " away from the reference paper
"""
import os
obs='DSG\n'

def getDataFiles():
    """
    put all the .dat files in the same directory in a list
    try to make sure you only open .dat files a
    nd don't touch the total dat file KLKS.dat
    """
    global FileList
    FilesInFolder=os.listdir(os.getcwd())
    print(FilesInFolder)
    FileNames=[x for x in FilesInFolder if os.path.splitext(x)[-1]==".dat"
          and os.path.splitext(x)[0]!="KLKS" ]
    FileList=FileNames


def AddDSG():
    """
    read each line as elmt of a list ,change the 3rd line to the obs
    then overwrite the original whole file
    """
    for item in FileList:
        try:
            with open(item,'r') as f:
                file=f.readlines()
                file[2]=obs
                #print(file[1][-4])
                #tricky for index -4, why?
                if file[1][0]=='"' and file[1][-4]=='"' :
                    #file is str type, not list,cann't use list operation
                   file[1]=file[1][1:-4]+"\n"
                f=open(item,'w+')
                f.writelines(file)
                f.close() 
        except:
            print("Can't found",str(item))
def _main_():
    getDataFiles()
    AddDSG()
    
_main_()

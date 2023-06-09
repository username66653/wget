import subprocess
import os
import shutil
import tkinter
import warnings
warnings.warn("started")
delete=0
while True:
    mapp=tkinter.Tk()
    def createfile():
        filenamer=input("filename: ")
        file=open(file=f"C:\\systemos\\{filenamer}",mode="w")
        file.close()
    def deletefile():
        filenamera=input("filename: ")
        sure=input("are you sure to delete the file?: ")
        if sure=="no":
            return 0
        delete=0
        if sure=="yes":
            os.remove(filenamera)
        delete=1
        files=os.scandir(r"C:\systemos\home")
    os.chdir(r"C:\systemos\home")
    files=os.scandir(r"C:\systemos\home")
    for file in files:
        def runfile():
            filenamerar=file.name
            subprocess.Popen(file.name,shell=True)
        b=tkinter.Button(text=f"{file.name} {file.path}",command=runfile)
        if delete==1:
            b.destroy()
        b.pack()
    def turnoff():
        subprocess.Popen("taskkill /F /IM python.exe", shell=True)
    tkinter.Button(text="create file",command=createfile).pack()
    tkinter.Button(text="delete file",command=deletefile).pack()
    tkinter.Button(text="turn off OS",command=turnoff).pack()
    tkinter.Label(text="close window to refresh").pack()
    mapp.mainloop()

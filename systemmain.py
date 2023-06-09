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
        filename=input("filename: ")
        file=open(file=f"C:\\Users\\maksf\\Downloads\\fabric-example-mod-1.19\\home\\{filename}",mode="w")
        file.close()
    def deletefile():
        filename=input("filename: ")
        sure=input("are you sure to delete the file?: ")
        if sure=="no":
            return 0
        delete=0
        if sure=="yes":
            os.remove(filename)
        delete=1
        files=os.scandir(r"C:\Users\maksf\Downloads\fabric-example-mod-1.19\home")
    os.chdir(r"C:\Users\maksf\Downloads\fabric-example-mod-1.19\home")
    files=os.scandir(r"C:\Users\maksf\Downloads\fabric-example-mod-1.19\home")
    for file in files:
        def runfile():
            filename=file.name
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
    print(f"added {tkinter.Button}")
    print(deletefile())
    mapp.mainloop()

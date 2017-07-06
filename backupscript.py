import tkinter as tk
import zipfile, os
import time, shutil
from tkinter.filedialog import askdirectory

class Application(tk.Frame):
    def __init__(self, master=None):
        master.minsize(width=250, height=60)
        super().__init__(master)
        self.pack()
        self.create_backup()

    def backupToZip(folder):

        os.getcwd()
        print(os.getcwd())
        os.chdir('c:\\temp')
        
        tlocal = time.localtime()
        timestamp = time.strftime('%b-%d-%Y_%H%M', tlocal) # Timestamp.

        folder = askdirectory(title="Choose folder to backup") # Open dir.
        folder = os.path.abspath(folder)

        while True:
            zipFilename = os.path.basename(folder) + '_' + str(timestamp) + '.zip' # Adding timestamp.
            if not os.path.exists(zipFilename):
                break

        # Create zip file.
        print('Creating %s...' % (zipFilename))
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        # Walk folders.
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in %s...' % (foldername))
            # Add folder to zip.
            backupZip.write(foldername)

            # Add files.
            for filename in filenames:
                if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                    continue 
                backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        src = (r"c:\\temp\\" + zipFilename)
        outfolder = askdirectory(title="Backup drive")
        shutil.move(src, outfolder) # move Data.
        print('Done.')
        

    def create_backup(self):

        self.backup = tk.Button(self, text="Scotty, Back me up!", command=self.backupToZip) # Backup Button.
        self.backup.pack(side="top")

        self.quit = tk.Button(self, text="Hasta la vista, Baby", command=root.destroy) # Exit.
        self.quit.pack(side="bottom")


root = tk.Tk(className = "Fast backup")
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()

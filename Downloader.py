from tkinter import *
from tkinter import messagebox, filedialog
import os
from urllib.request import urlopen, HTTPError, URLError
import _thread


fln = ' '
filesize = ' '

def startDownload():
    global fln
    fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File", filetypes=(("JPG Image File", "*.jpg"), ("PNG Image File", "*.png"),\
                                                                                              ("All files", "*.*")))
    filename.set(os.path.basename(fln))
    _thread.start_new_thread(initDownload, ())


def initDownload():
        global filesize
        furl = url.get()
        target = urlopen(furl)
        meta = target.info
        filesize = float(meta['Content-length'])
        filesize_mb = round((filesize / 1024 / 1024), 2)
        downloaded = 0
        chunks = 1024 * 5
        with open(fln, "wb") as f:
                while True:
                    parts = target.read(chunks)
                    if not parts:
                        messagebox.showinfo("Download Complete", "Your download is successfully completed")
                        break
                        downloaded += chunks
                        percent = round(((downloaded / filesize) * 100), 2)
                        if percentage > 100:
                            percentage = 100
                        download_progress.set(str(round((downloaded / 1024 / 1024), 2))+" MB / "+str(filesize_mb)+" MB")
                        download_percentage.set(str(percentage)+"%")
                        f.write(parts)
                    f.close()




def exitProg():
    if messagebox.askyesno("Exit Program?", "Are you sure you want to exit the program?") == False:
        return False
    exit()

root = Tk()

url = StringVar()
filename = StringVar()
download_progress = StringVar()
download_percentage = StringVar()

download_progress.set("N/A")
download_percentage.set("N/A")

wrapper = LabelFrame(root, text="File URL")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

wrapper2 = LabelFrame(root, text="Download Information")
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

label = Label(wrapper, text="Download URL: ")
label.grid(row=0, column=0, padx=10, pady=10)

textbox = Entry(wrapper, textvariable=url)
textbox.grid(row=0, column=1, padx=5, pady=10)

button1 = Button(wrapper, text="Download", command=startDownload)
button1.grid(row=0, column=2, padx=5, pady=10)

label2 = Label(wrapper2, text="File: ")
label2.grid(row=0, column=0, padx=10, pady=10)
label3 = Label(wrapper2, textvariable=filename)
label3.grid(row=0, column=1, padx=10, pady=10)

label4 = Label(wrapper2, text="Download Progress")
label4.grid(row=1, column=0, padx=10, pady=10)
label5 = Label(wrapper2, textvariable=download_progress)
label5.grid(row=1, column=1, padx=10, pady=10)

label6 = Label(wrapper2, text="Download Percentage")
label6.grid(row=2, column=0, padx=10, pady=10)
label7 = Label(wrapper2, textvariable=download_percentage)
label7.grid(row=2, column=1, padx=10, pady=10)

Button(wrapper2, text="Exit Downloader", command=exitProg).grid(row=3, column=0, padx=10, pady=10)

root.geometry("450x400")
root.title("Danyaal's Downloader v1.0")
root.resizable(True, True)
root.mainloop()

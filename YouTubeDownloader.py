from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#Functions 

##openLocation function 
Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        downloadLabel.config(text=Folder_Name, fg="green")
        DownloadVideo()
    else:
        downloadLabel.config(text="Chose folder to save", fg="red")


##Download function 
def DownloadVideo():
    try:
        choice = ytbChoice.get()
        url = urlEntry.get()


        if(len(url) > 1):
            urlError.config(text="")
            yt = YouTube(url)
            

            if(choice == choices[0]):
                select = yt.streams.filter(progressive = True).get_highest_resolution()
            elif(choice == choices[1]):
                select = yt.streams.filter(progressive = True).get_lowest_resolution()
            elif(choice == choice[2]):
                select = yt.streams.filter(only_audio=True).first()
        else:
            urlError.config(text="Paste URL again!", fg="red")
        select.download(Folder_Name)
        downloadLabel.config(text="Download Complete!", fg="green")
    except Exception as err:
        print(err)


#UI

root = Tk()
root.title('Youtube Video Downloader')
root.columnconfigure(0, weight=1) #set all content in the center 

#The title 

title = Label(root, text="YouTube Video Downloader",
       fg= "red",
       font= ('jost', 20))
title.grid(row=0, padx = 100, pady=20)

urlLabel = Label(root, text="Paste Video URL", font=('jost', 15))
urlLabel.grid(row=1)


#URL textbox
urlEntry = Entry(root, width=40, fg="blue", font=("jost", 15))
urlEntry.grid(row=2, pady=5)


#Error label 

urlError = Label(root, text="", fg="red", font=("jost", 13))
urlError.grid(row=3)

choiceLabel = Label(root, text="Chose type and quality", font=('jost, 15'))
choiceLabel.grid(row=4)


#combobox
choices = ["High quality Video", "Low quality Video", "Audio File"]
ytbChoice = ttk.Combobox(root, values=choices, font=('jost', 15))
ytbChoice.grid(row=5, pady=10)

#Button
downloadBtn = Button(root, command=openLocation, text="Download", width=20, bg="red", fg="White", font=('jost', 15))
downloadBtn.grid(row=6, pady=10)



downloadLabel = Label(root, text="", fg="red", font=('jost', 13))
downloadLabel.grid(row=7, pady= 10)


root.mainloop()


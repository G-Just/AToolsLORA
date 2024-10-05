import tkinter
import customtkinter
from CTkListbox import *

# System setting
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# App frame
app = customtkinter.CTk()
app.geometry("1000x900")

# Functions
def search():
    pass

def selectBot():
    pass

# Frames
mainBotListFrame = customtkinter.CTkFrame(app, width=305, height=870)
mainOptionsFrame = customtkinter.CTkFrame(app, width=645, height=870)

searchGroupDiv = customtkinter.CTkFrame(mainBotListFrame, width=300, height=850, bg_color='transparent')
botListDiv = customtkinter.CTkFrame(mainBotListFrame, width=300, height=840, bg_color='transparent')

# Ui elements
title = customtkinter.CTkLabel(app, text = 'Alora Bot', font = ('Arial Rounded MT', 30))

searchInput = customtkinter.CTkEntry(searchGroupDiv,height=25, placeholder_text="Search...")
searchButton = customtkinter.CTkButton(searchGroupDiv,width=50, height=25, text="🔎", command=search)

botListBox = CTkListbox(botListDiv, command=selectBot)
botListBox.insert(0, 'Bot 1')
botListBox.insert(1, 'Bot 2')
botListBox.insert(2, 'Bot 3')


# Insert all Ui elements
title.pack(pady=(15,0))

mainBotListFrame.pack(side = 'left', pady=15, padx=(15,0))
searchGroupDiv.pack(side = 'top')
searchInput.pack(side = 'left', padx=5, pady=(5,0))
searchButton.pack(side = 'left', padx=5, pady=(5,0))
botListDiv.pack(side = 'top', pady=(10,0))
botListBox.pack(side = 'top')

mainOptionsFrame.pack(side = 'right',pady=15, padx=(0,15))

# Run app
app.mainloop()
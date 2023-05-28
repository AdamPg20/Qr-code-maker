import customtkinter as ctk
import os
import qrcode


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.geometry("350x420")
root.resizable(False, False)
root.iconbitmap("favicon.ico")
root.title("QR Code")


path = 'QRCocde'


# check whether directory already exists
if not os.path.exists(path):
    os.mkdir(path)

else:
    pass

os.chdir('QRCocde')


def ExitCommand():
    root.destroy()


def OpenFileCommand():
    os.startfile(r'Pictures')


def about_window():
    about = ctk.CTkToplevel(root)
    about.geometry("300x200")
    about.title("About")

    MyName = ctk.CTkLabel(about,
                          text="Made by AdamPg",
                          font=("Ubuntu", 18))
    MyName.pack(pady=5)

    CtK = ctk.CTkLabel(about,
                       text="Made using customtkinter in python",
                       font=("Ubuntu", 15))
    CtK.pack(pady=5)

    def Exitabout():
        about.destroy()

    exitabout = ctk.CTkButton(about,
                              text="Exit",
                              font=("Ubuntu", 20),
                              fg_color='#d90429',
                              hover_color='#a4133c',
                              command=Exitabout)
    exitabout.pack(pady=20)

    verion = ctk.CTkLabel(about,
                          text="V 0.1",
                          font=("Ubuntu", 20),
                          )
    verion.pack()


def generateCode():
    obj_qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # using the add_data() function
    obj_qr.add_data(Qr_Data.get())
    # using the make() function
    obj_qr.make(fit=True)
    # using the make_image() function
    qr_img = obj_qr.make_image(fill_color=ColorList.get(), back_color="white")
    # saving the QR code image
    qr_img.save(File_Name.get() + '.png')


DataLable = ctk.CTkLabel(root,
                         text="Put your data hear",
                         fg_color="transparent",
                         font=('Ubuntu', 15))
DataLable.place(x=10, y=20)

Qr_Data = ctk.Variable()
DataEntry = ctk.CTkEntry(root,
                         font=('Ubuntu', 15),
                         width=180,
                         textvariable=Qr_Data)
DataEntry.place(x=155, y=20)

ColorLable = ctk.CTkLabel(root,
                          text="Chous a color",
                          font=('Ubuntu', 15))
ColorLable.place(x=10, y=60)


Fill_Color_List = ["black",
                   "red",
                   "blue",
                   "green",
                   "purple",
                   "cyan",
                   "Yellow"]

'''
def color(choois):
    print("this is " + choois)
'''

ColorList = ctk.CTkOptionMenu(root,
                              values=Fill_Color_List,
                              font=('Ubuntu', 15),
                              width=180
                              )
ColorList.set("black")
ColorList.place(x=155, y=60)


FileNameLable = ctk.CTkLabel(root,
                             text="Put a file name hare",
                             font=('Ubuntu', 15))
FileNameLable.place(x=10, y=100)


File_Name = ctk.Variable()
FileNameEntery = ctk.CTkEntry(root,
                              font=('Ubuntu', 15),
                              width=180,
                              textvariable=File_Name)
FileNameEntery.place(x=155, y=100)


GeneratButton = ctk.CTkButton(root,
                              text="Generate",
                              font=('Ubuntu', 30),
                              width=200,
                              height=50,
                              command=generateCode
                              )
GeneratButton.place(x=80, y=300)
'''
OpenButton = ctk.CTkButton(root,
                           text="Open Folder",
                           font=('Ubuntu', 18),
                           width=150,
                           height=20,
                           fg_color='#5e60ce',
                           hover_color='#7400b8',
                           command=OpenFileCommand
                           )
OpenButton.place(x=80, y=360)
'''

ExitButton = ctk.CTkButton(root,
                           text="Exit",
                           font=('Ubuntu', 18),
                           width=20,
                           height=20,
                           fg_color='#d90429',
                           hover_color='#a4133c',
                           command=ExitCommand
                           )
ExitButton.place(x=235, y=360)

AboutButon = ctk.CTkButton(root,
                           width=140,
                           text="About",
                           height=28,
                           fg_color='#5e60ce',
                           hover_color='#7400b8',
                           font=("Ubuntu", 18),
                           command=about_window
                           )
AboutButon.place(x=80, y=360)


root.mainloop()

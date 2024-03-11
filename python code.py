"""
Created on Thu Mar 31 14:50:55 2022

@author: Rachana
"""
import sys
import os
# import tkinter module
from tkinter import *

# import other necessery modules
import random
import string

# Vigenère cipher for encryption and decryption
import base64

import os



root= Tk()
root.title ("Message Cryptography")


root.configure(relief=SUNKEN)

def about():
    new_window = Toplevel(root)
    new_window.geometry('600x600')
    new_window.title("About Us")
    new_window.resizable(False, False)
    
    about_label= Label(new_window,text="About Us", height=1, bg="#03A9F4",  fg="#ffffff")

    about_label.pack()

    #creating tuple 
    Font_tuples = ("Comic Sans MS", 20 ,"bold")

    about_label.configure(font= Font_tuples)

    frame= Frame(new_window, width=500, height=400)
    frame.pack()
    frame.place(anchor='center',relx=0.5, rely=0.5)
    
    label_mem = Label(frame, text="GROUP MEMBERS:\n1. TANUSHRI PATIL\n2. SUJIT PATIL\n3. RACHANA THAKUR\n\nCLASS:\nTHIRD YEAR COMPUTER ENGINEERING\n\nCOLLEGE:\nCHHTRAPATI SHIVAJI MAHARAJ INSTITUTE OF TECHNOLOGY\n\nNAME OF GUIDE:\nPROF. MAHESH THAKUR\n\n\n\n\n\n", font="Times 15" )
    label_mem.pack(padx=10,pady=10)
      
    label_ver = Label(frame, text="Version 1.0", font="Times 12" )
    label_ver.pack(padx=10,pady=10)

    frame.pack()
    frame.place(anchor='center',relx=0.5, rely=0.5)
    
def encryption():
    encrpt = Toplevel(root)
    # defining size of window
    encrpt.geometry("1200x6000")

    # setting up the title of window
    encrpt.title("Message Encryption For Receiver")

    label_ver = Label(encrpt,font=('helvetica', 50, 'bold'),
                    text="SECRET MESSAGING \n Vigenère Cipher",
                    fg="Blue", bd=10, anchor='w' )
    label_ver.pack(padx=10,pady=10)

    Tops = Frame(encrpt, width=1600, relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(encrpt, width=800, relief=SUNKEN)
    f1.pack(side=TOP)

    # ==============================================

    lblInfo = Label(Tops,font=('Times 12', 25, 'bold'),
                    text="ENCRYPTION FOR SENDER",
                    fg="violet", bd=20, anchor='w' )

    lblInfo.grid(row=0, column=0)

    # Initializing variables
    Msg = StringVar()
    key = StringVar()
    mode = StringVar()
    Result = StringVar()

    # labels for the message
    lblMsg = Label(f1, font=('arial', 16, 'bold'),
                text="MESSAGE-", bd=16, anchor="w")

    lblMsg.grid(row=1, column=0)
    # Entry box for the message
    txtMsg = Entry(f1, font=('arial', 16, 'bold'),
                    textvariable=Msg, bd=10, insertwidth=4,
                    bg="powder blue", justify='left')

    txtMsg.grid(row=1, column=1)

    # labels for the result
    lblResult = Label(f1, font=('arial', 16, 'bold'),
                    text="CIPHER TEXT=", bd=16, anchor="w")

    lblResult.grid(row=1, column=2)

    # Entry box for the result

    txtResult = Entry(f1, font=('arial', 16, 'bold'),
                    textvariable=Result, bd=10, insertwidth=4,
                    bg="powder blue", justify='left')
    txtResult.grid(row=1, column=3)

    # labels for the key
    lblkey = Label(f1, font=('arial', 16, 'bold'),
                text="PUBLIC KEY-", bd=16, anchor="w")

    lblkey.grid(row=2, column=0)

    # Entry box for the key
    txtkey = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=key, bd=10, insertwidth=4,
                bg="powder blue", justify='left')
    txtkey.insert(0,random.randint(100000000000, 999999999999))
    #txtkey.insert(0, "".join(random.choices(string.ascii_lowercase, k=12)))

    txtkey.grid(row=2, column=1)

    #REFRESH BUTTON

    def refresh():
        key.set("")
        txtkey.insert(0,random.randint(100000000000, 999999999999))
        #txtkey.insert(0, "".join(random.choices(string.ascii_lowercase, k=12)))

    # Exit button
    btnRefresh = Button(f1, padx=5, pady=5,height=2,bd=10,
                    fg="white", font=('arial',12, 'bold'),
                    width=5, text="Refresh", bg="blue",
                    command=refresh).grid(row=2, column=2)


    # labels for the mode
    lblmode = Label(f1, font=('arial', 16, 'bold'),
                    text="MODE-",
                    bd=16, anchor="w")

    lblmode.grid(row=3, column=0)
    # Entry box for the mode
    txtmode = Entry(f1, font=('arial', 16, 'bold'),
                    textvariable=mode, bd=10, insertwidth=4,
                    bg="powder blue", justify='left')
    txtmode.insert(0, "Encrypt")
    txtmode.config(state=DISABLED)

    txtmode.grid(row=3, column=1)


    # Vigenère cipher

    # Function to encode

    def encode(key, msg):
        enc = []
        for i in range(len(msg)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(msg[i]) +
                        ord(key_c)) % 256)
            enc.append(enc_c)
            print("enc:", enc)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def Results():
        print("Plain Text= ", (Msg.get()))

        msg = Msg.get()
        k = key.get()
        m = mode.get()

        if (m == 'Encrypt'):
            Result.set(encode(k, msg))
        else:
            print("Please use decryption for decrypt message")
    # exit function

    def qHome():
        encrpt.destroy()

    
    # Function to reset the window

    def Reset():

        Msg.set("")
        key.set("")
       # mode.set("")
        Result.set("")

    # Show message button
    btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="white",
                    font=('arial', 16, 'bold'), width=10,
                    text="Encrypt", bg="powder blue",
                    command=Results).grid(row=7, column=1)

    # Reset button
    btnReset = Button(f1, padx=16, pady=8, bd=10,
                    fg="white", font=('arial', 16, 'bold'),
                    width=10, text="Reset", bg="blue",
                    command=Reset).grid(row=7, column=2)

    # Exit button
    btnExit = Button(f1, padx=16, pady=8, bd=10,
                    fg="white", font=('arial', 16, 'bold'),
                    width=10, text="Home", bg="red",
                    command=qHome).grid(row=7, column=3)

    # keeps window alive
    encrpt.mainloop()

def decryption():
       
    decrypt = Toplevel(root)
    # defining size of window
    decrypt.geometry("1200x6000")

    # setting up the title of window
    decrypt.title("Message Decryption for Receiver")

    label_ver = Label(decrypt,font=('helvetica', 50, 'bold'),
                    text="SECRET MESSAGING \n Vigenère Cipher",
                    fg="Blue", bd=10, anchor='w' )
    label_ver.pack(padx=10,pady=10)

    Tops = Frame(decrypt, width=1600, relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(decrypt, width=800, relief=SUNKEN)
    f1.pack(side=TOP)

    # ==============================================

    lblInfo = Label(Tops,font=('Times 12', 25, 'bold'),
                    text="DECRYPTION FOR RECEIVER",
                    fg="violet", bd=20, anchor='w' )

    lblInfo.grid(row=0, column=0)


    # Initializing variables
    Msg = StringVar()
    key = StringVar()
    mode = StringVar()
    Result = StringVar()

        
    # labels for the message
    lblMsg = Label(f1, font=('arial', 16, 'bold'),
                text="CIPHER TEXT-", bd=16, anchor="w")

    lblMsg.grid(row=1, column=0)
    # Entry box for the message
    txtMsg = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=Msg, bd=10, insertwidth=4,
                bg="powder blue", justify='left')

    txtMsg.grid(row=1, column=1)
    # labels for the key
    lblkey = Label(f1, font=('arial', 16, 'bold'),
                text="PUBLIC KEY-", bd=16, anchor="w")

    lblkey.grid(row=2, column=0)

    # Entry box for the key
    txtkey = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=key, bd=10, insertwidth=4,
                bg="powder blue", justify='left')

    txtkey.grid(row=2, column=1)

    # labels for the mode
    lblmode = Label(f1, font=('arial', 16, 'bold'),
                    text="MODE-",
                    bd=16, anchor="w")

    lblmode.grid(row=3, column=0)
    # Entry box for the mode
    txtmode = Entry(f1, font=('arial', 16, 'bold'),
                    textvariable=mode, bd=10, insertwidth=4,
                    bg="powder blue", justify='left')
    txtmode.insert(0, "Decrypt")
    txtmode.config(state=DISABLED)

    txtmode.grid(row=3, column=1)

    # labels for the result
    lblResult = Label(f1, font=('arial', 16, 'bold'),
                    text="MESSAGE-", bd=16, anchor="w")

    lblResult.grid(row=2, column=2)

    # Entry box for the result
    txtResult = Entry(f1, font=('arial', 16, 'bold'),width= 25,
                    textvariable=Result, bd=10, insertwidth=4,
                    bg="powder blue", justify='left')

    txtResult.grid(row=2, column=3)

    # Vigenère cipher

   

    # Function to decode
    def decode(key, enc):
        dec = []

        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) -
                        ord(key_c)) % 256)

            dec.append(dec_c)
            print("dec:", dec)
        return "".join(dec)

    def Results():
        print("Cipher Text= ", (Msg.get()))

        msg = Msg.get()
        k = key.get()
        m = mode.get()

        if (m == 'Decrypt'):        
            Result.set(decode(k, msg))

        else:
            print("Please use Encryption mode to encrypt messages")

    # exit function
    def qHome():
         decrypt.destroy()
    # Function to reset the window

    def Reset():

        Msg.set("")
        key.set("")
        #mode.set("")
        Result.set("")

    # Show message button
    btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="white",
                    font=('arial', 16, 'bold'), width=9,
                    text="Decrypt", bg="powder blue",
                    command=Results).grid(row=7, column=1)

    # Reset button
    btnReset = Button(f1, padx=16, pady=8, bd=10,
                    fg="white", font=('arial', 16, 'bold'),
                    width=10, text="Reset", bg="blue",
                    command=Reset).grid(row=7, column=2)

    # Exit button
    btnHome = Button(f1, padx=16, pady=8, bd=16,
                    fg="white", font=('arial', 16, 'bold'),
                    width=9, text="Home", bg="red",
                    command=qHome).grid(row=7, column=3)

    # keeps window alive
    decrypt.mainloop()




main_frame= Frame(root, width=1200, height=6000, relief=SUNKEN)
main_frame.pack()
main_frame.place(anchor='center',relx=0.5, rely=0.5)

welcome_text= Label(main_frame,font=('Times 12', 25, 'bold'),bd=15,text="WELCOME IN MESSAGE CRYPTOGRAPHY", height=1, bg="blue",  fg="#ffffff")

welcome_text.pack()

#creating tuple 
Font_tuple = ("Comic Sans MS", 20 ,"bold")

welcome_text.configure(font= Font_tuple)


label_img = Label(main_frame,bd=20,width=1000)
label_img.pack()

btn_encrypt = Button (main_frame, text="ENCRYPT (SENDER)", font=('arial', 12, 'bold'),command=encryption,height=3,width=25, bg="#006C62", fg='#fff')
btn_encrypt.pack(padx = 20, pady= 20)

btn_decrypt = Button (main_frame, text="DECRYPT (RECEIVER)",  font=('arial', 12, 'bold'),command=decryption , height=3,width=25,  bg="#006C62", fg='#fff')
btn_decrypt.pack(padx = 20, pady= 20)

btn_about = Button (main_frame, text="ABOUT US", font=('arial', 12, 'bold'), command=about, height=2,width=12,  bg="#006C62", fg='#fff')
btn_about.pack(padx = 20, pady= 20)

btn_exit = Button (main_frame, text="EXIT",  font=('arial', 12, 'bold'),command=root.destroy, height=2, width=8,  bg="red", fg='#fff')
btn_exit.pack(padx = 20, pady= 20)

main_frame.pack()
main_frame.place(anchor='center',relx=0.5, rely=0.5)

 
root.geometry('1200x6000')

root.mainloop() 



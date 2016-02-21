import tkinter

window = tkinter.Tk()
window.title("Spanish Analyzer")
window.geometry("800x400")
lblUser = tkinter.Label(window,text = "Username")
txtUser = tkinter.Entry(window)
lblPassword = tkinter.Label(window,text = "Password")
txtPassword = tkinter.Entry(window)

lblUser.pack()
txtUser.pack()
lblPassword.pack()
txtPassword.pack()

window.mainloop()

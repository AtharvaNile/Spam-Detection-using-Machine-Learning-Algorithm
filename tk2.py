#***************************************************
#dev-@atharva_nile


from Tkinter import *
from spam import *
from pyscreenshot import grab
import PIL

window = Tk()

topFrame= Frame(window)
topFrame.pack(side=TOP)
bottomFrame= Frame(window)
bottomFrame.pack(side=BOTTOM)


window.title("Spdec")

label1=Label(topFrame, text="FROM").grid(row=0)
#label1.pack(side=LEFT)
label2=Label(topFrame, text="TO").grid(row=1)
#label2.pack(side=LEFT)
label3=Label(topFrame, text="SUBJECT").grid(row=2)
#label3.pack(side=LEFT)
label4=Label(topFrame, text="Message").grid(row=3)
#label3.pack(side=LEFT)

e1=Entry(topFrame)
e2=Entry(topFrame)
e3=Entry(topFrame)
mail_msg=Entry(topFrame)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
mail_msg.grid(row=3,column=1)

yospam="Your mail has been classified as Spam."
nospam="Your mail has been classified as Non-spam."

msg1=Message(bottomFrame,text=yospam)
msg2=Message(bottomFrame,text=nospam)

def clicked():
	spam_probability = classify(mail_msg.get(), spam_training_set, 0.2)
	ham_probability = classify(mail_msg.get(), ham_training_set, 0.8)
	if spam_probability > ham_probability:
				
		msg1.config(bg='red', font=('times', 16, 'italic'))
		msg1.pack()
		msg2.pack_forget()
		
	else:
		msg2.config(bg='green', font=('times', 16, 'italic'))
		msg2.pack()
		msg1.pack_forget()

btn = Button(bottomFrame, text="Submit",bg="green" ,fg="white",command=clicked)
btn.pack()

btn2 = Button(bottomFrame,text="delete the spam message", command=msg1.forget)
btn2.pack()

btn3 = Button(bottomFrame,text="delete the non spam message", command=msg2.forget)
btn3.pack()

def repo():
	im = grab(bbox=(0, 0, 1280, 1024))
	im.save('/root/Desktop/sdl/screenshots/Screenshot.jpg', 'JPEG')
	print('A message has been reported...')


btn4 = Button(bottomFrame,text="Report", command=repo)
btn4.pack()


window.mainloop()

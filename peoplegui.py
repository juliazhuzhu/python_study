#!/usr/bin/python
from tkinter import * 
from tkinter.messagebox import showerror 
from tkinter.messagebox import showinfo
import shelve
from person import Person

def reply(name):
	showinfo(title='Reply', message='Hello %s!' % name)

def makeWidgets(db,fieldnames):
	window = Tk()
	window.title('People Shelve')
	form = Frame(window)
	form.pack()
	entries = {}

	for (ix, label) in enumerate( ('key',) + fieldnames):
		lab = Label(form, text=label)
		ent = Entry(form)
		lab.grid(row=ix, column=0)
		ent.grid(row=ix, column=1)
		entries[label] = ent

	Button(window, text="Fetch", command=(lambda: fetchRecord(db,entries,entries['key'].get()))).pack(side=LEFT)
	Button(window, text="Update",command=(lambda: updateRecord(db,entries,entries['key'].get()))).pack(side=LEFT)
	Button(window, text="Quit", command=window.quit).pack(side=RIGHT)

	return window




def fetchRecord(db,entries,key):
	try:
		record = db[key]
	except:
		showerror(title='error', message='no such key')
	else:
		for field in fieldnames:
			entries[field].delete(0,END)
			entries[field].insert(0,repr(getattr(record,field)))

def updateRecord(db,entries,key):
	if key in db:
		record = db[key]
	else:
		record = Person(name='?',age='?')

	for field in fieldnames:
		setattr(record,field,eval(entries[field].get()))
	db[key] = record

db = shelve.open('class-shelve')
fieldnames = ('name', 'age', 'job', 'pay')
window = makeWidgets(db,fieldnames)
window.mainloop()
db.close()
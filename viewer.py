import matplotlib.pyplot as plt
import pydicom.data
import os
import tkinter as tk

def dcm_viewer(path: str):
	path_components = os.path.split(path)
	if path_components[1] == "":
		return
	if path_components[0] == "":
		base = os.getcwd()
		file = path_components[1]
	else:
		base = path_components[0]
		file = path_components[1]
	filename = pydicom.data.data_manager.get_files(base, file)[0]
	ds = pydicom.dcmread(filename)
	plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
	plt.show()
	return

def dcm_gui():
	window = tk.Tk()
	prompt = tk.Label(window, text="Please enter the absolute or relative path of the .dcm file", foreground = "white", background = "black", width = 50, height = 10)
	entry = tk.Entry(window, width = 50)
	prompt.pack()
	entry.pack()
	entry.bind("<Return>", lambda command: _on_change(window, entry))
	window.mainloop()
	return

def _on_change(window, entry):
	path = entry.get()
	window.destroy()
	dcm_viewer(path)
	return

import matplotlib.pyplot as plt
import pydicom.data
import os
import tkinter as tk
import pathlib

def viewer(path: str):
	if os.path.exists(path) == False:
		assert False, "No Non-Existent File ERROR implemented"
	path_components = os.path.split(path)
	if path_components[1] == "":
		assert False, "No File ERROR not implemented"
		return
	if path_components[0] == "":
		base = os.getcwd()
		current_directory = pathlib.Path(".")
		found_match = False
		for current_file in current_directory.iterdir():
			if str(current_file).upper() == path.upper():
				file = str(current_file)
				found_match = True
				break
		if found_match != True:
			assert False, "Relative File Not Found ERROR not implemented"
			return
	else:
		base = path_components[0]
		file = path_components[1]
	filename = pydicom.data.data_manager.get_files(base, file)[0]
	ds = pydicom.dcmread(filename)
	plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
	plt.show()
	return

def viewer_gui():
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
	viewer(path)
	return

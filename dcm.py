import matplotlib.pyplot as plt
import pydicom.data
import os
import tkinter as tk
import pathlib
import numpy as np
from skimage import img_as_ubyte, exposure

def viewer(path: str):
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
	arr = np.uint8((ds.pixel_array / ds.pixel_array.max()) * 255)
	pixel_subtract = 220
	for array in arr:
		for i in range(len(array)):
			if array[i] < pixel_subtract:
				array[i] = 0
				continue
			array[i] = array[i] - pixel_subtract
	plt.imshow(arr, cmap='gray')
	plt.show()
	col_row_string = ' '.join(reversed([str(x) for x in arr.shape]))
	pgmheader = '\n'.join(('P5', col_row_string, str(arr.max())))
	pgmheader += '\n'
	with open('MRImage.pgm', 'wb') as file:
		file.write(pgmheader.encode('ascii'))
		file.write(arr.tobytes())
	return

def viewer_gui():
	window = tk.Tk()
	window.title("Coffman Medical")
	photo = tk.PhotoImage(file="icon.png")
	window.iconphoto(False, photo)
	prompt = tk.Label(window, text="Please enter the absolute or relative path of the .dcm file", foreground = "white", background = "black", width = 50, height = 10)
	entry = tk.Entry(window, width = 50)
	prompt.grid(row=0,column=0)
	entry.grid(row=1, column=0)
	entry.bind("<Return>", lambda command: _on_change(window, entry))
	window.mainloop()
	return

def _on_change(window, entry):
	path = entry.get()
	window.destroy()
	viewer(path)
	return

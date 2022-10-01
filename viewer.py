  1 import matplotlib.pyplot as plt
  2 import pydicom
  3 import pydicom.data
  4 
  5 def viewer(base, file):
  6         base = r"{}".format(base)
  7         filename = pydicom.data.data_manager.get_files(base, file)[0]
  8         ds = pydicom.dcmread(filename)
  9         plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
 10         plt.show()
 11         return

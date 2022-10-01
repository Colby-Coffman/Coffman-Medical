import matplotlib.pyplot as plt
import pydicom.data

def dcm_viewer(base, file):
  base = r"{}".format(base)
  filename = pydicom.data.data_manager.get_files(base, file)[0]
  ds = pydicom.dcmread(filename)
  plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
  plt.show()
  return

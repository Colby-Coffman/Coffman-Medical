import matplotlib.pyplot as plt
import pydicom
import pydicom.data
base = r"/home/colby_coffman/Code/Workspace"
pass_dicom = "MRBRAIN.DCM"
filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]
ds = pydicom.dcmread(filename)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()

import h5py
from Local_Cell_Density_Project.Updating_HDF_by_Density.Calculate_Local_Density_Class import Local_Density

# Call the class to create the density vectors:
hdf5_file = '/Users/kristinaulicna/Documents/Rotation_2/Example_Movie/HDF/segmented.hdf5'
density_lists = Local_Density(hdf5_file=hdf5_file).Calculate_for_Movie()


# Append those vectors as a group / dataset to the HDF5 file:
f = h5py.File(hdf5_file, 'a')

for channel in [1, 2]:

    if "density_raw" in list(f["objects"]["obj_type_{}".format(channel)]):
        del f["objects"]["obj_type_{}".format(channel)]["density_raw"]

    grp = f["objects"]["obj_type_{}".format(channel)]
    sub = grp.create_dataset(name="density_raw", data=density_lists[channel - 1],
                             shape=(len(density_lists[channel - 1]), 1), dtype="f4")



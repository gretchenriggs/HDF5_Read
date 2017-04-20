import h5py
import numpy as np


if __name__ == '__main__':
    # Select HDF5 file to be read in with h5py and save to h5py object
    filename = '../L1_files/Q2011079034400.L1A_SCI'
    f = h5py.File(filename, 'r')

    # Iterate through groups (heirarchical data structures in our h5py object)
    #   and append each group to a list.
    # Save each dataset in group to dataset
    # Appending each group and dataset to lists just for future reference
    group_key_list = []
    dataset_key_list = []
    for i in xrange(len(f.keys())):
        group_key = f.keys()[i]
        group_key_list.append(group_key)
        for item in list(f[group_key]):
            item = str(item)
            print("{0}/{1}".format(group_key, item))
            exec(item + "= np.array(list(f[group_key][item]))")
            dataset_key_list.append(item)

    # Saving 1st antenna beam (4th dim) and H polarization (5th dim) to
    #   simplify initial test input
    radiom_lavg_pol0_H = radiom_lavg[:,:,:,0,3]

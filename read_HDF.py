import h5py
import numpy as np


if __name__ == '__main__':
    filename = 'L1_files/Q2011079034400.L1A_SCI'
    f = h5py.File(filename, 'r')

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

#  _*_ coding:UTF-8 _*_
# HDF5的读取：
import h5py
# from pandas.tests.extension.numpy_.test_numpy_nested import np
import numpy as np

f = h5py.File('resnet50_coco_best_v2.0.1.h5', 'r')
for group in f.keys():  # 打开h5文件
    # print(group)
    group_read = f[group]
    for subgroup in group_read.keys():
        # print(subgroup)
        dset_read = f[group + '/' + subgroup]
        for dset in dset_read.keys():
            # print(dset)
            dset1 = f[group + '/' + subgroup + '/' + dset]
            print(dset1.name)
            # data = np.array(dset1)
            # print(data.shape)
            # x = data[..., 0]
            # y = data[..., 1]
# print(f.keys())
# dset = f['model_weights']
# print(dset)
# print(dset[0:10])
# b = a['model_weights']
# print(b)
# 取出主键为data的所有的键值
f.close()

import numpy as np

data = [ (1, 2), (3, 4.1), (13, 77) ]
dtype = [('x', float), ('y', float)]

print('\n ndarray')
nd = np.array(data)
print (nd)

print ('\n structured array')

struct_1dtype = np.array(data, dtype=dtype)
print (struct_1dtype)

print('\n structured to ndarray')
struct_1dtype_float = struct_1dtype.view(np.ndarray).reshape(len(struct_1dtype), -1)
print (struct_1dtype_float)

print('\n structured to float: alternative ways')
struct_1dtype_float_alt = struct_1dtype.view((np.float, len(struct_1dtype.dtype.names)))
print (struct_1dtype_float_alt)

# with heterogeneous dtype.
struct_diffdtype = np.array([(1.0, 'string1', 2.0), (3.0, 'string2', 4.1)],
dtype=[('x', float),('str_var', 'a7'),('y',float)])
print('\n structured array with different dtypes')
print (struct_diffdtype)
struct_diffdtype_nd = struct_diffdtype[['str_var', 'x', 'y']].view(np.ndarray).reshape(len(struct_diffdtype), -1)


print('\n structured array with different dtypes to reshaped ndarray')
print (struct_diffdtype_nd)


print('\n structured array with different dtypes to reshaped float array ommiting string columns')
struct_diffdtype_float = struct_diffdtype[['x', 'y']].view(float).reshape(len(struct_diffdtype),-1)
print (struct_diffdtype_float)
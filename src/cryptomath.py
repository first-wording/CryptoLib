import numpy

def ext_euclid(a, b):
    """ 扩展欧几里得算法 """
    if b == 0:
        return (a, 1, 0)
    d, x, y = ext_euclid(b, a % b)
    return (d, y, x-a//b*y)

def inverse_mat(mat):
    """ 求矩阵逆 """
    mat = numpy.array(mat)
    mat_det = numpy.linalg.det(mat)
    mat_inv = numpy.linalg.inv(mat)
    return mat_inv * mat_det


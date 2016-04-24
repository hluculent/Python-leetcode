#-×- coding:utf-8 -*-
"""
snake matrix就是蛇形矩阵，例如输入n = 3时矩阵为：
1 2 6
3 5 7 
4 8 9
"""
N = int(raw_input('Please input a number:'))
for i in range(N):
    for j in range(N):
        m = i + j
        if m < N:
            if m%2 != 0:
                print m*(m+1)/2+1+(m-j),
            else:
                print m*(m+1)/2+1+(m-i),
        else:
            m = 2*N -2 -m
            if m%2 != 0:
                print N*N-(m*(m+1)/2+(m-(N-1-j))),
            else:
                print N*N-(m*(m+1)/2+(m-(N-1-i))),
    print '\n'

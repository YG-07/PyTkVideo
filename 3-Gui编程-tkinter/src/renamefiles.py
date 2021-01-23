#-*- coding:utf-8 -*-
import os

srcf = './img/pukeImage/'
dstf = './img/dist/'

srctmp=''
dsttmp=''
for i in range(1,55):
    try:
        srctmp=srcf+str(i)+'.jpg'
        dsttmp=dstf+str(i)+'.gif'
        os.rename(srctmp,dsttmp)
    except:
        print('Error in ',srcf+str(i)+'.jpg')
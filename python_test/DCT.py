#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import scipy

from scipy import fft
from skimage.io import imread
from skimage.color import rgb2gray
from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc # pip install Pillow
import matplotlib.pylab as pylab
import matplotlib.image as mpimg

def dct2(a):
    return scipy.fft.dct( scipy.fft.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def get_imagedata(path):    
    im =imread(path)
    im_gray=rgb2gray(im)

    hist_value=plt.hist(im.ravel(),256,[0,256])

    imsize = im.shape
    dct_value = np.zeros(imsize)


    for i in r_[:imsize[0]:8]:
        for j in r_[:imsize[1]:8]:
            dct_value[i:(i+8),j:(j+8)] = dct2( im[i:(i+8),j:(j+8)] )
    hist_value2=hist_value[0].astype(int)
    dct_value2=dct_value[0].astype(int)
    hist_final="/".join(str(e) for e in hist_value2)
    dct_final="/".join(str(e) for e in dct_value2)
    return hist_final,dct_final
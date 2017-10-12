
#-*-coding:utf-8-*-
"""
CreatedonThuAug2409:23:432017

@author:Ivan

Twoandn-dimensionaldiscreteFouriertransforms

Thefunctionsfft2andifft2provide2-dimensionalFFT,
andIFFT,respectively.Similar,fftnandifftnproviden-dimensionalFFT,
andIFFT,respectively.

Theexamplebelowdemonstratesa2-dimensionalIFFTandplots
theresulting(2-dimensional)time-domainsignals.
"""

from scipy.fftpack import ifftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

N=30

f,((ax1,ax2,ax3),(ax4,ax5,ax6))=plt.subplots(2,3,sharex='col',sharey='row')

xf=np.zeros((N,N))
xf[0,5]=1
xf[0,N-5]=1
Z=ifftn(xf)

ax1.imshow(xf,cmap=cm.Reds)
ax4.imshow(np.real(Z),cmap=cm.gray)

xf=np.zeros((N,N))
xf[5,0]=1
xf[N-5,0]=1
Z=ifftn(xf)

ax2.imshow(xf,cmap=cm.Reds)
ax5.imshow(np.real(Z),cmap=cm.gray)

xf=np.zeros((N,N))
xf[5,10]=1
xf[N-5,N-10]=1
Z=ifftn(xf)

ax3.imshow(xf,cmap=cm.Reds)
ax6.imshow(np.real(Z),cmap=cm.gray)

plt.show()

"""
Brianca Washington
1001132562
Hw6
"""


import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt 
import soundfile as sf

def processFile(fn, offset):
	orig,fs  = sf.read(fn)
	myfft=0
	
	#apply the FFT to the signal and get the midpoint of the result 
	myfft=np.fft.fft(orig)         
	midpoint= round(len(myfft)/2)  
	myfft[midpoint]=0

	for i in range(offset):
		myfft[midpoint-i]=0
		myfft[midpoint+i]=0
	
	new=np.fft.ifft(myfft)#recreate the signal 

 	# plot them side by side
	plt.title("FFT Noise Removal")
	plt.subplot(1,2,1)
	plt.plot( abs(orig ))
	plt.subplot(1,2,2)
	plt.plot(abs(new))
	plt.show()

 	# create a new wavfile
	sf.write('cleanMusic.wav',new.real , fs)
   
##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 20000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)



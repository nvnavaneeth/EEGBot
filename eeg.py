#code to obtain data

from NeuroPy import NeuroPy
import time

datafile = open("testdata.txt","w+")

object=NeuroPy("COM11",57600) 
#Start communication
object.start()


f=200 #set sampling frequency
t=2   #set sampling time
N=f*2 #no of sample points


datafile.write('%d\n' %f)	
datafile.write('%d\n' %N)

i=0

while i<N:
	
	datafile.write('%d\n' %object.rawValue)
	time.sleep(1/f)
	i=i+1
	
	
	
datafile.close()
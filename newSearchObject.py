
'''
A class to build on 
and produce a binary
search algorithm
'''

import numpy as np
import matplotlib.pyplot as plt
from sys import exit


#####################################

class dataSorter(object):
  '''A class to hold data and provide examples of search algorithms'''

  def __init__(self,numb=100):
    '''Class initialiser'''
    self.numb=numb
    '''为什么这里是（numb）?'''
    self.arr=np.random.random((numb))

  def sortArray(self):
    '''Sort an array'''
    # preserve original array by copying
    copArr=np.copy(self.arr)
    # create workspace
    self.sortArr=np.empty(self.arr.shape)
    # sort the array
    for i in range(0,copArr.shape[0]):
      minN,minInd=self.findMin(copArr)
      self.sortArr[i]=minN
      copArr[minInd]=10000000

  def findMin(self,arr):
    '''A minimum finding function'''
    minN=10000000  # a big number
    minInd=0
    for i in range(0,arr.shape[0]):
      if(arr[i]<minN):
        minN=arr[i]
        minInd=i
    return(minN,minInd)

  def plotter(self):
      '''Add a function to plot a linegraph of the sorted array (y axis) against array index a axis'''
    plt.plot(self.arr)
    plt.show()

    
def binarySearch(self,target):
    '''Binary search for target in x by looping'''
    x = self.arr
    start = 0
    end = len(self.arr)

    mid = (start + end)//2

    # a flag to tell whether find the target or not 
    findTarget = False
   
    while((end-start)>1):
    
        if(x[mid]<target):   # answer is to the right
            start=midP
            midP=(start+end)//2
        elif(x[mid]>target):   # answer is to the left
            end=mid
            mid=(start+end)//2 
        elif(x[mid]==target):  # found answer, unlikely
            foundExact=True  # have found exact answer
            break
    
    # if we have not found the exact answer, find the closest element
    if(findTarget==False):
        sep=np.abs(x[start:end]-v)  # use a slice to find the absolute distance
        mid=sep.argmin()+start     # set mid point as element with smallest distance

    return(x[mid],mid)

import datetime
import random
def bubbleSort(array):
    sorted = False
    while (sorted == False):
        sorted = True
        i = 0
        for i in range(1,len(array)):
            if (array[i] < array[i-1]):
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                sorted = False
avg = datetime.datetime.now()-datetime.datetime.now()
print "start."
for j in range(0,10):
    a=[]
    for i in range(0,100):
        a.append(int(random.random()*100))
    print "Unsorted:",a
    time1= datetime.datetime.now()
    bubbleSort(a)
    avg = avg + (datetime.datetime.now()-time1)
    print "Sorted:",a
print avg

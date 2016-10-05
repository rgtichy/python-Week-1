import random
import datetime
def selectionSort(list):
    d = 1
    l = len(list)
    i = 0
    for d in range(1,l/2):
        s = d - 1
        t = l - 1
        for i in range(d-1,l):
            if (list[i]<list[s]):
                s=i
            if (list[i]>list[t]):
                t=i
        #put lowest found value at spot just before list[d]
        temp = list[d-1]
        list[d-1] = list[s]
        list[s] = temp
        # put highest value at endpoint list[l]
        temp = list[l-1]
        list[l-1] = list[t]
        list[t] = temp
        # move lower bound up, upper bound down
        d = d + 1
        l = l - 1
    return list
sum = datetime.datetime.now()-datetime.datetime.now()
print "start."
for j in range(0,10):
    a=[]
    for i in range(0,10000):
        a.append(int(random.random()*1000))
    print "Unsorted:",a
    time1= datetime.datetime.now()
    selectionSort(a)
    sum = sum + (datetime.datetime.now()-time1)
    print "Sorted  :",a
print sum, "for ten iterations"

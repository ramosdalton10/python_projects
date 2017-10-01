import matplotlib.pyplot as pyt

def plot():
    x= [2,3,4,5]
    y = [15,7,8,9]
    pyt.scatter(x,y, marker='*',s=200)

    # x1 = [2,4,6,8]
    # y1 = [1,3,5,7,]
    # # pyt.plot(x,y)
    # pyt.bar(x,y,label='bar1',color='c')
    # pyt.bar(x1,y1, label = 'bar2',color='b')
    # pyt.legend()
    pyt.title('progress')
    pyt.xlabel('time')
    pyt.ylabel('gain')
    # population_ages = [23,56,33,38,21,78,90,112,45,68,97,67,88,15,55,111,119,100,14,68,44,35,64,74,80]
    # bin = [20,30,40,50,60,70,80,90,100,110,120]
    # pyt.hist(population_ages,bins=bin,histtype='bar',rwidth=.5)
    pyt.show()
plot()
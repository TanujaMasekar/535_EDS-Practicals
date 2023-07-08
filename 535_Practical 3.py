import numpy as np
array3=np.loadtxt("/content/testmarks1.csv",delimiter=',',dtype=str,skiprows=1)
print(array3)
Rollno=[]
Eds=[]
son=[]
Dt=[]
Et=[]
for i in array3:
 Eds.append(float(i[1]))
 son.append(float(i[2]))
 Dt.append(float(i[3]))
 Et.append(float(i[4]))
print(Eds)
print(son)
print(Dt)
print(Et)
m=max(Edsarr)
mi=min(sonarr)
Edsarr=np.array(Eds)
sonarr=np.array(son)
Dtarr=np.array(Dt)
Etarr=np.array(Et)
std=np.std(Dtarr)
med=np.median(Etarr)
var=np.var(Edsarr)
mean=np.mean(sonarr)
sort=np.sort(Dtarr)
search = np.where(sonarr == 26.16)
print(dt)
print("The min of son",mi)
print("The max of eds",m)
print("The std of Dtarr",std)
print("The med of Etarr",med)
print("The var of Edsarr",var)
print("The mean ofsonarr ",mean)
print("The sortedc arr of Dtarr ",sort)
print("The search arr of sonarr ",search)

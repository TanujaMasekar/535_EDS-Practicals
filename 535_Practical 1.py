#Read file
file=open('C:\\Users\\Admin\\Documents\\dataset535\\stud_info.csv','r')
info_dataset=[]
while True:
   data=file.readline()
   if data:
      info_dataset.append(data.replace("\n","").split(','))
   else:
      break
print(info_dataset)
RollNo=[]
Name=[]
Gender=[]
DOB=[]
for row in info_dataset[1:]:
    RollNo.append(row[0])
    Name.append(row[1])
    Gender.append(row[2])
    DOB.append(row[3])
print(RollNo)
print(Name)
print(Gender)
print(DOB)
 #Read file
file=open('C:\\Users\\Admin\\Documents\\dataset535\\stud_placement.csv','r')
placement_dataset=[]
while True:
    data=file.readline()
    if data:
      placement_dataset.append(data.replace("\n","").split(','))
    else:
      break
print(placement_dataset)
RollNo=[]
Company=[]
JobRole=[]
Package=[]
for row in placement_dataset[1:]:
  RollNo.append(row[0])
  Company.append(row[1])
  JobRole.append(row[2])
  Package.append(row[3])
print(Company)
 #Read file
file=open('C:\\Users\\Admin\\Documents\\dataset535\\student_marks.csv','r')
mark_dataset=[]
while True:
  data=file.readline()
  if data:
    mark_dataset.append(data.replace("\n","").split(','))
  else:
    break
print(mark_dataset)
Roll=[]
Maths=[]
Physics=[]
Chemistry=[]
Total=[]
Percentage=[]
for row in mark_dataset[1:]:
  Roll.append(row[0])
  Maths.append(row[1])
  Physics.append(row[2])
  Chemistry.append(row[3])
  Total.append(row[4])
  Percentage.append(row[5])
studentdata=[]
studentdata.append(RollNo)
studentdata.append(Name)
studentdata.append(Gender)
studentdata.append(DOB)
studentdata.append(Company)
studentdata.append(JobRole)
studentdata.append(Package)
studentdata.append(Maths)
studentdata.append(Physics)
studentdata.append(Chemistry)
studentdata.append(Total)
studentdata.append(Percentage)
print(studentdata)
fw=open("C:\\Users\\Admin\\Documents\\dataset535\\All_Stud_detail.csv","w")
data_to_write=[]
for i in range(len(studentdata[0])):#10 rows
  row=list()
  for j in range(len(studentdata)):#12 col
    data=studentdata[j][i]
    row.append(data)
  row.append('\n')
  data_to_write.append(",".join(row))
data_to_write
fw.writelines(data_to_write)
fw.close()
#1.Sum of Marks
#2.Average Marks
print("Maths Marks=",Maths)
print("Physics Marks",Physics)
print("Chemistry Marks",Chemistry)
maths=[int(i) for i in Maths]
physics=[int(i) for i in Physics]
chemistry=[int(i) for i in Chemistry]
sum_of_marks=[]
avg=[]
for i in range(len(maths)):
  sum_of_marks.append(maths[i]+physics[i]+chemistry[i])
  avg.append(round(sum_of_marks[i],2))
print("Sum of Marks=",sum_of_marks)
print("Average Marks=",avg)
#3.Max Marks
print("Maximum Marks=",max(avg))
#4.Min Marks
# Max Marks
print("Maximum Marks=",min(avg))
#5. Count total no of student
print("Total No of Students=",len(studentdata[0]))
#6. Precentage
# assume Maths Marks=90, Physics Marks=90, Chemistry Marks=90
per=[]
for i in range(len(sum_of_marks)):
  per.append(round((100*sum_of_marks[i]/270),2))
print("Percentage=",per)

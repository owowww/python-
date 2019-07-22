"""
請撰寫一個程式，讀取「student.txt」的文字檔，依使用者的選擇進行分組，分組結果寫入「result.txt」檔案中。
1、依人數分組
2、依組數分組
"""
import random
with open("student.txt","r",encoding="UTF-8-SIG") as f:
    student=[]
    for line in f:
        student.append(line.strip('\t\n'))     
list=[]   #輸出用的空字串
Numberpeople = eval(input("輸入依人數分組:"))
Numbergroups = eval(input("輸入依組數分組:"))
studenta=student[1:11]
#print(studenta)
randomstudent=random.sample(studenta,k=10)#隨機

print("依人數分組的結果")
list.append("依人數分組的結果")
for i in range(0,10,Numberpeople):#0到10間，間隔
    print(randomstudent[i:i+Numberpeople])
    list.append(randomstudent[i:i+Numberpeople])

print("依組數分組的結果")
list.append("依組數分組的結果")

if Numbergroups<=10:
        number=10//Numbergroups 
else:
    print("錯誤")
    list.append("錯誤")
    
for k in range(0,10,number):
    print(randomstudent[k:k+number])
    list.append(randomstudent[k:k+number])
    
with open("result.txt","w",encoding="UTF-8-SIG") as f:
    for ii in list:
        kk=' '.join([str(jj) for jj in ii])
        f.write(kk+"\n")
            
import math
print('#############  Simple JNTUH Calculator  ##############')

grades={'O':10,'A+':9,'A':8,'B+':7,'B':6,'C':5,'F':0,'Ab':'Ab'}

print('How many subjects and lab are in total (exclude uncreditable subjects )')

subs=int(input('Enter Here :  '))

subsum=[]
credsum=0

for n in range(subs):
    cred=float(input(f'{n+1}.Subject Credits Input Here '))
    credsum+=cred
    grade=input(f'{n+1}.Subject Grade Input Here ')
    subsum.append(cred*grades[grade])

sgpa=(sum(subsum)/credsum)
print(sgpa)
print(sgpa*9.5)

# #3-2 = 5.9 , 51.8
# #3-1 = 6.5 , 57.5
# #2-1 = 6.3 , 56.3
# #2-2 = 7.9 , 62.9


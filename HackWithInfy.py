#q1(Sum of series)
'''x = eval(input("Enter X value"))
n = eval(input("Enter N value"))
sum = 0
for i in range(1,n+1):
    sum = sum + (x**i)
print(sum)'''

#q2(Length of a string)
'''x = input("Enter value")
print(len(x))'''

#q3(Sum of digits of a number)
'''n = int(input("Enter the number"))
s = 0
while(n>0):
    t=n%10
    s=s+t
    n = n//10
print(s)'''

#q4(Three digit number with all same digits)
'''n = input("Enter value")
if(len(n)!=3):
    print("Flase")
else:
    if(n[0]==n[1] and n[1]==n[2]):
        print("True")
    else:
        print("False")'''

#q5(GCD of two numbers)
'''n1 = int(input())
n2 = int(input())
gcd = 1
for i in range(1, min(n1, n2)+1):
    if(n1%i==0 and n2%i==0):
        gcd = i
print(gcd)'''

#q6(Neon Number)
'''n = int(input("Enter the number"))
m = n**2
s = 0
while(m>0):
    t = m%10
    s+=t
    m=m//10
if(s==n):
    print("Neon Number")
else:
    print("Not a Neon Number")'''

#q7(Perfect Number)
'''n = int(input("Enter the number"))
s = 0
for i in range(1, n):
    if(n%i==0):
        s+=i
if s==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")'''

#q8(Perfect Numbers in the range 1 to 1000)
'''for i in range(1,1001):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s+=j
    if s==i:
        print(i)'''

#q9(Amicable Numbers)
'''def fact(n):
    s1 = 0
    for i in range(1, n):
        if(n%i==0):
            s1+=i
    return s1
n1 = int(input("Enter the number"))
n2 = int(input("Enter the number"))
s1 = fact(n1)
s2 = fact(n2)
if s1==n2 and s2==n1:
    print("Amicable Numbers")
else:
    print("Not Amicable Numbers")'''

#q10(Deficient Number)
'''n = int(input("Enter the number"))
s = 0
for i in range(1, n):
    if(n%i==0):
        s+=i
if(s<n):
    print("Deficient Number")
else:
    print("Not a Deficient Number")'''

#q11(Harshad Number)
'''n = int(input("Enter the number"))
s = 0
temp = n
while(n>0):
    t = n%10
    s = s+t
    n = n//10
if(temp%s==0):
    print("Harshad Number")'''
    
#q12(Lucas Number)
'''n = int(input("Enter the number"))
n1 = 2
n2 = 1
for i in range(n):
    print(n1, end=" ")
    t = n1
    n1 = n2
    n2 = t+n2'''

#q13(Power of a number without using ** operator or pow())
'''n = int(input("Enter the number"))
m = int(input("Enter the number"))
a = n
for i in range(1,m):
    a = a*n
print(a)'''

#q14(Strong Number)
'''from math import factorial
n = int(input("Enter value"))
s = 0
temp = n
while(n>0):
    t = n%10
    s += factorial(t)
    n = n//10
if(s==temp):
    print("Strong Number")
else:
    print("Not a Strong Number")'''

#q15(Disarium Number)
'''n = int(input("Enter the number"))
l = len(str(n))
s = 0
temp = n
while(l>=1):
    t = n%10
    s += (t**l)
    n = n//10
    l-=1
if(s==temp):
    print("Disarium Number")
else:
    print("Not a Disarium Number")'''

#q16(Armstrong Number)
'''n =nt(input("Enter the number"))
l = len(str(n))
temp = n
s = 0
while(n>0):
    t = n%10
    s += (t**l)
    n = n//10
if(s==temp):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''

#q17(Automorphic Number)
'''n = int(input("Enter the number"))
m = n**2
if str(m)[-len(str(n)):] == str(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")'''
#q17(other method)
'''n = int(input("Enter the number"))
if((n**2).endswith(str(n))):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")'''

#LISTS
#q18(find the second largest and third largest numbers in the list)
'''n = list(map(int, input("Enter the numbers").split()))
if len(n) < 2:
    print("Not enough numbers")
else:
    print(sorted(n)[-2], sorted(n)[2])'''

#q19(find the odd numbers in the list at even indexes)
'''n = list(map(int, input("Enter the numbers").split()))
for i in range(0,len(n),2):
    if(n[i]%2!=0):
        print(n[i],end=" ")'''

#q20(count the maximum number of times a number occurs in the list)
'''n = int(input("Enter the number"))
l = list(map(int, input("Enter the numbers").split()))
print(l.count(max(l)))'''

#q21(find the total fee based on age)
'''n = list(map(int, input("Enter the numbers").split()))
s = 0
if(len(n)>20 or len(n)<=0 or not all(0<i<=120 for i in n)):
    print("Invalid Input")
    exit()
else:
    for i in n:
        if i>40:
            s+=300
        elif i>17:
            s+=400
        elif i>0:
            s+=200
print(s)'''

#q22(find the smallest and largest numbers in the list and print them in pairs)
'''n = list(map(int, input("Enter the numbers").split()))
n.sort()
for i in range(len(n)//2):
    print(n[i], n[len(n)-i-1])
if(len(n)%2!=0):
    print(n[len(n)//2])'''

#q23(find the target sum indexes)
'''numbers = list(map(int, input("Enter the numbers").split()))
target = int(input("Enter the target number"))
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Pair indices found: [{i}, {j}]")'''

#q24(find the first index if it is in descending order else last index of a number in the list)
'''numbers = list(map(int, input("Enter the numbers").split()))
val = all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))
print(numbers[0] if val else numbers[-1])'''

#q25(list of Running totals(cumulative Sum))
'''numbers = list(map(int, input("Enter the numbers").split()))
cumulative_sum = [numbers[0]]
for i in range(1, len(numbers)):
    cumulative_sum.append(cumulative_sum[i-1] + numbers[i])
print(cumulative_sum)'''

#q26(remove duplicates from the list)
'''n = list(map(int, input("Enter the numbers").split()))
print(list(set(n)))
#other method
unique = []
for i in n:
    if i not in unique:
        unique.append(i)
print(unique)'''

#q27
'''list = list(map(int, input("Enter the numbers").split()))
n = int(input("Enter the number"))
n = n%len(list)
list = list[n:] + list[:n]
print("Updated list:", list)'''

#q28(rotate the list)
'''n = int(input("Enter the number"))
list = list(map(int, input("Enter the numbers").split()))
for i in range(n//2):                 
    temp = list[i]                   
    list[i] = list[n-i-1]                    
    list[n-i-1] = temp
print("Updated list:", list)'''

#q29(verify if the list is palindrome or not)
'''n = list(map(int,input().split()))
if not n:
    print("List is empty")
else:
    for i in range(len(n)//2):
       if n[i] != n[len(n)-i-1]:
           print("False")
           break
    else:
        print("True")'''

#q30(Find the missing number in the list)
'''n = sorted(set(map(int, input("Enter the numbers").split())))
min, max = map(int, input("Enter the range (e.g., 1 10): ").split())
for i in range(min,max+1):
    if i not in n:
        print(i, end=" ")'''

#q31(Moving all zeroes to the end of the list)
'''n = list(map(int, input("Enter the numbers").split()))
m = []
count = 0
for i in n:
    if i!=0:
        m.append(i)
    else:
        count+=1
m.extend([0]*count)
print(m)'''
#other method
'''n = list(map(int, input("Enter the numbers: ").split()))
pos = 0  

for i in range(len(n)):
    if n[i] != 0:
        n[pos] = n[i]
        pos += 1
for i in range(pos, len(n)):
    n[i] = 0

print(n)'''

#q32(reverse the list)
'''n = list(map(int, input("Enter the numbers").split()))
for i in range(len(n)//2):
    temp = n[i]
    n[i] = n[len(n)-i-1]
    n[len(n)-i-1] = temp
print(n)'''

#q33(Find the max profit from the list of stock prices)
'''n = list(map(int, input("Enter the numbers").split()))
min_price = n[0]
max_profit = 0
for price in n[1:]:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price
print(max_profit)'''

#q34(move all even numbers to the front of the list without another list)
'''numbers = list(map(int, input("Enter the numbers").split()))
left, right = 0, 0
while right < len(numbers):
    if numbers[right] % 2 == 0:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
    right += 1
print(numbers)'''

#q35(print the repeated digit numbers in the list)
'''n = list(map(int, input("Enter the numbers").split()))
for i in n:
    if len(str(i))<=1:
        continue
    t = i
    l = t%10
    s = True
    while t>0:
        d = t%10
        if d!= l:
            s = False
            break
        t = t//10
    if s:
        print(i, end=" ")'''

#q36(transverse of matrix)
'''matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[] for _ in range(len(matrix1))]
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix2[j].append(matrix1[i][j])
for i in matrix2:
    print(i)'''

#q37(find the max of dignals of a matrix)
''' matrix1 = []
 row = int(input("Enter the number of rows"))
 col = int(input("Enter the number of columns"))
 for i in range(row):
     matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1}").split())))
 max_dig = matrix1[0][0]
 for i in range(min(row,col)):
         if matrix1[i][i] > max_dig:
             max_dig = matrix1[i][i]
 print(max_dig)'''

#q38(find the sum of the anti dignal elements of the matrix)
'''matrix1 = []
s = 0
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in range(row):
    s += matrix1[i][row-i-1]
print(s)'''

#q39(check if the matrix is lower triangular matrix or not)
'''matrix1 = []
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in range(row):
    for j in range(col):
        if i<j and matrix1[i][j]!=0:
            print("Not a lower triangular matrix")
            break
    else:
        continue
    break
else:
    print("Lower triangular matrix")'''

#q40(find max sum from cloumns of the matrix)
'''matrix1 = []
max_sum = float('-inf')
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in range(col):
    s = 0
    for j in range(row):
        s += matrix1[j][i]
    if s > max_sum:
        max_sum = s
print(max_sum)'''

#q41(find the max of the matrix)
'''matrix1 = []
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in matrix1:
    print(max(i),end=" ")'''

#q42(verify matrix is Symmetric or not)
'''matrix1 = []
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
if row!=col:
    print("Not a Symmetric Matrix")
    exit()
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in range(row):
    for j in range(col):
        if matrix1[i][j] != matrix1[j][i]:
            print("Not a Symmetric Matrix")
            break
    else:
        continue
    break
else:
    print("Symmetric Matrix")'''

#q43(find the max from each row and col must not be equal)
'''matrix1=[]
row = int(input())
col = int(input())
m = []
pc = -1
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in range(row):
    max = 0
    v = -1
    for j in range(col):
        if(j != pc and max<matrix1[i][j]):
            max = matrix1[i][j]
            v = j
    pc = v 
    m.append(max)
print(sum(m))'''

#q44(rotate the matrix 90 degrees clockwise)
'''matrix1 = []
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
for i in range(row):
    matrix1.append(list(map(int, input(f"Enter the numbers of row {i+1} ").split())))
for i in range(row):
    for j in range(col):
        matrix1[i][j],matrix1[j][i] = matrix1[j][i],matrix1[i][j]
for row in matrix1:
    row.reverse()
    print(row)'''

#q45(store string in matrix and print the matrix)
'''matrix1 = []
str = input("Enter the string")
k = int(input("Enter the number of col"))
for i in range(len(str)//k+1):
    matrix1.append([])
for i in range(len(str)//k):
        row = []
        for j in range(k):
            if i*k+j < len(str):
                 row.append(str[i*k+j])
        matrix1[i] = row
for i in matrix1:
    print(i)'''

#functions
#q46(factorial of a number)
'''def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
result = fact(int(input("Enter a value")))
print(result)'''

#q47(verify string is palindrome or not)
'''def isPal(n):
    l = len(n)
    for i in range(l//2):
        if n[i] != n[l-i-1]:
            return False
    else:
        return True
p = isPal(input("Enter a string"))
if p:
    print("Palindrome")
else:
    print("Not a Palindrome")'''


#q48(print nibhour values of list)
'''def nibhour(l,k):
    if k < 0 or k >= len(l):
        return None, None
    left = l[k-1] if k>0 else None
    right = l[k+1] if k<len(l) else None
    return left,right
l = list(map(int,input().split()))
k = int(input())
print(nibhour(l,k))'''

#q49(fibonacci series using recursion)
'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n = int(input("Enter the number"))
print(fib(n))'''

#q50(verify if given list is sorted or not using recursion)
'''def isSorted(l):
    if len(l) <= 1:
        return True
    if l[0] > l[1]:
        return False
    return isSorted(l[1:])
l = list(map(int, input("Enter the numbers").split()))
if isSorted(l):
    print("Sorted")
else:
    print("Not Sorted")'''

#q51(Right angle triangle)
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()'''

#q52(Left angle triangle)
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()'''

#q53(equilateral triangle)
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()'''

#q54(Reverse equilateral triangle)
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end=" ")
    print()'''

#q55(diamond)
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range(n-i-1):
        print("*", end=" ")
    print()'''

#q56(number right angle triangle)
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()'''

#q57
'''n = int(input("Enter The number"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()'''

#q58
'''n = int(input("Enter the number"))
for i in range(n):
    for j in range(i,n):
        print(j+1,end=" ")
    print()'''

#q59
'''n = int(input("Enter a Value"))
for i in range(n+1):
    for j in range(n-i+1,n+1):
        print(j,end = " ")
    print()'''

#q60
'''n = int(input())
for i in range(n):
    for j in range(i+1):
        print(n-j,end = " ")
    print()'''

#q61
'''n = int(input())
for i in range(n):
    for j in range(i+1):
        print(2*i+1,end=" ")
    print()'''

#q62
'''n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(2*i+1,end=" ")
    print()'''

#q64
'''n = int(input())
k = 1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()'''

#q65
'''n = int(input())
for i in range(n):
    k = i+1
    for j in range(i+1):
        print(k,end=" ")
        k+=n-j-1
    print()'''

#q66
'''n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()'''

#q67
'''n = int(input())
for i in range(n):
    val = 1 if i % 2 == 0 else 0
    for j in range(i+1):
        print(val,end=" ")
        val = 1-val
    print()'''

#q68
'''n = int(input())
for i in range(n):
    for j in range(i,n):
        print(j+1,end=" ")
    for j in range(i):
        print(j+1,end=" ")
    print()'''

#q69
'''n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    for j in range(2,i+2):
        print(j,end=" ")
    print()'''

#q70
'''n = int(input())
c = 1
for i in range(n):
    s = c
    e = c + i
    if i % 2 == 0:
        for j in range(s, e + 1):
            print(j, end=" ")
    else:
        for j in range(e, s - 1, -1):
            print(j, end=" ")
    c = e + 1
    print()'''

#q71
'''n = int(input())
c = n * (n + 1) // 2

for i in range(n):
    start = c - i
    end = c

    if i % 2 == 0:
        for j in range(end, start - 1, -1): 
            print(j, end=" ")
    else:
        for j in range(start, end + 1): 
            print(j, end=" ")

    c = start - 1
    print()'''

#q72
'''n = int(input())
matrix = [[0] * n for _ in range(n)]
top, bottom = 0, n - 1
left, right = 0, n - 1
num = 1
while num <= n * n:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
for row in matrix:
    print(*row)'''

#q73
'''n = int(input())
num = 7
for i in range(n-1):
    print(num,end=',')
    if i%2==0:
        num-=2
    else:
        num+=3
print(num)'''

#q74
'''n = list(map(int,input().split()))
i = 0
while i < len(n):
    if n[i] in n[i+1:]:
        n.remove(n[i])
    else:
        i += 1
print(n)
#other
n = list(map(int,input().split()))
s = set()
i = 0
while i < len(n):
    if n[i] in s:
        n.pop(i)
    else:
        s.add(n[i])
        i += 1
print(n)
#other
n = list(map(int, input().split()))
n.sort()
i = 0
while i < len(n) - 1:
    if n[i] == n[i + 1]:
        del n[i + 1]
    else:   
        i += 1
print(n)'''

#q75
'''n = input("Enter the string")
for i in range(0,len(n),2):
    print(n[i:i+2][::-1],end="")'''

#q76
'''n = input("Enter the string")
u,l,d,s = 0,0,0,0
for i in n:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print("Upper case letters:",u)
print("Lower case letters:",l)
print("Digits:",d)
print("Special characters:",s)'''

#q77
'''n = input("Enter the string")
o = 0
c = 0
vowels = "aeiouAEIOU"
for i in n:
    if i in vowels:
        o+=1
    elif i.isalpha():
        c+=1
print("Number of vowels:",o)
print("Number of consonants:",c)'''

#q78
'''n = input("Enter the string")
l = list(n)
for i in n:
    if i.isdigit():
        l.remove(i)
print("".join(l))'''

#q79
'''n = input("Enter the string")
if n.isalpha():
    print(n.swapcase())
else:
    print("Invalid Input")'''

#q80
'''n = input("Enter the string")
for i in range(0,len(n),2):
    print(n[i:i+2][::-1],end="")'''

#q81
'''n = input("Enter the string")
m = list(map(str,n.split()))
for i in range(len(m)):
    w = m[i]
    if len(w) > 1:
        w = w[-1] +w[1:-1]+ w[0]
    m[i] = w
print(' '.join(m))'''

#q82
'''n = input("Enter the string")
m = list(map(str,n.split()))
for i in m:
    print(i[::-1],end=" ")'''

#q83
'''n = input("Enter the string")
m = list(map(str,n.split()))
for i in range(len(m)):
    w = m[i]
    if len(w) > 1:
        w = w[0].upper() +w[1:-1]+ w[-1].upper()
    else:
        w = w.upper()
    m[i] = w
print(' '.join(m))'''

#q84
'''n = input("Enter the string")
m = int(input("Enter the number"))
m = m % len(n)
n = n[-m:] + n[:-m]
print(n)'''

#q85
'''n = input("Enter the string")
m = input("Enter the pattern")
if len(n) == len(m) and m in n+n:
    print("Yes")
else:
    print("No")'''

#q86
'''n = input("Enter the string")
m = input("Enter the substring")
count = 0
for i in range(len(n)-len(m)+1):
    if n[i:i+len(m)] == m:
        count += 1
print("Count of substring:", count)'''

#q87
'''n = input("Enter the string")
m = input("Enter the substring")
l = len(m)
count = 0
for i in range(len(n)-l+1):
    if n[i:i+l] == m:
        count += 1
print("Count of substring:", count)'''

#q88
'''n = input("Enter the string")
m = '{}[]()'
k = "".join([i for i in n if i not in m])
print(k)'''

#q89
'''n = input("Enter the string")
count = 0
for i in n:
    if not i.isalnum():
        count += 1
print("Count of special characters:", count)'''

#q90
'''n = input("Enter the string")
k = ""
for i in n:
    if i not in k:
        k += i
print(k)'''

#q91
'''n = input("Enter the string")
freq = {}
result = ""
for i in n:
    freq[i] = freq.get(i, 0) + 1
for char, count in freq.items():
    result += f"{char}{count}"
print(result)'''

#q92
'''from itertools import permutations
n = input("Enter the string: ")
perms = permutations(n)
for p in perms:
     print(''.join(p))'''
#q92(other)
'''n = input("Enter the string: ")
for i in n:
    for j in n:
        for k in n:
            if i != j and j != k and i != k:
                print(i+j+k)'''

#q93
'''n = list(input("Enter the string"))
i, j = 0, len(n) - 1

while i < j:
    if not n[i].isalnum():
        i += 1
    elif not n[j].isalnum():
        j -= 1
    else:
        n[i], n[j] = n[j], n[i]
        i += 1
        j -= 1

print("".join(n))'''

#q94
'''n = input("Enter the string").lower()
a = 'abcde'
r = []
for i in n:
    if i in a:
        k = (a.find(i)+1)%5
        r.append(a[k])
    else:
        r.append(i)
print("".join(r))'''

#q95
'''n = input("Enter the string: ")
i = 0
while i < len(n):
    c = 1
    while i + 1 < len(n) and n[i] == n[i + 1]:
        c += 1
        i += 1
    print(n[i] + str(c), end="")
    i += 1'''

#q96
'''n = input("Enter the string")
max_substr = ""
current_substr = ""
for i in n:
    if i not in current_substr:
        current_substr += i
        if len(current_substr) > len(max_substr):
            max_substr = current_substr
    else:
        current_substr = current_substr.split(i)[-1] + i
print("Maximum substring without repeating characters:", max_substr)'''

#q97
'''n = input("Enter the string1").lower()
m = input("Enter the string2").lower()
l = [0]*123
if len(n) != len(m):
    print("No")
else:
    for i in n:
        l[ord(i)] += 1
    for i in m:
        l[ord(i)] -= 1
        if l[ord(i)] !=  0:
            print("No")
            break
    else:
        print("Yes")'''

#q98
'''n = input("Enter the string")
m = input("Enter the string")
if len(n) != len(m):
    print("No")
else:
    mapping1 = {}
    mapping2 = {}
    for i in range(len(n)):
        if n[i] in mapping1:
            if mapping1[n[i]]!=m[i]:
                print("No")
                break
        else:
            mapping1[n[i]] = m[i]
        if m[i] in mapping2:
            if mapping2[m[i]]!=n[i]:
                print("No")
                break
        else:
            mapping2[m[i]] = n[i]
    else:
        print("Yes")'''

#q99
'''n = input("Enter the string")
max= 1
start = 0
for i in range(len(n)):
    for j in range(i, len(n)):
        if n[i:j+1] == n[i:j+1][::-1] and j-i+1 > max:
            max = j-i+1
            start = i
print("Longest palindrome substring:", n[start:start+max])'''

#other(2 pointers)
'''n = input("Enter the string")
def palindrome(l,r):
    while l <= r and l >= 0 and r < len(n):
        if n[l] == n[r]:
            l -= 1
            r += 1
            if l<0:
                l = 0
        else:
            return False
        l += 1
        r -= 1
    return n[l:r+1]
iseven = len(n)%2==0
for i in range(len(n)):
    if iseven:
        print(palindrome(i,i+1))
    else:
        print(palindrome(i,i))'''

#q100
'''n = int(input("Enter the number"))
l = [[' '] * n for _ in range(n)]
left, top = 0, 0
right, bottom = n - 1, n - 1
while left <= right and top <= bottom:
    for i in range(left, right + 1):
        l[top][i] = '*'
    top += 1
    if top>2:
        left += 1
    for i in range(top, bottom + 1):
        l[i][right] = '*'
    right -= 1
    top += 1
    if left==right:
        break
    for i in range(right, left - 1, -1):
        l[bottom][i] = '*'
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        l[i][left] = '*'
    left += 1
    right -= 1
    bottom -= 1
for i in l:
    print(*i)'''

#q101
'''n = int(input("Enter the number"))
s = 2*n-1
l = [[0] * s for _ in range(s)]
left, top = 0, 0
right, bottom = s - 1, s - 1
while left <= right and top <= bottom:
    for i in range(left, right + 1):
        l[top][i] = n
    top += 1
    for i in range(top, bottom + 1):
        l[i][right] = n
    right -= 1
    for i in range(right, left - 1, -1):
        l[bottom][i] = n
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        l[i][left] = n
    left += 1
    n -= 1
for i in l:
    print(*i)'''

#q102
'''x = [(1,4),(2,7),(3,2),(4,1),(5,3)]
x.sort(key=lambda x: x[1])
print(*x)'''

#q103
'''n = input("Enter the string")
d = {}
for i in n:
    d[i] = d.get(i, 0) + 1
print(d)'''

#q104
'''n = int(input())
c = 0
l1 = list(map(int,input().split()))
l2 = sorted(l1.copy()*2,reverse=True)
if sum(l2) < n:
    print(-1)
    exit()
for i in l2:
    n = n - i
    c += 1
    if n <= 0:
        break
print(c)'''

#q105
'''n, target = map(int, input().split())
nums = list(map(int, input().split()))
found = False
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print(i + 1, j + 1)
            found = True
            break
    if found:
        break
if not found:
    print('-1')'''

#q106
'''n = int(input())
l = list(map(int, input().split()))
max_list = []
for i in range(n):
    for j in range(i+1,n):
        if len(l[i:j])>len(max_list) and l[i:j].count(0) == l[i:j].count(1):
            max_list = l[i:j]
print(max_list)'''

#q107
'''def hi():
    try:
        n = int(input("Enter the number"))
        if n < 0:
            raise ValueError("Negative number")
    except ValueError as e:
        print("Invalid Input:", e)
        hi()
    else:
        print("Positive number")
hi()'''

#q108
'''a = input("Enter the string")
s = []
cn = 0
cs = ""
for char in a:
    if char.isdigit():
        cn = cn * 10 + int(char)
    elif char == '[':
        s.append((cs, cn))
        cs, cn = "", 0
    elif char == ']':
        last_str, last_num = s.pop()
        cs = last_str + last_num * cs
    else:
        cs += char
print(cs)'''

#q109(heros and villains)
'''n = int(input("Enter the number of villains: "))
m = int(input("Enter the number of heroes: "))
h = int(input("Enter the health of each hero: "))
vh = []
for i in range(n):
    v = int(input(f"Enter the health of villain {i+1}: "))
    vh.append(v)
s = m*h
c = 0
while sum(vh) > s:
    vh.pop(0)
    c += 1
print(c)'''

#q110(converting an array to mountain)
'''n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
c = 0
if n%2==1:
    max_index1 = max_index2=n//2
else:
    max_index1 = n//2 - 1
    max_index2 = n//2
for i in range(max_index1-1,-1,-1):
    if arr[i]>= arr[i+1]:
        arr[i] = arr[i+1] - 1
        c += 1
for i in range(max_index2+1,n):
    if arr[i]>=arr[i-1]:
        arr[i] = arr[i-1] - 1
        c += 1
print(c)'''


'''s = input("Enter the string")
n = len(s)
freq = {}
ans = 1
for char in s:
    freq[char] = freq.get(char, 0) + 1
def is_valid(k):
    for c in freq.keys():
        if freq[c] % k != 0:
            return False
    return True
for k in range(n,0,-1):
    if is_valid(k) and n%k==0:
        ans = k
        break
print(ans)'''

#q111
'''from collections import Counter
s = input("Enter the string")
v = Counter(s)
val = v.values()
if len(val) == 1 and min(val)%2== 0:
    print(len(s)//2)
else:
    print(min(val))
#other
s = input("Enter the string")
v = {}
for i in s:
    v[i] = v.get(i, 0) + 1
val = v.values()
if len(val) == 1 and min(val) % 2 == 0:
    print(len(s) // 2)
else:
    print(min(val))'''

#q112(find the smallest lexicographical array by swapping element to k differenced index)
'''n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter the index to swap with: "))
l = []
c = i = 0
while i+c<n:
    a = arr.copy()
    arr[i] ,arr[i+c] = arr[i+c], arr[i]
    m = "".join(map(str, arr))
    l.append(int(m))
    if c==k:
        c = 0
        i += 1
    c+=1
print(min(l))
#other
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
min_arr = arr[:]
for i in range(n):
    for j in range(i + 1, min(n,i+k+1)):
        temp = arr[:]
        temp[i], temp[j] = temp[j], temp[i]
        if temp < min_arr:
            min_arr = temp
print(*min_arr)'''

#q113
'''l = list(map(int, input("Enter the numbers: ").split()))
t = int(input("Enter the target: "))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==t:
            print(f"[{i},{j}]")
            break
    else:
        continue
    break
else:
    print(-1)'''

#q114
'''l = list(map(int, input("Enter the numbers: ").split()))
max_profit = 0
min_price = l[0]
for p in l[1:]:
    if p<min_price:
        min_price = p
    elif p-min_price>max_profit:
        max_profit = p-min_price
print(max_profit if max_profit > 0 else 0)'''

#q115(marge all the overlapping intervals)
'''intervals = list(input("Enter the intervals: ").split())
merged_intervals = []
for i in intervals:
    start, end = map(int, i.split(','))
    if not merged_intervals or merged_intervals[-1][1] < start:
        merged_intervals.append([start, end])
    else:
        merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
print("Merged intervals:", merged_intervals)'''

#q116(find the max subarray sum)
'''l = list(map(int, input("Enter the numbers: ").split()))
max_sum = float('-inf')
current_sum = 0
for num in l:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print("Max subarray sum:", max_sum)'''

#q117(find the max subarray without repeating elements)
'''s = input()
max_str = ""
current_str = ""
for char in s:
    if char not in current_str:
        current_str+=char
        if len(current_str) > len(max_str):
            max_str = current_str
    else:
        current_str = current_str.split(char)[-1] + char
print(max_str)
#other
s = input()
char_index = {}
max_length = 0
left = 0
for right in range(len(s)):
    if s[right] in char_index and char_index[s[right]]>=left:
        left = char_index[s[right]]+1
    char_index[s[right]] = right
    max_length = max(max_length, right - left + 1)
print(max_length)'''

#q118
'''l = list(map(int,input().split()))
d = {}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
print(max(d,key=d.get))'''

#q119
'''l = list(map(int,input().split()))
k = int(input())%len(l)
for i in range(k):
    l.insert(0,l.pop())
print(l)
#other
l = list(map(int,input().split()))
k = int(input())%len(l)
l[:] = l[::-1]
l[:k] = l[:k][::-1]
l[k:] = l[k:][::-1]
print(l)'''

#q120
'''rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    val = list(map(int,input().split()))
    matrix.append(val)'''

#q121
'''s = input()
s = "".join(c.lower() for c in s if c.isalnum())
l = len(s)
for i in range(l//2):
    if s[i]!=s[l-i-1]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")'''

#q122
'''l = list(map(int,input().split(",")))
k = int(input())
i = 0
m = []
while k<=len(l):
    m.append(max(l[i:k]))
    i+=1
    k+=1
print(m)'''

#q123
'''l = list(map(int, input().split(",")))
lz = 0
for i in range(len(l)):
    if l[i]!=0:
        l[lz] = l[i]
        lz+=1
for i in range(lz,len(l)):
    l[i] = 0
print(l)
l = list(map(int,input().split(",")))
n = len(l)
v = []
for i in range(n):
    mul = 1
    for j in range(n):
        if j == i:
            continue
        mul*=l[j]
    v.append(mul)
print(v)
#other
l = list(map(int,input().split(",")))
n = len(l)
v = [1]*n
prefix = 1
for i in range(n):
    v[i] = prefix
    prefix*=l[i]
suffix = 1
for i in range(n-1,-1,-1):
    v[i]*=suffix
    suffix*=l[i]
print(v)'''

#q124
'''s = input()
valid = "{}[]()"
val = {')':'(',']':'[','}':'{'}
stack = []
for i in s:
    if i not in valid:
        continue
    if i not in val:
        stack.append(i)
    else:
        if stack and stack[-1]==val[i]:
            stack.pop()
        else:
            print(False)
            break
else:
    print(not stack)'''

#q125(find index of peak)
'''l = list(map(int,input().split(',')))
print(l.index(max(l)))'''

#1.Subarray Sum Equals K
'''
def subarraySum(nums, k):
    count = 0
    total = 0
    prefix_sums = {0: 1}
    
    for num in nums:
        total += num
        count += prefix_sums.get(total - k, 0)
        prefix_sums[total] = prefix_sums.get(total, 0) + 1
        
    return count
'''

# 2. Longest Subarray with Sum K
'''
def longestSubarrayWithSumK(nums, K):
    prefix_sum = 0
    max_len = 0
    seen = {}
    
    for i in range(len(nums)):
        prefix_sum += nums[i]
        
        if prefix_sum == K:
            max_len = i + 1
            
        if prefix_sum - K in seen:
            max_len = max(max_len, i - seen[prefix_sum - K])
            
        if prefix_sum not in seen:
            seen[prefix_sum] = i
            
    return max_len
'''

#3. Count Distinct Elements in Every Window
'''
from collections import defaultdict

def countDistinctInWindow(nums, k):
    freq = defaultdict(int)
    res = []
    
    for i in range(len(nums)):
        freq[nums[i]] += 1
        if i >= k:
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]
        if i >= k - 1:
            res.append(len(freq))
    
    return res
'''

#  4. Top K Frequent Elements
'''
from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
'''

# 5. Isomorphic Strings
'''
def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
'''

# 6. Longest Palindromic Substring
# Already answered — check above

# 7. Minimum Window Substring
'''
from collections import Counter

def minWindow(s, t):
    if not t or not s:
        return ""
    
    t_count = Counter(t)
    window = {}
    have, need = 0, len(t_count)
    res, res_len = [-1, -1], float('inf')
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1
        
        if c in t_count and window[c] == t_count[c]:
            have += 1
        
        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            
            window[s[l]] -= 1
            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1
            
    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""
'''

# 8. Four Sum
'''
def fourSum(nums, target):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            l, r = j+1, n-1
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total == target:
                    quad = [nums[i], nums[j], nums[l], nums[r]]
                    if quad not in res:
                        res.append(quad)
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
    return res
'''

# 9. Ransom Note
'''

from collections import Counter

def canConstruct(ransomNote, magazine):
    return not Counter(ransomNote) - Counter(magazine)
'''

# 10. Group Shifted Strings
'''
from collections import defaultdict

def groupStrings(strings):
    groups = defaultdict(list)
    
    for s in strings:
        shift = tuple((ord(char) - ord(s[0])) % 26 for char in s)
        groups[shift].append(s)
    
    return list(groups.values())
'''

# 11. Repeated DNA Sequences
'''
def findRepeatedDnaSequences(s):
    seen = set()
    repeated = set()
    
    for i in range(len(s) - 9):
        seq = s[i:i+10]
        if seq in seen:
            repeated.add(seq)
        else:
            seen.add(seq)
    
    return list(repeated)
'''

# 12. Anagrams in a String
'''
from collections import Counter

def findAnagrams(s, p):
    res = []
    p_count = Counter(p)
    s_count = Counter()
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        if s_count == p_count:
            res.append(i - len(p) + 1)
    
    return res
'''

# 13. Custom Sort String
'''
def customSortString(order, s):
    count = Counter(s)
    res = []
    
    for char in order:
        res.append(char * count[char])
        count[char] = 0
    
    for char in count:
        res.append(char * count[char])
    
    return ''.join(res)
'''

#14.Max Points on a Line
'''
from collections import defaultdict

def maxPoints(points):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    max_count = 0
    
    for i in range(len(points)):
        slopes = defaultdict(int)
        overlap = 0
        curr_max = 0
        x1, y1 = points[i]
        
        for j in range(i+1, len(points)):
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1
            
            if dx == 0 and dy == 0:
                overlap += 1
                continue
            
            g = gcd(dx, dy)
            slope = (dx // g, dy // g)
            slopes[slope] += 1
            curr_max = max(curr_max, slopes[slope])
        
        max_count = max(max_count, curr_max + overlap + 1)
    
    return max_count
'''

# 15. Count Pairs with Given Sum
'''from collections import Counter
def countPairs(nums, k):
    count = 0
    freq = Counter()
    
    for num in nums:
        count += freq[k - num]
        freq[num] += 1
    
    return count
'''

'''s = input()
vowels = 'aeiouAEIOU'
vowel_list = sorted([char for char in s if char in vowels])
result = []
vowel_index = 0
for char in s:
    if char in vowels:
        result.append(vowel_list[vowel_index])
        vowel_index += 1
    else:
        result.append(char)

print("".join(result))'''

'''nums = list(map(int, input().split()))
curr_max = curr_min = overall_max = nums[0]
for i in nums[1:]:
    temp_max = max(i, i * curr_max, i * curr_min)
    curr_min = min(i, i * curr_max, i * curr_min)
    curr_max = temp_max
    overall_max = max(overall_max, curr_max)
print(overall_max)'''

'''nums = list(map(int, input().split(',')))
curr_max = curr_min = overall_max = nums[0]
for i in nums[1:]:
    temp_max = max(i, i + curr_max, i + curr_min)
    curr_min = min(i, i + curr_max, i + curr_min)
    curr_max = temp_max
    overall_max = max(overall_max, curr_max)
print(overall_max)'''

'''n = list(input().strip("[]").split(','))
stack = []
mat = "+-*/"
sum = 0
for i in n:
    if i not in mat:
        stack.append(int(i))
    else:
        v1,v2 = stack.pop(),stack.pop()
        if i == '+':
            stack.append(v2+v1)
        elif i=='-':
            stack.append(v2-v1)
        elif i=='*':
            stack.append(v2*v1)
        elif i=='/':
            stack.append(int(v2/v1))
print(stack.pop())'''

'''n = list(map(int,input().split(",")))
res = []
for i in range(len(n)):
    c = 1
    for j in range(i+1,len(n)):
        if n[j]>n[i]:
            res.append(c)
            break
        else:
            c = c+1
print(res)'''

'''from multipledispatch import dispatch
class demo:
    @dispatch(int, int)
    def add(a, b):
        return a + b
    @dispatch(float, float)
    def add(a, b):
        return a + b
    @dispatch(str, str)
    def add(a, b):
        return a + b
d = demo()
print(d.add(5, 10))
print(d.add(5.5, 10.5))
print(d.add("Hello, ", "World!"))'''

# q126
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
temp = head
while temp :
    print(temp.data, end=" ")
    temp = temp.next'''

# q127
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
n = node(int(input()))
n.next = head
head = n
temp = head
while temp :
    print(temp.data, end=" ")
    temp = temp.next'''

# q128
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
temp = head
n = node(int(input()))
while temp.next :
    temp = temp.next
temp.next = n
temp = head
while temp :
    print(temp.data, end=" ")
    temp = temp.next'''

#q129
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
temp = head
while temp.next.data != 6:
     temp = temp.next
n = node(int(input()))
n.next = temp.next
temp.next = n
temp = head
while temp :
    print(temp.data, end=" ")
    temp = temp.next'''

#q130
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
temp = head
n =int(input())
while temp.next.data != n:
     temp = temp.next
temp.next = temp.next.next
temp = head
while temp :
    print(temp.data, end=" ")
    temp = temp.next'''

#q131
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
f,s = head, head
while f and f.next:
     f = f.next.next
     s = s.next
print(s.data)'''

#q132
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
prev = None
cur = head
while cur:
    nn = cur.next
    cur.next = prev
    prev = cur
    cur = nn
head = prev
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next'''

#q133
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
        n = node(i)
        temp.next = n
        temp = temp.next
n = int(input())
if n == 1:
     head = head.next
else:
    c = 1
    temp = head
    while c<n-1:
         temp = temp.next
         c += 1
temp.next = temp.next.next if temp.next else None
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next'''

#q134(palindrome or not in linkedlist)
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
l = list(map(int,input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
    n = node(i)
    temp.next = n
    temp = temp.next
f = s = head
while f and f.next:
    s = s.next
    f = f.next.next
prev = None
while s:
    nn = s.next
    s.next = prev
    prev = s
    s = nn
l,r = head,prev
while r:
    if l.data != r.data:
        print("Not a palindrome")
        break
    l = l.next
    r = r.next
else:
    print("Palindrome")'''

#q135
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
head1 = node(l[0])
head2 = node(l1[0])
temp1 = head1
temp2 = head2
dummy = node(0)
tail = dummy
for i in l[1:]:
    n = node(i)
    temp1.next = n
    temp1 = temp1.next
for i in l1[1:]:
    n = node(i)
    temp2.next = n
    temp2 = temp2.next
temp1 = head1
temp2 = head2
while temp1 and temp2:
    if temp1.data < temp2.data:
        tail.next = temp1
        temp1 = temp1.next
    else:
        tail.next = temp2
        temp2 = temp2.next
    tail = tail.next
tail.next = temp1 if temp1 else temp2
temp1 = dummy.next
while temp1:
    print(temp1.data, end=" ")
    temp1 = temp1.next'''

#q136(find if a linked list is circular or not)
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int, input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
    n = node(i)
    temp.next = n
    temp = temp.next
temp1 = head
temp2 = head
while temp2 and temp2.next:
    temp1 = temp1.next
    temp2 = temp2.next.next
    if temp1 == temp2:
        print("Circular")
        break'''

# q137
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
head1 = node(l[0])
head2 = node(l1[0])
temp1 = head1
temp2 = head2
for i in l[1:]:
    n = node(i)
    temp1.next = n
    temp1 = temp1.next
for i in l1[1:]:
    n = node(i)
    temp2.next = n
    temp2 = temp2.next
s1 = []
temp1 = head1
temp2 = head2
while temp1:
    s1.append(temp1.data)
    temp1 = temp1.next
v1 = 0
while s1:
    v1 = v1 * 10 + s1.pop()
while temp2:
    s1.append(temp2.data)
    temp2 = temp2.next
v2 = 0
while s1:
    v2 = v2 * 10 + s1.pop()
v3 = v1 + v2
head3 = node(v3 % 10)
temp = head3
v3 //= 10
while v3:
    n = node(v3 % 10)
    temp.next = n
    temp = temp.next
    v3 //= 10
temp = head3
while temp:
    print(temp.data, end=" ")
    temp = temp.next'''

# q138
'''n,v = map(int, input().split())
f = False
l = list(map(int, input().split()))
for i in range(n):
    for j in range(i,n):
        if sum(l[i:j+1]) == v:
            print(i,j)
            break'''

# q139
'''class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
l = list(map(int, input().split()))
head = node(l[0])
temp = head
for i in l[1:]:
    n = node(i)
    temp.next = n
    n.prev = temp
    temp = temp.next
n = int(input())
temp = head
while temp:
    if temp.data == n:
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == head:
            head = temp.next
    temp = temp.next
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next'''

# q140
'''l = list(map(int, input().split()))
target = int(input())
left, right = 0, len(l) - 1
found = False
while left < right:
    if l[left] + l[right] == target:
        print(left, right)
        found = True
    elif l[left] + l[right] < target:
        left += 1
    else:
        right -= 1
if not found:
    print("No pair found")'''

#141
'''def bs(a, t, l, r):
    if l > r:
        return -1
    mid = (l + r) // 2
    if a[mid] == t:
        return mid
    elif a[mid] < t:
        return bs(a, t, mid + 1, r)
    else:
        return bs(a, t, l, mid - 1)
a = list(map(int, input().split(',')))
t = int(input())
r = bs(a, t, 0, len(a) - 1)
if r != -1:
    print(r)
else:
    print("Not found")'''

#142
'''def count(l):
    for idx, val in enumerate(l):
        if val >= 0:
            return idx
    return len(l)'''

#143
'''l = list(map(int, input().split(',')))
m1, m2 = float('-inf'), float('-inf')
for i in l[1:]:
    if i > m1:
        m2 = m1
        m1 = i
    elif i > m2 and i != m1:
        m2 = i
print(m2)'''

#144
'''n = int(input())
if n & 1:
    print("Odd")
else:
    print("Even")'''
    
#145
'''l = list(map(int, input().split(',')))
for i in range(len(l)//2):
    l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
print(l)'''

#146
'''l = list(map(int, input().split(',')))
n = len(l)
for i in range(n//2):
    if l[i] > l[n-1-i]:
        l[i], l[n-1-i] = l[n-1-i], l[i]
print(l)'''

#147(power of a number using recursion)
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = power(base, exp)
print(f"{base} raised to the power {exp} is {result}")
#for Further codes and problems visit my LeetCode Account
#https://leetcode.com/u/sreecharan750/
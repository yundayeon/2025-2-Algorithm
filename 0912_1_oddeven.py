# #5050
# #1부터 100까지 홀수 합과 짝 합을 구는 파이썬 프로그램 작성 

a=0
b=0

for i in range(101):
    if i%2==0:
        a+=i
    else:
        b+=i

print(f"짝수합: {a}, 홀수합: {b}")
#방법1:
def f1():
    evenSum = 0 ; oddSum = 0
    for i in range(101):
        if (i % 2 == 0):
            evenSum += i
        else:
            oddSum += i
            
    print(f"방법1 : 홀수합 {oddSum}, 짝수합 {evenSum}")
    
#방법2:
def f2():
    totalSum = 0
    evenSum = 0 ; oddSum = 0
    for i in range(101):
        totalSum+=i
        if (i % 2 == 0):
            evenSum += i
            
    print(f"방법2 : 홀수합 {totalSum-evenSum}, 짝수합 {evenSum}")
    
#방법3: 
def f3():
    evenSum = 0 ; oddSum = 0
    for i in range(1,101,2):
        oddSum += i
    for i in range(0,101,2):
        evenSum += i
            
    print(f"방법3 : 홀수합 {oddSum}, 짝수합 {evenSum}")
    
    
#방법4: 등차수열 합
def f4():
    oddSum = 50*(1+99) // 2
    evenSum = 50*(2+100) // 2
            
    print(f"방법4 : 홀수합 {oddSum}, 짝수합 {evenSum}")
    
if __name__ == "__main__":
    f1()
    f2()
    f3()
    f4()
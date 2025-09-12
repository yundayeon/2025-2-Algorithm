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

def f1():
    evenSum = 0 ; oddSum = 0
    for i in range(101):
        if (i % 2 == 0):
            evenSum += i
        else:
            oddSum += i
            
    print(f"방법1 : 홀수합 {oddSum}, 짝수합 {evenSum}")
    
def f2():
    totalSum = 0
    evenSum = 0 ; oddSum = 0
    for i in range(101):
        totalSum+=i
        if (i % 2 == 0):
            evenSum += i
            
    print(f"방법2 : 홀수합 {totalSum-evenSum}, 짝수합 {evenSum}")

if __name__ == "__main__":
    f1()
    f2()
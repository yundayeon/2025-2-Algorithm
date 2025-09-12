#5050
#1부터 100까지 홀수 합과 짝 합을 구는 파이썬 프로그램 작성 

a=0
b=0

for i in range(101):
    if i%2==0:
        a+=i
    else:
        b+=i

print(f"짝수합: {a}, 홀수합: {b}")
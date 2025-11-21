import sys
sys.stdin = open('c1121_input.txt', 'r', encoding='utf-8')
sys.stdout = open('c1121_output.txt', 'w', encoding='utf-8')


d = [0] * 101
def main():
    result = dp_fibinacciFn(100)
    print(f'100번째 피보나치 수열 값: {result}')
    result = dp_fibinacciFn(10)
    print(f'10번째 피보나치 수열 값: {result}')
    
    dp_bottomupFn()
    dp_makeoneFn()
    dp_antwarrierFn()
    dp_tileFn()
    dp_coinsFn()
    
def dp_coinsFn():
    print('동전 문제 함수')
    n,m = map(int,input().split())
    array = []
    
    for i in range(n):
        array.append(int(input()))
        
        d = [10001] * (m + 1)
        
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001:
                d[j] = min(d[j],d[j - array[i] + 1])
    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])
    
    
def dp_tileFn():
    n = int(input().rstip())
    d2 = [0] * (n+1)
    
    d2[1] = 1
    d2[2] = 3
    
    for i in range(3, n+1):
        d2[i] = d2[i - 1]+ 2 *d2[i-2]
        
    print(f'2xn 타일링 {n}번 값: {d2[n]}')
    
    
def dp_antwarrierFn():
    n = int(input().strip())
    array = list(map(int, input().split()))
    #dp 테이블 초기화
    d = [0] * 100
    #첫 번째 값, 두 번째 값 설정
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    #계산
    for i in range(2,n):
        d[i] - max(d[i -1], d[1 - 2] + array[i])
    #결과출력
    print(f'결과출력')
    

    
def dp_fibinacciFn(n):
    if n <= 2:
        d[0] = 1
        d[1] = 1
        
    if d[n] != 0:
        return d[n]
    
    d[n] = dp_fibinacciFn(n-1) + dp_fibinacciFn(n-2)
    
    return d[n]

def dp_bottomupFn():
    #바텀업(하향식) 피보나치 수열 함수
    d[0] = 1
    d[1] = 1
    
    for i in range(2, 101):
        d[i] = d[i - 1] + d[i - 2]
        
    print(f'bottomup 100번째 값: {d[100]}')
    print(f'bottomup 10번째 값: {d[10]}')
    
def dp_makeoneFn():
    n = int(input().strip())
    
    d1 = [0] * (n+1)
    d1[0] = 0
    d1[1] = 0
    
    for i in range(2, n+1):
        d1[i] = d1[i-1] + 1
        
        if i % 2 == 0:
            d1[i] = min(d1[i], d1[i//2] + 1)
        if i % 3 == 0:
            d1[i] = min(d1[i], d1[i//3] + 1)
        if i % 5 == 0:
            d1[i] = min(d1[i], d1[i//5] + 1)
            
    print(f'1로 만들기 {n}번 값: {d1[n]} ')


if __name__ == "__main__":
    main()
    
sys.stdin.close()
sys.stdout.close()

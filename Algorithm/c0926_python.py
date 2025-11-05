import numpy as np

##import sys

from itertools import permutations, combinations
##try:
##    sys.stdin = open("input.txt", "r")
##    sys.stdout = open("output.txt", "w")
##except FileNotFoundError:
##    pass # 파일이 없으면 그냥 표준 입출력 사용

from itertools import product
data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result)  

from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)

def main():
    print("main")
    f1()
    f2()
    listvsnumpyfn() #변수 이름 잘 지정하기
    dictfn()
    setfn()
    intputFn()
    percomFn()
    
def percomFn():
    data = ['A', 'B', 'C']
    perm1 = permutations(data, 3)
    print(list(perm1))
    #print(*perm1) #이터레이터는 한번 사용하면 소멸됨.
    
    # ^l:현재위치, ^F2: 같은 단어 동시 선택
    
    perm2 = permutations(data, 1)
    print(list(perm2))
    
    combi1 = list(combinations(data, 3))
    print(list(combi1))
    
    combi2 = list(combinations(data, 2))
    print(list(combi2))
    
    
def intputFn():
    #data = input("데이터 입력 \n")
    #input()은 하나의 문자열로 입력.
    #print(data)
    data = map(int,input("데이터 입력 \n").split())
    #print(a,b,c)
    #a,b,c = map(int,input("데이터 입력 \n").split())
    #data = list(map(int,input("데이터 입력 \n").split()))
    #data = tuple(map(int,input("데이터 입력 \n").split()))
    #print(a,b,c)
    print(type(data))
    
    #data1 = sys.stdin.readline().rstrip() #빠입출
    #print(data1)
    #a,b,c = tuple(sys.stdin.readline().rstrip())
    #a,b,c = tuple(list(map(sys.stdin.readline().rstrip().split())))
    #print(type(data),data)
    #print(a,b,c)
    
    argfn(1,2,3, a=1, b=1)
    
def argfn(*t1,**d1):
    print(t1, type(t1))
    print(d1, type(d1))
    
    
def setfn():
    a = {1,2,3,4,5}
    b = {4,5,6,7,8}
    
    aub1 = a | b
    aub2 = a.union(b)
    print(aub1, aub2, sep="\n")
    
    if 10 in aub1:
        aub1.remove(10)
        print(aub1)
        
def dictfn():
    d1 = {"사과":"apple", "바나나":"banana", "코코넛":"coconut"}
    
    
    for i in d1:
        print(d1[i])
        
    for item in d1.items():
        print(item)
        
    for key in d1.keys():
        print(key)     
        
    for value in d1.values():   
        print(value)
        
def listvsnumpyfn():
    print("리스트와 넘파이 차이")
    l1 = [1,2,3,4,5]
    nl1 = np.array([1,2,3,4,5])
    
    for i in range(5):
        print(l1[i], id(l1[i]), type(l1[i]))
    for i in range(5):
        print(nl1[i], id(nl1[i]), type(nl1[i]))
        
    l1 = [1, 1.2, "Hello", True]
    nl1 = np.array([1, 1.2, "Hello", True])
    
    for i in range(4):
        print(l1[i], id(l1[i]), type(l1[i]))
    for i in range(4):
        print(nl1[i], id(nl1[i]), type(nl1[i]))
        
    
def f1():
    print("miniconda -> 가상환경 설정(3.10)")
    print("패키지, numpy, pandas, etc")
    print("패키지 : conda -> pip")


def f2():
    print("아래쪽에 함수를 넣어도 된다.")
    a = (1,2,3) #packing
    aa,bb,cc = a #unpacking
    
if __name__ == "__main__":
    print("파이썬 문법 심화")

    main()
    
# 9월 19일 파이썬 기초 문법
# boolean은 정수에 포함.

def minFn():
    x = 1 #정수는 immutable(값 변경 불가)
    y = x
    
    print("1. ",x,y,id(x),id(y))
    
    y = 3
    print("2. ",x,y,id(x),id(y))
    
    list1 = [1,2,3] #리스트는 mutable(값 변경 가능)
    list2 = list1
    print("3. ",list1,list2,id(list1),id(list2))
    list2[0] = 100
    print("4. ",list1,list2,id(list1),id(list2))
    list2.append(4) # 값이 바뀐다.
    print("5. ",list1,list2,id(list1),id(list2))
    list2 = [10,20,30]
    print("6. ",list1,list2,id(list1),id(list2))
    
    ㅣ1 = [1,2,3]
    ㅣ2 = [1,2,3]
    print("7. ",ㅣ1,ㅣ2,id(ㅣ1),id(ㅣ2))
    
def zeroFn():
    if(1):
        print("1, True")
    if(0):
        print("0, False")
    if(-1):
        print("-1, True")
    if(""): #False
        print("Empty string, True")
    if(" "): #True
        print("Null string, True")
    if("\0:"): #Null 문자 : True
        print("\0, True")
    if([]):
        print("Null list, True")
    if(0.00000000000000001):
        print("0.00000000000000001, True")
    if(None):
        print("None, True")
        
def complexFn():
    a = 3 + 4j
    print("complex :", a, type(a))
    print("real :", a.real)
    print("imag :", a.imag)
    
def f1():
    a = 0.3; b = 0.6
    total = a + b
    if (total == 0.9):
        print("True")
    else:
        print("False")
    print(total)
    
def matrixFn():
    #2차원 리스트 초기화의 잘못된 예제
    m = 5
    n = 7
    l1 = [[0] * m] * n #2차원 리스트
    l1[2][3] = 100
    for i in range(m):
        print(l1[i])
        
    #2차원 리스트 초기화의 올바른 예제 **중요**
    l2 = [[0]*m for i in range(n)] #2차원 리스트
    l2[2][3] = 100
    for i in range(m):
        print(l2[i])
        
def listsortFn():   
    data = [3,1,4,2,5,8,7,6]
    #리스트의 멤버 함수로 리스트 자체를 정렬
    data.sort()
    print(data)
    
    data = [3,1,4,2,5,8,7,6]
    #리스트를 정렬해서 결과를 반환하는 내장함수
    sorted(data)
    print(data)
    
    data = [3,1,4,2,5,8,7,6]
    data1 = data[::-1] #리스트를 역순으로 배열
    print(data1)
    
    #리스트의 값을 지울 때는 있는지 확인하고 지우는 것이 안전
    if 10 in data:
        data.remove(10)
    print(data)
    
    #Tip: 1. set(data) -> 필요한 작업 - 2. list로 바꾸자!
    
    
def listsetFn():
    data = [3,2,4,3,5,6,7,3,4,4,4,2,5,8,7,6]
    remove_set = {3,5,7} #중복값 허용하지 않음
    
    #!!!!!아주 중요함!!!!!
    result = [i for i in data if i  not in remove_set]
    print(result)
    

if __name__ == "__main__":
    print("test")
    
    minFn()
    zeroFn()
    complexFn()
    f1()
    matrixFn()
    listsortFn()
    listsetFn()
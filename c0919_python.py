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
    
    
    
    

if __name__ == "__main__":
    print("test")
    
    minFn()
    
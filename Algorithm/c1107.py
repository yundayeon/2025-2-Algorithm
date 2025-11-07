#정렬연습
#퀵 정렬 기말 문제로 나올 확률 500% 피벗

def main():
    selectionFn()
    insertionFn()
    quicksortFn()
    quicksortFn2()
    sortlibFn()
    listTupleFn()
    listTupleFn2()
    
def listTupleFn2():
    array = [23,12,45,67,34]
    #첫 번쨰 원소를 기준으로 정렬
    TupleinList = list(enumerate(array))
    print("튜플 정렬 결과:", TupleinList)
    TupleinList.sort(key = lambda x: x[1])
    print("튜플 정렬 결과:", TupleinList)
    TupleinList.sort(key = lambda x: -x[1])
    print("튜플 정렬 결과:", TupleinList)
    
    #리스트 안에서 첫 번째 원소만 출력
    result = [x[0] for x in TupleinList]
    print("튜플 정렬 결과:", result)
    #리스트 안에서 두 번째 원소만 출력
    result = [x[1] for x in TupleinList]
    print("튜플 정렬 결과:", result)
    
def listTupleFn():
    array = [('바나나',3),('사과',1),('귤',2)]
    #첫 번째 원소를 기준으로 정렬
    array.sort()
    print('튜플 정렬 결과:',array)
    #두 번째 원소를 기준으로 정렬
    array.sort(key=lambda x: x[1])
    print("튜플 결과 정렬:",array)
    #두 번째 원소를 기준으로 내림차순 정렬
    array.sort(key=lambda x: x[1], reverse=True)
    print("튜플 결과 정렬:",array)
    array.sort(key=lambda x: -x[1])
    print("튜플 결과 정렬:",array)
    
    
    
def sortlibFn():
    array = [7,5,9,0,3]
    print(sorted(array)) #1) [0,3,5,7,9], 값을 반환
    print(array)         #2) [7,5,9,0,3], 원본은 그대로
    
    array = [7,5,9,0,3]
    print(array.sort())  #3) None, 자신을 정렬하고 None 반환
    print(array)         #4) [0,3,5,7,9] 
    
    
    
def quicksortFn2(array):
    print("퀵 정렬2 시작")
    
    array = [7,5,9,0,3,1,6,2,4,8]
    
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quicksortFn2(left_side) + [pivot] + quicksortFn2(right_side)

print("퀵 정렬2 결과:", quicksortFn2(array))
    
    
def quicksort(array,start,end):
    #종료 조건
    if start >= end:
        return
    
    pivot = start
    left = start +1
    right = EncodingWarning
    
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때 까지 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right += 1
            
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
            
        quicksort(array, start, right -1)
        quicksort(array,right+1, end)
        
def quicksortFn():
    print("퀵 정렬 시작")
    array = [7,5,9,0,3,1,6,2,4,8]
    
    quicksortFn(array,0,len(array) -1)
    print(array)
    
def insertionFn(): ##기말고사 문제: 삽입 정렬 for문 6-3.py 삽입 정렬 소스 코드
    print("삽입 정렬 시작")
    array = [7,5,9,0,3,1,6,2,4,8]
    length = len(array)
    for i in range(1, length):
        for j in range(i, 0 ,-1):
        #     print(f"({i},{j})", end=' ')
        # print()
            print(f"({i},{j})", end=' ')
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
        print('삽입 정렬 결과', array)
    
    array
def selectionFn():
    array=[7,5,9,0,3,1,6,2,4,8]
    
    length = len(array)
    for i in range(length-1): ##**기말고사 시험문제
        min_index = i
        for j in range(i+1, length):
            print(f"({i},{j})", end=' ')
            if array[min_index] > array[j]:
                min_index = j
                
            #swap
            array[i],array[min_index] = array[min_index], array[i]
                
            print()
            # if array[j] < array[j-1]:
            #     array[j],array[j-1] = array[j-1],array[j]
            # else:
            #     break
            
    ## 01 02 03 0(n-1)
    ## 12 13 1(n-1)
    ## (n-2)(n-1)


if __name__ == "main":
    main()


def main():
    print('test')
    binarySearch1()
    binarySearch2()
    
    ricecakerFn()
    
def ricecakerFn():
    n = 5 #떡의 개수
    m = 20 #요청한 떡의 길이
    
    rice_cakes = [4, 42, 40, 26, 46]
    
    start = 0
    end = max(rice_cakes)
    
    result = 0
    
    while start <= end:
        total = 0
        mid = (start + end) // 2
        
        for cake in rice_cakes:
            if cake > mid:
                total += cake - mid
                
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
            
    print(f"Optinal cutting height: {result}")
    
    
    
#재귀 함수를 사용한 이진 탐색
def binarySearch1():
    array = [1,3,5,7,9,11,13,15,17,19]
    target = 7
    
    result = binary_search_recursive(array, target, 0, len(array) - 1)
    if result is not None:
        print(f"Target {target} found at index {mid}.")
    else:
        print(f"Taget {target} not found in the array.")
        
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None #Target not found
    
    mid = (start + end)
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, start, mid + 1, end)   
    
    
#순환문을 사용한 이진 탐색
def binarySearch2():
    array = [1,3,5,7,9,11,13,15,17,19]
    target = 7
    
    start = 0
    end = len(array) -1
    
    while start <= end:
        mid = (start + end) // 2 #중간 인덱스 계산
        
        if array[mid] == target:
            print(f"Target {target} found at index {mid}.")
            return
        elif array[mid] < target:
            s
            tart = mid + 1
        elif array[mid] > target:
            end = mid -1
            
    if mid == target:
        print(f"Target {target} found index {mid}.")
    else:
        print(f"Taget {target} not found in the array.")
        
    
    
if __name__ == "__main__":
    main()
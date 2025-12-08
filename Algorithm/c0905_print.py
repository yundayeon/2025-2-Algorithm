import time

start = time.time()

sum=0

for i in range(10000000):
    sum+=i

end = time.time()

excute = end-start


print('Hello Python!')
print("Nice to meet you.")
print('Hello "Python"')
print("Hello 'Python'")
print('Hello', 'Python!') # 나열 연산자
print('Hello' + 'Python!')



# 방법 2
print("one") ; print("two")
print('I like Python \
    But I do not like Ruby.')
print("""I like Python
But I don't like C.""")
# 2) 다중 문자열 : """, '''
multiline = """
여러줄 주석을 사용할 때
이렇게 큰따옴표 또는 작은따옴표 씀
""" # 여러 줄 문자열을 나타내는 것, 주석은 (#)을 쓴다.

tset='teststring'


# 방법 3
print('Hello', end='엔터대신 들어갈 문자열') 
print('Python')
print('Hello', end='&&&')
print('Python')
print('Hello', 'Python', sep='공백대신 들어갈 문자열') 
f = open('dump.txt', 'w')
# 파일 입출력 open -> fopen
# print -> pprint

print('Hello Python', file=f)
print('문자열을 파일에 쓰기 연습', file=f) 
f.close()
import sys
print('Hello Python', file=sys.stderr)


# 방법 4
print('My mother\'s house')
print('\', \", \\, \a, \t, \n')


# 방법 5
i = 123 
f = 3.14 
s = 'Hello' 

# 옛날 버전이라 요즘엔 안씀
print('i: %d, f: %f, s: %s' % (i, f, s))
print('i: %9d, f: %5.2f, s: %7s' % (i, f, s))
print('i: %09d, f: %05.2f, s: %7s' % (i, f, s))
print('i: {}, f: {}, s: {}'.format(i, f, s))
print('f: {1}, i: {0}, s: {2}'.format(i, f, s))
print('f: {ff}, i: {ii}, s: {ss}'.format(ii=i, ff=f, ss=s))

# 많이 사용하는 방법
print(f"정수: {i:5}, 실수: {f:5.2}, 문자열: {s:20}")
print(f"정수: {i:05}, 실수: {f:.2}, 문자열: {s:<20}")


# 방법 6. 
# 파이썬은 모든 데이터 타입을 객체 처리한다.
print('Hello Python!'.center(20))
print('Hello Python!'.rjust(20))
print('Hello Python!'.ljust(20))
print('Hello Python!'.zfill(20))
print('hello python!'.capitalize())
print('hello python!'.upper())
print('hello python!'.lower())


# 방법 7. f-string(3.6)
# f-string은 print에서만 사용하는 것이 아니고, 문자열을 만들때도 사용한다.
x=1
y=2
f"{x}+{y}는 {x+y}입니다."
print(f"{x=}, {y=}")
str1 = "Python"
f"{str1}의 길이는 {len(str1)}입니다."
f"첫 두 글자는 {str1[:2]}입니다."
f"거꾸로 하면 {str1[::-1]}입니다."
from datetime import date
오늘 = f"오늘은 {date.today()}입니다."
print(오늘)


print(f"실행시간은 {excute}, 합:{sum}")
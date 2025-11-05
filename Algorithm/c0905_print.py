import time

start = time.time()

sum=0

for i in range(10000000):
    sum+=i

end = time.time()

excute = end-start

#작은 따옴표, 큰 따옴표
# ' "" ', " ' ' "
# C언어 : '' : 문자 (character), "" : 문자열(string)

print('Hello Python!')
print("Nice to meet you.")
print('Hello "Python"')
print("Hello 'Python'")
print('Hello', 'Python!') # 나열 연산자
print('Hello' + 'Python!')

# 1. 문법(syntax) -> 2. 입력(input) -> 3. 출력(output) interface
# 4. 유지관리(버전 관리) -> 5. 최적화(optimization) - refactoring


# 방법 2
# 1) 한 문장이 너무 길때 백슬래쉬(\) 주의사항. 공백을 포함하여 문자가 들어가면 안됨
# 한 줄에 두 문장 이상 쓸때 : 세미콜론(;)
print("one") ; print("two")
print('I like Python \
      But I do not like Ruby.')
print("""I like Python
But I don't like C.""")
# 2) 다중 문자열 : """, ''' -> (multiline string)
multiline = """
여러줄 주석을 사용할 때
이렇게 큰따옴표 또는 작은따옴표 씀
""" # 여러 줄 문자열을 나타내는 것이지, 주석은 (#)만 쓴다.

tset='teststring'


# 방법 3
print('Hello', end='엔터대신 들어갈 문자열') # default: 엔터키, cout<<a<<" ";
print('Python')
print('Hello', end='&&&')
print('Python')
print('Hello', 'Python', sep='공백대신 들어갈 문자열') # default: blank, space
f = open('dump.txt', 'w')
# 파일 입출력 open -> fopen 추천
# print -> pprint
print('Hello Python', file=f)
print('문자열을 파일에 쓰기 연습', file=f) # 한글 셋팅 안하고 쓰면 utf-8 인코딩 이슈로 안보임
f.close()
import sys
print('Hello Python', file=sys.stderr)


# 방법 4
# 탈출문자 (escape sequance, escape character)
print('My mother\'s house')
print('\', \", \\, \a, \t, \n')


# 방법 5
i = 123 # integer
f = 3.14 # float
s = 'Hello' # string

# 여기는 옛날 버전이라 요즘엔 안씁니다.
print('i: %d, f: %f, s: %s' % (i, f, s))
print('i: %9d, f: %5.2f, s: %7s' % (i, f, s))
print('i: %09d, f: %05.2f, s: %7s' % (i, f, s))
print('i: {}, f: {}, s: {}'.format(i, f, s))
print('f: {1}, i: {0}, s: {2}'.format(i, f, s))
print('f: {ff}, i: {ii}, s: {ss}'.format(ii=i, ff=f, ss=s))

# 제일 많이 사용하는 방법
print(f"정수: {i:5}, 실수: {f:5.2}, 문자열: {s:20}")
print(f"정수: {i:05}, 실수: {f:.2}, 문자열: {s:<20}")


# 방법 6. 파이썬은 모든 데이터 타입을 객체(object) 처리한다.
print('Hello Python!'.center(20))
print('Hello Python!'.rjust(20))
print('Hello Python!'.ljust(20))
print('Hello Python!'.zfill(20))
print('hello python!'.capitalize())
print('hello python!'.upper())
print('hello python!'.lower())


# 방법 7. f-string(3.6)
# f-string은 print에서만 사용하는 것이 아니라, 문자열을 만들때도 사용함.
x=1
y=2
f"{x}+{y}는 {x+y}입니다."
print(f"{x=}, {y=}")
str1 = "Python"
f"{str1}의 길이는 {len(str1)}입니다."
f"첫 두 글자는 {str1[:2]}입니다."
f"거꾸로 하면 {str1[::-1]}입니다." # 리스트를 역순(reverse)으로 만들때 : [::-1] <-- 중간고사 정답임 이거
from datetime import date
오늘 = f"오늘은 {date.today()}입니다."
print(오늘)


print(f"실행시간은 {excute}, 합:{sum}")
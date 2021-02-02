# Lambda 는 함수를 딱 한줄만으로 만들게 해주는 훌륭한 도구이다.

#lambda 인자 : 표현식

def plus(x, y):
    return x + y


print(plus(10, 20))


a = (lambda x, y: x+y)(10, 20)
print(a)

# 아직은 이게 편한지에 대한 감이 잘 오지 않는다.

# map 에서의 활용
# map(함수, 리스트)
# map은 함수와 리스트를 인자로 받아서, 리스트로부터 원소를 꺼내어 함수에 적용시키고 그것을
# 새로운 리스트에 담아준다.

c = map(lambda x: x + 2, range(5))
print(c)
# 함수 객체가 나오는 이유는, 람다 표현식은 이름이 없는 함수를 만들기 떄문이다.
# 그래서 람다 표현식을 익명함수(anonymous function)이라하기도한다

v = list(map(lambda x: x + 2, range(5)))
print(v)

g = list(map(lambda x: x + 10, [1, 2, 3]))
print(g)
# filter
#filter(함수, 리스트)
# filter는 리스트의 요소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어 준다.
f = list(filter(lambda x: x < 5, range(10)))
print(f)

# 요전에 풀엇던 문제에서의 람다
#sorted(fail, key=lambda x: fail[x], reverse=True)
#

a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
c = sorted(a, key=lambda x: x[0])
print(c)


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
gg = sorted(student_tuples, key=lambda x: x[2])
print(gg)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        print(first, second)

    def add(self):
        result = self.first + self.second
        return result


a = FourCal()   # a라는 객체를 만듭니다.
# 객체를 통해 클래스의 메서드를 호출하려면 다음과 같은 방식을 취해야한다. dot(.)이용
a.setdata(4, 2)
print(a.setdata(4, 2))
print(a.first)
print(a.add())
# print(FourCal.setdata(4, 2))
# TypeError: setdata() missing 1 required positional argument: 'second'

# 객체 . 함수 처럼 호출하면 함수(메서드:클래스안의 함수)의 첫번쨰 매개변수 self에는
# 메서드를 호출한 객체 a가 자동으로 전달되기 떄문입니다.

# 즉그러니까 객체형태로 클래스를 불러와 메서드를 사용하면 self 자리에 뭐 안넣어줘도된다는것


# add 메서드의 매개 변수는 self 이고 반환 값은 result이다.
# result = self.first + self.second 였지만
# a.add() 와 같이 객체에 의해 add메서드를 수행하면 self에는 객체 a가 자동입력되므로
# result = a.first + a.second 로 해석을 한다. 
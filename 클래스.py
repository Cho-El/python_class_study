class Family:
    a = 1 # 클래스 변수
    def __init__(self, k) -> None:
        self.lastname = k
    def change(self, key):
        self.lastname = key

a = Family('d')
b = Family('e')
print(a.a)
print(b.a)
print(a.lastname)
print(b.lastname)

a.change('x')
b.change('y')

Family.a = 2
print(a.a)
print(b.a)
print(a.lastname)
print(b.lastname)

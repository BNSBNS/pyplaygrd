class Test1:
    print('class test1')
    def doTest1(self, mass: float, height:float) -> None:
        print("i am in class test1, do test1, ")

        tot = self.doTest2(mass, height)
        print("i am in class test1, do test1, ")

        return 100+ tot
    
    def doTest2(self, mass: float, height: float):
        pe = mass * 10000 
        print('i am in class test1, do test2 ')

        return pe
    
    print('class test1 end')


class Test2:
    print('class test2')
    def doTest1(self, mass:float, velocity: float) -> None:

        print('i am in class test2, dotest1')

        tot = self.doTest2(mass, velocity)
        print("i am in class test2, do test1, ")

        return tot


    print('class test2 end')




class Tayo(Test1, Test2):
    def __init__(self, a:float, b:float = 100) -> None:
        print('i am in class tayo, a = {}, b = {}'.format(a,b))

        self.a = a
        self.b = b
        if b is None: 
            print('b is none')
        else: 
            print('created')

        # tee = self.getdoTest1()

    def getdoTest1(self) -> float:
        print('i am in tayo, getdotest1')

        return self.doTest1(self.a,self.b)


def main():
    ka = Tayo(1,0)
    ke = ka.getdoTest1()

if __name__ == "__main__":
    main()
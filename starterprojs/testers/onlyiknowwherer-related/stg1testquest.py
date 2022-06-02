class Anna:

    def ana_ener(self, mass: float, height: float) -> None:
        pe = self.ana_pot_ene(mass, height)
        print('i am anna, anna ener')
        return 1000 - pe

    def ana_pot_ene(self, mass:float, height:float):
        pe = mass * 9.81 * height
        print('i am anna, anna pot ene')
        return pe


class Kar:

    def ana_ener(self, mass:float, velocity: float) -> None:
        print('kar')
        ke = 0.5 * mass * velocity ** 2

        return ke

class Yoyota(Kar,Anna):
    def __init__(self, a: float, b: float=100) -> None:

        self.a = a
        self.b = b

        if b is None:
            print("provide val for b")
        else: 
            print(self.a)
            print(self.b)
            print(self.ana_ener(5,5))
            print(self.ana_pot_ene(6,6))
            
            print("created")

    def get_kin(self) -> float:
        print('yoyota get kin')
        return self.ana_ener(self.a, self.b)



def main():
    print('im main')
    ca = Yoyota(1)

if __name__ == "__main__":
    main()
class Moraba:
    def __init__(self, tool):
        self.tool = tool

    def mohit(self, tool):
        print("=-" * 20)
        return f"Mohit Moraba : {tool * 4}"

    def masahat(self, tool):
        print("=-" * 20)
        return f"Masahat Moraba : {tool * tool}"

    def __str__(self):
        return f"class Moraba : {self.tool}"


class Mostatil:
    def __init__(self, tool, arz):
        self.tool = tool
        self.arz = arz

    def mohit(self, tool, arz):
        print("=-" * 20)
        return f"Mohit Mostatil : {(tool + arz) * 2}"

    def masahat(self, tool, arz):
        print("=-" * 20)
        return f"Masahat Mostatil : {tool * arz}"

    def __str__(self):
        return f"class Mostatil : {self.tool} , {self.arz}"


class Mosalas:
    def __init__(self, zel1, zel2, ghaede, ertefa):
        self.zel1 = zel1
        self.zel2 = zel2
        self.ghaede = ghaede
        self.ertefa = ertefa

    def mohit(self, zel1, zel2, ghaede):
        print("=-" * 20)
        return f"Mohit Mosalas : {zel1 + zel2 + ghaede}"

    def masahat(self, ghaede, ertefa):
        print("=-" * 20)
        return f"Masahat Mosalas : {(ertefa + ghaede) / 2}"

    def __str__(self):
        return f"class Mosalas : {self.zel1}, {self.zel2}, {self.ghaede}, {self.ertefa}"


class Dayere:
    def __init__(self, shoa):
        self.shoa = shoa
        self.pi = 3

    def mohit(self, shoa):
        print("=-" * 20)
        return f"Mohit Dayere : {2 * self.pi * shoa}"

    def masahat(self, shoa):
        print("=-" * 20)
        return f"Masahat Dayere : {self.pi * (shoa ** 2)}"

    def __str__(self):
        return f"class Dayere : {self.shoa}, {self.pi}"


if __name__ == '__main__':
    print("=-" * 20)
    while True:
        try:
            quest1 = int(input("Moraba (1) , Mostatil (2) , Mosalas (3) , Dayere (4) : "))
            quest2 = int(input("Mohit (1) , Masahat (2) : "))
            break
        except ValueError:
            print("#-" * 15)
            print("Faghat Adad Vared Konid!")
            print("# " * 15)
            continue

    if quest1 == 1 and quest2 == 1:
        num1 = int(input("Zel : "))
        if num1 < 0:
            print("Adad zire 0 ast!")
        else:
            moraba = Moraba(num1)
            print(moraba.mohit(num1))
    elif quest1 == 1 and quest2 == 2:
        num1 = int(input("Zel : "))
        if num1 < 0:
            print("Adad zire 0 ast!")
        else:
            moraba = Moraba(num1)
            print(moraba.masahat(num1))
    if quest1 == 2 and quest2 == 1:
        num1 = int(input("Tool : "))
        num2 = int(input("Arz : "))
        if num1 < 0 or num2 < 0:
            print("Adad zire 0 ast!")
        else:
            mostatil = Mostatil(num1, num2)
            print(mostatil.mohit(num1, num2))
    elif quest1 == 2 and quest2 == 2:
        num1 = int(input("Tool : "))
        num2 = int(input("Arz : "))
        if num1 < 0 or num2 < 0:
            print("Adad zire 0 ast!")
        else:
            mostatil = Mostatil(num1, num2)
            print(mostatil.masahat(num1, num2))
    if quest1 == 3 and quest2 == 1:
        zel1 = int(input("Zel 1 : "))
        zel2 = int(input("Zel 2 : "))
        zel3 = int(input("Zel 3 : "))
        if zel1 < 0 or zel2 < 0 or zel3 < 0:
            print("Adad zire 0 ast!")
        else:
            mosalas = Mosalas(zel1, zel2, zel3, 0)
            print(mosalas.mohit(zel1, zel2, zel3))
    elif quest1 == 3 and quest2 == 2:
        ghaede = int(input("Ghaede : "))
        ertefa = int(input("Ertefa : "))
        if ghaede < 0 or ertefa < 0:
            print("Adad zire 0 ast!")
        else:
            mosalas = Mosalas(0, 0, ghaede, ertefa)
            print(mosalas.masahat(ghaede, ertefa))
    if quest1 == 4 and quest2 == 1:
        shoa = int(input("Shoa : "))
        if shoa < 0:
            print("Adad zire 0 ast!")
        else:
            dayere = Dayere(shoa)
            print(dayere.mohit(shoa))
    elif quest1 == 4 and quest2 == 2:
        shoa = int(input("Shoa : "))
        if shoa < 0:
            print("Adad zire 0 ast!")
        else:
            dayere = Dayere(shoa)
            print(dayere.masahat(shoa))
    if quest1 < 0 or quest1 > 4:
        print("-" * 30)
        print("Gozine ra dorost vared konid !")
        print("-" * 30)
    elif quest2 < 0 or quest2 > 2:
        print("-" * 30)
        print("Gozine ra dorost vared konid !")
        print("-" * 30)
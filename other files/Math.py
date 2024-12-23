import math


def Jam(num1, num2):
    print("=-" * 20)
    return f"{num1} + {num2} = {num1 + num2}"


def Menha(num1, num2):
    print("=-" * 20)
    return f"{num1} - {num2} = {num1 - num2}"


def zarb(num1, num2):
    print("=-" * 20)
    return f"{num1} x {num2} = {num1 * num2}"


def Taghsim(num1, num2):
    print("=-" * 20)
    return f"{num1} / {num2} = {num1 / num2}"


def Tavaan(num1, num2):
    print("=-" * 20)
    return f"{num1} ^ {num2} = {num1 ** num2}"


def Radical(num1):
    print("=-" * 20)
    if num1 <= 0:
        return f"adade {num1} zire 0 ast! [Please Try Again]"
    else:
        radi = math.sqrt(num1)
        return f"√{num1} = {radi}"


def Ghadre_Motlagh(num1):
    print("=-" * 20)
    num = str(num1)
    if num[0] == "-":
        return f"|{num1}| = +{num[1:]}"
    else:
        return f"|+{num1}| = +{num1}"


def DarSad(num1, num2):
    print("=-" * 20)
    return f"{num1} % {num2} = {num1 * 100 / num2} %"


if __name__ == '__main__':
    while True:
        while True:
            try:
                print("-" * 40)
                number1 = int(input("Lotfan adad vared konid : "))
                break
            except ValueError:
                print("Adad sahih vared konid ! [Please Try Again]")
                continue

        question = input("+ , - , x , / , ^ , V , % , || : ")

        if (question == "+" or question == "=" or question == "-" or question == "x" or question == "8" or
                question == "/" or question == "^" or question == "6" or question == "%" or question == "5"):
            while True:
                try:
                    number2 = int(input("Lotfan adad dovom ra vared konid : "))
                    break
                except ValueError:
                    print("Adad sahih vared konid ! [Please Try Again]")
                    continue

        if question == "+" or question == "=":
            jam = Jam(number1, number2)
            print(jam)

        elif question == "-":
            menha = Menha(number1, number2)
            print(menha)

        elif question == "x" or question == "8":
            zarb = zarb(number1, number2)
            print(zarb)

        elif question == "/":
            taghsim = Taghsim(number1, number2)
            print(taghsim)

        elif question == "^" or question == "6":
            tavan = Tavaan(number1, number2)
            print(tavan)

        elif question.upper() == "V":
            radical = Radical(number1)
            print(radical)

        elif question == "%" or question == "5":
            darsad = DarSad(number1, number2)
            print(darsad)

        elif question == "||":
            ghadre_motlagh = Ghadre_Motlagh(number1)
            print(ghadre_motlagh)

        else:
            print("yani chi ?! [ Please try again ]")

        print("=-" * 20)
        question = input("Dobare ? [y, n] : ")

        javab = {"movafagh bashi :)",
                 "Khoda hafez :)",
                 "Badan mibinamet ;)",
                 "Bye bye :D",
                 "Dobare biai ha (^_^)"}
        if question.lower() == "y":
            continue
        elif question.lower() == "n":
            for item in javab:
                a = item
            print("-" * 40)
            print(a)
            break
        else:
            print("Lotfan ya [ y ] ya [ n ] ra vared konid !")
            break

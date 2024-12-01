

porsesh = 0
nomarat = 0
while True:
    print("=-" * 20)
    try:
        name_dars = input("Name dars : ")
    except FileNotFoundError:
        print("")
    if name_dars == "end":
        break
    if name_dars == "":
        print("[ Name dars vared nashode ! ]")
        break
    else:
        try:
            print("-" * 40)
            nomre = float(input("Nomre : "))
            if nomre < 0:
                print("[ Nomre zir 0 ast ! ]")
                continue
            elif nomre > 20:
                print("[ Nomre bayad beyn 0 ta 20 bashe ]")
                continue
            print("-" * 40)
            zarib = float(input("Zarib : "))
        except ValueError:
            print("[ Lotfan adad sahih vared konid ! ]")
            continue
        if zarib <= 0 or zarib > 4:
            print("[ Lotfan zarib 1 ta 4 vared konid ! ]")
            continue
        if zarib == 1:
            nomarat += nomre
            porsesh += 1
        elif zarib == 2:
            zaribat = nomre * 2
            nomarat += zaribat
            porsesh += 2
        elif zarib == 3:
            zaribat = nomre * 3
            nomarat += zaribat
            porsesh += 3
        elif zarib == 4:
            zaribat = nomre * 4
            nomarat += zaribat
            porsesh += 4
        else:
            print("-" * 40)
            print("what ???")

namayesh = nomarat / porsesh
namayesh = str(namayesh)
print("-" * 40)
print(f"Moadel danesh amooz = {namayesh[:6]}")


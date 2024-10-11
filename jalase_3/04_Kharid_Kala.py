print("-" * 40)
print("agar benvisid 'next' be marhale bad"
      " miravid.")
print("-" * 40)

name_vasile = {}


def kharid_kala():
    while True:
        try:
            kala = str(input("Kala ye Morede nazar khod ra vared konid : "))
            if kala.lower() == "next":
                break
            else:
                hazine = input("hazine Kala chaghadr ast? ")
                hazine = int(hazine)
        except ValueError:
            print("adad sahih vared kon!")
            continue
        if hazine <= 0:
            print("hazine zir 0 nadarim!")
        else:
            if kala in name_vasile.keys():
                hazine_1 = name_vasile.get(kala) + hazine
                name_vasile.update({kala: hazine_1})
            else:
                name_vasile.update({kala: hazine})

    return name_vasile

list_Kala = kharid_kala()


def majmoo_hazine():
    majmoo = 0
    for numbers in list_Kala.values():
        majmoo += numbers
    return majmoo


jam_kala = majmoo_hazine()


def boodje():
    while True:
        try:
            boodje_karbar = int(input("Boodje shoma cheghadr ast?"))
            if boodje_karbar > 0:
                baghi_mande = boodje_karbar - jam_kala
                if 0 > baghi_mande:
                    print("=-" * 20 + "=")
                    print(f"Hazine kala ha : {jam_kala}")
                    print("Hazine kala ha Bishtar az Boodje shoma hast !")
                    print("=-" * 20 + "=")
                else:
                    print("=-" * 20 + "=")
                    print("shoma mitavanid pardakht konid. :)")
                    print("-" * 40)
                    print(f"Hazine Kala ha ({jam_kala}) ast ,boodje shoma ({boodje_karbar}) ast ")
                    print(f"Hazine Baghi mandeh : {baghi_mande}")
                    print("=-" * 20 + "=")
            else:
                print("-" * 30)
                print("adad boodje zir 0 ast!")
                print("-" * 30)
                continue
            break
        except ValueError:
            print("adad sahih vared kon!, dobare emtehan kon.")
            continue
    return

boodje()


print("-" * 40)
print("Agar benvisid 'end' barname baste mishe.")
print("-" * 40)
def mohit_masahat():
    while True:
        tool = input("tool ra vared konid : ")
        arz = input("arz ra vared konid : ")
        if tool.lower() == "end" or arz.lower() == "end":
            print("Rooze Khoobi dashte bashid. :)")
            break
        else:
            try:
                tool = int(tool)
                arz = int(arz)
            except ValueError:
                print("-" * 40)
                print("adad sahih vared konid!")
                print("-" * 40)
                continue

        if tool == 0 or arz == 0:
            print("-" * 40)
            print("mage 0 ham mishe ???")
            print("-" * 40)
            continue
        if tool < 0 or arz < 0:
            print("-" * 40)
            print("adad zir 0 ast")
            print("-" * 40)
            continue
        if tool < arz:
            print("-" * 40)
            print("mage mishe arz bishtar az tool?")
            print("-" * 40)
            continue
        else:
            print("=-" * 20 + "=")
            print("mohit mostatil =", (tool + arz) * 2)
            print("masahat mostatil =", tool * arz)
            print("=-" * 20 + "=")
    return
mohit_masahat()
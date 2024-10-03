def mohit_masahat():
    while True:
        try:
            tool = int(input("tool ra vared konid : "))
            arz = int(input("arz ra vared konid : "))
        except ValueError:
            print("adad sahih vared konid!")
            continue
        print("---------------------------------------\nmohit mostatil =", (tool + arz) * 2)
        print("masahat mostatil =", tool * arz)
        break
    return
mohit_masahat()
print("------------------------------------------\nrooz khoobi dashte bashid khodahafez :)")

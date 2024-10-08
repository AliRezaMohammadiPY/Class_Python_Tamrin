def mohit_masahat():
    while True:
        try:
            tool = int(input("tool ra vared konid : "))
            arz = int(input("arz ra vared konid : "))
        except ValueError:
            print("adad sahih vared konid!")
        if tool < 0 or arz < 0:
            print("adad zir 0 ast")
            continue
        if tool < arz:
            print("mage mishe arz bishtar az tool?")
            continue
        else:
            print("---------------------------------------\nmohit mostatil =", (tool + arz) * 2)
            print("masahat mostatil =", tool * arz)
    return
mohit_masahat()
jam_kon = lambda voroodi1, voroodi2: voroodi1 + voroodi2
if __name__ == '__main__':
    while True:
        try:
            list1 = list(map(int, input("adaad list aval ra vared konid (ba fasele joda konid) : ").split()))
            list2 = list(map(int, input("adaad list dovom ra vared konid (ba fasele joda konid) : ").split()))
        except ValueError:
            print("lotfan adad sahih vared konid!")
            continue
        if len(list1) == len(list2):
            majmoo = list(map(jam_kon, list1, list2))
            print(f"list jam nazir be nazir = {majmoo}")
        else:
            print("lotfan list ha ro ham andaze benvisid!")

        retry = input("Dobare? (yes, no) : ")
        if retry == "yes":
            continue
        else:
            print("Movafagh bashi, KhodaHafez :)")
            break


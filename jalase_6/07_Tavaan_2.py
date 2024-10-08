print("-----------------------------------------")
print("agar benvisid 'end' barname be shoma adad haii ke dadid ra tavaan 2 midahad.")
print("-----------------------------------------")

tavaan = lambda num:num ** 2

list_num = []
while True:
    voroodi = input("adad ra vared konid: ")
    if voroodi == "end":
        if list_num == []:
            print("hich adadi vared nashode!")
            continue
        break
    else:
        try:
            voroodi = int(voroodi)
            list_num.append(voroodi)
            tavaan(voroodi)
            output = map(tavaan, list_num)
            output = list(output)
        except ValueError:
            print("adad sahih vared konid!")
print(f"Javab Tavaan 2 haye Shoma : {output}")

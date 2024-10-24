tavaan = lambda number: number ** 2


voroodi = input("List adad ra vared konid : ")
voroodi = voroodi.split(",")
list_num = []
for char in voroodi:
    char = char.replace('[', '')
    char = char.replace(']', '')
    char = char.strip()
    list_num.append(char)

try:
    list_num = map(int, list_num)
    output = map(tavaan, list_num)
    print("=-" * 20)
    print(f"Javab Tavaan 2 haye Shoma : {list(output)}")
    print("=-" * 20)

except ValueError:
    print("*" * 40)
    print("Error!\nlotfan adad sahih vared konid!\n\n[Please try Again]")
    print("*" * 40)
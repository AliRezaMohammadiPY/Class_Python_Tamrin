def majmoo(input):
    number = 0
    for item in input:
        number += item
    print(f"majmoo adad : {number}")

    
voroodi = input("list ra vared konid :")
voroodi = voroodi.replace(" ", "")
voroodi = voroodi.replace("[", "")
voroodi = voroodi.replace("]", "")
split1 = voroodi.split(",")
try:
    map1 = list(map(int, split1))
    majmoo(map1)
except ValueError:
    print("Lotfan List Adad sahih Vared konid ! [Please Try Again]")

with open("Tamrin2/Tamrin_3Voroodi", "r", encoding="utf-8") as input_txt:
    list1 = []
    read_txt = input_txt.read()
    read_txt = read_txt.replace(",",  "")
    split1 = read_txt.split()
    for i in split1:
        for j in i:
            for k in range(1, 10):
                if j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9":
                    list1.append(i)
                    break
    map1 = list(map(int, list1))
    tedad = 0
    number = 0
    for i in map1:
        number += i
        tedad += 1

    print(f"Miangin Nomarat : {number / tedad}")

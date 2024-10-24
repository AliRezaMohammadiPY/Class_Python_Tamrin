import csv

voroodi = input("addres file ra vared konid : ")
joda = voroodi.split(".")
if joda[-1] == "csv":
    try:
        with open(voroodi, "r") as csv_file:
            majmoo = 0
            reader = csv.reader(csv_file)
            header = next(reader)
            print("=-" * 10)
            print("gheymat ha :")
            for row in reader:
                print(f"\t+ {row[3]}")
                row = float(row[3])
                majmoo += row
            print(f"-" * 17)
            print(f"\t {majmoo}")
            print("=-" * 10)
    except FileNotFoundError:
        print("-" * 40)
        print("Error!\nFile peyda nashod !, [ Please Try Again ]")
        print("-" * 40)
else:
    print("-" * 40)
    print("Error !\nLotfan file [csv] vared konid!, [ Please Try Again ]")
    print("-" * 40)
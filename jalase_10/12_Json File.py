import json
with open('apple.json', 'r') as json_file:
    dict_json = json.load(json_file)
    try:
        name = input("Nam Sherkat ra vared konid : ")
    except ValueError:
        print("Error!\n[ Please Try Again ]")
    with open("report.txt", 'w', encoding="utf-8") as report:
        report.write("*" * 40)
        report.write("\n")
        report.write(f"[ etelaate sherkat {name} ]")
        report.write("\n")
        for etelaat in dict_json:
            if etelaat == "sector":
                report.write("\n")
                report.write(f"Bakhsh Sherkat : {dict_json[etelaat]}")
                report.write("\n")

            if etelaat == "fullTimeEmployees":
                report.write("=-" * 10 + "=")
                report.write("\n")
                report.write(f"Tedad karmandan tamam vaght: {dict_json[etelaat]}")
                report.write("\n")

            if etelaat == "longBusinessSummary":
                report.write("=-" * 10 + "=")
                report.write("\n")
                list_etelaat = dict_json[etelaat].split(". ")
                report.write("Kholase ye kasbo kar:")
                report.write("\n")
                for ch in list_etelaat:
                    for ch2 in ch:
                        if ch2 == ".":
                            report.write(f"\t{ch}")
                            report.write("\n")
                            break
                    else:
                        report.write(f"\t{ch}.")
                        report.write("\n")

            if etelaat == "city":
                report.write("=-" * 10 + "=")
                report.write("\n")
                report.write(f"Shahr: {dict_json[etelaat]}")
                report.write("\n")

            if etelaat == "phone":
                report.write("=-" * 10 + "=")
                report.write("\n")
                report.write(f"( Baraye ertebat ba ma be shomare ye zir tamas begirid )\nshomare telephone: {dict_json[etelaat]}")
                report.write("\n")

            if etelaat == "country":
                report.write("=-" * 10 + "=")
                report.write("\n")
                report.write(f"Keshvar: {dict_json[etelaat]}")
                report.write("\n")


        report.write("*" * 40)
        report.write("\n")
    with open("report.txt", "r") as Report:
        print(Report.read())
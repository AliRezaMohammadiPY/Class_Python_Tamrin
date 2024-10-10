index_text = input("address file .txt ra vared konid : ")
with open(index_text, "r", encoding='utf-8') as file_txt:
    content = file_txt.read()
print("-" * 40)
def kalame_shomar(matn):
    kalamat = 0
    kalame_kon = matn.split()
    for ch in kalame_kon:
        kalamat += 1
    return kalamat

def khat_shomar(matn):
    khat_ha = 0
    for ch in matn:
        for ch2 in ch:
            if ch2 == '\n':
                khat_ha += 1
            if ch2 == "'n'":
                khat_ha += 1
    khat_ha += 1
    return khat_ha

def Kalame_Yaab(matn, kalame):
    Number_kalame_yaab = 0
    kalame_kon = matn.split()
    for ch in kalame:
        Number_kalame_yaab = kalame_kon.count(kalame)

    return Number_kalame_yaab
kalame_yaab = input("kalame morede nazar ra vared konid : ")
output = Kalame_Yaab(content, kalame_yaab)

with open("Class_Python/My_File/report.txt", "w", encoding='utf-8') as report:
    report.write("-" * 40)
    report.write("\n"
                 f"tadad kalamat : {kalame_shomar(content)}"
                 "\n"
                 f"tedad khat ha : {khat_shomar(content)}"
                 "\n")
    if output == 0:
        report.write("[ kalame morede nazar yaft nashod! ]"
                     "\n")
    else:
        report.write(f"Tedad Kalame morede nazar : {Kalame_Yaab(content, kalame_yaab)}"
                     "\n")
    report.write("-" * 40)

with open("Class_Python/My_File/report.txt", "r", encoding='utf-8') as report1:
    print(report1.read())

# kalame_kon = content.split(kalame_yaab)
# if len(kalame_kon) == 1:
#     print("kalame yaft nashod!")
# elif len(kalame_kon) >= 2:
#     for ch in kalame_kon:
#         Number_kalame_yaab += 1
#     Number_kalame_yaab = Number_kalame_yaab - 1
#     print(Number_kalame_yaab)
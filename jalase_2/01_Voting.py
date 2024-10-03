print("age khasti barname baste beshe benvis 'end'")
while True:
    age = input("Sen Khod Ra Vared Konid : ")
    try:
        if age.lower() == "end":
            print("Khodahafez Rooz Khoobi dashte bashi :)")
            break
        age = int(age)
    except ValueError:
        print("Lotfan Adad Sahih (integer) Vared Konid!")
        continue
    
    if age <= 0:
        print("Manzooret ro nemifahmam :(")
    elif age >= 18:
        print("You Can Vote!")
    else:
        print("You Can't Vote!")

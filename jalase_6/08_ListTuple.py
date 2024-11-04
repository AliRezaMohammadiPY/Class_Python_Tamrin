print("-" * 55)
print("! Tavajoh: !"
      "\n\tFaghat Ozv ra vared konid va ba fasele joda konid.")
print("-" * 55)

list_tuples = []
while True:
    tedad_tuple = input("Tedad tuple haye khod ra vared konid : ")
    try:
        tedad_tuple = int(tedad_tuple)
    except ValueError:
        print("adad sahih vared konid!")
        continue
    break
for ch in range(tedad_tuple):
    tuple_bardaar = []
    tuples = input("Tuple Ra vared konid : ")
    tuple_list = lambda tup: tuples.split(",")
    tuples = tuple_list(tuples)
    for char in tuples:
        char = char.replace("(", "")
        char = char.replace(")", "")
        char = char.replace(" ", "")
        tuple_bardaar.append(char)
    try:
        int_kon = list(map(int, tuple_bardaar))
    except ValueError:
        print("adad sahih vared konid! (Please Try Again)")
        break
    if len(tuple_bardaar) < 2:
        print("Error! Tuple az 2 ozv kamtar ast. (Please Try Again)")
        break
    if len(tuple_bardaar) > 2:
        print("Error! Tuple az 2 ozv bishtar ast. (Please Try Again)")
        break
    else:
        list_tuples.append(int_kon[-1])
if len(list_tuples) == 0:
    print("-" * 30)
    print(f"list moratab shode ba ozv dovom : list khali ast")
else:
    print("-" * 30)
    print(f"list moratab shode ba ozv dovom : {list_tuples}")

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
    tuples = input("Tuple Ra vared konid : ")
    tuple_list = lambda tup:tuples.split()
    tuples = tuple_list(tuples)
    if len(tuples) < 2:
        print("Error! Tuple az 2 ozv kamtar ast. (Please Try Again)")
        break
    if len(tuples) > 2:
        print("Error! Tuple az 2 ozv bishtar ast. (Please Try Again)")
        break
    else:
        tuple_kon = lambda tuplekon:tuple(tuples)
        tuples = tuple_kon(tuples)
        list_tuples.append(tuples[1])
print(list_tuples)

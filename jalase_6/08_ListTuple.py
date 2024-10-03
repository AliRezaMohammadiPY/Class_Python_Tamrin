print("------------------------------------------\n"
      "! Tavajoh: !"
      "\nFaghat Ozv ra vared konid va ba fasele joda konid."
      "\n------------------------------------------")

list_tuples = []
tedad_tuple = int(input("Tedad tuple haye khod ra vared konid : "))
for ch in range(tedad_tuple):
    tuples = input("Tuple Ra vared konid : ")
    tuple_list = lambda tup:tuples.split()
    tuples = tuple_list(tuples)
    if len(tuples) < 2:
        print("Error! Tuple az 2 ozv kamtar ast. (Please Try Again)")
        break
    if len(tuples) > 2:
        print("Error! Tuple az 2 ozv bishtar ast. (Please Try Again)")
    else:
        tuple_kon = lambda tuplekon:tuple(tuples)
        tuples = tuple_kon(tuples)
        list_tuples.append(tuples[1])

print(list_tuples)

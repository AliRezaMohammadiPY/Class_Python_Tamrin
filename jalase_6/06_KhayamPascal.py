while True:
    try:
        number = int(input("yek adad vared konid : "))
        break
    except ValueError:
        print("adad sahih vared konid!")
        continue

#ozv aval [1]
mosalas = [[1]]

# radif = range [5] ==> [4]
for radif in range(number - 1):

#aval hame list ha [1] mizare
    radif_jadid = [1]

#agar mosalas [[1]] nabood biad tedad ro jam bezane
    if mosalas != [[1]]:

#az mosalas akhari ra migirad
        radif_ghabli = mosalas[-1]

        for ch in range(len(radif_ghabli) - 1):
#be radif jadid ezafe mishe tedad ch + yeki badesh.
            radif_jadid.append(radif_ghabli[ch] + radif_ghabli[ch + 1])

#akhar hame 1 mizare
    radif_jadid.append(1)
    mosalas.append(radif_jadid)

for radif in mosalas:
    print(radif)

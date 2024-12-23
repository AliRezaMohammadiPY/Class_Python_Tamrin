def seda_dar(input):
    horoof_seda_dar = 0
    for item in input:
        if (item.lower() == "a" or item.lower() == "e" or item.lower() == "i" or item.lower() == "o" or
                item.lower() == "u"):

            horoof_seda_dar += 1
    print("=-" * 13)
    print(f"Tedad horoof seda dar : {horoof_seda_dar}")


if __name__ == '__main__':
    voroodi = input("Yek matn vared konid : ")
    seda_dar(voroodi)

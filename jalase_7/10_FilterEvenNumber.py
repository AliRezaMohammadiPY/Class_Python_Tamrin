def EvenNumber(number):
        if number % 2 == 0:
            return number
if __name__ == '__main__':
    print("adaad list ra ba fasele joda konid.\n-----------------------------------")
    list_numbers = []
    while True:
        num = input('yek adad vared konid : ')
        if num == "end":
            break
        else:
            num = int(num)
            list_numbers.append(num)
    filter_Numbers = filter(EvenNumber, list_numbers)
    print(list(filter_Numbers))

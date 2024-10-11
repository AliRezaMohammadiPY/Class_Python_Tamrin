def EvenNumber(number):
        if number % 2 == 0:
            return number
if __name__ == '__main__':
    list_numbers = []
    while True:
        try:
            num = input('yek adad vared konid : ')
            if num == "end":
                break
            else:
                num = int(num)
                list_numbers.append(num)
        except ValueError:
            print("adad sahih vared konid!")
    filter_Numbers = filter(EvenNumber, list_numbers)
    print(f"List adaad zoj = {list(filter_Numbers)}")
def EvenNumber(number):
    if number % 2 == 0:
        return number


if __name__ == '__main__':
    list_numbers = []

    num = input('list adad ra vared konid : ')
    num = num.split(",")
    for item in num:
        item = item.replace("[", "").replace("]", "").replace(" ", "")
        list_numbers.append(item)
    try:
        int_list = map(int, list_numbers)
    except ValueError:
        print("*" * 40)
        print("Error!\nAdad sahih vared konid!")
        print("*" * 40)

    filter_Numbers = filter(EvenNumber, int_list)
    print(f"List adaad zoj = {list(filter_Numbers)}")

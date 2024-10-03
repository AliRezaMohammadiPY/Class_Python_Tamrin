def fibonacci(num):
    if num == 1:
        return 1

    elif num == 2:
        return 1

    elif num >= 2:
        javab = fibonacci(num - 1) + fibonacci(num - 2)
        return javab
if __name__ == '__main__':
    number = int(input("Enter a number: "))
    result = [fibonacci(i) for i in range(1, number + 1)]
    if result is not None:
        print(result)
    else:
        print("adad sahih vared konid.")

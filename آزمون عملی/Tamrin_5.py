class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def masahat(self):
        print("=-" * 13)
        print(f"Masahat Mostatil : {self.width * self.height}")

    def mohit(self):
        print("=-" * 13)
        print(f"Mohit Mostatil : {(self.width + self.height) * 2}")

if __name__ == '__main__':
    tool = input("Tool Mostatil : ")
    arz = input("Arz Mostatil : ")
    try:
        tool = int(tool)
        arz = int(arz)
    except ValueError:
        print("Error : Lotfan adad sahih vared konid !")

    else:
        if tool < 1 or arz < 1:
            print("Error : Adad manfi(-) vared nakonid !")
        elif tool < arz:
            print("Error : Arz Bozorg tar az Tool ast!")
        elif tool == arz:
            print("Error : Mostatil Toolesh Bozorg tar az Arz ast!")
        else:
            rect = Rectangle(tool, arz)
            rect.masahat()
            rect.mohit()

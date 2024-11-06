class Dars:
    def __init__(self, name_dars, name_ostad, zarfiate_dars):
        self.name_dars = name_dars
        self.name_ostad = name_ostad
        self.zarfiate_dars = zarfiate_dars
        self.vojoode_dars = True


class DaneshAmooz:
    def __init__(self, name_danesh_amooz):
        self.name_danesh_amooz = name_danesh_amooz
        self.nomre = {}  #dars : nomre
        self.darse_bardashte_shode = {}  #name_daneshamooz : dars

    def bardashtane_dars(self, name_danesh_amooz, name_dars, madrese, dars):
        if name_dars not in madrese.doroos:
            print("in dars vojood nadarad!")
            return
        if len(self.darse_bardashte_shode) > dars.zarfiate_dars:
            print("zarfiat in dars por ast!")
        else:
            self.darse_bardashte_shode.update({name_danesh_amooz: name_dars})
            print(f"{name_danesh_amooz} dars {name_dars} ra bardasht!")
            dars.vojoode_dars = False
        return

    def add_nomre(self, name_danesh_amooz, name_dars, nomre, madrese):
        if name_danesh_amooz in madrese.danesh_amoozan and name_dars in madrese.doroos:
            self.nomre.update({name_dars: nomre})

    def show_nomre(self):
        return f"nomre ye {self.nomre.keys()} : {self.nomre.values()}"


class Madrese:
    def __init__(self):
        self.doroos = []
        self.danesh_amoozan = []

    def add_dars(self, name_dars):
        self.doroos.append(name_dars)

    def add_danesh_amooz(self, name_danesh_amooz):
        self.danesh_amoozan.append(name_danesh_amooz)

    def nesbate_dars(self, name_danesh_amooz, name_dars, danesh_amooz):
        if name_danesh_amooz in self.danesh_amoozan and name_dars in self.doroos:
            danesh_amooz.bardashtane_dars(name_danesh_amooz, name_dars)

        else:
            return "peyda nashod!"

    def sabte_nomre(self, name_danesh_amooz, name_dars, danesh_amooz):
        print(f"nomre ye {name_danesh_amooz} dar darse {name_dars} : {danesh_amooz.nomre.values()}")

    def show_stu_in_dars(self, name_danesh_amooz, name_dars, danesh_amooz):
        for char in danesh_amooz.darse_bardashte_shode:
            if char == name_dars:
                return f"danesh amooze {name_danesh_amooz} dar darse {char}"

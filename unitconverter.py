class unitconverter:
    def __init__(self)-> None:
        pass
    def temp(self,a,b):
        b=b.lower()
        if b=="fahrenheit":
            f=(a-32)*(5/9)
            return round(f,2)
        elif b=="celsius":
            c=(a*(9/5))+32
            return round(c,2)
        else:
            return "INVALID!!"
    def weight(self,a,b):
        b=b.lower()
        if b=="kg":
            return f"converted to lb {a*2.2}"
        elif b=="lb":
            return f"converted to kilo{a/2.2}"
    def length(self, a,b):
        b=b.lower()
        if b=="km":
            return f"converted to miles {a/1.60934}"
        elif b=="miles":
            return f"converted to km {a*1.60934}"
        else:
            return "Invalid length unit! Use 'km' or 'miles'."
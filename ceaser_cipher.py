class cipher:
    def __init__(self)-> None:
        pass
    def en_cipher(self,key:int,text:str):
        a=text
        ans=""
        for i in range(len(a)):
            if a[i]==" ":
                ans+=" "
            elif (a[i].isupper()):
                ans+=chr((ord(a[i])+key-ord("A"))%26 +ord("A"))
            elif (a[i].islower()):
                ans+=chr((ord(a[i])+key-ord("a"))%26 +ord("a"))
            else:
                ans+=a[i]
        return ans
    def de_cipher(self,key:int,text:str):
        a=text
        ans=""
        for i in range(len(a)):
            if a[i]==" ":
                ans+=" "
            elif (a[i].isupper()):
                ans+=chr((ord(a[i])-key-ord("A"))%26 +ord("A"))
            elif (a[i].islower()):
                ans+=chr((ord(a[i])-key-ord("a"))%26 +ord("a"))
            else:
                ans+=a[i]
        return ans
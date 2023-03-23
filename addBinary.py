class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        finalStr = ""

        if len(b) > len(a):
            zerotoAdd = len(b) - len(a)
            a = a[::-1]
            b = b[::-1]
            for i in range(zerotoAdd):
                a += '0'
            length_totraverse = len(b)
        else:
            zerotoAdd = len(a) - len(b)
            b = b[::-1]
            a = a[::-1]
            for i in range(zerotoAdd):
                b += '0'
            length_totraverse = len(a)
        
        
        
        i = 0
        print(a,b,length_totraverse)
        while i < length_totraverse:

            if a[i] == "0" and b[i] == "0" and carry == 0:
                carry = 0
                finalStr += "0"
            elif a[i] == "0" and b[i] == "0" and carry == 1:
                carry = 0
                finalStr += "1"                        
            elif a[i] == "0" and b[i] == "1" and carry == 0:
                carry = 0
                finalStr += "1"
            elif a[i] == "0" and b[i] == "1" and carry == 1:
                carry = 1
                finalStr += "0"
            elif a[i] == "1" and b[i] == "0" and carry == 0:
                carry = 0
                finalStr += "1"
            elif a[i] == "1" and b[i] == "0" and carry == 1:
                carry = 1
                finalStr += "0"

            elif a[i] == "1" and b[i] == "1" and carry == 0:
                carry = 1
                finalStr += "0"
            elif a[i] == "1" and b[i] == "1" and carry == 1:
                carry = 1
                finalStr += "1"
            i+=1
        if carry == 1:
            finalStr += "1"
        return finalStr[::-1]


a = Solution()
print(a.addBinary("111","111"))
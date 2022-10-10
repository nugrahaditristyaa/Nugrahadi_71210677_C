class Node:
    def _init_(self,element,n):
        self._element = element
        self._next = n

class PrefixConverter:
    def _init_(self):
        self.stackList = []
        self._top = -1                    
        self._array = []               
        self._outputArray = []
        self._operator = {'+':1, '-':1, '*':2, '/':2, '^':3} 

    def isEmpty(self):
        if self._top == -1 :    
            return True
        else:
            return False

    # method untuk menambahkan expression baru
    def push(self,expression):
        self.stackList.append(expression)

    # method untuk melihat expression paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    # method untuk menghapus expression palin atas
    def pop(self):
        if self.stackList:
            expression = self.stackList.pop(-1)
            return expression
        else:
            return "Isi Stack Kosong"

    def isCommand(self, opp):     
        return opp.isalpha()

    def cekValidExpression(self, expression):
        for i in expression:
            if i.isalpha() or i == "(":
                return False
        return True

    def infixToPrefix(self, expression):
            if " " in expression:
                expression = expression.split()

            if not self.cekValidExpression(expression):
                return "Expresi Infix yang anda masukkan tidak valid !!"
            a = []
            b = []
            
# Test Case
if __name__== '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))

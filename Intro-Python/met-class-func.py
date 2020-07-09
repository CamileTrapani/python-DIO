# Funções, Metodos e Classes

def soma(a,b):
    return a + b

def mult(a,b):
    return a*b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

print(soma(3,5))
print(mult(5,9))
print(sub(7,6))
print(div(18,9))

# Ou eu posso criar uma Classe Calculadora

class Calculadora:
    def __init__(self, num1, num2): #toda classe começa com o metodo init. esse metodo serve pra gente definir o proprio objeto
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

calculadora = Calculadora(10, 2) #instanciar a classe
print(calculadora.a)
print(calculadora.b)
print(calculadora.soma())
print(calculadora.mult())
print(calculadora.sub())
print(calculadora.div())
#Comandos do controle da TV

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 7

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal +=1
        else:
            pass
    def diminui_canal(self):
        if self.ligada == True and self.canal >1:
            self.canal -=1
        elif self.ligada == True and self.canal ==1:
            self.canal = 99
        else:
            pass


televisao = Televisao()
televisao.power()
televisao.aumenta_canal()
print('Televisão está ligada: {} \nCanal: {}'.format(televisao.ligada, televisao.canal))
televisao.power()
televisao.aumenta_canal()
print('Televisão está ligada: {} \nCanal: {}'.format(televisao.ligada, televisao.canal))
televisao.power()
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
televisao.diminui_canal()
print('Televisão está ligada: {} \nCanal: {}'.format(televisao.ligada, televisao.canal))
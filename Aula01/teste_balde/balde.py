from random import randint


class Balde:
    def __init__(self,__balde,__balde_atual):
        self.__balde = 0
        self.__balde_atual = 0


    def get_volume_balde(self):
        return self.__balde

    def set_volume_balde(self,volume_balde):
        self.volume_balde = volume_balde

    def enchendo_balde(self,volume_agua):
        self.volume_agua = volume_agua
        if self.volume_agua == 0:
            return print('Vazio')
        elif self.volume_agua == 15:
            pass

    def sorteio(self):
        self.volume = randint(10,50)
        return self.volume


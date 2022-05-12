from random import randrange


class DiceBag:

    # construtor
    def __init__(self, dices=[]):
        self._dices = dices

    def add_dice(self, dice):
        self._dices.append(dice)

    def take_dice(self, number_of_dices=1):
        choosed_dices = []
        for i in range(number_of_dices):
            choosed_dices.append(self._dices.pop(randrange(len(self._dices))))
        return choosed_dices

    def clear(self):
        self._dices = []

    def print(self):
        print(f'\nO copo de dados está com {len(self._dices)} 🎲')
        print('Dados no copo:', self._dices)
        input('\nPressione ENTER para continuar... ⏳')

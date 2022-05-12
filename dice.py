from random import randrange


class Dice:

    # Última face sorteada
    _last_roll = None

    # construtor
    def __init__(self, dice_type, faces):
        self._dice_type = dice_type
        self._faces = faces

    def __repr__(self):
        return self._dice_type

    def __str__(self):
        return self._dice_type

    def roll(self):
        """
        Sorteia uma face do dado
        """
        self._last_roll = self._faces[randrange(len(self._faces))]
        return self._last_roll

    def get_last_roll(self):
        return self._last_roll

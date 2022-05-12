class Player:

    _score = 0

    # construtor
    def __init__(self, player_name):
        self._name = player_name

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def score(self, points_to_add):
        self._score += points_to_add

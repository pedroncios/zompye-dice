# Importa a função 'randrange' do módulo 'random' para que seja
# possível obter um número randômico em um range específico
from random import randrange
# Importa o módulo time para controle de delays entre as jogadas
import time

from dice import Dice
from dice_bag import DiceBag
from player import Player

DELAY = 1
SHOW_CUP = False

# Define as faces de cada cor de dado
# C = Cérebro
# T = Tiro
# F = Fugitivo
green_dice = Dice('🟩', ('🧠', '🧠', '🧠', '💥', '👣', '👣'))
yellow_dice = Dice('🟨', ('🧠', '🧠', '💥', '💥', '👣', '👣'))
red_dice = Dice('🟥', ('🧠', '💥', '💥', '💥', '👣', '👣'))

answer = ''
while answer.lower() != 'n':
    current_player = 0

    # Define o número de jogadores
    number_of_players = input('Bem-vindo ao Zompye Dice! 🎲 Vamos jogar? Digite o número de jogadores: ')
    while not number_of_players.isnumeric() or int(number_of_players) < 2:
        number_of_players = input('Por favor digite um número de jogadores maior que 1: ')
    number_of_players = int(number_of_players)  # Converte para inteiro para facilitar o uso no restante do código

    players = []
    for i in range(number_of_players):
        # Define o nome dos jogadores
        players.append(Player(input(f'Qual o nome do jogador {i + 1}? ')))

    current_round = 1
    end_of_game = False
    cup = DiceBag()

    while not end_of_game:

        # ['🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟨', '🟨', '🟨', '🟨', '🟥', '🟥', '🟥']
        cup.clear()
        for i in range(6):
            cup.add_dice(Dice('🟩', ('🧠', '🧠', '🧠', '💥', '👣', '👣')))
        for i in range(4):
            cup.add_dice(Dice('🟨', ('🧠', '🧠', '💥', '💥', '👣', '👣')))
        for i in range(3):
            cup.add_dice(Dice('🟥', ('🧠', '💥', '💥', '💥', '👣', '👣')))

        footprints_dices = []
        round_score = 0
        shotgun_blasts = 0
        next_player_round = False

        while not next_player_round:
            print(f'\n******* Rodada {current_round} - {players[current_player].get_name()} *******')

            if SHOW_CUP:
                cup.print()

            # O turno sempre considera os dados fugitivos do turno anterior
            dices_to_roll = footprints_dices
            footprints_dices = []
            rolled_dices = []
            footprints = 0

            # Sorteia os dados
            print('\nSorteando dados... 🎲')
            time.sleep(DELAY)
            dices_to_roll.extend(cup.take_dice(3 - len(dices_to_roll)))
            print('Dados sorteados:', dices_to_roll)

            if SHOW_CUP:
                cup.print()

            # Sorteia as faces dos dados
            print('\nJogando os dados sorteados...')
            time.sleep(DELAY)
            for dice in dices_to_roll:
                rolled_dices.append(dice.roll())
            print('Faces que saíram:', rolled_dices)

            # Verifica as faces que saíram
            for i in range(3):
                if rolled_dices[i] == '🧠':  # brains
                    round_score += 1
                elif rolled_dices[i] == '💥':  # shotgun blasts
                    shotgun_blasts += 1
                elif rolled_dices[i] == '👣':  # footprints
                    footprints += 1
                    footprints_dices.append(dices_to_roll[i])

            time.sleep(0.5)
            print('\n------ Saldo acumulado da rodada ------')
            print(f'Cérebros: {"🧠" * round_score}\nTiros: {"💥" * shotgun_blasts}\nFugitivos: {"👣" * footprints}')
            if footprints > 0:
                print('Dados dos fugitivos:', footprints_dices)
            print('---------------------------------------')

            # Verifica se perdeu a rodada
            if shotgun_blasts >= 3:
                print(f'\nVocê levou {shotgun_blasts} tiros! 💥 Não marca pontos nessa rodada e é a vez do próximo jogador...')
                next_player_round = True
            else:
                answer = ''
                while not (answer.lower() == 's' or answer.lower() == 'n'):
                    answer = input('\nQuer tentar comer mais cérebros? 🧟 (s/n) ')

                if answer == 'n':
                    # Se optar por parar computa os pontos do jogador
                    players[current_player].score(round_score)
                    next_player_round = True

        # Mostra o placar atual
        print('\n------ Placar ------')
        print(f'Rodada {current_round}\n')
        for i in range(number_of_players):
            print(f'{players[i].get_name()}: {players[i].get_score()} ponto(s)')
        print('--------------------')
        input('\nPressione ENTER para continuar... ⏳')

        # Define quem é o próximo jogador
        if current_player == (number_of_players - 1):
            # Todos jogaram esta rodada, verifica se alguém ganhou
            for i in range(number_of_players):
                if players[i].get_score() >= 13:
                    print(f'\n--------------- 🎊 O JOGADOR {players[i].get_name()} VENCEU!!! 🎉 ---------------')
                    end_of_game = True
                    break

            if not end_of_game:
                # Volta para o primeiro jogador
                current_player = 0
                # Contabiliza a rodada, pois todos jogaram
                current_round += 1
        else:
            current_player += 1

    answer = ''
    while not (answer.lower() == 's' or answer.lower() == 'n'):
        answer = input('\nGostaria de jogar novamente? (s/n) ')

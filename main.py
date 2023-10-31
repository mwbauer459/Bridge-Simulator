
import game

trial = game.Game(6, 16)

trial.play_game()

# bot = ''
# top = ''
# 
#
# def make_bridge(num):
#     bridge = []
#     for i in range(num):
#         x = random.randint(0,1)
#         bridge.append(x)
#     return bridge
#
#
# def make_players(num):
#     players = []
#     for i in range(num):
#         players.append(i)
#     return players
#
#
# def take_step(bridge, row):
#     guess = random.randint(0,1)
#     if bridge[row] == guess:
#         return True
#     else:
#         return False
#
#
# def display_bridge(bridge, row, state):
#     global top
#     global bot
#
#     if state:
#         if bridge[row] == 0:
#             top += "[]"
#             bot += " O"
#             print(top)
#             print(bot)
#         else:
#             top += " O"
#             bot += "[]"
#             print(top)
#             print(bot)
#     else:
#         if bridge[row] == 0:
#             top += "[]"
#             bot += " X"
#             print(top)
#             print(bot)
#         else:
#             top += " X"
#             bot += "[]"
#             print(top)
#             print(bot)
#
#
# def play_game(rows, num_players):
#     current_player = 1
#     current_row = 1
#     bridge = make_bridge(rows)
#     right = False
#     players = make_players(num_players)
#     while True:
#         result = take_step(bridge, current_row)
#         if result:
#             current_row += 1
#             right = True
#         else:
#             print(f'{current_player} fell!')
#             current_player += 1
#             current_row += 1
#             right = False
#
#         display_bridge(bridge, current_row -1, right)
#
#         if current_player >= num_players:
#             print(f'Last player broke on row {current_row}')
#             break
#
#         if current_row >= rows:
#             print(f'First player to make it was {current_player}')
#             break
#
#     print('Game is over!')
#
#
# play_game(10, 16)

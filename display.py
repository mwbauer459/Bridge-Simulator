import PySimpleGUI as sg
import game
import threading
# import matplotlib.colors as mcolors

canvas = sg.Canvas(size=(500,500), background_color='#838B8B', expand_x=True, expand_y=True)
text_top = sg.Text("[O]", size=(18, 1), font="Helvetica 12", key='text_top')
text_bot = sg.Text("[O]", size=(18, 1), font="Helvetica 12", key='text_bot')
btn = sg.Btn(button_text="Play Game", font='Helvetica 12 bold italic', button_color='purple', border_width=2)
image_top = sg.Image(source=r'C:\Users\mbwil\PycharmProjects\Glass Bridge Simulator\pictures\pane.png', size=(40, 40), subsample=15 )
image_bot = sg.Image(source=r'C:\Users\mbwil\PycharmProjects\Glass Bridge Simulator\pictures\pane.png', size=(40, 40), subsample=15 )

# make function to create data structure to hold images/positions
# will make it easier to update later


def bridge_images(rows):
    bridge = []
    for a in range(rows):
        row = [sg.Image(source=r'C:\Users\mbwil\PycharmProjects\Glass Bridge Simulator\pictures\pane.png', size=(40, 40), subsample=15, key=f'top{a}'),
               sg.Image(source=r'C:\Users\mbwil\PycharmProjects\Glass Bridge Simulator\pictures\pane.png', size=(40, 40), subsample=15, key=f'bot{a}')]


layout = [
    [image_top],
    [image_bot],
    [text_top],
    [text_bot],
    [btn]
]

window = sg.Window("Glass Bridge Simulator", layout)

trial = game.Game(6, 16)
t1 = threading.Thread(target=trial.play_game)
t1.start()

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
    window['text_top'].update(value=trial.top)
    window['text_bot'].update(value=trial.bot)


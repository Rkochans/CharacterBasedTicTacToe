import subprocess

chart_positions = {}
up_down = "|"
end_mark = '+'


def spaces_to_the_right():
    spaces_right = ""
    for sp in range(0, 6):
        spaces_right += " "
    return spaces_right


def line_spacer():
    lp = '-'
    for ls in range(0, 5):
        lp += '-'
    return lp


def spaces(length: int = 7):
    string = ""
    for s in range(0, length):
        string += " "
    return string


def initialize_chart_positions():
    global chart_positions
    chart_positions = {}
    for r in range(1, 10):
        for c in range(1, 4):
            chart_positions[f'R{r}C{c}'] = ' '


def clear_and_refresh():
    initialize_chart_positions()
    refresh_screen()


def clear():
    subprocess.call('cls', shell=True)


def refresh_screen():
    clear()
    print(f'{spaces()}{spaces()}Column')
    print(f'{spaces()}  1{spaces()}2{spaces()[:len(spaces()) -1]}3')
    for row in range(0, 3):
        print(f'{spaces()}{spaces_to_the_right()}{up_down}{spaces_to_the_right()}{up_down}')
        for column in range(0, 3):
            if column == 0:
                print(f' Row {row + 1}   {chart_positions[f"R{row + 1}C{column + 1}"]}   {up_down}', end='')
            if column == 1:
                print(f'   {chart_positions[f"R{row + 1}C{column + 1}"]}  {up_down}', end='')
            if column == 2:
                print(f'   {chart_positions[f"R{row + 1}C{column + 1}"]}')
        print(f'{spaces()}{spaces_to_the_right()}{up_down}{spaces_to_the_right()}{up_down}')
        if row != 2:
            print(f'{spaces()}{line_spacer()}{end_mark}{line_spacer()}{end_mark}{line_spacer()}')


def is_moves_remaining():
    return True


def is_there_a_winner(player: str, move_count: int):
    print(f"in is_there_a_winner move_count={move_count} player={player}")
    global chart_positions
    if move_count == 1 or move_count == 2:
        return False
    # check across rows
    for row in range(0, 3):
        if chart_positions[f'R{row + 1}C1'] == player and \
           chart_positions[f'R{row + 1}C2'] == player and \
           chart_positions[f'R{row + 1}C3'] == player:
            return True
    # check down columns
    for column in range(0, 3):
        if chart_positions[f'R1C{column + 1}'] == player and \
           chart_positions[f'R2C{column + 1}'] == player and \
           chart_positions[f'R3C{column + 1}'] == player:
            return True
    # diagonal check 1
    if chart_positions['R1C1'] == player and \
       chart_positions['R2C2'] == player and \
       chart_positions['R3C3'] == player:
        return True
    # diagonal check 2
    if chart_positions['R3C1'] == player and \
       chart_positions['R2C2'] == player and \
       chart_positions['R1C3'] == player:
        return True

    return False


def play_game():
    global chart_positions
    initialize_chart_positions()
    refresh_screen()
    playing = True
    current_player = 'X'
    moves = 0
    while playing:
        play = input(f" Please specify the row and column to place a {current_player} ").upper()
        rc = f'R{play[0:1]}C{play[1:]}'
        if chart_positions[rc] != ' ':
            input(rc + " is already taken. Please try again. ")
            refresh_screen()
        else:
            chart_positions[rc] = current_player
            if is_there_a_winner(current_player, moves):
                response = input(f'{current_player} Wins the Game!! Press <Enter> to Continue ')
                playing = False
                # break
            elif moves >= 8:
                response = input('No winner for this game. ')
                playing = False
            else:
                refresh_screen()
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
                refresh_screen()
                moves += 1


def run():
    we_play = True
    while we_play:
        play_game()
        response = input('Do you want to play another game (Y/N)? ').upper()
        if response == 'Y' or response == 'YES':
            continue
        else:
            break


run()

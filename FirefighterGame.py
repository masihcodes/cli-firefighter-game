import time
from firefighter_class import FirefighterGame

my_firefighter = FirefighterGame()

while True:
    x = my_firefighter.print_start_hud()
    my_firefighter.clear_screen()

    if x.lower() == 'n':
        print("Game in progress...")
        time.sleep(1.5)
        break

    if x.lower() == 'l':
        save_game_file_status = my_firefighter.load_game()

        if save_game_file_status:
            print("Saved Game found and game is being loaded...")
        else:
            print("Saved Game not found and game in progress at start...")
        time.sleep(1.5)
        break

my_firefighter.clear_screen()
my_firefighter.print_my_board()

while True:

    what_the_hell_do_I_want = my_firefighter.print_hud()
    my_firefighter.clear_screen()

    if what_the_hell_do_I_want == '2':
        my_firefighter.clear_screen()
        my_firefighter.print_goodbye()
        break

    if what_the_hell_do_I_want == '1':
        my_firefighter.save_game()
        my_firefighter.clear_screen()
        my_firefighter.print_goodbye()
        break

    what_the_hell_am_I_doing = my_firefighter.move_player(
        what_the_hell_do_I_want)
    my_firefighter.print_my_board()

    print(what_the_hell_am_I_doing)

    if my_firefighter.win_check():
        my_firefighter.clear_screen()
        my_firefighter.print_victory()
        break

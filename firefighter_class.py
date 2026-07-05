import os
import json
from pathlib import Path
from game_data import get_game_data


class FirefighterGame:
    def __init__(self) -> None:
        data = get_game_data()
        self.row = data[0][0][0]
        self.col = data[0][0][1]
        self.hash_points = data[1]
        self.p_points = data[2]
        self.e_points = data[3]
        self.game_height = data[4]
        self.game_width = data[5]
        self.total_people = data[6]
        self.rescued_count = 0
        self.save_path = Path(__file__).parent / 'save_data.json'

    def board_maker(self):
        board = [['0' for j in range(self.game_width)]
                 for i in range(self.game_height)]
        for i in range(self.game_height):
            for j in range(self.game_width):
                if (i, j) == (self.row, self.col):
                    board[i][j] = '@'
                elif (i, j) in self.hash_points:
                    board[i][j] = '#'
                elif (i, j) in self.p_points:
                    board[i][j] = 'P'
                elif (i, j) in self.e_points:
                    board[i][j] = 'E'
                else:
                    board[i][j] = '.'
        return board

    def print_my_board(self):
        COLORS = {'@': '\033[32m', '#': '\033[31m',
                  'P': '\033[33m', 'E': '\033[34m', '.': '\033[37m'}
        RESET = '\033[0m'
        for row in self.board_maker():
            for cell in row:
                color = COLORS.get(cell, RESET)
                print(f"{color}{cell}{RESET}", end=' ')
            print()

    def print_hud(self):
        RED = '\033[31m'
        GREEN = '\033[32m'
        BLUE = '\033[34m'
        YELLOW = '\033[33m'
        RESET = '\033[0m'
        MAGENTA = '\033[35m'
        print('', "─" * 61)
        print(
            f"|{RED}🔥{RESET} "
            f"{GREEN}Rescued:{RESET} "
            f"{GREEN}{self.rescued_count}{RESET} / "
            f"{GREEN}{self.total_people}{RESET} "
            f"{RED}❤️{RESET} | "
            f"{GREEN}           Position:{RESET} "
            f"{GREEN}({self.row},{self.col}){RESET}             |")
        print('', "─" * 61)
        print(
            f"|{BLUE}🎮 W↑  A←  S↓  D→{RESET}   | "
            f"{YELLOW}💾 (1) Save & Quit  {RESET}  "
            f"{RED}❌ (2) Just Quit{RESET} |")
        print('', "─" * 61)
        x = input(f"{MAGENTA}Enter your choice: {RESET}").lower()
        return x

    def move_player(self, user_input):
        new_row = self.row
        new_col = self.col
        user_input = user_input.lower()

        if user_input not in ['w', 'a', 's', 'd']:
            return "invalid input try again w, a, s, d only please"
        else:
            if user_input == 'w':
                new_row = self.row - 1
                new_col = self.col
            if user_input == 's':
                new_row = self.row + 1
                new_col = self.col
            if user_input == 'a':
                new_row = self.row
                new_col = self.col - 1
            if user_input == 'd':
                new_row = self.row
                new_col = self.col + 1

            if (new_row, new_col) in self.hash_points or new_row < 0 or new_col < 0 or new_row > self.game_height - 1 or new_col > self.game_width - 1:
                return "blocked by wall or out of bounds try again"
            else:
                self.row = new_row
                self.col = new_col
                if (self.row, self.col) in self.p_points:
                    self.rescued_count += 1
                    self.p_points.remove((self.row, self.col))
                    return "successfully a person was rescued 👨"
                return "move successful"

    def win_check(self):
        win_status = False
        if (self.row, self.col) in self.e_points and self.rescued_count == self.total_people:
            win_status = True
        return win_status

    def print_victory(self):
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        RED = '\033[31m'
        RESET = '\033[0m'

        print("\n" + "🔥" * 13)
        print(f"{GREEN}🏆 ALL PEOPLE RESCUED!{RESET}".center(13))
        print(f"{YELLOW}You escaped successfully!{RESET}".center(13))
        print(
            f"{RED}👨 Rescued: {self.rescued_count} / {self.total_people}❤️{RESET}".center(13))
        print("🔥" * 13 + "\n")

    def print_goodbye(self):
        BLUE = '\033[34m'
        YELLOW = '\033[33m'
        RED = '\033[31m'
        RESET = '\033[0m'

        print("\n" + "─" * 35)
        print(f"{YELLOW}Goodbye!{RESET}".center(35))
        print(f"{BLUE}😉 Have a nice day!{RESET}".center(35))
        print(f"{RED}❤️ Stay safe!{RESET}".center(35))
        print("─" * 35 + "\n")

    def print_start_hud(self):
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        RESET = '\033[0m'
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "🔥" * 15)
        print(f"{YELLOW} Firefighter Rescue Simulator{RESET}")
        print("🔥" * 15, '\n')
        print(f"      {GREEN}N{RESET} - New Game 🆕")
        print(f"    {BLUE}L{RESET} - Load Saved Game 💾")
        print(" -"*15)
        choice = input(f"{MAGENTA}Enter your choice: {RESET}").lower()
        return choice

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def save_game(self):
        save_data = {
            "row": self.row,
            "col": self.col,
            "rescued_count": self.rescued_count,
            "p_points": [list(item) for item in self.p_points]
        }
        with open(self.save_path, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, indent=4)

    def load_game(self):
        if self.save_path.exists():
            try:
                with open(self.save_path, 'r', encoding='utf-8') as f:
                    save_data = json.load(f)

                self.row = save_data["row"]
                self.col = save_data["col"]
                self.rescued_count = save_data["rescued_count"]
                self.p_points = [tuple(item) for item in save_data["p_points"]]
                return True
            except (json.JSONDecodeError, KeyError):
                return False
        else:
            return False

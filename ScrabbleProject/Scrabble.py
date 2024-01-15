import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        

class ScrabbleGame:
    dl=[(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8),(6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14),(12, 6), (12, 8), (14, 3), (14, 11)]
    tl=[(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13),(13, 5), (13, 9)]
    dw=[(1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13),(1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1),(7, 7)]
    tw=[(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scrabble Game")
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.tiles = [
            'A']*9 + ['B']*2 + ['C']*2 + ['D']*4 + ['E']*12 + ['F']*2 + ['G']*3 + ['H']*2 + ['I']*9 + ['J']*1 + ['K']*1 + ['L']*4 + ['M']*2 + ['N']*6 + ['O']*8 + ['P']*2 + ['Q']*1 + ['R']*6 + ['S']*4 + ['T']*6 + ['U']*4 + ['V']*2 + ['W']*2 + ['X']*1 + ['Y']*2 + ['Z']*1
        random.shuffle(self.tiles)
        self.total_letters = 100
        self.current_player = None
        self.players = [Player("Player 1"), Player("Player 2")]
        self.racks = [self.draw_tiles(7), self.draw_tiles(7)]
        self.active_player=0  
        self.played_letters = []
        self.played_words = [] 
        self.remain_letters=7 
        self.letter_scores = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
            'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
            'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
        }
        self.word_list = self.load_word_list("dictionary.txt")
        self.create_widgets()
       
    def switch_player(self):
        print(self.racks[self.active_player])
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        self.active_player=1 if self.active_player==0 else 0
        print(self.racks[self.active_player])


    def create_widgets(self):
        self.label = tk.Label(self.root, text="Scrabble Game", font=("Helvetica", 16))
        self.label.grid(row=0, column=1, columnspan=16)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=1, column=1, columnspan=15, padx=10, pady=10)
        self.create_board()

        self.rack_frame = tk.Frame(self.root)
        self.rack_frame.grid(row=2, column=1, columnspan=15, padx=10, pady=10)
        self.create_rack()

        self.word_entry_frame = tk.Frame(self.root)
        self.word_entry_frame.grid(row=4, column=1, columnspan=15, padx=10, pady=10)
        self.create_word_entry()

        self.score_label = tk.Label(self.root, text=f"{self.players[0].name}'s Score: {self.players[0].score} | {self.players[1].name}'s Score: {self.players[1].score}", font=("Helvetica", 12))
        self.score_label.grid(row=1, column=18, columnspan=15)

        self.change_letters_button = tk.Button(self.root, text="Change Letters", command=self.change_letters)
        self.change_letters_button.grid(row=3, column=1, columnspan=15, pady=10)

        self.remaining_letters_label = tk.Label(self.root, text=f"Remaining Letters: {self.total_letters}", font=("Helvetica", 12))
        self.remaining_letters_label.grid(row=2, column=30, columnspan=15, pady=10)

    def create_word_entry(self):
        self.word_entry_label = tk.Label(self.word_entry_frame, text="Enter Word:")
        self.word_entry_label.grid(row=0, column=0, padx=5, pady=5)

        self.word_entry = tk.Entry(self.word_entry_frame)
        self.word_entry.grid(row=0, column=1, padx=5, pady=5)

        self.play_word_button = tk.Button(self.word_entry_frame, text="Play Word", command=self.play_word)
        self.play_word_button.grid(row=0, column=2, padx=5, pady=5)

    def create_board(self):
        for i in range(15):
            for j in range(15):
                cell = tk.Label(self.board_frame, text=self.board[i][j], width=2, height=1, relief="ridge", borderwidth=2)
                cell.grid(row=i, column=j, padx=1, pady=1, ipadx=5, ipady=5)
                cell.bind("<Button-1>", lambda event, row=i, col=j: self.cell_clicked(row, col))
                if (i, j) in self.tw:
                     cell.configure(bg="red")  #triplu cuvant
                elif (i, j) in self.dw:
                     cell.configure(bg="pink")  #dublu cuvant
                elif (i, j) in self.tl:
                     cell.configure(bg="blue")  #triplu literă
                elif (i, j) in self.dl:
                     cell.configure(bg="lightblue")  #dublu litera
                

    def create_rack(self):
        for i, letter in enumerate(self.racks[self.active_player]):
            tile = tk.Label(self.rack_frame, text=letter, width=2, height=1, relief="ridge", borderwidth=2)
            tile.grid(row=0, column=i, padx=1, pady=1, ipadx=5, ipady=5)
            tile.bind("<Button-1>", lambda event, col=i: self.rack_tile_clicked(col))
        print(self.racks[self.active_player])

    def cell_clicked(self, row, col):
        messagebox.showinfo("Cell Clicked", f"Clicked on cell at ({row}, {col})")

    def rack_tile_clicked(self, col):
        selected_tile = self.racks[self.active_player][col]
       

    def change_letters(self):
        number_of_tiles = len(self.racks[self.active_player])
        self.clear_rack()
        self.draw_new_tiles(number_of_tiles)
        self.update_rack()
        self.remaining_letters_label.config(text=f"Remaining Letters: {self.total_letters}")
        print(self.tiles)
        print(self.total_letters)
    
    def draw_new_tiles(self, num_tiles):
        self.racks[self.active_player] += self.draw_tiles(num_tiles)
    
    def draw_tiles(self, num_tiles):
        tiles = []
        for _ in range(num_tiles):
            if self.tiles:
                tiles.append(self.tiles.pop())
        return tiles

    def load_word_list(self, file_path="dictionary.txt"):
        try:
            with open(file_path, "r") as file:
                word_list = set(word.strip().upper() for word in file.readlines())
            return word_list
        except FileNotFoundError:
            messagebox.showerror("Error", "Word list file not found.")
            return set()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return set()

    def play_word(self):
        word = self.word_entry.get().upper()
        if word and self.validate_word(word) and self.is_word_valid(word):
            if self.place_word_on_board(word):
                score = self.calculate_score(word)
                self.current_player.score += score
                self.score_label.config(
                    text=f"{self.players[0].name}'s Score: {self.players[0].score} | {self.players[1].name}'s Score: {self.players[1].score}")
                messagebox.showinfo("Word Played", f"{self.current_player.name} played the word '{word}' with a score of {score}")
                self.clear_used_letters_from_rack(word)
                self.total_letters -= len(word)
                self.remaining_letters_label.config(text=f"Remaining Letters: {self.total_letters}")
                self.played_letters=[]
                self.played_words.append(word)
                print(self.played_letters, self.played_words)
                self.switch_player()
                self.update_rack()
            else:
                messagebox.showwarning("Invalid Placement", "The word cannot be placed on the board.")
        else:
            messagebox.showwarning("Invalid Word", "The word is not valid or cannot be placed on the board.")

    def validate_word(self, word):
        return word.upper() in self.word_list

    def is_word_valid(self, word):
        return all(letter in self.racks[self.active_player] + self.played_letters + self.played_words for letter in word)
    
    def clear_used_letters_from_rack(self,word):
        for letter in word:
            if letter in self.racks[self.active_player]:
                self.racks[self.active_player].remove(letter)

    def update_rack(self):
        for widget in self.rack_frame.winfo_children():
            widget.destroy()
        self.create_rack()

    def place_word_on_board(self, word):
        word_length = len(word)
        word_direction = simpledialog.askstring("Word Direction", "Enter word direction (Horizontal/Vertical):").lower()
        start_row, start_col = map(int, simpledialog.askstring("Starting Position", "Enter starting position (row, col):").split(','))

        if word_direction == "horizontal":
            if start_col + word_length > 15:
                return False
            for i, letter in enumerate(word):
                if self.board[start_row][start_col + i] != ' ' and self.board[start_row][start_col + i] != letter:
                    return False
                self.board[start_row][start_col + i] = letter
        elif word_direction == "vertical":
            if start_row + word_length > 15:
                return False
            for i, letter in enumerate(word):
                if self.board[start_row + i][start_col] != ' ' and self.board[start_row + i][start_col] != letter:
                    return False
                self.board[start_row + i][start_col] = letter
        else:
            return False
        self.update_board()
        return True

    def calculate_score(self, word):
     score = 0
     word_multiplier = 1

     for letter in word:
        if letter.isalpha():
           for i in range(15):
            for j in range(15):
                if self.board[i][j] == letter:
                    if (i, j) in self.tl:
                        score += self.letter_scores.get(letter.upper(), 0) * 3
                    elif (i, j) in self.dl:
                        score += self.letter_scores.get(letter.upper(), 0) * 2
                    else:
                        score += self.letter_scores.get(letter.upper(), 0)

                    if (i, j) in self.tw:
                        word_multiplier *= 3
                    elif (i, j) in self.dw:
                        word_multiplier *= 2

     score *= word_multiplier
     return score

    def clear_rack(self):
        self.racks[self.active_player] = []

    def update_board(self):
        for i in range(15):
            for j in range(15):
                self.board_frame.grid_slaves(row=i, column=j)[0].config(text=self.board[i][j])

    def reset_rack(self):
        self.total_letters = 100
        self.racks[self.active_player] = self.draw_tiles(7)
        self.update_rack()
        self.remaining_letters_label.config(text=f"Remaining Letters: {self.total_letters}")
    

    def run(self):
        self.current_player = self.players[0]
        self.root.mainloop()

if __name__ == "__main__":
    scrabble_game = ScrabbleGame()
    scrabble_game.run()
    
    
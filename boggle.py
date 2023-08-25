from tkinter import *
import tkinter
from boggle_board_randomizer import randomize_board
from ex11_utils import *

global current_sequence, current_path
current_sequence = []
current_path = []

def update_time():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        timer_label.config(text="Time Remaining: {}".format(remaining_time))
        root.after(1000, update_time)
    else:
        timer_label.config(text="Time's up!")
        submit_button.config(text='Cant submit')
        #New_game.config(text='New Game')
        

def select_letter(x, y):
    letter = board[x][y]
    global current_sequence, current_path
    current_sequence.append(letter)
    current_path.append([x,y])
    current_sequence_label.config(text=''.join(current_sequence))

def update_score(word):
    global score
    score+= len(word)**2
    score_label.config(text="Score:{}".format(score))
    
    

def submit_word(board, boggle_words):
    global current_sequence, current_path
    curr_word=''.join(current_sequence)
    print(current_sequence, current_path, curr_word)
    good_words=find_words(len(curr_word),board,boggle_words)
    print(good_words)
    if is_valid_path(board,current_path,boggle_words) and curr_word in good_words:
        print("Great! You found a word!")
        update_score(curr_word)
        
    else:
        print("Not a word!")
    #empty the current word
    current_sequence=[]
    current_path=[]



def read_boggle_dict():
    with open('boggle_dict.txt', 'r') as f:
        lines = f.readlines()
    words = [line.strip() for line in lines]
    return words


#initialize the tkinter instance
root = Tk()




def make_new_board():
    # generate the game board using the provided function
    global score 
    score = 0
    board = randomize_board()
    print(board)
    current_sequence_label = tkinter.Label(root, text=current_sequence, font=("Helvetica", 16))
    current_sequence_label.grid(row=len(board)+1, column=0)
    # create a button for each letter of the board
    buttons = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            b = tkinter.Button(root, text=board[i][j], command=lambda x=i, y=j: select_letter(x, y),padx = 60, pady = 15)
            b["width"] = 1
            b.grid(row=i, column=j)
            row.append(b)
        buttons.append(row)
    return board
    


board=make_new_board()
remaining_time = 182

# Create a label to display the timer
timer_label = tkinter.Label(root, text="Time Remaining: {}".format(remaining_time))
timer_label.grid(row=len(board)+3, column=2)

# Start the timer
root.after(1000, update_time())

#Keep track of the score after submitting a valid word
score = 0
score_label = tkinter.Label(root, text="Score: {}".format(score))
score_label.grid(row=len(board)+2, column=0)


#get all the words from the boggle_dict.txt file
boggle_words = read_boggle_dict()

#Make a submit button 
submit_button = tkinter.Button(root, text="Submit", command=lambda: submit_word(board, boggle_words))
submit_button.grid(row=len(board)+2, column=2)

#New game button
#New_game = tkinter.Button(root, text="New Game", command=lambda: make_new_board())
#New_game.grid(row=len(board)+2, column=3)

#showing the current word being typed
current_sequence_label = tkinter.Label(root, text=current_sequence, font=("Helvetica", 16))
current_sequence_label.grid(row=len(board)+1, column=0)



root.mainloop()




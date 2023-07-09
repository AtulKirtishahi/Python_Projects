
####################################################### importing libararys ##########################################################


from tkinter import *
from tkinter import messagebox

#################################################### making window ###################################################################

root = Tk()
root.title('Tic-Tac-Toe')
# root.iconbitmap('C:/gui/codemy.ico')

#################### Defining Variablsa ##############################################################################################

clicked = True
count = 0

################# desable Function #####################################################################################################

def disable_all_buttons():
    btn_1.config(state=DISABLED)
    btn_2.config(state=DISABLED)
    btn_3.config(state=DISABLED)
    btn_4.config(state=DISABLED)
    btn_5.config(state=DISABLED)
    btn_6.config(state=DISABLED)
    btn_7.config(state=DISABLED)
    btn_8.config(state=DISABLED)
    btn_9.config(state=DISABLED)
############################# WON Function ######################################################################################################

def check_if_won():
    global winner
    winner = False

    if btn_1['text'] == 'x' and btn_2['text'] == 'x' and btn_3['text'] == 'x':
        btn_1.config(bg='green')
        btn_2.config(bg='green')
        btn_3.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons()

    elif btn_4['text'] == 'x' and btn_5['text'] == 'x' and btn_6['text'] == 'x':
        btn_4.config(bg='green')
        btn_5.config(bg='green')
        btn_6.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons()

    elif btn_7['text'] == 'x' and btn_8['text'] == 'x' and btn_9['text'] == 'x':
        btn_7.config(bg='green')
        btn_8.config(bg='green')
        btn_9.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons()     

    elif btn_1['text'] == 'x' and btn_4['text'] == 'x' and btn_7['text'] == 'x':
        btn_1.config(bg='green')
        btn_4.config(bg='green')
        btn_7.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons() 

    elif btn_2['text'] == 'x' and btn_5['text'] == 'x' and btn_8['text'] == 'x':
        btn_2.config(bg='green')
        btn_5.config(bg='green')
        btn_8.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons() 

    elif btn_3['text'] == 'x' and btn_6['text'] == 'x' and btn_9['text'] == 'x':
        btn_3.config(bg='green')
        btn_6.config(bg='green')
        btn_9.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons() 

    elif btn_1['text'] == 'x' and btn_5['text'] == 'x' and btn_9['text'] == 'x':
        btn_1.config(bg='green')
        btn_5.config(bg='green')
        btn_9.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons() 

    elif btn_3['text'] == 'x' and btn_5['text'] == 'x' and btn_7['text'] == 'x':
        btn_3.config(bg='green')
        btn_5.config(bg='green')
        btn_7.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   X wins')  
        disable_all_buttons()

###################### check for o Wins ###############################################################################################                         

    elif btn_1['text'] == 'o' and btn_2['text'] == 'o' and btn_3['text'] == 'o':
        btn_1.config(bg='green')
        btn_2.config(bg='green')
        btn_3.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons()

    elif btn_4['text'] == 'o' and btn_5['text'] == 'o' and btn_6['text'] == 'o':
        btn_4.config(bg='green')
        btn_5.config(bg='green')
        btn_6.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons()

    elif btn_7['text'] == 'o' and btn_8['text'] == 'o' and btn_9['text'] == 'o':
        btn_7.config(bg='green')
        btn_8.config(bg='green')
        btn_9.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons()     

    elif btn_1['text'] == 'o' and btn_4['text'] == 'o' and btn_7['text'] == 'o':
        btn_1.config(bg='green')
        btn_4.config(bg='green')
        btn_7.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons() 

    elif btn_2['text'] == 'o' and btn_5['text'] == 'o' and btn_8['text'] == 'o':
        btn_2.config(bg='green')
        btn_5.config(bg='green')
        btn_8.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons() 

    elif btn_3['text'] == 'o' and btn_6['text'] == 'o' and btn_9['text'] == 'o':
        btn_3.config(bg='green')
        btn_6.config(bg='green')
        btn_9.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons() 

    elif btn_1['text'] == 'o' and btn_5['text'] == 'o' and btn_9['text'] == 'o':
        btn_1.config(bg='green')
        btn_5.config(bg='green')
        btn_9.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons() 

    elif btn_3['text'] == 'o' and btn_5['text'] == 'x' and btn_7['text'] == 'o':
        btn_3.config(bg='green')
        btn_5.config(bg='green')
        btn_7.config(bg='green')
        winner = True
        messagebox.showinfo('Tick Tac Toe','Congratulations !!   o wins')  
        disable_all_buttons()
##################### CHECK IF TIE ####################################################################################################

    if count == 9 and winner == False:
       messagebox.showinfo('Tick Tac Toe',"It's Tie!\n No One Wins!")
       disable_all_buttons()

#################### Click Button function ############################################################################################

def b_click(btn):
    global clicked, count
    
    
    if btn['text']==' ' and clicked == True:
        btn['text'] = 'x'
        clicked = False
        count +=1
        check_if_won()
    elif btn['text']==' ' and clicked == False:
        btn['text'] = 'o'
        clicked = True
        count +=1
        check_if_won()
    else:
        messagebox.showerror("Tick Tac Toe","Hey! That box has already been selected\nPick Another Box...")


######################### Reset Function #############################################################################################

def reset():
    global btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9
    global clicked, count 
    clicked = True
    count = 0

########################## Buttons ######################################################################################################

    btn_1 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_1))
    btn_2 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_2))
    btn_3 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_3))

    btn_4 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_4))
    btn_5 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_5))
    btn_6 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_6))

    btn_7 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_7))
    btn_8 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_8))
    btn_9 = Button(root, text=' ',font=('halvetica',20),height=3,width=6,bg='SystemButtonFace', command=lambda: b_click(btn_9))

    ########################## Buttons Grid #####################################################################################################

    btn_1.grid(row=0, column=0)
    btn_2.grid(row=0, column=1)
    btn_3.grid(row=0, column=2)

    btn_4.grid(row=1, column=0)
    btn_5.grid(row=1, column=1)
    btn_6.grid(row=1, column=2)

    btn_7.grid(row=2, column=0)
    btn_8.grid(row=2, column=1)
    btn_9.grid(row=2, column=2)
##################################### MENUE ##################################################################################################

my_menu = Menu(root)
root.config(menu=my_menu)

############################### Create option Menu ###########################################################################################

option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)

######################### Calling window And Functions ######################################################################################################  

reset()

root.mainloop()
from colorama import Fore		#for imparting colour in certain lines

def print_my_grid(my_list):		#for printing whole 3x3 grid
    
    print(f"{my_list[0]:^7}|{my_list[1]:^7}|{my_list[2]:^7}")
    print("-------+-------+-------")
    print(f"{my_list[3]:^7}|{my_list[4]:^7}|{my_list[5]:^7}")
    print("-------+-------+-------")
    print(f"{my_list[6]:^7}|{my_list[7]:^7}|{my_list[8]:^7}")

def general_inst():				#General instructions for how to play the game
    
    print("Welcome to Tic Tac toe game")
    print("Please enjoy the game while playing")
    print("")
    print(Fore.RED+"----------INSTRUCTIONS----------")
    print(Fore.BLUE+"1. There will be 2 players atmost to play this game")
    print("2. You can only use 'X' and 'O' to play")
    print("2. First player always starts with 'X'")
    print("3. You can choose your 1st player accordingly")

def check(mylist):				#checking the condition whether any player has won the game or not

	#Match WIN condition
    if (mylist[0]=='X' and mylist[1]=='X' and mylist[2]=='X' or mylist[3]=='X' and 
        mylist[4]=='X' and mylist[5]=='X' or mylist[6]=='X' and mylist[7]=='X' and 
        mylist[8]=='X' or mylist[0]=='X' and mylist[3]=='X' and mylist[6]=='X' or 
        mylist[1]=='X' and mylist[4]=='X' and mylist[7]=='X' or mylist[2]=='X' and 
        mylist[5]=='X' and mylist[8]=='X' or mylist[0]=='X' and mylist[4]=='X' and 
        mylist[8]=='X' or mylist[2]=='X' and mylist[4]=='X' and mylist[6]=='X' or 
        mylist[0]=='O' and mylist[1]=='O' and mylist[2]=='O' or mylist[3]=='O' and 
        mylist[4]=='O' and mylist[5]=='O' or mylist[6]=='O' and mylist[7]=='O' and 
        mylist[8]=='O' or mylist[0]=='O' and mylist[3]=='O' and mylist[6]=='O' or 
        mylist[1]=='O' and mylist[4]=='O' and mylist[7]=='O' or mylist[2]=='O' and 
        mylist[5]=='O' and mylist[8]=='O' or mylist[0]=='O' and mylist[4]=='O' and 
        mylist[8]=='O' or mylist[2]=='O' and mylist[4]=='O' and mylist[6]=='O'):
        return False

    #Match DRAW condition
    elif ((mylist[0]=='X' or mylist[0]=='O') and (mylist[1]=='X' or mylist[1]=='O') and 
          (mylist[2]=='X' or mylist[2]=='O') and (mylist[3]=='X' or mylist[3]=='O') and 
          (mylist[4]=='X' or mylist[4]=='O') and (mylist[5]=='X' or mylist[5]=='O') and 
          (mylist[6]=='X' or mylist[6]=='O') and (mylist[7]=='X' or mylist[7]=='O') and 
          (mylist[8]=='X' or mylist[8]=='O')):				
        return False

    else:
        return True


if __name__ == '__main__':			#main program starts here
	
	general_inst()
	mylist = ['','','','','','','','','']
	flag = 1
	while(check(mylist)):
	    print_my_grid(mylist)
	    choice = int(input(Fore.RED + "Enter you choice (0-8) :"))	#this line will be in RED colour

	    if flag == 1 and mylist[choice]=='':
	        mylist[choice] = 'X'
	        flag = 0
	    elif flag == 0 and mylist[choice]=='':
	        mylist[choice] = 'O'
	        flag = 1
	    else:
	        print("Wrong choice")

	print_my_grid(mylist)
	if ((mylist[0]=='X' or mylist[0]=='O') and (mylist[1]=='X' or mylist[1]=='O') and 
	    (mylist[2]=='X' or mylist[2]=='O') and (mylist[3]=='X' or mylist[3]=='O') and 
	    (mylist[4]=='X' or mylist[4]=='O') and (mylist[5]=='X' or mylist[5]=='O') and 
	    (mylist[6]=='X' or mylist[6]=='O') and (mylist[7]=='X' or mylist[7]=='O') and 
	    (mylist[8]=='X' or mylist[8]=='O')):
	    print(Fore.GREEN + "Match Draws! No one wins the title")			#this line will be in GREEN colour

	elif flag == 1:
	    print(Fore.GREEN + "Player 2 wins")				#this line will be in GREEN colour
	    
	elif flag == 0:
	    print(Fore.GREEN + "Player 1 wins")				#this line will be in GREEN colour
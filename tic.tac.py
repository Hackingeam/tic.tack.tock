#3 en raya

import random
import os
import socket
import sys
import time

reb = "\033[0;37;40m"
interw = "\033[5;37;40m"


def limpiar():
	if os.name == 'posix':
		time.sleep(1)
		os.system("clear")
	else:
		time.sleep(1)
		os.system("cls")

def drawBoard(board):
    print('\n   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
 
def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Cual quieres elegir \033[1;31mX\033[1;0m o \033[1;34mO\033[1;0m?')
        letter = input().upper()
 
    if letter == 'X':
        return ['\033[1;31mX\033[1;0m', '\033[1;34mO\033[1;0m']
    else:
        return ['\033[1;34mO\033[1;0m', '\033[1;31mX\033[1;0m']
 
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def playAgain():
	while True:
		print('\033[1;32mquieres jugar otra vez?\033[1;37m (SI/NO)\033[1;0m')
		opt = input().lower()
		if opt == "si":
			return True
		elif opt == "no":
			print("\033[1;31mAdios...\033[1;0m")
			main()
		else:
			print("Error")
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 
 
def getBoardCopy(board):
    dupeBoard = []
 
    for i in board:
        dupeBoard.append(i)
 
    return dupeBoard
 
def isSpaceFree(board, move):
    return board[move] == ' '
 
def getPlayerMove(board):
	try:
	    move = ' '
	    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
	        print('\033[1;32mcual es tu siguiente movimineto?\033[1;37m (1-9)\033[1;0m')
	        move = input("\033[1;32m[\033[1;35m#\033[1;32m]\033[1;34mopcion>\033[1;0m ")
	    return int(move)
	except KeyboardInterrupt:
			main() 



def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
 
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

 
def game():

	while True:
	   
	    theBoard = [' '] * 10
	    playerLetter, computerLetter = inputPlayerLetter()
	    turn = whoGoesFirst()
	    print('El jugador ' + turn + ' es el primero en empezar')
	    gameIsPlaying = True
	 
	    while gameIsPlaying:
	        if turn == 'player':
	            limpiar()
	            drawBoard(theBoard)
	            print("Jugador 1")
	            move = getPlayerMove(theBoard)
	            makeMove(theBoard, playerLetter, move)
	 
	            if isWinner(theBoard, playerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\nJugador 1 gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate!')
	                    break
	                else:
	                    turn = 'computer'
	 
	        else:
	            limpiar()
	            drawBoard(theBoard)
	            print("\nJugador 2")                
	            move = getPlayerMove(theBoard)
	            makeMove(theBoard, computerLetter, move)
	 
	            if isWinner(theBoard, computerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\njugador 2 gana.\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate')
	                    break
	                else:
	                    turn = 'player'
	 
	    if not playAgain():
	       	main()

def gamebot():
	 
	while True:
	    
	    theBoard = [' '] * 10
	    playerLetter, computerLetter = inputPlayerLetter()
	    turn = whoGoesFirst()
	    print('El jugador ' + turn + ' es el primero en empezar')
	    gameIsPlaying = True
	 
	    while gameIsPlaying:
	        if turn == 'player':
	           
	            limpiar()
	            print("Jugador 1")
	            drawBoard(theBoard)
	            move = getPlayerMove(theBoard)
	            makeMove(theBoard, playerLetter, move)
	 
	            if isWinner(theBoard, playerLetter):
	                drawBoard(theBoard)
	                print(interw+'\nJugador 1 gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    drawBoard(theBoard)
	                    print('El juego esta en empate!')
	                    break
	                else:
	                    turn = 'computer'
	 
	        else:
	           
	            limpiar()
	            print("\nBot")
	            drawBoard(theBoard)
	            move = getComputerMove(theBoard, computerLetter)
	            makeMove(theBoard, computerLetter, move)

	            if isWinner(theBoard, computerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\nBot gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate')
	                    break
	                else:
	                    turn = 'player'
	 
	    if not playAgain():
	        main()

def servers(HOST="127.0.0.1", PORT=5050):
	try:
		s = socket.socket()
		
		
		s.bind((HOST, PORT))
		s.listen(1)
		c = None
	except OSError:
		port = input("puerto a usar: ")
		servers(PORT=int(port))
	while True:
		
		if c is None:
			print("Para copiar selecciona ip:port y usa ctrl+shift+c")
			print("Escuchando en {}:{}".format(HOST, PORT))
			print('Esperando conexion...')
			c, addr = s.accept()
			print('Conectado!')
		else:
			while True:
			    
			    theBoard = [' '] * 10
			    playerLetter, computerLetter = ['/033[1;31mX\033;1;0m', 'O']
			    turn = 'player'
			    
			    gameIsPlaying = True
			 
			    while gameIsPlaying:
			        
			        if turn == 'player':
			            
			            limpiar()
			            print("Eres el Jugador 1")
			            print('El Jugador 1 es el primero en empezar')
			            drawBoard(theBoard)
			            print("\nJugador 1")
			            move = getPlayerMove(theBoard)
			            print(move)
			            makeMove(theBoard, playerLetter, move)
			            c.send(bytes(str(move).encode('utf-8')))
			 
			            if isWinner(theBoard, playerLetter):
			                limpiar()
			                drawBoard(theBoard)
			                print(interw+'\nJugador 1 gana\n'+reb)
			                gameIsPlaying = False
			            else:
			                if isBoardFull(theBoard):
			                    limpiar()
			                    drawBoard(theBoard)
			                    print('El juego esta en empate!')
			                    break
			                else:
			                    turn = 'computer'
			 
			        else:
			            
			            limpiar()
			            drawBoard(theBoard)
			            print("\nJugador 2")
			            print("Esperando movimineto...")
			            move = c.recv(1024).decode('utf-8')
			            print(move)
			            makeMove(theBoard, computerLetter, int(move))
			 
			            if isWinner(theBoard, computerLetter):
			                limpiar()
			                drawBoard(theBoard)
			                print(interw+'\njugador 2 gana.\n'+reb)
			                gameIsPlaying = False
			            else:
			                if isBoardFull(theBoard):
			                    limpiar()
			                    drawBoard(theBoard)
			                    print('El juego esta en empate')
			                    break
			                else:
			                    turn = 'player'
			 
			    if not playAgain():
			        main()

def clientes():
	try:
		opt1 = input("Url servidor ip:puerto : ")
		HOST, PORT = opt1.split(":")
	except ValueError:
		print("\nError ip:puerto no valido\n")
		clientes()
	try:
		s = socket.socket()
		s.connect((HOST, int(PORT)))
		print('Conectado a ', HOST)
	except ConnectionRefusedError:
		print("Error, no se puede conectar con el servidor!")
		main()


	while True:
	    
	    theBoard = [' '] * 10
	    playerLetter, computerLetter = ['X', 'O']
	    turn = 'player'
	    gameIsPlaying = True
	 
	    while gameIsPlaying:
	        if turn == 'player':
	           
	            limpiar()
	            print("Eres el Jugador 2")
	            print('El Jugador 1 es el primero en empezar')
	            drawBoard(theBoard)
	            print("\nJugador 1")
	            print("Esperando movimiento...")
	            move = s.recv(1024).decode('utf-8')
	            try:
	            	makeMove(theBoard, playerLetter, int(move))
	            except ValueError:
	            	print("Jugador desconectado..")
	            	main()
	 
	            if isWinner(theBoard, playerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\nJugador 1 gana\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate!')
	                    break
	                else:
	                    turn = 'computer'
	 
	        else:
	            
	            limpiar()
	            drawBoard(theBoard)
	            print("\nJugador 2")
	            move = getPlayerMove(theBoard)

	            makeMove(theBoard, computerLetter, int(move))
	            s.send(bytes(str(move).encode('utf-8')))
	 
	            if isWinner(theBoard, computerLetter):
	                limpiar()
	                drawBoard(theBoard)
	                print(interw+'\njugador 2 gana.\n'+reb)
	                gameIsPlaying = False
	            else:
	                if isBoardFull(theBoard):
	                    limpiar()
	                    drawBoard(theBoard)
	                    print('El juego esta en empate')
	                    break
	                else:
	                    turn = 'player'
	 
	    if not playAgain():
	        main()
def info():
	print("Para ayuda comunicate : \n 	\033[1;32m+56937760516\033[1;0m")

def main():
	__author__ = "_edi_962_a_"

	if sys.version_info[0] == 3:
		limpiar()
		print("""
							
	   |   |	\033[1;33m3 en raya\033[1;0m
	\033[1;31m X\033[1;0m | \033[1;34mO\033[1;0m | \033[1;34mO\033[1;0m
	   |   |	  \033[1;33mClasico:\033[1;0m
	-----------	    \033[1;31m[\033[1;37m1\033[1;31m]\033[1;37m 1 vs bot\033[1;0m				
	   |   |	    \033[1;31m[\033[1;37m2\033[1;31m]\033[1;37m 1 vs 1\033[1;0m
	 \033[1;34mO\033[1;0m | \033[1;31mX\033[1;0m | \033[1;31mX\033[1;0m		
	   |   |	  \033[1;33mMultijugador:\033[1;0m
	-----------	    \033[1;31m[\033[1;37m3\033[1;31m]\033[1;37m server\033[1;0m
	   |   |	    \033[1;31m[\033[1;37m4\033[1;31m]\033[1;37m cliente\033[1;0m
	 \033[1;31mX\033[1;0m | \033[1;34mO\033[1;0m | \033[1;31mX\033[1;0m
	   |   |	 \033[1;31m[\033[1;37m5\033[1;31m]\033[1;37m Info\033[1;0m
	   		 \033[1;31m[\033[1;37m6\033[1;31m]\033[1;37m Salir\033[1;0m
""")

		try:
			while True:

				op = input("\033[1;32m[\033[1;34m#\033[1;32m]\033[1;31mopcion>\033[1;0m ")
				if op == "1":
				    gamebot()
				elif op == "2":
				    game()
				elif op == "3":
				    servers()
				elif op == "4":
				    clientes()
				elif op == "5":
					info()
				elif op == "6":
					print("\033[1;31mEXIT\033[1;0m")
					limpiar()
					sys.exit()
				else:
				    print("No existe esa opcion.")


		except KeyboardInterrupt:
			print("\033[1;31mEXIT\033[1;0m")
			limpiar()
			sys.exit()
	else:
		print("\033[1;32mEste juego aun no tiene soporte python 2\033[1;0m")
		limpiar()
if __name__ == '__main__':
	main()


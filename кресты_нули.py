# -*- coding: utf-8 -*-
"""кресты нули

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vKuWCSMD1ZJ9Ox_uP7-Nd_1hKOwEM6Xn
"""

board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-'],
]
s=0
curplayer = "X"
def vision(board):
  print(' ',1,2,3)
  print(1,*board[0])
  print(2,*board[1])
  print(3,*board[2])
def move(board,sign):
  check = False
  while check == False:
    try:
      movex = int(input('Введите номар строчки :'))
      movey = int(input("Введите номер столбца :"))
      if (movex == 1 or movex == 2 or movex == 3) and (movey == 1 or movey == 2 or movey == 3):
        if board[movex-1][movey-1] == '-':
          board[movex-1][movey-1] = sign
          check = True
          return board
        else:
          print('поле занято')
          check=False
      else:
        print('ошибка в воде')
        check=False
    except:
      print('ошибка в вводе')
def turn(sign):
  if sign == 'X':
    return 'O'
  elif sign =='O':
    return 'X'
def wincheck(board):
  if board[0][0] == board[1][1] == board[2][2] != '-':
    return 'WIN'
  elif board[0][2] == board[1][1] == board[2][0] != '-':
    return 'WIN'
  for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] != '-':
        return "WIN"
      elif board[0][i] == board[1][i] == board[2][i] != '-':
        return "WIN"

while wincheck(board) != "WIN":
  if s == 9:
    print('ничья')
    break
  vision(board)
  board = move(board,curplayer)
  curplayer = turn(curplayer)
  s+=1

if 1 == 1 == 1 == 1 :
  print(2)
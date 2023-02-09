row1=['🀤','🀤','🀤']
row2=['🀤','🀤','🀤']
row3=['🀤','🀤','🀤']
board=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
row,col=input("Enter the row(0-2) and coloum(0-2) value: ").split(" ")
board[int(row)][int(col)]='x'
print(f"{row1}\n{row2}\n{row3}")

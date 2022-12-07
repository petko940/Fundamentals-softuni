row1 = input().split()
row2 = input().split()
row3 = input().split()

player1 = False
player2 = False

if row1[0] == row1[1] == row1[2] == "1" or row2[0] == row2[1] == row2[2] == "1" or row3[0] == row3[1] == row3[2] == "1" \
        or row1[0] == row2[0] == row3[0] == "1" or row1[1] == row2[1] == row3[1] == "1" or row1[2] == row2[2] == row3[
    2] == "1" \
        or row1[0] == row2[1] == row3[2] == "1" or row1[2] == row2[1] == row3[0] == "1":
    player1 = True
elif row1[0] == row1[1] == row1[2] == "2" or row2[0] == row2[1] == row2[2] == "2" or row3[0] == row3[1] == row3[
    2] == "2" \
        or row1[0] == row2[0] == row3[0] == "2" or row1[1] == row2[1] == row3[1] == "2" or row1[2] == row2[2] == row3[
    2] == "2" \
        or row1[0] == row2[1] == row3[2] == "2" or row1[2] == row2[1] == row3[0] == "2":
    player2 = True

if player1:
    print("First player won")
elif player2:
    print("Second player won")
else:
    print("Draw!")

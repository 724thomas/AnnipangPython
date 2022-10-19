from src import Board
import random

scores = 0
charRange = 6
sleepTimeMil = 100
theBoard = Board.board


def showBoard():
    global scores
    for i in range(1, len(theBoard)-1):
        print(theBoard[i][1:len(theBoard)-1])
    print()


def randomChar():
    return chr(int(random.random() * charRange + 65))


def fillAllLines():
    for i in range(len(theBoard)):
        for j in range(len(theBoard[i])):
            if theBoard[i][j] == "@":
                theBoard[i][j] = randomChar()


def charGoesDown():
    for j in range(len(theBoard)):
        for i in range(len(theBoard) - 3, 0, -1):
            for j in range(len(theBoard[i]) - 2, 0, -1):
                if theBoard[i + 1][j] == "@":
                    theBoard[i + 1][j] = theBoard[i][j]
                    theBoard[i][j] = "@"


def checkRowPang():
    global scores
    index = 0
    for j in range(1, len(theBoard) - 1):
        count = 1
        maxCount = 1
        for i in range(1, len(theBoard[j]) - 2):
            if theBoard[j][i] == theBoard[j][i + 1]:
                count += 1
                if count > maxCount:
                    maxCount = count
                    index = i
            else:
                count = 1
        if maxCount >= 3:
            for i in range(0, maxCount):
                theBoard[j][index - i + 1] = "@"
            scores += maxCount - 2
            charGoesDown()
            fillAllLines()
            showBoard()
            print(str(maxCount - 2) + "점 획득!")
            print("현재 점수는 : " + str(scores))
            return True
    return False


def checkColumnPang():
    global scores
    index = 0
    for j in range(1, len(theBoard) - 1):
        maxCount = 1
        count = 1
        for i in range(1, len(theBoard[j]) - 2):
            if theBoard[i][j] == theBoard[i + 1][j]:
                count += 1
                if count > maxCount:
                    maxCount = count
                    index = i
            else:
                count = 1
        if maxCount >= 3:
            for i in range(0, maxCount):
                theBoard[index - i + 1][j] = "@"
            scores += maxCount - 2
            charGoesDown()
            fillAllLines()
            showBoard()
            print(str(maxCount - 2) + "점 획득!")
            print("현재 점수는 : " + str(scores))
            return True
    return False


def checkAllPang():
    while checkColumnPang() | checkRowPang():
        checkColumnPang()
        checkRowPang()


# ----------------------------------------------------------------------------------------------------------------------
def swap(row, column, direction):
    temp = 0
    if direction == "UP":
        temp = theBoard[row][column]
        theBoard[row][column] = theBoard[row - 1][column]
        theBoard[row - 1][column] = temp
    if direction == "DOWN":
        temp = theBoard[row][column]
        theBoard[row][column] = theBoard[row + 1][column]
        theBoard[row + 1][column] = temp
    if direction == "LEFT":
        if column - 1 >= 0:
            temp = theBoard[row][column]
            theBoard[row][column] = theBoard[row][column - 1]
            theBoard[row][column - 1] = temp
    if direction == "RIGHT":
        if column + 1 <= 9:
            temp = theBoard[row][column]
            theBoard[row][column] = theBoard[row][column + 1]
            theBoard[row][column + 1] = temp


def checkPotentialRowPang():
    check=False
    for j in range(1, len(theBoard) - 1):
        for i in range(1, len(theBoard[j]) - 2):
            if theBoard[j][i] == theBoard[j][i + 1]:
                checkChar = theBoard[j][i]
                if theBoard[j - 1][i - 1] == checkChar:  # 왼위
                    swap(j, i - 1, "UP")
                    check=True
                elif theBoard[j + 1][i - 1] == checkChar:  # 왼아래
                    swap(j, i - 1, "DOWN")
                    check=True
                elif theBoard[j - 1][i + 2] == checkChar:  # 오위
                    swap(j, i + 2, "UP")
                    check=True
                elif theBoard[j + 1][i + 2] == checkChar:  # 오아래
                    swap(j, i + 2, "DOWN")
                    check=True
                checkAllPang()

        for i in range(1, len(theBoard[j]) - 3):
            if theBoard[j][i] == theBoard[j][i + 1]:
                checkChar = theBoard[j][i]
                if theBoard[j][i - 2] == checkChar:  # 왼왼
                    if i - 2 >= 0:
                        swap(j, i - 1, "LEFT")
                    check=True
                elif theBoard[j][i + 3] == checkChar:  # 오오
                    if i + 3 <= 9:
                        swap(j, i + 2, "RIGHT")
                    check=True
                checkAllPang()
    if check==False:
        return False


def checkPotentialColumnPang():
    check=False
    for j in range(1, len(theBoard) - 1):
        for i in range(1, len(theBoard[j]) - 2):
            if theBoard[i][j] == theBoard[i + 1][j]:
                checkChar = theBoard[i][j]
                if theBoard[i - 1][j - 1] == checkChar:  # 위왼
                    swap(i-1, j, "LEFT")
                    check=True
                elif theBoard[i - 1][j + 1] == checkChar:  # 위오
                    swap(i-1, j, "RIGHT")
                    check=True
                elif theBoard[i + 2][j - 1] == checkChar:  # 아래왼
                    swap(i + 2, j, "LEFT")
                    check=True
                elif theBoard[i + 2][j + 1] == checkChar:  # 아래오
                    swap(i + 2, j, "RIGHT")
                    check=True
                checkAllPang()

        for i in range(1, len(theBoard[j]) - 3):
            if theBoard[i][j] == theBoard[i + 1][j]:
                checkChar = theBoard[i][j]
                if theBoard[i - 2][j] == checkChar:  # 위위
                    if i - 2 >= 0:
                        swap(i - 1, j, "UP")
                        check=True
                elif theBoard[i + 3][j] == checkChar:  # 아래아래
                    if i + 3 <= 9:
                        swap(i + 2, j, "DOWN")
                        check=True
                checkAllPang()
    if check==False:
        return False


def checkAllPotentialPang():
    check=False
    for j in range(1, len(theBoard) - 1):
        for i in range(1, len(theBoard[j]) - 2):
            if theBoard[j][i] == theBoard[j][i + 1]:
                checkChar = theBoard[j][i]
                if theBoard[j - 1][i - 1] == checkChar:  # 왼위
                    swap(j, i - 1, "UP")
                    check=True
                elif theBoard[j + 1][i - 1] == checkChar:  # 왼아래
                    swap(j, i - 1, "DOWN")
                    check=True
                elif theBoard[j - 1][i + 2] == checkChar:  # 오위
                    swap(j, i + 2, "UP")
                    check=True
                elif theBoard[j + 1][i + 2] == checkChar:  # 오아래
                    swap(j, i + 2, "DOWN")
                    check=True
                checkAllPang()

        for i in range(1, len(theBoard[j]) - 3):
            if theBoard[j][i] == theBoard[j][i + 1]:
                checkChar = theBoard[j][i]
                if theBoard[j][i - 2] == checkChar:  # 왼왼
                    if i - 2 >= 0:
                        swap(j, i - 1, "LEFT")
                    check=True
                elif theBoard[j][i + 3] == checkChar:  # 오오
                    if i + 3 <= 9:
                        swap(j, i + 2, "RIGHT")
                    check=True
                checkAllPang()
    for j in range(1, len(theBoard) - 1):
        for i in range(1, len(theBoard[j]) - 2):
            if theBoard[i][j] == theBoard[i + 1][j]:
                checkChar = theBoard[i][j]
                if theBoard[i - 1][j - 1] == checkChar:  # 위왼
                    swap(i-1, j, "LEFT")
                    check=True
                elif theBoard[i - 1][j + 1] == checkChar:  # 위오
                    swap(i-1, j, "RIGHT")
                    check=True
                elif theBoard[i + 2][j - 1] == checkChar:  # 아래왼
                    swap(i + 2, j, "LEFT")
                    check=True
                elif theBoard[i + 2][j + 1] == checkChar:  # 아래오
                    swap(i + 2, j, "RIGHT")
                    check=True
                checkAllPang()

        for i in range(1, len(theBoard[j]) - 3):
            if theBoard[i][j] == theBoard[i + 1][j]:
                checkChar = theBoard[i][j]
                if theBoard[i - 2][j] == checkChar:  # 위위
                    if i - 2 >= 0:
                        swap(i - 1, j, "UP")
                        check=True
                elif theBoard[i + 3][j] == checkChar:  # 아래아래
                    if i + 3 <= 9:
                        swap(i + 2, j, "DOWN")
                        check=True
                checkAllPang()
    if check==False:
        return False


# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def check_down_neighbour(chessboard: list, x: int, y: int):
    while x <= len(chessboard) - 2:
        if chessboard[x + 1][y] != 0:
            return False
        else:
            x += 1
    else:
        return True

def check_up_neighbour(chessboard: list, x: int, y: int):
    while x >= 1:
        if chessboard[x - 1][y] != 0:
            return False
        else:
            x -= 1
    else:
        return True

def check_right_neighbour(chessboard: list, x: int, y: int):
    while y <= len(chessboard) - 2:
        if chessboard[x][y + 1] != 0:
            return False
        else:
            y += 1
    else:
        return True

def check_left_neighbour(chessboard: list, x: int, y: int):
    while y >= 1:
        if chessboard[x][y - 1] != 0:
            return False
        else:
            y -= 1
    else:
        return True

def check_right_down_diagonal(chessboard: list, x: int, y: int):
    while x <= len(chessboard) - 2 and y <= len(chessboard) - 2:
        if chessboard[x + 1][y + 1] != 0:
            return False
        else:
            x += 1
            y += 1
    return True

def check_right_up_diagonal(chessboard: list, x: int, y: int):
    while x >= 1 and y <= len(chessboard) - 2:
        if chessboard[x - 1][y + 1] != 0:
            return False
        else:
            x -= 1
            y += 1
    return True

def check_left_up_diagonal(chessboard: list, x: int, y: int):
    while x >= 1 and y >= 1:
        if chessboard[x - 1][y - 1] != 0:
            return False
        else:
            x -= 1
            y -= 1
    return True
def check_left_down_diagonal(chessboard: list, x: int, y: int):
    while x <= len(chessboard) - 2 and y >= 1:
        if chessboard[x + 1][y - 1] != 0:
            return False
        else:
            x += 1
            y -= 1
    return True

def check_neighbour(chessboard: list, x: int, y: int):
    if x in range(len(chessboard)) and y in range(len(chessboard)):
        if (check_left_neighbour(chessboard, x, y) and
            check_right_neighbour(chessboard, x, y) and
            check_up_neighbour(chessboard, x, y) and
            check_down_neighbour(chessboard, x, y) and
            check_right_down_diagonal(chessboard, x, y) and
            check_right_up_diagonal(chessboard, x, y) and
            check_left_up_diagonal(chessboard, x, y) and
            check_left_down_diagonal(chessboard, x, y)):
                return True
        else:
            return False
    else:
        return False

def queen(tup_):
    chessboard = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    for item in tup_:
        x, y = item
        if check_neighbour(chessboard, x, y):
            chessboard[x][y] = 1
        else:
            return False
    return True

# def variants():
#     chessboard = [
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0],
#     ]
#     last = tuple()
#     i = 0
#     while i < len(chessboard):
#         j = 0
#         while j < len(chessboard):
#             if chessboard[i][j] == 0 and check_neighbour(chessboard, i, j):
#                 chessboard[i][j] = 1
#                 last = (i, j)
#                 j = len(chessboard)
#             else:
#                 j += 1
#         else:
#             chessboard[last[0]][last[1]] = 0
#             i = last[0]
#             j = last[1] + 1
#         i += 1
#     print(chessboard)
# variants()
print(queen([(0, 0), (1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2)]))
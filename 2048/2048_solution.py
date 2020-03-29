#! /usr/bin/python3
import sys

def swipe_left_row(row):
    swiped_row = [] # [(numebr, collapsed)]
    for number in row:
        if number == 0:
            continue

        # if the current row is not empty
        if len(swiped_row) != 0:
            if swiped_row[-1][0] == number:
                if not swiped_row[-1][1]:
                    swiped_row[-1][0] = 2 * number
                    swiped_row[-1][1] = True
                    continue

        swiped_row.append([number, False])

    swiped_row = [tup[0] for tup in swiped_row]
    zeros_to_add = 4 - len(swiped_row)
    return swiped_row + ([0] * zeros_to_add)


def swipe_left(board):
    new_board = []
    for row in board:
        new_board.append(swipe_left_row(row))

    return new_board


def swipe_right(board):
    new_board = []
    for row in board:
        new_board.append(swipe_left_row(row[::-1])[::-1])

    return new_board


def get_flipped_board(board):
    flipped_board = []
    ziped_board = zip(board[0], board[1], board[2], board[3])
    for flippped_row in ziped_board:
        flipped_board.append(list(flippped_row))

    return flipped_board


def swipe_up(board):
    swiped_flipped_board = swipe_left(get_flipped_board(board))
    return get_flipped_board(swiped_flipped_board)


def swipe_down(board):
    swiped_flipped_board = swipe_right(get_flipped_board(board))
    return get_flipped_board(swiped_flipped_board)


def swipe(board, direction):
    return switch_directions[direction](board)


switch_directions = {
    "0": swipe_left,
    "1": swipe_up,
    "2": swipe_right,
    "3": swipe_down,
}


def main():
    board = []
    for _ in range(4):
        board.append([int(i) for i in sys.stdin.readline().strip().split(" ")])

    direction = sys.stdin.readline().strip()
    new_board = swipe(board, direction)
    for row in new_board:
        print(" ".join(str(i) for i in row))


main()

#!/usr/bin/python3
"""he N queens puzzle is the challenge of
placing N non-attacking queens on an N×N
chessboard. Write a program that solves the
N queens problem"""
import sys


def init_board(n):
    """initialize board"""
    board = []
    [board.append([]) for row in range(n)]
    [row.append(' ') for row in range(n) for row in board]
    return (board)

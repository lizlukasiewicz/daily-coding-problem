"""
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that 
all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

"""
# tour = SEQUENCE of moves or number of knights tours?

from collections import defaultdict

def add_edge(graph, vertex_a, vertex_b):
    graph[vertex_a].add(vertex_b)
    graph[vertex_b].add(vertex_a)

def build_graph(board_size):
    graph = defaultdict(set)
    for row in range(board_size):
        for col in range(board_size):
            for to_row, to_col in legal_moves_from(row, col, board_size):
                add_edge(graph, (row, col), (to_row, to_col))
    return graph

MOVE_OFFSETS = (
              (-1, -2), ( 1, -2),
    (-2, -1),                     ( 2, -1),
    (-2,  1),                     ( 2,  1),
              (-1,  2), ( 1,  2),
)
def legal_moves_from(row, col, board_size):
    for row_offset, col_offset in MOVE_OFFSETS:
        move_row, move_col = row + row_offset, col + col_offset
        if 0 <= move_row < board_size and 0 <= move_col <board_size:
            yield move_row, move_col
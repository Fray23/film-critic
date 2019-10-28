import random

import numpy as np

from net.database.write_db import write_data_to_move_meta_table, write_data_to_move_table
from net.neural_network.clear_python import NeuralNetwork
from net.database.db import data_db as db
from net.move.models import Move


def write_db():
    write_data_to_move_meta_table('datasets/movies_metadata.csv')
    write_data_to_move_table('datasets/movies_metadata.csv')

def get_data():
    pass

def normilize_data_min_max(x , xmin, xmax):
    return (x - xmin) / (xmax - xmin)

def restore_data_min_max(x , xmin, xmax):
    return x * (xmax - xmin) + xmin

def normilize_data_bool(x):
    if x:
        return 1
    return 0

def train():
    input_nodes = 2
    hidden_nodes = 800
    output_nodes = 1
    lear = 0.1

    n = NeuralNetwork(
        input_nodes=input_nodes,
        hidden_nodes=hidden_nodes,
        output_nodes=output_nodes,
        lear=lear
        )


    moves = list(db.Session.query(Move).filter(Move.budget!='0').filter(Move.revenue!='0'))
    max_b = 380000000

    for i in range(1000):
        random.shuffle(moves)
        for move in moves:
            budget = normilize_data_min_max(float(move.budget), 0, max_b)
            revenue = normilize_data_min_max(float(move.revenue), 0, max_b)
            vote_average = normilize_data_min_max(float(move.vote_average), 0, 10)

            n.train(
                [budget, revenue], vote_average
                )
    # n.load()
    n.save()

            
    for move in moves:
        budget = normilize_data_min_max(float(move.budget), 0, max_b)
        revenue = normilize_data_min_max(float(move.revenue), 0, max_b)
        print(move.vote_average, restore_data_min_max(n.q([budget, revenue]), 0, 10)[0][0])
train()

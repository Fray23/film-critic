import csv
from net.database.db import data_db as db
from net.move.models import Move
from net.neural_network.clear_python import NeuralNetwork
from net.database.write_db import write_data_to_move_table


def write_db():
    write_data_to_move_table()

def train():
    pass

import csv
from net.database.db import data_db as db
from net.move.models import Move
from net.neural_network.clear_python import NeuralNetwork
from net.database.write_db import write_data_to_move_table, write_data_to_move_meta_table
from net.database.db import data_db as db


def write_db():
    write_data_to_move_meta_table()
    write_data_to_move_table()

def train():
    input_nodes  = 1
    hidden_nodes = 1
    output_nodes = 1
    lear         = 0.3

    net = NeuralNetwork(
        input_nodes  = input_nodes,
        hidden_nodes = hidden_nodes,
        output_nodes = output_nodes,
        lear         = lear,
    )

write_db()

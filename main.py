from net.neural_network.clear_python import NeuralNetwork
from net.database.write_db import write_data_to_move_meta_table, write_data_to_move_table


def write_db():
    write_data_to_move_meta_table('datasets/movies_metadata.csv')
    write_data_to_move_table('datasets/movies_metadata.csv')

write_db()

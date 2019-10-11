import numpy
import scipy.special


class NeuralNetwork:
    def __init__(self,  input_nodes, hidden_nodes, output_nodes, lear):
        self.input_nodes  = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.lear         = lear
        self.activate     = lambda x: scipy.special.expit(x)

        self.wih = numpy.random.normal(0.0, pow(self.hidden_nodes, -0.5), (self.hidden_nodes, self.input_nodes))
        self.who = numpy.random.normal(
            0.0, pow(self.output_nodes, -0.5), (self.output_nodes, self.hidden_nodes))

    def q(self, input_list):
        inputs         = numpy.array(input_list, ndmin=2).T

        hidden_input   = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activate(hidden_input)

        final_inputs   = numpy.dot(self.who, hidden_outputs)
        final_outputs  = self.activate(final_inputs)

        return final_outputs

    def train(self, list_input, target_list):
        inputs         = numpy.array(list_input, ndmin=2).T
        targets        = numpy.array(target_list, ndmin=2).T

        hidden_input   = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activate(hidden_input)

        final_inputs   = numpy.dot(self.who, hidden_outputs)
        final_outputs  = self.activate(final_inputs)

        output_error   = targets - final_outputs
        hidden_error   = numpy.dot(self.who.T, output_error)

        self.who += self.lear * numpy.dot((output_error * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lear * numpy.dot((hidden_error * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass


input_nodes = 3
hidden_nodes = 3
output_nodes = 2
lear = 3

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, lear)
t1 = n.q([1, 1, 1, ])
# print(t1)
for i in range(10000):
    n.train([1, 1, 1, ], [0, 2])

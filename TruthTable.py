from collections import OrderedDict
import sys

class TruthTable:
    
    def __init__(self):
        self.truth_table_inputs = OrderedDict()
        self.truth_table_outputs = OrderedDict()

    def create_input_headers(self, inputs):
        for input in inputs:
            self.truth_table_inputs[input] = []

    def get_num_inputs(self):
        return len(self.truth_table_inputs.keys())

    def fill_inputs(self):
        inputs = self.truth_table_inputs.keys()

        num_inputs = self.get_num_inputs() 

        for i in range(num_inputs):
            for k in range(0, pow(2, i)):
                for j in range(0, pow(2, num_inputs)/(2*(pow(2, i)))):
                    self.truth_table_inputs[inputs[i]].append(False)
                for j in range(0, pow(2, num_inputs)/(2*(pow(2, i)))):
                    self.truth_table_inputs[inputs[i]].append(True)

    def display(self):
        inputs = self.truth_table_inputs.keys()
        for title in inputs:
            sys.stdout.write("%-6s" % title + " ")
        sys.stdout.write("\n")

        num_rows = pow(2, self.get_num_inputs())
        for row in range(0, (num_rows)):
            for value in inputs:
                sys.stdout.write('%-6s' %  str(self.truth_table_inputs[value][row]) + " ")
            sys.stdout.write("\n")

if __name__ == "__main__":
    truth_table = TruthTable()
    inputs = ['a', 'b', 'c', 'd']
    truth_table.create_input_headers(inputs)
    truth_table.fill_inputs()
    truth_table.display()
        
        

from collections import OrderedDict
import sys

class TruthTable:
    
    def __init__(self, inputs = [], outputs = [], expression = None):
        self.expression = ""
        self.inputs = OrderedDict()
        self.outputs = OrderedDict()
        self.create_col_headers(inputs, outputs)
        self.fill_inputs()

    def create_col_headers(self, inputs, outputs):
        for input in inputs:
            self.inputs[input] = []
        for output in outputs:
            self.outputs[output] = []
    
    def fill_inputs(self):
        inputs = self.inputs.keys()
        num_inputs = self.get_num_inputs() 
        for i in range(num_inputs):
            for k in range(0, pow(2, i)):
                for j in range(0, pow(2, num_inputs)/(2*(pow(2, i)))):
                    self.inputs[inputs[i]].append(False)
                for j in range(0, pow(2, num_inputs)/(2*(pow(2, i)))):
                    self.inputs[inputs[i]].append(True)

    def get_num_inputs(self):
        return len(self.inputs.keys())

    def get_longest_key_len(self):
        keys = self.inputs.keys() + self.outputs.keys()
        return len(sorted(keys, key = len)[-1])

    def display(self):
        inputs = self.inputs.keys()
        outputs = self.outputs.keys()
        longest_key_len = self.get_longest_key_len()
        for title in inputs:
            sys.stdout.write("%-*s" % (longest_key_len, title) + " ")
        for title in outputs:
            sys.stdout.write("%-*s" % (longest_key_len, title) + " ")
        sys.stdout.write("\n")
        num_rows = pow(2, self.get_num_inputs())
        for row in range(0, (num_rows)):
            for value in inputs:
                if (self.inputs[value][row] == True):
                    sys.stdout.write('%-*s' % (longest_key_len,"1") + " ")
                else:
                    sys.stdout.write('%-*s' % (longest_key_len,"0") + " ")
            sys.stdout.write("\n")

if __name__ == "__main__":
    inputs = ['a', 'b', 'c']
    outputs = ['sum']
    truth_table = TruthTable(inputs, outputs)
    truth_table.display()
        
        

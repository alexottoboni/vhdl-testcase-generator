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

        combined_inputs_outputs = (inputs + outputs)
        num_rows = pow(2, self.get_num_inputs())
        for row in range(0, (num_rows)):
            for value in combined_inputs_outputs:
            
                if value in inputs:
                    sys.stdout.write('%-*s' % (longest_key_len, str(int(self.inputs[value][row]))))
                    sys.stdout.write(" ")
               
                if value in outputs:
                    sys.stdout.write('%-*s' % (longest_key_len, str(int(self.outputs[value][row]))))
                    sys.stdout.write(" ")
            sys.stdout.write("\n")

    def fill_outputs(self):
        num_inputs = self.get_num_inputs()
        outputs = self.outputs.keys()

        for output in outputs:
            sys.stdout.write("Filling: " + output + "\n") 
            for i in range(0, pow(2, num_inputs)):
                is_valid = False
                while not is_valid:
                    new_value = raw_input()
                    if (new_value.upper() == "TRUE") or (new_value == "1") or (new_value.upper() == "T"):
                        self.outputs[output].append(True)
                        is_valid = True
                    elif (new_value.upper() == "FALSE") or (new_value == "0") or (new_value.upper() == "F"):
                        self.outputs[output].append(False)
                        is_valid = True
                    else:
                        print "Invalid input, must be: true, false, 1, or 0"
                    
            
            
    def output_vhdl(self):
        output_file = open("./output.vhd", 'w')
        output_file.write("\tstim_proc: process\n")
        output_file.write("\tbegin")
        output_file.write("\n")
        num_inputs = self.get_num_inputs()
        for i in range(0, pow(2, num_inputs)):
            output_file.write("\t\t-- Test #" + str(i + 1) + "\n")
            for input in self.inputs.keys():
                output_file.write("\t\t" + input + " <= " + "'" + str(int(self.inputs[input][i])) + "';" + "\n")
            output_file.write("\n")
            output_file.write("\t\t" + "wait for 10 ns;\n")
            output_file.write("\n")
            for output in self.outputs.keys():
                output_file.write("\t\t" + "assert " + output + " = " + "'" + str(int(self.outputs[output][i])) + "' ")
                output_file.write("report \"Failed test " + str(i + 1) + " for variable: " + output + "\"" + ";" + "\n")
            output_file.write("\n")
        output_file.write("\t\twait;\n")
        output_file.write("\tend process;\n")

    @staticmethod
    def get_user_input():
        print "Enter --end to stop"
        value_list = []
        is_valid = True
        while is_valid:
            new_input = raw_input()
            if new_input == "--end":
                is_valid = False
            else:
                value_list.append(str(new_input))
        print "\n"
        return value_list

if __name__ == "__main__":
    inputs = []
    outputs = []

    print "Enter the names of input variables:"
    inputs = TruthTable.get_user_input() 

    print "Enter the names of the output variabes:"
    outputs = TruthTable.get_user_input()

    truth_table = TruthTable(inputs, outputs)
    truth_table.fill_outputs()
    truth_table.display()
    truth_table.output_vhdl()
        
        

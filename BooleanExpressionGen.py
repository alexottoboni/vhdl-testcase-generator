class BooleanExpression:
    """
        Supports "and" and "or" and "not"
    """
    def __init__(self, expr):
        self.expression = expr
        self.variables = []

    def parse_expression(self, expression):
        return None

    def get_variables(self):
        terms = self.expression.split(" ")
        variables = set()
        
        for term in terms:
            is_and = (term.upper() == "AND")
            is_or = (term.upper() == "OR")
            is_not = (term.upper() == "NOT")
            is_open_paren = (term == "(")
            is_close_paren = (term == ")")

            if not (is_and or is_or or is_not or is_open_paren or is_close_paren):
                self.variables.append(term)

if __name__ == "__main__":

    print "Test #1:"
    expr1 = "( A and B )"
    bool1 = BooleanExpression(expr1)
    bool1.get_variables()
    print "Variables are:"
    print bool1.variables
        
        

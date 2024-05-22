class SyntaxAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def analyze(self):
        try:
            self.S()
            if self.index == len(self.input_string):
                print("Cadeia válida.")
            else:
                print("Cadeia inválida.")
        except Exception as e:
            print("Cadeia inválida.")

    def match(self, expected):
        if self.index < len(self.input_string) and self.input_string[self.index] == expected:
            self.index += 1
        else:
            raise Exception()

    def S(self):
        self.T()
        self.K()

    def K(self):
        if self.index < len(self.input_string):
            if self.input_string[self.index] == '+' or self.input_string[self.index] == '-':
                self.match(self.input_string[self.index])
                self.T()
                self.K()

    def T(self):
        self.F()
        self.Z()

    def Z(self):
        if self.index < len(self.input_string):
            if self.input_string[self.index] == '*' or self.input_string[self.index] == '/':
                self.match(self.input_string[self.index])
                self.F()
                self.Z()

    def F(self):
        if self.index < len(self.input_string):
            if self.input_string[self.index] == '(':
                self.match('(')
                self.S()
                self.match(')')
            elif self.input_string[self.index] == '-':
                self.match('-')
                self.N()
            else:
                self.N()
        else:
            raise Exception()

    def N(self):
        if self.index < len(self.input_string):
            if self.input_string[self.index].isdigit():
                self.match_digit()
                self.D()

    def D(self):
        if self.index < len(self.input_string):
            if self.input_string[self.index].isdigit():
                self.match_digit()
                self.D()

    def match_digit(self):
        if self.index < len(self.input_string) and self.input_string[self.index].isdigit():
            self.index += 1
        else:
            raise Exception()


def test_syntax_analyzer(inputs):
    for input_string in inputs:
        analyzer = SyntaxAnalyzer(input_string)
        print("Teste:", input_string)
        analyzer.analyze()
        print("\n")


correct_inputs = [
    "1+2*3",
    "(1+2)*3",
    "1+(2*3)",
    "1*2+3",
    "1+(2+3)*4",
    "1+2*3/4",
    "1+(2*3)/4",
    "1*2+(3/4)",
    "1*2*3*4",
    "1-(2+3)*4",
    "1+(2*3)*4",
    "1+(2*3/4)",
    "1+2*3+4",
    "1*2+3*4",
    "(1*2)+3*4",
    "1+2*(3*4)",
    "1*2*3/4",
    "1+2*(3+4)",
    "(1+2)*(3+4)",
    "1*2*3+4",
]

incorrect_inputs = [
    "1+2*",
    "(1+2*3",
    "1+(2*3",
    "1*2+",
    "1+(2+3*4",
    "1+2*3/",
    "1+(2*3)/",
    "1*2+3/",
    "1*2*3*",
    "1-(2+3)*",
    "1+(2*3*4",
    "1+(2*3/4",
    "1+2*3+",
    "1*2+3*",
    "(1*2)+3*",
    "1+2*(3*4",
    "1*2*3/",
    "1+2*(3+4",
    "(1+2)*(3+4",
    "1*2*3+",
    "1+"
]

test_syntax_analyzer(correct_inputs)

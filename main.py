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
            if self.input_string[self.index] == '0':
                self.match('0')
            elif self.input_string[self.index].isdigit() and self.input_string[self.index] != '0':
                self.match_digit()
                self.D()
        else:
            raise Exception()

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
    i = 1
    for input_string in inputs:
        analyzer = SyntaxAnalyzer(input_string)
        print(f"Teste {i}:", input_string)
        analyzer.analyze()
        print("\n")
        i+=1


correct_inputs = ['10+21*30',
'7-(8/4)+10',
'(15*2)-30',
'5*(6+2)/8',
'20/4*5-2',
'9+(10*3)-8',
'18-(9*2)',
'14/2+16',
'25-10+3*7',
'(12+4)*(3-1)',
'45/(5+5)-2',
'3*(20/4)',
'7+(8-2)*5',
'30/(5*2)',
'10*(4+3)',
'(9-6)*(8+3)',
'50-20*2',
'(5+5)*(10/2)',
'24/(8-2)',
'100/(25*2)'
]

incorrect_inputs = ['10+*21',
'7-(8/)+10',
'(15*)-30',
'5*(6+2/8',
'20//4*5-2',
'9+(10*3)-',
'18-(*9*2)',
'014/2+16',
'25-10+*3*7',
'(12+4)*(3-)1)',
'45/(5+)-2',
'3*(20/',
'7+(8-2)*',
'30/(5*',
'10*(4+)3',
'(9-6)*(8+3',
'50-20*',
'(5+5)*(10/',
'24/(8-2)+)',
'100/(25*2))'
]


test_syntax_analyzer(incorrect_inputs)

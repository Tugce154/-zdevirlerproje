class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape) + ['_']
        self.head = 0
        self.state = 'q0'

    def current_symbol(self):
        return self.tape[self.head]

    def move_right(self):
        self.head += 1

    def run(self):
        while True:
            symbol = self.current_symbol()

            print(f"Durum: {self.state}")
            print(f"Okunan sembol: {symbol}")
            print(f"Bant: {''.join(self.tape)}")
            print("-" * 30)

            # q0 -> ilk rakam
            if self.state == 'q0':
                if symbol.isdigit():
                    self.state = 'q1'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q1 -> ikinci rakam
            elif self.state == 'q1':
                if symbol.isdigit():
                    self.state = 'q2'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q2 -> ilk büyük harf
            elif self.state == 'q2':
                if symbol.isalpha() and symbol.isupper():
                    self.state = 'q3'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q3 -> ikinci büyük harf
            elif self.state == 'q3':
                if symbol.isalpha() and symbol.isupper():
                    self.state = 'q4'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q4 -> ilk rakam
            elif self.state == 'q4':
                if symbol.isdigit():
                    self.state = 'q5'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q5 -> ikinci rakam
            elif self.state == 'q5':
                if symbol.isdigit():
                    self.state = 'q6'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q6 -> üçüncü rakam
            elif self.state == 'q6':
                if symbol.isdigit():
                    self.state = 'q7'
                    self.move_right()
                else:
                    self.state = 'RED'

            # q7 -> kabul kontrolü
            elif self.state == 'q7':
                if symbol == '_':
                    print("SONUÇ: KABUL")
                else:
                    print("SONUÇ: RED")
                break

            elif self.state == 'RED':
                print("SONUÇ: RED")
                break


# Kullanıcıdan giriş alma
plate = input("Plaka giriniz: ")

tm = TuringMachine(plate)
tm.run()
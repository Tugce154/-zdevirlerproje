class TuringMachine:
    def __init__(self, num1, num2):

        if not (all(c in '01' for c in num1) and all(c in '01' for c in num2)):
            raise ValueError("Sadece 0 ve 1 girilebilir!")

        self.num1 = num1
        self.num2 = num2

        self.tape = list(num1 + "*" + num2 + "=")
        self.head = 0

        self.state = "q0"
        self.step = 0

    def print_step(self, read, write, move):
        print(f"\nAdım: {self.step}")
        print(f"Durum: {self.state}")
        print(f"Okunan: {read}")
        print(f"Yazılan: {write}")
        print(f"Hareket: {move}")
        print("Bant:", "".join(self.tape))
        print("      " + " " * self.head + "^")
        print("-" * 40)

    def move_head(self, direction):
        if direction == "R":
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append("_")
        elif direction == "L":
            self.head -= 1
            if self.head < 0:
                self.tape.insert(0, "_")
                self.head = 0

    def find_star(self):
        while self.state == "q0":
            self.step += 1

            read = self.tape[self.head]
            write = read
            move = "R"

            if read == "*":
                self.state = "q1"

            self.print_step(read, write, move)
            self.move_head(move)

    def find_equal(self):
        while self.state == "q1":
            self.step += 1

            read = self.tape[self.head]
            write = read
            move = "R"

            if read == "=":
                self.state = "q2"

            self.print_step(read, write, move)
            self.move_head(move)

    def binary_add(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

    def multiply(self):
        multiplicand = self.num1
        multiplier = self.num2[::-1]

        result = "0"
        shift = 0

        while self.state == "q2":
            for bit in multiplier:
                self.step += 1

                read = bit
                move = "R"

                if bit == "1":
                    temp = multiplicand + "0" * shift
                    write = "ADD"
                    result = self.binary_add(result, temp)
                else:
                    write = "SKIP"

                self.print_step(read, write, move)
                shift += 1

            self.result = result
            self.state = "q3"

    def write_result(self):
        while self.tape[self.head] != "=":
            self.head -= 1

        self.head += 1

        while self.state == "q3":
            for bit in self.result:
                self.step += 1

                read = "_"
                write = bit
                move = "R"

                self.tape.insert(self.head, bit)

                self.print_step(read, write, move)
                self.move_head(move)

            self.state = "q_accept"

    def run(self):
        self.find_star()
        self.find_equal()
        self.multiply()
        self.write_result()

        print("\nİŞLEM BİTTİ")
        print("Binary:", self.result)
        print("Decimal:", int(self.result, 2))

print("Turing Machine Binary Çarpma")

n1 = input("1. sayı: ")
n2 = input("2. sayı: ")

tm = TuringMachine(n1, n2)
tm.run()
import math

def GPTcalculator(inpt: str) -> str:
    # Place your actual calculation logic here, leveraging Python's capabilities
    # This should handle all operations, including +, -, *, /, ^, factorials, etc.
    # Return the result as a string
    pass  # Placeholder

def test():
    LevelBasic = [
        [("6 + 3", str(9)), ("32 + 54", str(86)), ("43 + 23 + 11", str(77))],  # addition
        [("6 - 3", str(3)), ("18 - 8", str(10)), ("1 - 20", str(-19))],      # subtraction
        [("5 * 11", str(55)), ("102 * 10", str(1020)), ("16 * 32", str(512))],  # multiplication
        [("15 / 5", str(3)), ("9 / 1", str(9)), ("121 / 11", str(11))]         # division
    ]

    LevelMedium = [
        [("(2 + 6) * 2", str(16)), ("5 * (6 / 2) - 5", str(10)), ("(23 - 24) / 10", str(-0.1))], # brackets
        [("6**2 - 2", str(34)), ("7**4 / 5 + 6", str(486.2)), ("35**4 - 34**4", str(164289))],   # powers
        [("9! / 5", str(72576)), ("6! - 5! * 3!", str(0)), ("7! / 4! * 5 - 24", str(1024))]  # factorials
    ]

    LevelHard = [
        [("log(100)(10)", str(2)), ("log(1000)(10)", str(3)), ("log(10)(10)", str(1))],  # logs
        [("abs(-42 / 2)", str(21)), ("abs(64-2143)", str(2079)), ("abs(-64 * 3 + 423)", str(231))],  # absolutes
        [("sqr(2)(64)", str(8)), ("sqr(3)((44 * 10 + 1) * 21)", str(21)), ("sqr(2)(32)*43", str())]  # roots
    ]

    for level, level_name in zip([LevelBasic, LevelMedium, LevelHard], ['Basic', 'Medium', 'Hard']):
        print(f"level {level_name}: ")
        completed = 0
        total = 0

        for operation in level:
            for i in operation:
                temp = GPTcalculator(i[0])
                if temp == i[1]:
                    completed += 1
                else:
                    print(f"on {i[0]} got: {str(temp)} expected: {str(i[1])}")
                total += 1

        print(f"passed: {str(completed)}/{str(total)}\n")

if __name__ == "__main__":
    test()

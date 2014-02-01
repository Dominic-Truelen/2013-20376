#Grid is 5x5
import random
class menu():
    def __init__(self):
        self.game = game()

    def menu(self):
        while True:
            choice = raw_input("New Game -- N, Quit -- Q")
            choice = choice.lower()
            if choice == 'n':
                self.game.run()
            elif choice == 'q':
                print"Thank you for playing"
                break
            else:
                print"Invalid Input"

class game():
    def __init__(self):
        self.creator = creator()
        self.printer = printer()
        self.validator = validator()
        self.swapper = swapper()
        self.checker = checker()
        self.scorer = scorer()
        self.floater = floater()
        self.dropper = dropper()
        self.grid = [[0 for x in range(5)] for x in range (5)]
        self.score = 0
        self.goal = 0

    def run(self):
        print"Enter 1 to swap with Up, 2 for Down, 3 for Left,and 4 for Right.\nEnter 0 for both row and column to quit.\n"
        choice = raw_input("How many choices do you want?")
        if choice.isdigit() == True:
            choice = int(choice)
            if 0 < choice < 25:
                self.creator.create(self.grid, choice)
                self.validator.validate(self.grid, choice)
                while True:
                    self.goal = raw_input("Input goal score")
                    if self.goal.isdigit() == False or int(self.goal) <= 0:
                        print"Invalid input"
                    else:
                        break
                self.goal = int(self.goal)
                while True:
                    self.printer.printing(self.grid)
                    if self.score >= self.goal:
                        print"You win"
                        break
                    print "Your score is " + str(self.score)
                    while True:
                        row = raw_input("Enter row: ")
                        if row.isdigit() == False or 5 < int(row) < 0:
                            print"Invalid input"
                        else:
                            break
                    row = int(row)
                    while True:
                        column = raw_input("Enter column: ")
                        if column.isdigit() == False or 5 < int(column) < 0:
                            print"Invalid input"
                        else:
                            break
                    column = int(column)
                    if row == column == 0:
                        print"Game over"
                        break
                    elif row == 0 or column == 0:
                        print"Invalid input"
                    else:
                        direction = raw_input("Enter number (1 - Up, 2 - Down, 3 - Left, 4 - Right)")
                        if direction.isdigit() == True:
                            direction = int(direction)
                            row -= 1
                            column -= 1
                            if (row == 0 and direction == 1) or (row == 5 and direction == 2) or (column == 0 and direction == 3) or (column == 5 and direction == 4):
                                print"Invalid input"
                                row += 1
                                column += 1
                            else:
                                self.grid = self.swapper.swapping(row, column, direction, self.grid)
                                self.grid = self.checker.checking(self.grid)
                                self.score += self.scorer.scoring(self.grid)
                                if self.scorer.scoring(self.grid) == 0:
                                    self.swapper.swapping(self, row, column, direction, self.grid)
                                else:
                                    self.grid = self.floater.floating(self.grid)
                                    self.grid = self.dropper.dropping(self.grid, choice)
                                    for x in range(200):
                                        self.grid = self.checker.checking(self.grid)
                                        self.grid = self.floater.floating(self.grid)
                                        self.score += self.scorer.scoring(self.grid)
                                        self.grid = self.dropper.dropping(self.grid, choice)
                        else:
                            print"Invalid input"
                else:
                    print"Invalid input"
            else:
                print"Invalid input"
        else:
            print"Invalid input"

class printer():
    def printing(self, grid):
        for y in range(6):
            for x in range(6):
                if y < 5:
                    if x < 5:
                        print str(grid[x][y]) + '\t',
                    elif x == 5:
                        print "(" + str(y + 1) + ")",
                elif y == 5:
                    if x != 5:
                        print "(" + str(x + 1) + ")\t",
            print '\n\n',

class creator():
    def __init__(self):
        self.random_gen = random_gen()
    def create(self, grid, choice):
        for x in range(5):
                for y in range(5):
                    grid[x][y] = self.random_gen.gen(choice)
        return grid

class validator():
    def __init__(self):
        self.random_gen = random_gen()
    def validate(self, grid, choice):
        for k in range(200):
            for x in range(5):
                for y in range(5):
                    if x < 3 and grid[x][y] == grid[x + 1][y] == grid[x + 2][y]:
                        while grid[x][y] == grid[x + 1][y] == grid[x + 2][y]:
                            grid[x][y] = self.random_gen.gen(choice)
                            grid[x + 1][y] = self.random_gen.gen(choice)
                            grid[x + 2][y] = self.random_gen.gen(choice)
            for x in range(5):
                for y in range(5):
                    if y < 3 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2]:
                        while grid[x][y] == grid[x][y + 1] == grid[x][y + 2]:
                            grid[x][y] = self.random_gen.gen(choice)
                            grid[x][y + 1] = self.random_gen.gen(choice)
                            grid[x][y + 2] = self.random_gen.gen(choice)
        return grid

class swapper():
    def swapping(self, row, column, direction, grid):
        if direction == 1:
            grid[column][row], grid[column][row - 1] = grid[column][row - 1], grid[column][row]
        elif direction == 2:
            grid[column][row], grid[column][row + 1] = grid[column][row + 1], grid[column][row]
        elif direction == 3:
            grid[column][row - 1], grid[column][row] = grid[column - 1][row], grid[column][row]
        elif direction == 4:
            grid[column][row + 1], grid[column][row] = grid[column + 1][row], grid[column][row]
        return grid

class checker():
    def checking(self, grid):
        for k in range(200):
            for x in range(5):
                for y in range(5):
                    if x == y == 0 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2] == grid[x][y + 3] == grid[x][y + 4] == grid[x + 1][y] == grid[x + 2][y] == grid[x + 3][y] == grid[x + 4][y]:
                        grid[x][y] = 0
                        grid[x][y + 1] = 0
                        grid[x][y + 2] = 0
                        grid[x][y + 3] = 0
                        grid[x][y + 4] = 0
                        grid[x + 1][y] = 0
                        grid[x + 2][y] = 0
                        grid[x + 3][y] = 0
                        grid[x + 4][y] = 0
                    elif x <= y <= 1 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2] == grid[x][y + 3] == grid[x + 1][y] == grid[x + 2][y] == grid[x + 3][y]:
                        grid[x][y] = 0
                        grid[x][y + 1] = 0
                        grid[x][y + 2] = 0
                        grid[x][y + 3] = 0
                        grid[x + 1][y] = 0
                        grid[x + 2][y] = 0
                        grid[x + 3][y] = 0
                    elif x <= y <= 2 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2] == grid[x + 1][y] == grid[x + 2][y]:
                        grid[x][y] = 0
                        grid[x][y + 1] = 0
                        grid[x][y + 2] = 0
                        grid[x + 1][y] = 0
                        grid[x + 2][y] = 0
            for x in range(5):
                for y in range(5):
                    if y == 0 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2] == grid[x][y + 3] == grid[x][y + 4]:
                        grid[x][y] = 0
                        grid[x][y + 1] = 0
                        grid[x][y + 2] = 0
                        grid[x][y + 3] = 0
                        grid[x][y + 4] = 0
                    elif y <= 1 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2] == grid[x][y + 3]:
                        grid[x][y] = 0
                        grid[x][y + 1] = 0
                        grid[x][y + 2] = 0
                        grid[x][y + 3] = 0
                    elif y <= 2 and grid[x][y] == grid[x][y + 1] == grid[x][y + 2]:
                        grid[x][y] = 0
                        grid[x][y + 1] = 0
                        grid[x][y + 2] = 0
            for x in range(5):
                for y in range(5):
                    if x == 0 and grid[x][y] == grid[x + 1][y] == grid[x + 2][y] == grid[x + 3][y] == grid[x + 4][y]:
                        grid[x][y] = 0
                        grid[x + 1][y] = 0
                        grid[x + 2][y] = 0
                        grid[x + 3][y] = 0
                        grid[x + 4][y] = 0
                    elif x <= 1 and grid[x][y] == grid[x + 1][y] == grid[x + 2][y] == grid[x + 3][y]:
                        grid[x][y] = 0
                        grid[x + 1][y] = 0
                        grid[x + 2][y] = 0
                        grid[x + 3][y] = 0
                    elif x <= 2 and grid[x][y] == grid[x + 1][y] == grid[x + 2][y]:
                        grid[x][y] = 0
                        grid[x + 1][y] = 0
                        grid[x + 2][y] = 0
        return grid

class scorer():
    def scoring(self, grid):
        score = 0
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 0:
                    score += 1
        return score

class floater():
    def floating(self, grid):
        for x in range(200):
            for i in range(5):
                for j in range(5):
                    if j != 0 and grid[i][j] == 0:
                        temp = grid[i][j]
                        grid[i][j] = grid[i][j - 1]
                        grid[i][j - 1] = temp
        return grid

class dropper():
    def __init__(self):
        self.random_gen = random_gen()
    def dropping(self, grid, choice):
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 0:
                    grid[i][j] = self.random_gen.gen(choice)
        return grid

class random_gen():
    def gen(self, choice):
        return random.randint(1, choice)

c = menu()
c.menu()
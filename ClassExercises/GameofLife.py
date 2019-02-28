class cell(object):

    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.set_state(state)

    def get_state(self):
        return self.state

    def set_state(self,state):
        self.state = state
        if state != 1 and state != 0:
            die("Idiot")

# test_cell = cell(1,0,1)
#
# state = test_cell.get_state()
# print(f"{state}")
#
# test_cell.set_state(1)
#
# state = test_cell.get_state()
# print(f"{state}")

class grid(object):

    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range (0,rows):
            cols_list =[]
            for j in range (0, cols):
                cols_list.append(cell(i,j,0))
            self.grid.append(cols_list)

    def print(self):
        for i in range (0,self.rows):
            for j in range (0, self.cols):
                state = self.grid[i][j].get_state()
                if state == 0:
                    print("-", end='')
                else:
                    print("X", end='')
            print("\n", end='')

    def next_move(self):
        pass

    def set_cell(self,x,y,state):
        self.grid[x][y].set_state(state)

    def play(self,ticks):
        pass

gofl = grid(30, 80)
gofl.set_cell(14, 40, 1)
gofl.set_cell(15, 42, 1)
gofl.set_cell(16, 39, 1)
gofl.set_cell(16, 40, 1)
gofl.set_cell(16, 43, 1)
gofl.set_cell(16, 44, 1)
gofl.set_cell(16, 45, 1)
gofl.print()

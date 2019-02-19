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


test_cell = cell(1,0,1)

state = test_cell.get_state()
print(f"{state}")

test_cell.set_state(1)

state = test_cell.get_state()
print(f"{state}")

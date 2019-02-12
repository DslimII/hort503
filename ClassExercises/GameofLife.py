class cell(object):

    def __init__(self,x,y,state):
        self.x = x_coordinate
        self.y = y_coordinate
        self.set_state(state)

    def get_state(self):
        return self.state

    def set_state(self,state):
        self.state = state
        if state != 1 and state != 0:
            die("Idiot")

def test_cell():

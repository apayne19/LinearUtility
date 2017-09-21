from brickpy import utility as u

test = u.Linear_Utility(3, 3, 2, 50)
test.continuity()
test.concavity()
test.plot()
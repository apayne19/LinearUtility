import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from colorama import *
print("hi")
class Linear_Utility(object):
    print(Fore.BLUE + "Welcome to the Linear Utility Model")  # changes color of display text
    print("created by Alex Payne")
    print("-"*40)

    def __init__(self, num_b, num_m, num_c, items):
        b_i = []
        m_i = []
        c_i = []
        self.num_b = num_b  # number of b intercepts
        self.num_m = num_m  # number of m slopes
        self.num_c = num_c  # number of c1,c2, etc
        self.items = items  # number of items (x values)
        self.b_i = b_i
        self.m_i = m_i
        self.c_i = c_i
        restart_b = True  # error trap (alarm off)
        restart_m = True  # error trap (alarm off)
        restart_c = True  # error trap (alarm off)
        while restart_b:
            restart_b = False  # will restart when = True (alarm set)
            for intercept in range(self.num_b):  # asks for each intercept value
                try:
                    b = float(input("Enter Intercept " + str(intercept + 1) + ": "))
                    b_i.append(b)
                except ValueError:  # value error when letter is entered
                    print("Intercepts must be rational numbers")
                    print("Starting Over...")
                    restart_b = True  # sets off error alarm
                    print(b_i)  # print intercepts before reset
                    b_i.clear()  # clears intercepts dictionary before exiting loop
                    print(b_i)  # proves reset dictionary
                    break  # breaks loop and enters again until values are correct
        while restart_m:  # same thing for slope values
            restart_m = False  # restart when = True (alarm set)
            for slope in range(self.num_m):  # asks for each slope value
                try:
                    m = float(input("Enter Slope " + str(slope + 1) + ": "))
                    m_i.append(m)
                except ValueError:
                    print("Slopes must be rational numbers")
                    print("Starting Over...")
                    restart_m = True  # sets off error alarm
                    print(m_i)
                    m_i.clear()  # clears slope dictionary before exiting loop
                    print(m_i)
                    break  # breaks loop and enters again until values are correct
        while restart_c:  # same thing for C values, but two traps set
            restart_c = False  # restart when = True (alarm set)
            for constraint in range(self.num_c):  # asks for each c1, c2, etc.
                try:
                    c = float(input("Enter C" + str(constraint + 1) + ": "))
                    c_i.append(c)
                except ValueError:
                    print("Constraints must be rational numbers")
                    print("Starting Over...")
                    restart_c = True  # triggers 1st alarm for letters entered etc
                    print(c_i)
                    c_i.clear()  # clears c values dictionaries before exiting loop
                    print(c_i)
                    break  # breaks loop and continues entering until all values = numbers
            if restart_c == True:  # if 1st alarm triggered
                pass  # skips the 2nd error check until values = numbers
            else:
                while c_i[1] < c_i[0]:  #
                    print("C2 must be larger than C1")
                    print("Starting Over...")
                    restart_c = True  # triggers 2nd alarm for C1 value > C2
                    print(c_i)
                    c_i.clear()  # clears c values dictionary before exiting loop
                    print(c_i)
                    break  # breaks until C1 < C2, only continues while-loop not for-loop
        print("\n")
        print(Fore.GREEN + "Our function is")  # changes color of display text
        print("-"*20)  # so user sees function
        print("U(x) =")
        print(str(b_i[0]) + "+" + str(m_i[0]) + "x")
        print(str(b_i[1]) + "+" + str(m_i[1]) + "x")
        print(str(b_i[2]) + "+" + str(m_i[2]) + "x")
        print("\n")

    def piecew(self, x):  # obtains utility values
        # TODO make user input lambda functions and params
        params = [(x > 0) & (x < float(self.c_i[0])),
                 (x >= float(self.c_i[0])) & (x < float(self.c_i[1])),
                 x >= float(self.c_i[1])]  # creates conditions of piecewise function
        funcs = [lambda x: float(self.b_i[0]) + float(self.m_i[0]) * x,
                 lambda x: float(self.b_i[1]) + float(self.m_i[1]) * x,
                 lambda x: float(self.b_i[2]) + float(self.m_i[2]) * x]  # creates piecewise functions
        return np.piecewise(x, params, funcs)  # numpy extension that returns U(x)

    def continuity(self):
        # TODO make y*_c* iterable through lambda functions
        print(Fore.MAGENTA + "Let's check the continuity")  # changes color of display text
        print("-"*40)
        y1_c1 = float(self.b_i[0]) + float(self.m_i[0]) * float(self.c_i[0])  # checks 1st function values at c1
        y2_c1 = float(self.b_i[1]) + float(self.m_i[1]) * float(self.c_i[0])  # checks 2nd function values at c1
        y2_c2 = float(self.b_i[1]) + float(self.m_i[1]) * float(self.c_i[1])  # checks 2nd function values at c2
        y3_c2 = float(self.b_i[2]) + float(self.m_i[2]) * float(self.c_i[1])  # checks 3rd function values at c2
        if y1_c1 != y2_c1:  # if 1st function at x=c1 != 2nd function at x=c1
            print("U(x) is not continuous at X = " + str(self.c_i[0]))
        else:
            print("U(x) is is continuous at X = " + str(self.c_i[0]))
        if y2_c2 != y3_c2:  # if 2nd function at x=c2 != 3rd function at x=c2
            print("U(x) is not continuous at X = " + str(self.c_i[1]))
        else:
            print("U(x) is is continuous at X = " + str(self.c_i[1]))
        print("Check the graph")
        with plt.style.context('fivethirtyeight'):  # plotting points of function 1-3 with x values of c1 and c2
            x1 = float(self.c_i[0])
            y1 = y1_c1
            plt.plot(x1,
                     y1,
                     label='y1(' + str(self.c_i[0]) + ')' + ' =' + str(y1),
                     marker="o")
            x2 = float(self.c_i[0])
            y2 = y2_c1
            plt.plot(x2,
                     y2,
                     label='y2(' + str(self.c_i[0]) + ')' + ' =' + str(y2),
                     marker="s")
            x3 = float(self.c_i[1])
            y3 = y2_c2
            plt.plot(x3,
                     y3,
                     label='y2(' + str(self.c_i[1]) + ')' + ' =' + str(y3),
                     marker="s")
            x4 = float(self.c_i[1])
            y4 = y3_c2
            plt.plot(x4,
                     y4,
                     label='y3(' + str(self.c_i[1]) + ')' + ' =' + str(y4),
                     marker="D")
            plt.grid(True)
            plt.legend(loc='center')
            plt.xlabel("Items")
            plt.ylabel("Utility")
            plt.show()

    def concavity(self):  # using sympy module to check concavity of functions
        # TODO make 2nd derivatives iterable through lambda functions
        print("\n")
        x = symbols('x')  # makes x a variable for differentiation  # diff() takes derivative
        dd_U1 = diff(diff(float(self.b_i[0]) + float(self.m_i[0]) * x))  # takes 1st function derivative
        dd_U2 = diff(diff(float(self.b_i[1]) + float(self.m_i[1]) * x))  # takes 2nd function derivative
        dd_U3 = diff(diff(float(self.b_i[2]) + float(self.m_i[2]) * x))  # takes 3rd function derivative
        print("Let's check the concavity by taking the 2nd derivative")
        print("-"*40)
        print("The 2nd derivative of...")
        print("piece 1 is: " + str(dd_U1))  # shows 2nd derivatives to user
        print("piece 2 is: " + str(dd_U2))
        print("piece 3 is: " + str(dd_U3))
        if dd_U1 + dd_U2 + dd_U3 == 0:  # checks to make sure all 2nd derivatives = 0
            print("\n")                 # when 2nd derivatives = 0 means linear function
            print("The piecewise utility function U(x) is linear!")  # also means no concavity
        else:
            print("The function U(x) is not linear!")
        print("Check the graph of U(x)")



    def plot(self):  # plots our function U(x)
        end = self.items
        with plt.style.context('fivethirtyeight'):
            x_1 = np.linspace(0, float(self.c_i[0]))  # 1st parameter 0<x<c1
            x_2 = np.linspace(float(self.c_i[0]), float(self.c_i[1]))  # 2nd parameter c1<=x<c2
            x_3 = np.linspace(float(self.c_i[1]), end)  # parameter x>=c2
            plt.plot(x_1,
                     self.piecew(x_1),  # plots 1st piece of U(x)
                     label=str(self.b_i[0]) + '+' + str(self.m_i[0]) + 'x')
            plt.plot(x_2,
                     self.piecew(x_2),  # plots 2nd piece of U(x)
                     label=str(self.b_i[1]) + '+' + str(self.m_i[1]) + 'x')
            plt.plot(x_3,
                     self.piecew(x_3),  # plots 3rd piece of U(x)
                     label=str(self.b_i[2]) + '+' + str(self.m_i[2]) + 'x')
            plt.grid(True)  # creates a grid in the graph
            plt.legend(loc='upper left')  # puts legend in upper left of graph
            plt.xlabel("Items")  # x-axis = items
            plt.ylabel("Utility")  # y-axis = U(x) = utility
            plt.show()

# number of b intercepts, number of m slopes, number of c constraints, number of items
# model currently only set up to only take 3 intercepts, 3 slopes, and 2 constraints
# user can enter as many items as desired
test = Linear_Utility(3, 3, 2, 50)
test.continuity()  # checks continuity
test.concavity()  # checks concavity
test.plot()  # plots U(x)

# ENJOY!

import numpy as np 
import random
import math

# call move class in main by following step:
# AnyNameYouLike = move()
# and inside your for loop:
#   turnangle(omega) = AnyNameYouLike(frount_sensor_data, right_sensor_data, left_sensor_data)
#   and the rest is your part
class move():
    def __init__(self):
        self.pose = 0
        self.rigth = -1
        self.left = -1
        self.branch_one = 20
        self.count = 0
        self.branch_two = np.array([30,45])
        self.branch_three = np.array([-5,5])
    def decision_tree(self,frount,right,left):
        if self.right != -1
            dr = right - self.rigth
        if self.left != -1
            dl = left - self.left
        self.rigth = right
        self.left = left
        lr = left - right

        #root1
        if self.pose == 0:
            if frount <= self.branch_two[0]:
                if lr < self.branch_three[0]:
                    y = 4.5 / (1 + math.exp(-0.5 * lr)
                elif lr > self.branch_three[1]:
                    y = 4.5 / (1 + math.exp(-0.5 * lr)
                else:
                    y = random.random() * 2 - 1
            elif frount <= self.branch_two[1]:
                if lr < self.branch_three[0]:
                    y = 1 / (1 + math.exp(-0.5 * lr)
                elif lr > self.branch_three[1]:
                    y = 1 / (1 + math.exp(-0.5 * lr)
                else:
                    y = random.random() * 0.6 - 0.3
            else:
                y = 0
        elif self.pose == -1:
            if dr > self.branch_one:
                self.pose = 0
        else:
            if dl > self.branch_one:
                self.pose = 0
        
        if y > 2 or y < -2:
            if self.pose == 0:
                self.count += 1
        
        if self.count >3:
            if y > 2:
                self.pose = -1
            elif y < 2:
                self.pose = 1
            self.count = 0
        return y
        '''
        #root2
        if frount < self.branch_two[0]:
            self.output_one = 0
        elif frount < self.branch_two[1]:
            self.output_one = 1
        elif frount < self.branch_two[2]:
            self.output_one = 2
        elif frount < self.branch_two[3]:
            self.output_one = 3
        else:
            self.output_one = 4

        #root3
        if lr < self.branch_three[0]:
            y = -4
        elif lr < self.branch_three[1]:
            y = -3
        elif lr < self.branch_three[2]:
            y = -1
        elif lr < self.branch_three[3]:
            y = 1
        elif lr < self.branch_three[4]:
            y = 3
        else:
            y = 4
        '''


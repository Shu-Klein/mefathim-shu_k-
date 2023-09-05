import random
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, dimantions, steps):
        self.dimantions = dimantions

        self.steps = steps

        self.coordinates = [[0 for step in range(self.steps)] for dim in range(self.dimantions)]

    def r_walk(self):
        for step in range(self.steps - 1):
            random_dimantion = random.randint(0, self.dimantions - 1)
            for dim in range(self.dimantions):
                if dim == random_dimantion:
                    self.move(dim, step)
                else:
                    self.stey(dim, step)

    def move(self, dim, step):
        direction = 1
        random_direction = random.random()
        if random_direction < 0.5:
            direction = -1
        self.coordinates[dim][step + 1] = self.coordinates[dim][step] + direction



    def stay(self, dim, step):
        self.coordinates[dim][step] = self.coordinates[dim][step - 1]

    def display(self):
        if self.dimantions == 1:
            plt.plot([step for step in range(self.steps)], self.coordinates[0])
            plt.show()
        elif self.dimantions == 2:
            pass
        elif self.dimantions == 3:
            pass
        else:
            pass



rw = RandomWalk(1,15)
rw.r_walk()
rw.display()
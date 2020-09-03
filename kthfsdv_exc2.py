import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import time


class Function:
    fig = plt.figure()
    global ax
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Function = 3*Pi*exp(-5*sin(2*Pi*1*t))')

    def __init__(self, plotting_mode='-d'):
        self.plotting_mode = plotting_mode
        os.system("clear")
        if self.plotting_mode == '-d':
            self.default_plot()
        elif self.plotting_mode == '-s':
            try:
                self.static_plot()
            except ValueError:
                os.system("clear")
                print('Wrong arguments passed')
        elif self.plotting_mode == '-t':
            self.time_plot()
        else:
            print('No such arguments')

    def update(self, t):
            h = lambda a: 3 * np.pi *\
                np.exp(-1 * 5 * np.sin(2 * np.pi * 1 * a))
            return h(self.t)

    def plot(self, t, h):
        ax.plot(self.t, h)
        plt.show()

    def default_plot(self, t=np.array(np.linspace(0, 2, 100))):
        self.t = t
        h = self.update(self.t)
        self.plot(self.t, h)

    def static_plot(self):
        print('Plotting with user-defined variables')
        self.t = np.array(np.linspace(int(sys.argv[2]),
                                      int(sys.argv[3]),
                                      int(sys.argv[4])))
        h = self.update(self.t)
        self.plot(self.t, h)

    def time_plot(self, t=np.array(np.linspace(0, 2, 100))):
        self.t = t
        h = self.update(self.t)
        self.plot(self.t, h)
        while True:
            self.t = np.linspace(t[0]+1, t[-1]+1, 100)
            h = self.update(self.t)
            ax.clear()
            ax.plot(self.t, h)
            time.sleep(1.0)


if __name__ == "__main__":
    try:
        prog = Function(sys.argv[1])
    except IndexError:
        prog = Function()

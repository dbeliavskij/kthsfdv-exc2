import matplotlib.pyplot as plt
import numpy as np
import sys
import os


class Function:
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
                print('Specify: first_number last_number number_of_samples')
        elif self.plotting_mode == '-t':
            self.time_plot()
        else:
            print('No such arguments')

    def update(self, t):
            h = lambda a: 3 * np.pi *\
                np.exp(-1 * 5 * np.sin(2 * np.pi * 1 * a))
            return h(self.t)

    def plot(self, t, h):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('Function = 3*Pi*exp(-5*sin(2*Pi*1*t))')
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
        plt.bone()
        plt.plot(self.t, h, color='green')
        try:
            while True:
                plt.pause(0.05)
                self.t = self.t + 0.05
                h = self.update(self.t)
                plt.xlim((self.t[0], self.t[-1]))
                plt.plot(self.t, h, color='green')
        except KeyboardInterrupt:
            plt.show()
            pass


if __name__ == "__main__":
    try:
        prog = Function(sys.argv[1])
    except IndexError:
        prog = Function()

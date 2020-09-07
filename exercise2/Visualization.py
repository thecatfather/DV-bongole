import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import matplotlib.animation as animation

import numpy as np


class Visualization:
    def __init__(self,t_speed,t_max):
        self.dt = t_speed
        self.t_max = t_max
        self.pause = False
        self.T = []
        self.X = []
        

    def simData(self):
        t_max = self.t_max
        dt = self.dt
        x = 0.0
        t = 0.0
        while t < t_max:
            if not self.pause:
                lambda_t = 5*np.sin(2*np.pi*t)
                h_t = 3*np.pi*np.exp(-lambda_t)

                t = t + dt
            yield h_t, t

    def onClick(self,event):
        self.pause ^= True

    def simPoints(self,simData):
        x, t = simData[0], simData[1]
        self.T.append(t)
        self.X.append(x)	
        self.time_text.set_text(self.time_template%(t))
        self.sinegraph.set_data(self.T,self.X)
        self.line.set_data(t, x)
        return self.line, self.time_text

    def visualize(self,x_label="t",y_label="value",title="KTHFSDV Visualization"):

        fig = plt.figure()
        ax = fig.add_subplot(111)
        self.sinegraph, = ax.plot([], [])
        self.line, = ax.plot([], [], 'bo', ms=10)
        ax.set_ylim(-1, 5)
        ax.set_xlim(0, 10)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        #ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
        #ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))

        self.time_template = 't = %.1f '
        self.time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
        fig.canvas.mpl_connect('button_press_event', self.onClick)
        ani = animation.FuncAnimation(fig, self.simPoints, self.simData, blit=False, interval=10,
            repeat=True)
        #plt.xticks(np
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.grid(True,which='both')
        plt.show()

if __name__ == "__main__":
    visualization_obj = Visualization(0.01,100)
    visualization_obj.visualize()
        

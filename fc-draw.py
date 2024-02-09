import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt


def fc_draw():
    background = 3.0
    m = 1000
    observed = np.linspace(0, 15, m)
    expected_lower_mu, expected_upper_mu = np.zeros(m), np.zeros(m)

    fc = rt.TFeldmanCousins()
    fc.SetCL(0.9)
    fc.SetMuMax(50)
    fc.SetMuStep(0.0005)

    for i in range(m):
        expected_upper_mu[i] = fc.CalculateUpperLimit(observed[i], background)
        expected_lower_mu[i] = fc.CalculateLowerLimit(observed[i], background)

    plt.plot(observed, expected_lower_mu, color='black')
    plt.plot(observed, expected_upper_mu, color='black')
    plt.fill_between(observed, expected_lower_mu, expected_upper_mu, color='red', alpha=.5, linewidth=0)
    plt.show()

    return


if __name__ == '__main__':
    fc_draw()

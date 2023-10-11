import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sps
from scipy.interpolate import interp1d
from scipy.special import gamma, gammaincinv


def generate_laplace_value():
    b = 3.0
    mu = np.arange(0, 17, 1)
    x = np.arange(0, 17, 1)
    n, m = mu.size, x.size

    mu_matrix = np.repeat([mu], m).reshape([n, m])
    x_matrix = np.repeat([x], n).reshape([n, m]).T
    laplace_matrix = (mu_matrix + b)**x_matrix / gamma(x_matrix+1) * np.exp(-(mu_matrix+b))

    g_highest = gammaincinv(x, 0.9) - 3
    f_g_highest = interp1d(x, g_highest, kind='nearest')

    g_middle_top = gammaincinv(x, 0.95) - 3
    g_middle_low = gammaincinv(x, 0.05) - 3

    f_g_middle_top = interp1d(x, g_middle_top, kind='nearest')
    f_g_middle_low = interp1d(x, g_middle_low, kind='nearest')

    plt.imshow(laplace_matrix, origin='lower')
    plt.xticks(x)
    plt.yticks(mu)
    plt.colorbar()

    x0 = np.linspace(0, 16, 1000)
    plt.plot(x0 - 1, f_g_highest(x0) - 0.5, color='red', label='highest 90%')
    plt.plot(x0 - 1, f_g_middle_top(x0) - 0.5, color='#faa', label='centered 90%')
    plt.plot(x0 - 1, f_g_middle_low(x0) - 0.5, color='#faa')
    plt.legend()
    plt.tight_layout()
    plt.ylim(-0.5, 14.5)
    plt.xlim(-0.5, 14.5)

    plt.show()
    return


if __name__ == '__main__':
    generate_laplace_value()

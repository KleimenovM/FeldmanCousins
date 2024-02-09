import ROOT as rt
import numpy as np
import time


def main():
    fc = rt.TFeldmanCousins()
    fc.SetCL(.9)
    fc.SetMuMax(50)
    fc.SetMuStep(0.0005)

    n_obs = np.random.random(1000) * 5
    n_bg = np.random.random(1000) * 10

    t0 = time.time()
    for i in range(1000):
        fc.CalculateUpperLimit(n_obs[i], n_bg[i])

    t1 = time.time()

    print(f"TIME {t1 - t0} s")
    return


main()

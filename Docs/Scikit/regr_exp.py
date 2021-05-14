import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def monoExp(x, m, t, b):
    return m * np.exp(-t * x) + b

xs = np.arange(12) + 7
ys = np.array([304.08994, 229.13878, 173.71886, 135.75499,
               111.096794, 94.25109, 81.55578, 71.30187, 
               62.146603, 54.212032, 49.20715, 46.765743])

# plt.figure(figsize=(10,7))
# plt.plot(xs, ys, '.')
# plt.title("Originalne dane")
# plt.show()

# perform the fit
p0 = (2000, .1, 50) # zacząć od wartości których oczekujemy ()
params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
m, t, b = params
sampleRate = 20_000 # Hz
tauSec = (1 / t) / sampleRate

# determine quality of the fit
squaredDiffs = np.square(ys - monoExp(xs, m, t, b))
squaredDiffsFromMean = np.square(ys - np.mean(ys))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
print(f"R² = {rSquared}")

# plot the results
plt.figure(figsize=(10,7))
plt.plot(xs, ys, '.', label="data")
plt.plot(xs, monoExp(xs, m, t, b), '--', label="fitted")
plt.legend()
plt.title("Dopasowana krzywa eksponencjalna")
plt.show()

# inspect the parameters
print(f"Y = {m} * e^(-{t} * x) + {b}")
print(f"Tau = {tauSec * 1e6} µs")

xs_extr = np.arange(25)
ys_extr = monoExp(xs_extr, m, t, b)

plt.figure(figsize=(10,7))
plt.plot(xs_extr, ys_extr, 'b', label="fitted")
plt.plot(xs, ys, 'r.', label="data")
plt.legend()
plt.title("Extrapolated Exponential Curve")
plt.show()
import numpy as np

LAMBDA = "the arrival rate into the system as a whole."
MU = "the capacity of each of n equal servers."
n = "the amount of servers with capacity MU."

P = LAMBDA / MU
P = LAMBDA / (n * MU)
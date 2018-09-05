import glob
import numpy as no
import matplotlib.pyplot as plt

import analysis_tools

filenames = sorted(glob.glob('../03-fundamentals-of-python/inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analyse(f)
    detect_problems(f)


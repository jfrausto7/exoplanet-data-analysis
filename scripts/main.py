import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import distance_from_earth_analyze as dist
import orbper_analyze as orbper
import planet_mass_analyze as plmass
import semimajor_analyze as semi
import stellar_mass_analyze as stmass
import temp_analyze as temp


planets = pd.read_csv("data/planets.csv", sep=',', comment='#')
sns.set(style="ticks")

f, ax = plt.subplots(nrows=2, ncols=3, figsize=(98,24))

ax[0, 0].set_xscale("log")
ax[0, 1].set_xscale("log")
ax[0, 2].set_xscale("log")
ax[1, 0].set_xscale("log")
ax[1, 1].set_xscale("log")
ax[1, 2].set_xscale("log")

# distance
dist.analyze(f, ax[0, 0], planets)

# orbital period
orbper.analyze(f, ax[0, 1], planets)

# planet mass
plmass.analyze(f, ax[0, 2], planets)

# orbit semi-major axis
semi.analyze(f, ax[1, 0], planets)

# stellar mass
stmass.analyze(f, ax[1, 1], planets)

# stellar effective temperature
temp.analyze(f, ax[1, 2], planets)

plt.show()


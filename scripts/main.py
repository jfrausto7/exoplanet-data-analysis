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

f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")

# distance
dist.analyze(f, ax, planets)


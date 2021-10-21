import seaborn as sns


def analyze(f, ax, planets):

    # process data from st_teff and pl_discmethod as a boxplot
    sns.boxplot(ax=ax,x="st_teff", y="pl_discmethod", data=planets)

    # add in points (as a swarmplot) to show precise data through each observation
    sns.swarmplot(ax=ax,x="st_teff", y="pl_discmethod", data=planets,
                  size=1, color=".3", linewidth=0)

    # tweak the visual presentation to fit all points and the figure itself
    ax.xaxis.grid(True)
    ax.set(ylabel="", xlabel="Stellar Effective Temperature (K)")

    # we also don't need to call despine on this because the axes don't have spines here
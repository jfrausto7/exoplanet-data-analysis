import seaborn as sns


def analyze(f, ax, planets):

    # Load the example planets dataset
    # planets = sns.load_dataset("planets")

    # replace pl_pnum and st_mass with other column names
    sns.boxplot(ax=ax, x="pl_bmassj", y="pl_discmethod", data=planets)

    # Add in points to show each observation
    sns.swarmplot(ax=ax, x="pl_bmassj", y="pl_discmethod", data=planets,
                  size=1, color=".3", linewidth=0)
    # Tweak the visual presentation

    ax.xaxis.grid(True)
    ax.set(ylabel="")
    sns.despine(trim=True, left=True)
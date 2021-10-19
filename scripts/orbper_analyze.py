import seaborn as sns
import matplotlib.pyplot as plt


def analyze(f, ax, planets):

    # Load the example planets dataset
    # planets = sns.load_dataset("planets")

    # replace pl_pnum and st_mass with other column names
    sns.boxplot(x="pl_orbper", y="pl_discmethod", data=planets)

    # Add in points to show each observation
    sns.swarmplot(x="pl_orbper", y="pl_discmethod", data=planets,
                  size=1, color=".3", linewidth=0)
    # Tweak the visual presentation

    ax.xaxis.grid(True)
    ax.set(ylabel="")
    sns.despine(trim=True, left=True)
    plt.show()
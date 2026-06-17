import matplotlib.pyplot as plt

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
hours_coded = [2, 4, 3, 6, 5]
bugs_fixed = [5, 12, 8, 20, 15]

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,5))

axes[0].plot(days,hours_coded,color="blue",marker=".")
axes[0].set_title("Daily Coding Hours")

axes[1].bar(days,bugs_fixed,color="orange")
axes[1].set_title("Bugs Fixed per Day")

plt.tight_layout()
plt.show()
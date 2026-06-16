import matplotlib.pyplot as plt

weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

models_built = [1, 3, 2, 5, 4]
earnings_usd = [150, 400, 250, 800, 600]
accuracy_score = [75, 82, 80, 91, 88]

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(12,5))

axes[0].scatter(models_built,earnings_usd,color="green",s=100)
axes[0].set_title("Models vs Earnings")

axes[1].plot(weeks,accuracy_score,color="red",marker="*")
axes[1].set_title("Model Accuracy Trend")

plt.tight_layout()
plt.show()
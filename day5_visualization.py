import matplotlib.pyplot as plt

din = [1, 2, 3, 4, 5]
temperature = [30, 32, 34, 33, 36]
plt.plot(din,temperature,color="blue",linestyle="--",marker=".",linewidth=2)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("sahiwal temperature")
plt.grid(True)
plt.show()


subjects = ["DBMS", "OOP", "DLD", "Math"]
marks = [85, 92, 78, 88]

plt.scatter(subjects,marks,color="blue",s=100)
plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("result")
plt.show()


mahine = ["Jan", "Feb", "Mar", "Apr"]
kamai = [10, 20, 15, 30]
kharcha = [8, 10, 12, 10]

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,5))
axes[0].plot(mahine,kamai,color="purple",marker=".")
axes[0].set_title("profit")

axes[1].bar(mahine,kharcha,color="blue")
axes[1].set_title("mahana karcha")
plt.tight_layout()
plt.show()
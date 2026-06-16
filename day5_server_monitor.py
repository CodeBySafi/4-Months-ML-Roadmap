import matplotlib.pyplot as plt

# Data for Graph 1 (Time Series)
hours = ["1 PM", "2 PM", "3 PM", "4 PM", "5 PM"]
cpu_usage = [30, 45, 80, 60, 25]  # Red Line
ram_usage = [50, 55, 90, 75, 40]  # Blue Line

# Data for Graph 2 (Categories)
server_names = ["Server A", "Server B", "Server C"]
active_users = [1500, 3200, 800]

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(12,5))

axes[0].plot(hours,cpu_usage,color="red",marker=".",label="CPU Usage")
axes[0].plot(hours,ram_usage,color="blue",marker="*",label="RAM Usage")
axes[0].set_title("Server Load Over Time")
axes[0].legend()

axes[1].bar(server_names , active_users,color="orange")
axes[1].set_title("Active Users per Server")

plt.tight_layout()
plt.show()

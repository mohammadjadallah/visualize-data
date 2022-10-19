# How to show the relationship between three variables using scatter plot

data = pd.read_csv("Lab.csv")
print(data)
# to show the relationship between 3 parameters use the below way
# data.plot(kind='scatter', y='Lab', x='established in', c='num of device')

# or this way
plt.scatter(x='Lab', y='established in', c='num of device', data=data)
# plt.colorbar().ax.set_title("num of device")  # for title of colorbar
# customize the chart
color_bar = plt.colorbar()
color_bar.set_label("num of device", fontsize=10)  # label of colorbar, you can use ha -> horizontal align, va -> verticale align
plt.xlabel('Lab', fontsize=10)
plt.ylabel('established in', fontsize=10)
plt.show()



# Created By Mohammad Al Jadallah, developerx2

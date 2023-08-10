import matplotlib.pyplot as plt

# x轴和y轴的数据
x = ["yolov5s", "yolov5s+IDCDA", "yolov5s+Retinex",  "yolov5s+ssr", "yolov5s+msr"]
y = [0.626, 0.82, 0.661, 0.794, 0.813]

# 绘制折线图
plt.plot(x, y)

# 设置标题和坐标轴标签
plt.title("The Precison of Different Models")
plt.xlabel("models")
plt.ylabel("all-p")

# 添加纵坐标的标注，用红色字体
for i, j in zip(x, y):
    plt.annotate(str(j), xy=(i, j), color="red")

# 显示图表
plt.show()

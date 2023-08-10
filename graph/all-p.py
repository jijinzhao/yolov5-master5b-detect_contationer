import matplotlib.pyplot as plt

# x轴和y轴的数据
x = ["yolov5s", "yolov5s+IDCDA", "yolov5s+Retinex",  "yolov5s+ssr", "yolov5s+msr"]
y = [0.626, 0.82, 0.661, 0.794, 0.813]

# 创建一个画布，并设置宽度和高度为661和428像素
plt.figure(figsize=(661/100, 428/100))

# 绘制折线图
plt.plot(x, y)

# 设置标题和坐标轴标签
plt.title("The Precison of Different Models")
plt.xlabel("models")
plt.ylabel("all-p")

# 添加纵坐标的标注，用红色字体
for i, j in zip(x, y):
    plt.annotate(str(j), xy=(i, j), color="red")

# 保存图片到指定的文件夹和文件名，格式为jpg
plt.savefig("D:\\zhaojijin\\picsOfRes\\all-p.jpg")

# 显示图表
plt.show()

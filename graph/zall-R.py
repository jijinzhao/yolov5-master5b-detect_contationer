import matplotlib.pyplot as plt

# x轴和y轴的数据
x = ["YOLOv5s", "YOLOv5s+IDCDA", "YOLOv5s+Retinex",  "YOLOv5s+SSR", "YOLOv5s+MSR"]
y = [0.128, 0.82, 0.471, 0.737, 0.79]
plt.figure(figsize=(749/100, 428/100))
# 绘制折线图
plt.bar(x, y)

# 设置标题和坐标轴标签
plt.title("The Recall of Different Models")
plt.xlabel("models")
plt.ylabel("all-R")

# # 添加纵坐标的标注，用红色字体
# for i, j in zip(x, y):
#     plt.annotate(str(j), xy=(i, j), color="red")

# 保存图片到指定的文件夹和文件名，格式为jpg
plt.savefig(r"C:\Users\Administrator\Desktop\expdataPro")
# 显示图表
plt.show()

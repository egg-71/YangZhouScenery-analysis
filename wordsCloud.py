import os

import numpy as np
import pandas as pd
from PIL import Image  # 图像处理库
import jieba
from stylecloud import gen_stylecloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文件
file_path = 'D:/Data-spy/Hangzhou/result.csv'
pd_data = pd.read_csv(file_path, encoding='ANSI', usecols=['comments'])

# 删除空行
exist_col = pd_data.dropna()

# 读取内容
text = exist_col['comments'].tolist()  # 确保列名正确
# 分词
result = ' '.join(jieba.cut(' '.join(text)))

# 打开背景图片，也就是想要生成的词云形状底图
img_path=r'D:\pythonProject\img\江苏.jpg'
#img = Image.open(r'.\img\hz地图.jpg')
#检查文件是否存在
if not os.path.exists(img_path):
    print(f"文件不存在:{img_path}")
else:
    #读取遮罩图像
    img=np.array(Image.open(img_path))

#设置词云字体
font=r'D:\pythonProject\font\DouFont-PinboGB-Flash-Fast.ttf'

# 生成词云
wordcloud = WordCloud(
                      font_path=font,  # 指定字体路径
                      background_color='black',  # 背景颜色
                      colormap='spring',
                      collocations=False,
                      contour_width=10.0,
                      contour_color='white',
                      scale=3,
                      mask=img,#使用遮罩图片
                      width=800, height=600,
                      stopwords={'你', '我', '的', '了', '在', '吧', '相信', '是', '也', '都', '不', '吗', '就', '我们', '还', '大家',
                                 '你们', '就是', '以后','有','和','到','去','到','很'}).generate(result)

# 显示词云
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()

#保存词云图片的路径
save_path=r'D:\pythonProject\img\扬州泰州景点词云.jpg'
#确保保存路径文件夹存在
os.makedirs(os.path.dirname(save_path),exist_ok=True)
# 保存词云图片
wordcloud.to_file(save_path)
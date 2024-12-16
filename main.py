#pandas进行数据预处理
import os
import pandas as pd
#使用snowNLP进行数据处理
from matplotlib import pyplot as plt
from snownlp import SnowNLP

#显示中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path='D:/Data-spy/Hangzhou/result.csv'
#本次使用的数据均为ANSI编码格式
data=pd.read_csv(file_path,encoding='ANSI',usecols=['comments'])

#删除缺失值
data=data.dropna()

#删除重复值
data=data.drop_duplicates()

#输出数据集大小
print('数据集大小：',data.shape)
#读取评论这一列的数据：comments

print(data.head())

# 中文分词
#定义一个函数来处理每条评论
def process_comments(comment):
    s=SnowNLP(comment)
    return s.words,s.sentiments
#应用分词函数到每条评论
#将分词结果给到新的列words
data['words']=data['comments'].apply(lambda comment: ' '.join(process_comments(comment)[0]))
#将情感得分给到新的列score
data['score'] = data['comments'].apply(lambda comment: process_comments(comment)[1])
#打印前几行的分词结果和情感得分情况
print(data[['words', 'score']].head())
#计算正面、负面、中性情感的数量
positive_count = len(data[(data['score'] > 0.6) & (data['score'] <= 1)])#正面
negative_count = len(data[(data['score'] >= 0) & (data['score'] <= 0.4)])#负面
neutral_count = len(data[(data['score'] > 0.4) & (data['score'] <= 0.6)])#中性

#将情感得分绘制成饼状图，分为正面、负面、中性，根据比例看当前景点的好评度,中性：0.4~0.6分，正面：0.6~1分，负面：0~0.4分
def visualize_sentiment_classification(data):
    #计算正面、负面、中性情感的数量
    #sentiment_counts = {'Positive': positive_count, 'Negative': negative_count, 'Neutral': neutral_count}
    sentiment_classes = {'Positive': positive_count, 'Negative': negative_count, 'Neutral': neutral_count}
    labels = list(sentiment_classes.keys())
    sizes = [sentiment_classes[label] for label in labels]
    #设置饼状图样式
    #'#FCFAF1'：白，'#FF37C8'：粉，'#000000'：黑,#FECF2E:明黄
    #正面，负面，中性
    colors = ['#FF37C8', '#FCFAF1', '#FECF2E']#三个饼的颜色,在线取色器：zxqsq.wiicha.com，取和词云相同的配色
    explode=(0.1,0.2,0.3)#突出显示第一部分
    plt.gcf().set_facecolor('#000000')
    plt.pie(sizes,explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=140)
    plt.axis('equal')#使饼图长宽相等
    # 显示图例
    plt.legend()
    plt.title('扬泰景点情感得分饼状图')

#保存图片
save_path=r'D:\pythonProject\img\扬泰景点情感评分饼状图.jpg'
#确保保存路径文件夹存在
os.makedirs(os.path.dirname(save_path),exist_ok=True)
#绘制情感分类饼状图
visualize_sentiment_classification(data)
# 保存饼状图（一定要先保存再show,plt.show会清空当前的图形）
plt.savefig(save_path)
#展示饼状图
plt.show()

#计算每个情感得分区间的评论数量
bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0]
labels=['0-0.2','0.2-0.4','0.4-0.6','0.6-0.8','0.8-1.0']
data['score_bin']=pd.cut(data['score'],bins=bins,labels=labels,right=False)
score_counts=data['score_bin'].value_counts().sort_index()
# 绘制柱状图
fig=plt.figure(figsize=(10, 6))
colors=['#FF37C8','white','#FECF2E','#FF37C8','white']
plt.rcParams['axes.facecolor']='#000000'
fig.patch.set_facecolor('#000000')
#设置透明度
fig.patch.set_alpha(0.9)
plt.bar(score_counts.index, score_counts.values,color=colors,width=0.45,edgecolor='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.xlabel('Sentiment Score Range',color='white')
plt.ylabel('Counts',color='white')
plt.title('Sentiment Score Distribution',color='white')
# plt.xticks(rotation=45)  # 旋转x轴标签，以便更好地显示
#保存柱状图
save_path=r'D:\pythonProject\img\扬泰景点情感评分柱状图.jpg'
#确保保存路径文件夹存在
os.makedirs(os.path.dirname(save_path),exist_ok=True)
# 保存柱状图
plt.savefig(save_path)
plt.show()



# text = '希望本无所谓有，也无所谓无，这就像地上的路，其实地上本没有路，走的人多了，也便成了路。'
# s = SnowNLP(text)
# print(s.words)
#
# # 词性标注
# text = '哪里有天才，我是把别人喝咖啡的工夫都用在了工作上了。'
# s = SnowNLP(text)
# print(list(s.tags))
#
# 情感分析
# text1 = '这是我遇见的最棒的一家店，种类多，价格低，更喜欢的是服务质量很好'
# text2 = '这是我遇到的最差的一家店，种类少，价格贵，更气人的是服务质量很差'
# s1 = SnowNLP(text1)
# s2 = SnowNLP(text2)
# print(s1.sentiments)
# print(s2.sentiments)
#
# # 转换成拼音
# text = '哪里有天才，我是把别人喝咖啡的工夫都用在了工作上了。'
# s = SnowNLP(text)
# print(s.pinyin)
#
# # 繁体转简体
# text = '希望本無所謂有，也無所謂無，這就像地上的路，其實地上本沒有路，走的人多了，也便成了路。'
# s = SnowNLP(text)
# print(s.han)
#
# # 提取文本关键词，总结3个关键词
# text = '随着顶层设计完成，全国政协按下信息化建设快进键：建设开通全国政协委员移动履职平台，开设主题议政群、全国政协书院等栏目，建设委员履职数据库，拓展网上委员履职综合服务功能；建成网络议政远程协商视频会议系统，开展视频调研、远程讨论活动，增强网络议政远程协商实效；建立修订多项信息化规章制度，优化电子政务网络。'
# s = SnowNLP(text)
# print(s.keywords(3))
#
# # 提取文本摘要
# text = '随着顶层设计完成，全国政协按下信息化建设快进键：建设开通全国政协委员移动履职平台，开设主题议政群、全国政协书院等栏目，建设委员履职数据库，拓展网上委员履职综合服务功能；建成网络议政远程协商视频会议系统，开展视频调研、远程讨论活动，增强网络议政远程协商实效；建立修订多项信息化规章制度，优化电子政务网络。'
# s = SnowNLP(text)
# print(s.summary(2))# 总结两条摘要
#
# # 文本相似度(BM25)
# s = SnowNLP([['机器学习', '人工智能'],
#              ['深度学习', '自然语言处理'],
#              ['数据挖掘']])
# artilc1 = ['自然语言处理']
# print(s.sim(artilc1))
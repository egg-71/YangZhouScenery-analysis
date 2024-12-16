#pandas进行数据预处理
import os
import csv
import pandas as pd
#使用snowNLP进行数据处理
import pyecharts
from matplotlib import pyplot as plt
from snownlp import SnowNLP

#批量处理csv文件并存回csv中
folder_path='D:/Data-spy/Hangzhou/heatmap'
newFolder_path='D:/Data-spy/Hangzhou/heatmap/cleaned'
# 遍历文件夹中的所有CSV文件
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)

        # 尝试不同的编码读取CSV文件
        try:
            df = pd.read_csv(file_path,encoding='ANSI')
        except UnicodeDecodeError:
            try:
                df=pd.read_csv(file_path,encoding='ANSI')
            except UnicodeDecodeError:
                df=pd.read_csv(file_path,encoding='GBK')

        # 删除重复值
        df = df.drop_duplicates()

        # 删除缺失值
        df = df.dropna()

        # 构建新的文件名，例如在原文件名后添加'_cleaned'
        new_file_path = os.path.join(newFolder_path, filename.replace('.csv', '_cleaned.csv'))

        # 保存处理后的CSV文件
        df.to_csv(new_file_path, index=False,encoding='ANSI')
        print(f'Processed and saved {new_file_path}')

#对评论进行情感打分并存入当前csv文件中的新一列中
#遍历数据预处理后的csv文件
for filename in os.listdir(newFolder_path):
    if filename.endswith('.csv'):
        # 构建完整的文件路径
        file_path = os.path.join(newFolder_path, filename)

        # 尝试ANSI编码读取CSV文件（根据文件的编码方式来读取），取出评论列的数据，情感打分，并写回csv文件中
        data=pd.read_csv(file_path,encoding='ANSI')
        #定义情感打分函数
        def process_comments(comment):
           s = SnowNLP(comment)
           return s.sentiments
        # 将情感得分给到新的列score
        data['score'] = data['comments'].apply(process_comments)
        #保存包含情感得分的csv文件
        data.to_csv(file_path,index=False,encoding='ANSI')
        print(f'Updated {file_path} with sentiment scores')


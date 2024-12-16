## 扬州&&泰州地区景点情感分析

**开发工具：PyCharm**

**Python版本：3.9.0**

**数据集来源：携程**

**项目组成：**

- Data-spy：爬取的原始数据和数据清洗后的数据，合并文件夹下的合并csv.bat使用方法：将需要合并的csv文件拖至当前文件夹，执行这个.bat文件则会自动合并，生成一个名为result.csv的合并后文件

- font：存放了各种字体，可以在生成词云等地方使用

- img：放置了词云的遮罩和项目生成的各种饼状图、条形图等

- dataPre.py：数据预处理

- heatmap.py：生成热力图

- main.py：分词、情感打分等
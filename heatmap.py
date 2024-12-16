from pyecharts.charts import Geo
from pyecharts import options as opts

# 景点及其情感得分数据和真实经纬度坐标
data = {
    'scenery': ['大明寺', '东关街', '个园', '扬州古运河', '何园', '溱湖', '瘦西湖', '茱萸湾'],
    'score': [0.847764, 0.859501, 0.877837, 0.85959, 0.90283, 0.873117, 0.774611, 0.858948],
    'coords': [
        (119.4265, 32.3972), (119.4273, 32.3955), (119.4216, 32.3978),
        (119.4162, 32.3926), (119.4204, 32.3851), (119.9691, 32.3025),
        (119.4196, 32.3923), (119.4234, 32.3967)
    ]
}

# 创建Geo实例，并设置地图类型为 '江苏'
geo = Geo(init_opts=opts.InitOpts(width="1000px", height="600px"))
geo.add_schema(maptype="江苏")  # 显式指定使用江苏省地图

# 添加坐标和数据到地图
for name, score, coord in zip(data['scenery'], data['score'], data['coords']):
    geo.add_coordinate(name, coord[0], coord[1])  # 添加坐标点
geo.add(
    "江苏景点情感得分",
    [(name, score) for name, score in zip(data['scenery'], data['score'])],
    type_="heatmap"  # 设置为热力图模式
)

# 设置全局选项
geo.set_global_opts(
    title_opts=opts.TitleOpts(title="江苏省景点情感得分热力图"),
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        min_=0, max_=1,  # 数据范围
        range_text=["High", "Low"],  # 颜色范围描述
        orient="horizontal",  # 水平放置
        pos_top="10%",  # 位置
        pos_left="center"
    ),
)

# 渲染地图到HTML文件
geo.render("江苏省景点情感得分热力图.html")

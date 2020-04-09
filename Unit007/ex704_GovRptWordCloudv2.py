#ex704_GovRptWordCloudv1.py
import jieba
import wordcloud
from matplotlib.pyplot import imread
mask = imread("star.png")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="STHeiti Medium.ttc", width=1000, height=700, background_color="white", mask=mask)
w.generate(txt)
w.to_file("grwordcloudstar.png")
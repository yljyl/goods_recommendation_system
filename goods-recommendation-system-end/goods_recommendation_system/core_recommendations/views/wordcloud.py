import base64
import os
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import jieba
from rest_framework.views import APIView
from rest_framework.response import Response
from user_management.utils.json_response import SuccessResponse

def scan_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.xlsx'):
                files.append(os.path.join(root, filename))
    return files

def build_wordcloud():
    data_directory = 'data'

    # 扫描目录下的所有xlsx文件
    files = scan_files(data_directory)

    # 提取所有文件中的品名
    names = []
    for file in files:
        df = pd.read_excel(file)
        if '产品名称' in df.columns:
            names.extend(df['产品名称'].tolist())

    # 将商品名称拼接为字符串
    text = ' '.join(names)

    # 定义无意义的语气词列表
    stop_words = ['的', '了', '和', '在', '是', '有', '我', '我们', '你', '您', '他', '她']

    # 使用jieba进行中文分词
    seg_list = jieba.cut(text)
    seg_text = ' '.join(seg_list)
    seg_list = jieba.cut(text)
    seg_text = ' '.join([word for word in seg_list if word not in stop_words])

    # 统计词频
    words = seg_text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    return word_counts

# 词云
class WordCloudView(APIView):
    def get(self, request):
        word_counts = build_wordcloud()
        word_list = []
        for word, count in word_counts.items():
            word_list.append({'name': word, 'value': count})
        return SuccessResponse(data=word_list)
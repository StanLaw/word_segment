# coding=utf-8
from word_segment.utils import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 分词模型
aa = ArticleAnalysis(RawFile, SaveFile)

# 分词模型运行
aa.run()

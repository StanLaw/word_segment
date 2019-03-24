无监督分词模型(Naive Bayes)
参考博客：https://blog.csdn.net/amds123/article/details/68955395

<参数设置>
文件参数
    1、训练的文章文件 raw_file
    2、保存的词汇文件 save_file
细节参数（可不设置，复用settings.py中的即可）
    1、初始将文章拆解为词汇统计时的词汇长度：nWordMaxLen （该参数不重要，与最后词汇长度无关）
    2、词汇出现频次阈值: minCount（出现次数低于该阈值的词汇不放入统计）
    3、词汇粘合度阈值：minProbThreshold（词汇粘合度低于阈值时，拆开词汇，该粘合度与词的长度有关，因此为字典类型）
    4、测试文件 RawFile（用天龙八部作为测试文件）
    5、测试文件切分后的词汇文件SaveFile

文件作用说明：
1、data:
    1.1、tianlongbabu.txt
            天龙八部测试文件
    1.2、dict.txt
            天龙八部的模型切割词汇文件
2、utils：
    2.1、settings.py
            保存参数设置的文件
    2.2、functions.py
            自定义函数的文件
    2.3、base.py
            封装好的分词模型class保存文件
3、demo.py
    模型应用demo



# coding=utf-8
from settings import *
import numpy as np
import re


def texts(raw_file):
    with open(raw_file, 'r') as f:
        for line in f.readlines():
            line = unicode(line).strip()
            if line != u'':
                for tt in re.split(u'[^\u4e00-\u9fa50-9a-zA-Z]+', line):
                    if tt:
                        yield tt


def is_keep(s, total_cnt, word_grams):
    """
    检验词汇是否应该保存下来
    :param s: 要检验的词汇
    :param total_cnt: 训练集总字数
    :param word_grams: 词汇出现次数字典
    """
    if len(s) >= 2:
        score = min([total_cnt * word_grams[s] / (word_grams[s[:i + 1]] * word_grams[s[i + 1:]])
                     for i in range(len(s) - 1)])
        if score > minProbThreshold[len(s)]:
            return True
    else:
        return False


def is_real(s, word_grams):
    """
    :param s: 要检验的词汇
    :param word_grams: 词典
    """
    if len(s) >= 3:
        for i in range(3, nWordMaxLen + 1):
            for j in range(len(s) - i + 1):
                if s[j:j + i] not in word_grams:
                    return False
        return True
    else:
        return True


def cut(s, word_grams):
    """
    :param s: 要切割的句子
    :param word_grams: 词典
    """
    r = np.array([0] * (len(s) - 1))
    for i in range(len(s) - 1):
        for j in range(2, nWordMaxLen + 1):
            if s[i:i + j] in word_grams:
                r[i:i + j - 1] += 1
    w = [s[0]]
    for i in range(1, len(s)):
        if r[i - 1] > 0:
            w[-1] += s[i]
        else:
            w.append(s[i])
    return w


def sorted_save(my_dict, file_name):
    """
    将字典my_dict里的item（key, value），按照value进行降序保存，保存在文件file_name中
    :param file_name: 保存文件
    :param my_dict:   待保存的字典

    """
    with open(file_name, 'w') as f_write:
        for key, value in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
            string = "{key},{value}\n".format(key=key, value=value)
            f_write.write(string)
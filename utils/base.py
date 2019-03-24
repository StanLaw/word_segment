# coding=utf-8
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from functions import *


class _AnalysisAbstractClass:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def _raw_input(self):
        """
        step 1:
            将文章拆解成词汇
        """
        pass

    @abstractmethod
    def _words_summary(self):
        """
        step 2:
            统计step1中拆解后的结果
        """
        pass

    @abstractmethod
    def _remove_useless_words(self):
        """
        step 3:
            清除不合理的词汇
        """
        pass

    @abstractmethod
    def _generate_word_dict(self):
        """
        step 4:
            生成词汇字典
        """
        pass

    @abstractmethod
    def save_dict(self):
        """
        step 5:
            保存词汇字典
        """
        pass

    @abstractmethod
    def run(self):
        """
        主函数，模型运算执行的模块
        """
        pass


class ArticleAnalysis(_AnalysisAbstractClass):
    __slots__ = ('_rawGrams', '_gramSet', 'wordGrams',
                 'total', 'raw_file', 'save_file',)

    def __init__(self, raw_file, save_file):
        super(ArticleAnalysis, self).__init__()
        self._rawGrams = defaultdict(int)
        self._gramSet = None
        self.total = 0.
        self.wordGrams = None
        self.raw_file = raw_file
        self.save_file = save_file

    def _raw_input(self):
        for line in texts(self.raw_file):
            for i in range(len(line)):
                for j in range(1, nWordMaxLen + 1):
                    if i + j <= len(line):
                        self._rawGrams[line[i:i + j]] += 1
        self._rawGrams = {i: j for i, j in self._rawGrams.iteritems() if j >= minCount}

    def _words_summary(self):
        self.total = 1. * sum([j for i, j in self._rawGrams.iteritems() if len(i) == 1])
        print self.total

    def _remove_useless_words(self):
        self._gramSet = set(i for i, j in self._rawGrams.iteritems()
                            if is_keep(i, total_cnt=self.total, word_grams=self._rawGrams))

    def _generate_word_dict(self):
        words = defaultdict(int)
        for t in texts(self.raw_file):
            for i in cut(t, self._rawGrams):
                words[i] += 1

        words = {i: j for i, j in words.iteritems() if j >= minCount}
        self.wordGrams = {i: j for i, j in words.iteritems() if is_real(i, self._gramSet)}

    def save_dict(self):
        sorted_save(self.wordGrams, self.save_file)

    def run(self):
        self._raw_input()
        self._words_summary()
        self._remove_useless_words()
        self._generate_word_dict()
        self.save_dict()

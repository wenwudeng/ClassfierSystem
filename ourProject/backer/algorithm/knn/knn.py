import datetime
import glob

# starttime = datetime.datetime.now()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import os
import cv2

acc = 0.0
runtime = 0.0

# X_train = []
# y_train = []

path='backer/algorithm/knn/photo/train/'
path1='backer/algorithm/knn/photo/test/'
# path = os.path.abspath(os.path.dirname(__file__))+str(r'\photo\train/')
# path1 = os.path.abspath(os.path.dirname(__file__))+str(r'\photo/test/')
# cate = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]
# cate1 = [path1 + x for x in os.listdir(path1) if os.path.isdir(path1 + x)]
# for idx, folder in enumerate(cate):
#     for im in glob.glob(folder + '/*.jpg'):
#         # 打开一张图片并灰度化
#         Images = cv2.imread(im)
#         image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
#         hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
#         X_train.append((hist / 255).flatten())
#         y_train.append(idx)
# X_train = np.array(X_train)
# y_train = np.array(y_train)
# print('this is X_train %s' %X_train)
# print('this is y_train %s' %y_train)
#
# X_test = []
# y_test = []
#
# for idx, folder in enumerate(cate1):
#     print('enter cate1 %s' %enumerate(cate1))
#     for im in glob.glob(folder + '/*.jpg'):
#         print('reading image :'+im)
#         # 打开一张图片并灰度化
#         Images = cv2.imread(im)
#         image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
#         hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
#         X_test.append((hist / 255).flatten())
#         y_test.append(idx)
# X_test = np.array(X_test)
# y_test = np.array(y_test)
# print('this is X_test %s' % X_test)
# print(y_test)


# X = []
# Y = []
#
# for i in range(0, 2):
#     # 遍历文件夹，读取图片
#     for f in os.listdir("./photo/%s" % i):
#         # 打开一张图片并灰度化
#         Images = cv2.imread("./photo/%s/%s" % (i, f))
#         image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
#         hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
#         X.append(((hist / 255).flatten()))
#         Y.append(i)
# X = np.array(X)
# Y = np.array(Y)
# print(X)
# input()
# print(Y)
# input()
# # 切分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
#
# print('this is X_train+%s' %X_train)
# input()
# print(y_train)
# input()
# print(X_test)
# input()
# print(y_test)
# input()
# 随机率为100%（保证唯一性）选取其中的30%作为测试集

class KNN:
    def __init__(self, train_data, train_label, test_data):
        self.train_data = train_data
        self.train_label = train_label
        self.test_data = test_data

    def knnclassify(self):
        num_train = (self.train_data).shape[0]
        num_test = (self.test_data).shape[0]
        labels = []
        for i in range(num_test):
            y = []
            for j in range(num_train):
                dis = np.sum(np.square((self.train_data)[j] - (self.test_data)[i]))
                y.append(dis)
            labels.append(self.train_label[y.index(min(y))])
        labels = np.array(labels)
        return labels


# knn = KNN(X_train, y_train, X_test)
# predictions_labels = knn.knnclassify()
#
# print('this is predict:%s' %predictions_labels)
#
# print(confusion_matrix(y_test, predictions_labels))
# print(classification_report(y_test, predictions_labels))
#
# # 计算准确率
# account = 0
# result = 0
# for truth, predict in zip(y_test, predictions_labels):
#     account += 1
#     if truth == predict:
#         result += 1
# acc = result / account
# print('acc is %f' % acc)
#
# endtime = datetime.datetime.now()
# runtime = endtime.timestamp() - starttime.timestamp()
# print(runtime)





def knnTest():
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    # path3 = 'photo/train/'
    # path4 = 'photo/test/'
    # path3 = os.path.abspath(os.path.dirname(__file__)) + str(r'\photo\train/')
    # path4 = os.path.abspath(os.path.dirname(__file__))+str(r'\photo/test/')
    print("进入算法")
    global path,path1
    starttime = datetime.datetime.now()
    cate = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]
    cate1 = [path1 + x for x in os.listdir(path1) if os.path.isdir(path1 + x)]
    for idx, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.jpg'):
            # 打开一张图片并灰度化
            Images = cv2.imread(im)
            image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
            hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
            X_train.append((hist / 255).flatten())
            y_train.append(idx)
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    print('this is X_train %s' % X_train)
    print('this is y_train %s' % y_train)
    for idx, folder in enumerate(cate1):
        print('enter cate1 %s' % enumerate(cate1))
        for im in glob.glob(folder + '/*.jpg'):
            print('reading image :' + im)
            # 打开一张图片并灰度化
            Images = cv2.imread(im)
            image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
            hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
            X_test.append((hist / 255).flatten())
            y_test.append(idx)
    X_test = np.array(X_test)
    y_test = np.array(y_test)
    print('this is X_test %s' % X_test)
    print(y_test)

    knn = KNN(X_train, y_train, X_test)
    predictions_labels = knn.knnclassify()

    print('this is predict:%s' % predictions_labels)

    print(confusion_matrix(y_test, predictions_labels))
    print(classification_report(y_test, predictions_labels))

    # 计算准确率
    account = 0
    result = 0
    for truth, predict in zip(y_test, predictions_labels):
        account += 1
        if truth == predict:
            result += 1
    global acc, runtime
    acc = result / account
    print('acc is %f' % acc)
    endtime = datetime.datetime.now()
    runtime = endtime.timestamp() - starttime.timestamp()
    print(runtime)
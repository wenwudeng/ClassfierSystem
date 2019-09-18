import glob
import platform
import time
from PIL import Image
from skimage.feature import hog
import numpy as np
import os
import joblib
from skimage import io, transform
from sklearn.svm import LinearSVC
import shutil
import sys

test_image_path = 'testdata/'
test_feat_path = 'test/'
model_path = 'model/'
image_height = 100
image_width = 128

label_map = {0: 'sheep',
             1: 'dog'
             }


def get_feat(image_list, name_list, label_list, savePath):
    i = 0
    for image in image_list:
        try:
            # 如果是灰度图片  把3改为-1
            image = np.reshape(image, (image_height, image_width, 3))
        except:
            print('发送了异常，图片大小size不满足要求：', name_list[i])
            continue
        gray = rgb2gray(image) / 255.0
        # 这句话根据你的尺寸改改
        fd = hog(gray, orientations=12, block_norm='L1', pixels_per_cell=[8, 8], cells_per_block=[4, 4],
                 visualize=False,
                 transform_sqrt=True)
        fd = np.concatenate((fd, [label_list[i]]))
        fd_name = name_list[i] + '.feat'
        fd_path = os.path.join(savePath, fd_name)
        joblib.dump(fd, fd_path)
        i += 1
    print("Test features are extracted and saved.")


# 变成灰度图片
def rgb2gray(im):
    gray = im[:, :, 0] * 0.2989 + im[:, :, 1] * 0.5870 + im[:, :, 2] * 0.1140
    return gray


# 提取特征
def extra_feat():
    test_name =[]
    test_label=[]
    test = []
    for x in os.listdir(test_image_path):
        for a, b, c in os.walk(test_image_path + '/' + x):
            test.append(c)
        for y in test:
            for index in y:
                test_name.append(index)
                test_label.append(x)
    print('testname:::%s' %test_name)

    cate = ['0','1']
    for i in cate:
        test_image = get_image_list(test_image_path+'/'+i, test_name)
    get_feat(test_image, test_name, test_label, test_feat_path)


# 获得图片列表
def get_image_list(filePath, nameList):
    print('read image from ',filePath)
    print('nameList:', nameList)
    img_list = []
    for name in nameList:
        temp = Image.open(os.path.join(filePath,name))
        img_list.append(temp.copy())
        temp.close()
    print(img_list)
    return img_list



def train_and_test():

    extra_feat()
    t0 = time.time()
    features = []
    labels = []
    correct_number = 0
    total = 0

    # 下面的代码是加载模型  可以注释上面的代码   直接进行加载模型  不进行训练
    clf = joblib.load(model_path + 'model')
    print("训练之后的模型存放在model文件夹中")
    # exit()
    result_list = []
    for feat_path in glob.glob(os.path.join(test_feat_path, '*.feat')):
        total += 1
        if platform.system() == 'Windows':
            symbol = '\\'
        else:
            symbol = '/'
        image_name = feat_path.split(symbol)[1].split('.feat')[0]
        data_test = joblib.load(feat_path)
        data_test_feat = data_test[:-1].reshape((1, -1)).astype(np.float64)
        result = clf.predict(data_test_feat)
        result_list.append(image_name + ' ' + label_map[int(result[0])] + '\n')
        if int(result[0]) == int(data_test[-1]):
            correct_number += 1
    write_to_txt(result_list)
    rate = float(correct_number) / total
    t1 = time.time()
    print('准确率是： %f' % rate)
    print('耗时是 : %f' % (t1 - t0))


def write_to_txt(list):
    with open('result.txt', 'w') as f:
        f.writelines(list)
    print('每张图片的识别结果存放在result.txt里面')


if __name__ == '__main__':
    train_and_test()  # 训练并预测

# -*- coding: cp936 -*-
import cv2
import numpy
import time
import random
import os


def judge():
    # ����һ��3��3�ĽṹԪ��
    # return 0 stone ,1 jiandao, 2 bu
    img = cv2.imread("wif.jpg", 0)
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    dilate = cv2.dilate(img, element)
    erode = cv2.erode(img, element)
    # ������ͼ�������ñߣ���һ�����������ͺ��ͼ�񣬵ڶ��������Ǹ�ʴ���ͼ��
    result = cv2.absdiff(dilate, erode);
    # ����õ��Ľ���ǻҶ�ͼ�������ֵ���Ա������Ĺ۲���
    retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY);

    # ��ɫ�����Զ�ֵͼÿ������ȡ��
    result = cv2.bitwise_not(result);
    result = cv2.medianBlur(result, 23)
    a = []
    posi = []
    width = []
    count = 0
    area = 0
    for i in range(result.shape[1]):
        for j in range(result.shape[0]):
            if (result[j][i] == 0):
                area += 1
    for i in range(result.shape[1]):
        if (result[5 * result.shape[0] / 16][i] == 0 and result[5 * result.shape[0] / 16][i - 1] != 0):
            count += 1
            width.append(0)
            posi.append(i)
        if (result[5 * result.shape[0] / 16][i] == 0):
            width[count - 1] += 1
    """
    print 'the pic width is ',result.shape[1],'\n'
    for i in range(count):
        print 'the ',i,'th',' ','is';
        print 'width ',width[i]
        print 'posi ',posi[i],'\n'
    print count,'\n'
    print 'area is ',area,'\n'

    cv2.line(result,(0,5*result.shape[0]/16),(214,5*result.shape[0]/16),(0,0,0))
    cv2.namedWindow("fcuk")
    cv2.imshow("fcuk",result)
    cv2.waitKey(0)
    """
    # �ж�ʱ��

    width_length = 0
    width_jiandao = True
    for i in range(count):
        if width[i] > 45:
            # print 'bu1';
            return 2;
        if width[i] <= 20 or width[i] >= 40:
            width_jiandao = False
        width_length += width[i]
    if width_jiandao == True and count == 2:
        return 1;
    if (area < 8500):
        # print 'shi tou';
        return 0;
    print
    "width_leng", width_length
    if (width_length < 35):
        # ���ʱ��˵����Ƭ��ƫ�µģ�������Ҫ���²ⶨ��
        a = []
        posi = []
        width = []
        count = 0
        for i in range(result.shape[1]):
            if (result[11 * result.shape[0] / 16][i] == 0 and result[11 * result.shape[0] / 16][i - 1] != 0):
                count += 1
                width.append(0)
                posi.append(i)
            if (result[11 * result.shape[0] / 16][i] == 0):
                width[count - 1] += 1
        """
        print 'the pic width is ',result.shape[1],'\n'
        for i in range(count):
            print 'the ',i,'th',' ','is';
            print 'width ',width[i]
            print 'posi ',posi[i],'\n'
        print count,'\n'
        print 'area is ',area,'\n'
        """
    width_length = 0
    width_jiandao = True
    for i in range(count):
        if width[i] > 45:
            # print 'bu1';
            return 2;
        if width[i] <= 20 or width[i] >= 40:
            width_jiandao = False
        width_length += width[i]
    if width_jiandao == True and count == 2:
        return 1;
    if (area > 14000 or count >= 3):
        # print 'bu2';
        return 2;
    if (width_length < 110):
        # print 'jian dao';
        return 1;
    else:
        # print 'bu3';
        return 2;


"""
print("����ͨ������ͷ����ļ���ʯͷ������Ϸ������y��ʼ\n")
s = raw_input()
capture = cv2.VideoCapture(0)
cv2.namedWindow("camera",1)
start_time = time.time()
print("����5���ʱ����ַŵ������λ��\n")
while(s=='y' or s=='Y'):
    ha,img =capture.read()
    end_time = time.time()
    cv2.rectangle(img,(426,0),(640,250),(170,170,0))
    cv2.putText(img,str(int((5-(end_time- start_time)))), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow("camera",img)

    if(end_time-start_time>5):
        break
    if(cv2.waitKey(30)>=0):
        break
ha,img = capture.read()
capture.release()
cv2.imshow("camera",img)
img = img[0:210,426:640]
cv2.imwrite("wif.jpg",img)
judge()  
cv2.waitKey(0)
print "fuck"
"""


def game():
    fuck = []
    fuck.append("ʯͷ")
    fuck.append("����")
    fuck.append("��")
    capture = cv2.VideoCapture(0)
    cv2.namedWindow("camera", 1)
    start_time = time.time()
    print("����5���ʱ����ַŵ������λ��\n")
    while (1):
        ha, img = capture.read()
        end_time = time.time()
        cv2.rectangle(img, (426, 0), (640, 250), (170, 170, 0))
        cv2.putText(img, str(int((5 - (end_time - start_time)))), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
        cv2.imshow("camera", img)
        if (end_time - start_time > 5):
            break
        if (cv2.waitKey(30) >= 0):
            break
    ha, img = capture.read()
    capture.release()
    cv2.imshow("camera", img)
    img = img[0:210, 426:640]
    cv2.imwrite("wif.jpg", img)
    p1 = judge()
    pc = random.randint(0, 2)
    # print p1,' ',pc,'\n'
    print
    "�������", fuck[p1], " ���Գ�����", fuck[pc], "\n"
    cv2.destroyAllWindows()
    if (p1 == pc):
        print
        "ƽ��\n"
        return 0
    if ((p1 == 0 and pc == 1) or (p1 == 1 and pc == 2) or (p1 == 2 and pc == 0)):
        print
        '��Ӯ��\n'
        return 1
    else:
        print
        '������\n'
        return -1


def main():
    you_win = 0
    pc_win = 0
    print("����ͨ������ͷ����ļ���ʯͷ������Ϸ��������س���ʼ��Ϸ\n")
    s = input()
    while (1):
        print
        "�ȷ�(��ң�����) ", you_win, ":", pc_win, '\n'
        s = input()
        os.system('cls')
        ans = game()
        if (ans == 1):
            you_win += 1
        elif (ans == -1):
            pc_win += 1
        print
        "Ϊ�˼������У��뾡���ܽ���ռ�ݾ����ܴ�Ŀ��"


main()

import scipy.spatial 
# библиотека для косинусного расстояния
import numpy as np
import re

# lines = [line.rstrip('\n') for line in open(r"C:\Users\Lenovo\Desktop\Лабы\ml\sentences.txt")]


# все строки файла записываем в lines
lines = [line.rstrip('\n') for line in open(r"sentences.txt")] 
i = 0
# создаю новый лист, в который потом запишутся строки из lines , разделенные на слова
lines2=[]
# в цикле разделяю каждую строку на слова и записываю их в lines2
# filter нужен для удаления пустых строк ""
for sentence in lines:
    sentence = re.split('[^a-z]', sentence.lower())
    lines2.append(list(filter(None, sentence)))
# мэп который будет номер каждого уникального слова в предложениях
wordsNum = dict()
i=0
for line in lines2:
    for word in line:
        if word not in wordsNum:
            wordsNum[word] = i
            i += 1
#считаем сколько раз слово встречается в предложениях
wordsMatrix=[]

for curSentence in range(0, len(lines2)):
    wordsMatrix.append([0 for x in wordsNum])
    for word in lines2[curSentence]:
        curWord = wordsNum[word]
        wordsMatrix[curSentence][curWord] += 1
wordsMatrix_Np = np.array(wordsMatrix)
# лист для хранения косинусного расстояния между первым предложением и каждым i-тым
cosDists = list()
# в цикле считаем расстояния каждого предложения до самого первого
for i in range(len(lines2)):
    dist = scipy.spatial.distance.cosine(wordsMatrix_Np[0], wordsMatrix_Np[i])
    cosDists.append((i, dist))
#     сортируем
sorted_list = sorted(cosDists, key=lambda tup: tup[1])
# печатаем номера самых "похжих"
print (sorted_list[1][0], sorted_list[2][0])
#   печатаем эти предложения 
print(lines[0])
print(lines[6])
print(lines[4])
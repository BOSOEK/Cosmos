import os
import cv2

count = 1

files = os.listdir('D:\googleDrive\Cosmos\data/')

for file in files:
    img = cv2.imread('D:\googleDrive\Cosmos\data/' + file)
    res = cv2.resize(img, dsize=(500, 350))
    cv2.imwrite('D:\googleDrive\Cosmos\imgs/' + str(count) + '.png', res)
    count += 1
    print(count)
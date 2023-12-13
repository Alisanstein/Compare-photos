import cv2
import os
import random


while True:

    aza = [f for f in os.listdir() if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    lenght = len(aza)

    if lenght == 1:
        break

    a = random.randint(0,lenght-1)
    b = random.randint(0,lenght-1)

    if a == b:
        continue

    else:

        img1 = cv2.imread(aza[a])
        img2 = cv2.imread(aza[b])
        cv2.imshow('1', img1)
        cv2.imshow('2', img2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        choice = int(input('Wich person do you perfer? '))

        if choice == 1:
            os.remove(aza[b])

        elif choice == 2:
            os.remove(aza[a])

    
winner = cv2.imread(aza[0])
cv2.imshow('Winner', winner)

cv2.waitKey(0)
cv2.destroyAllWindows()

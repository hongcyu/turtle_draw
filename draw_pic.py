import cv2
import numpy as np
import turtle

def array_pic(pic):
    image = cv2.imread(pic,0)
    edges = cv2.Canny(image,100,200)
    img_gray = cv2.cvtColor(edges,cv2.COLOR_BAYER_BG2GRAY)
    ret, thresh = cv2.threshold(img_gray,127,255,0)
    # 下面这句是老版本opencv的写法，如果运行报错可以将下句注释，取消下下句的注释
    image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xy = []
    for i in range(0,len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        list_xy = [x,y]
        xy.append(list_xy)
    return xy
    # file = open("array.txt", mode="x")
    # file.writelines(str(contours))
    # file.close()
    # cv2.imshow("1.jpg",image)
    # cv2.waitKey(0)
    
def draw(xy):
    turtle.pensize(2)
    turtle.setup(width=0.6,height=1.0)
    turtle.speed(0)
    for array in xy[::-1]:
        turtle.penup()
        turtle.goto((array[0]/2)-100,-(array[1]/2)+250)
        turtle.pendown()
        turtle.forward(1)
        print(turtle.pos())
        
    turtle.done()


if __name__ == "__main__":
    pic = "image.jpg"
    xy = array_pic(pic)
    draw(xy)

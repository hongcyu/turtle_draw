# turtle_draw
python将图片进行边缘检测和轮廓提取进行turtle绘画
1. 你需要安装opencv，在cmd中输入：**pip3 install opencv-python**
2. 要使用需要将图片放置在和py同一个文件夹下，接着修改
**
if __name__ == "__main__":
    pic = "image.jpg"
    xy = array_pic(pic)
    draw(xy)
 **
中的pic为图片名字。


import numpy as np
import cv2
 
 
def main():
 
    # 1.创建白色背景图片
    d = 200
    img = np.ones((d, d, 3), np.uint8) * 255
 
    # 2.循环随机绘制实心圆
    for i in range(0, 100):
        # 随机中心点
        center_x = np.random.randint(0, high=d)
        center_y = np.random.randint(0, high=d)
 
        # 随机半径与颜色
        radius = np.random.randint(5, high=d/5)
        color = np.random.randint(0, high=256, size=(3, )).tolist()
 
        cv2.circle(img, (center_x, center_y), radius, color, -1)
 
    # 3.显示结果
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    main()
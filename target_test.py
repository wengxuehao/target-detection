#  _*_ coding:UTF-8 _*_

# 导入目标检测类
from imageai.Detection import ObjectDetection
import os
# 确定保存路径
execution_path = os.getcwd()
# 定义目标检测类
detector = ObjectDetection()
# 将这个模型类设置成RetinaNet
detector.setModelTypeAsRetinaNet()
# 用于目标检测的RetinaNet模型文件 resnet50_coco_best_v2.0.1.h5
# 设置检测模型的路径RetinaNet的文件所在路径
detector.setModelPath(os.path.join(execution_path, "target_detection/resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()  # 加载这个目标检测类

# 调用检测函数,获得结果,解析输入图片的路径和输出图片的路径
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "target_detection/1.jpg"),
                                             output_image_path=os.path.join(execution_path, "target_detection/imagenew.jpg"))

for eachObject in detections:
    # 遍历结果,并打印模型检测出的图片中每个目标的类型和概率
    print(eachObject["name"] + " : " + eachObject["percentage_probability"])

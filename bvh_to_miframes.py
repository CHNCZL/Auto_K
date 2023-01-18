import os
import json
body_part = []
MiDict = {}
# 缩放倍数
scale = 1

def read_miframe():
    with open("template.miframes", "r") as file:
        MiFileData = file.read()
    MiDict = json.loads(MiFileData)
    print(MiDict)

def read_bvh():
    with open('test.bvh', encoding='utf-8') as file:
        for line in file:
            # 以空格切分关键词
            dataBlock = line.split()
            # 读取HIERARCHY部分数据
            if dataBlock[0] == "ROOT" or dataBlock[0] == "JOINT":
                body_part.append(dataBlock[1])
            # 读取MOTION部分数据
            if dataBlock[0] == "Frame":
                for line in file:
                    keyframe = line.split()
                    print("------")
                    for i in range(len(body_part)):
                        print(body_part[i], keyframe[6*i: 6*i+6])

if __name__ == "__main__":
    read_bvh()
    read_miframe()    
                    
   


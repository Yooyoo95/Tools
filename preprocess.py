from PIL import Image
import os
from random import Random
import shutil

# 预处理生成样本
def generate_samples():
    img_src = Image.open("1.png")

    rows = img_src.height
    cols = img_src.width

    out_path = "data/data"

    count = 0

    #iterate starting X
    for i in range(0, cols-256, 128):
        #iterate starting Y
        for j in range(0, rows-256, 128):
            img_out = img_src.crop((i, j, i+256, j+256))
            # img_out.save("{}/{:05d}_beijing_S1.png".format(out_path,count))
            img_out.save("{}/{:05d}_{:05d}_changsha.png".format(out_path,i//128,j//128))
            count += 1
            # img_out = img_out.rotate(90)
            # img_out.save("{}/{:05d}.jpg".format(out_path,count))
            # count += 1
            # img_out = img_out.rotate(90)
            # img_out.save("{}/{:05d}.jpg".format(out_path,count))
            # count += 1
            # img_out = img_out.rotate(90)
            # img_out.save("{}/{:05d}.jpg".format(out_path,count))
            # count += 1

# # 分割训练集和测试集
# def split_sets():
#     input_path = "data/raw/"
#
#     train_path = "data/train_labels/"
#     test_path  = "data/test_labels/"
#
#     rand = Random()
#
#     for file in os.listdir(input_path):
#         if file.endswith(".png"):
#             r = rand.random()
#             if r <= .8:
#                 shutil.copyfile(input_path+file, train_path+file)
#             else:
#                 shutil.copyfile(input_path+file, test_path+file)
#
#
# def generate_dirty():
#     input_train_path = "data/train_labels/"
#     input_test_path = "data/test_labels/"
#
#     output_train_path = "data/train/"
#     output_test_path = "data/test/"
#
#     rows, cols = (384,384)
#
#     for file in os.listdir(input_train_path):
#         img = Image.open(input_train_path+file)
#         temp = img.resize((int(rows/2), int(cols/2)), Image.BILINEAR)
#         temp = temp.resize((rows,cols), Image.BILINEAR)
#         temp.save(output_train_path+file)
#
#     for file in os.listdir(input_test_path):
#         img = Image.open(input_test_path+file)
#         temp = img.resize((int(rows/2), int(cols/2)), Image.BICUBIC)
#         temp = temp.resize((rows,cols), Image.BICUBIC)
#         temp.save(output_test_path+file)


generate_samples()
# split_sets()
# generate_dirty()

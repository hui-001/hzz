import os
from ocr import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))
    result, image_framed = ocr(image)
    return result,image_framed


if __name__ == '__main__':
    image_files = glob('./test_images/*.*')
    result_dir = './test_result'
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)
    import os

    # 获取文件路径中的目录部分
    dir_path = os.path.dirname('./test_result\\test_images\\t1.txt')
    # 创建目录，如果目录已经存在则不会重复创建（避免报错）
    os.makedirs(dir_path, exist_ok=True)

    # 再进行文件打开操作
    txt_f = open('./test_result\\test_images\\t1.txt', 'w')
    for image_file in sorted(image_files):
        t = time.time()
        result, image_framed = single_pic_proc(image_file)
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        txt_file = os.path.join(result_dir, image_file.split('/')[-1].split('.')[0]+'.txt')
        print(txt_file)
        txt_f = open(txt_file, 'w')
        Image.fromarray(image_framed).save(output_file)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")
        for key in result:
            print(result[key][1])
            txt_f.write(result[key][1]+'\n')
        txt_f.close()
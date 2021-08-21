## 基本说明
IF-Dataset是首个针对抖音平台短视频中的无关人脸识别的数据集。
数据集包含了视频人脸识别后的人脸图片和有关每个人脸的5个统计特征，提供人脸图片内容特征和人脸统计特征2个方面进行无关人脸识别的可能。

## video文件结构说明
video
-->video0_dir(dir)
------>0(dir)
---------->img0(file)
---------->img1(file)
---------->img2(file)
------>1(dir)
------>2(dir)
-->video1_dir(dir)
-->video2_dir(dir)

## 使用说明
如果想使用IF-Dataset，请将该项目全部文件放在名为dataset的文件夹下，并解压缩test.rar。文件夹中结构如下：

dataset
-->test(dir)
-->readme.md(file)
-->structure.csv(file)

随后，使用pandas等库读取strucure.csv内容，便可以使用该数据集了

If you want to use IF-dataset, you need to place all of the content of the program under a dir called dataset. Then, decompress the test.rar.

The structure of the dir is supposed to be:
dataset
-->test(dir)
-->readme.md
-->structure.csv

After that, you can easilly use the IF-Dataset through accessing to the content of the structure.csv with tools like pandas.


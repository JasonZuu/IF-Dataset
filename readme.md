## 基本说明
IF-Dataset是首个针对抖音平台短视频中的无关人脸识别的数据集。
IF-Dataset中共包含43965张无关人脸图片，89924张有关人脸图片，共133889张图片
IF-Dataset包含了视频人脸识别后的人脸图片和每个人脸的5个统计特征。统计特征描述如下
![avatar](features_description.PNG)

## test文件结构说明
test   
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
从百度云下载test.rar, 下载链接如下：  
链接：https://pan.baidu.com/s/1BUANlG6zIU6lnMTV4GWQLQ   
提取码：td2e 

下载后，在创建dataset文件夹，并在其中解压缩test.rar
随后，将该项目的其余内容放在名为dataset的文件夹下，使文件夹中结构如下：  

dataset  
-->test(dir)  
-->structure.csv(file)  

最后，使用pandas等库读取strucure.csv内容，便可以使用该数据集了

## Basic Description
To our best knowledge, IF-Dataset is the first dataset of irrelevant faces recognition in Chinese short-form video. 
IF-Datast includes 43965 images of irrelevant faces and 89924 images of relevant faces, with 133889 face images in total. 
ID-Dataset contains the face image as well as five statistical features of each face. The statistical features are described as follows:  
![avatar](features_description.PNG)

## Structure of the test directory
test   
-->video0_dir(dir)  
------>0(dir)  
---------->img0(file)  
---------->img1(file)  
---------->img2(file)  
------>1(dir)  
------>2(dir)  
-->video1_dir(dir)  
-->video2_dir(dir)

## How to use
Firstly, download test.rar form the Baidu Cloud.  
Download URL：https://pan.baidu.com/s/1BUANlG6zIU6lnMTV4GWQLQ   
Download Code：td2e 

Then, create a directory called dataset and decompressed test.rar in the directory. Place the structure.csv file in the dataset directory as well. The directory structure is supposed to be like this:
dataset  
-->test(dir)
-->structure.csv(file) 

Finally, you can use the IF-Dataset by accessing the structure.csv.
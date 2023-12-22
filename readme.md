# IF-Dataset
IF-Dataset refers to "Irrelevant Face Dataset".

This is the dataset used in the paper <a  href ="https://www.sciencedirect.com/science/article/abs/pii/S0925231222008013">Recognizing irrelevant faces in short-form videos based on feature fusion and active learning</a>

The codes for the MMFNet is available at <a href="https://github.com/JasonZuu/MMFNet-2022"> MMFNet-2022 </a>

## Basic Information
To our best knowledge, IF-Dataset is the first dataset for irrelevant faces recognition in Chinese short-form video, which includes 43965 images of irrelevant faces and 89924 images of relevant faces, with 133889 face images in total. 

### Description of features
IF-Dataset contains the face image as well as five statistical features of each face. The statistical features are described as follows:  
![features_description](imgs/features_description.png)

### Description of files
IF_train.csv: Containing features and image access of the IF-Dataset's training set.</br>
IF_test.csv: Containing features and image access of the IF-Dataset's testing set.</br>
active100.csv: Containing data used for active learning.</br>
tiktok.csv: Containing data used for evaluating the generalization performance of the model.</br>

### Structure of the project
dataset</br>
-->IF-Dataset</br>
---->video0_dir(dir)</br> 
------>0(dir)</br>
--------->img0(file)</br>
--------->img1(file)</br>
--------->img2(file)</br>
------>1(dir)</br> 
------>2(dir)</br> 
---->video1_dir(dir)</br>
-->tiktok(dir)</br>
-->active_100(dir)</br>

## Samples of data
### Relevant faces and irrelevant faces
![frames of short-form video](imgs/frames.png)  
In the above frames, relevant faces are those surrounded by green boxes while irrelevant faces are those surrounded by red boxes.  

In the IF-Dataset, faces are extracted from those frames of short-form videos and labeled according to our rules.

### Samples
+ Samples of relevant faces
![relevant faces](imgs/relevant_sample.jpg)

+ Samples of irrelevant faces
![irrelevant faces](imgs/irrelevant_sample.jpg)

Note that all samples are resized to the [224, 224] in order to output visual results. As most of the irrelevant samples are smaller than this shape, their visual results are lower in quality than the relevant.


## How to use
### Access to data
IF-Dataset can be downloaded from the Baidu Cloud and the Google Could.

Download from Baidu Cloud:  
URL: https://pan.baidu.com/s/19lwR19v2cafyTsVu2wTPmg     
Password: i4in  

Download from Google Cloud:  
https://drive.google.com/file/d/14MjWdUUc79jyD_iRVQV5RMkDpZbLVfMF/view?usp=sharing

### Guidences for use
1. Download the dataset.zip file.
2. Decompress the dataset.zip and move the dataset directory into this project. Make surethe directory structure looks like this:
dataset(dir)</br>
-->IF_Dataset(dir)</br>
-->active_100(dir)</br>
-->tiktok(dir)</br>
IF_train.csv(file)</br>
IF_test.csv(file)</br>
tiktok.csv(file)</br>
active100.csv(file)</br>

3. Use the IF-Dataset through reading csv files.

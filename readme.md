# IF-Dataset
IF-Dataset refers to "Irrelevant Face Dataset".

## Basic Information
To our best knowledge, IF-Dataset is the first dataset for irrelevant faces recognition in Chinese short-form video, which includes 43965 images of irrelevant faces and 89924 images of relevant faces, with 133889 face images in total. 

### Desceiption of features
IF-Dataset contains the face image as well as five statistical features of each face. The statistical features are described as follows:  
![features_description](imgs/features_description.png)

### Structure of the project
IF-Dataset</br>
-->video0_dir(dir)</br> 
------>0(dir)</br>
---------->img0(file)</br>
---------->img1(file)</br>
---------->img2(file)</br>
------>1(dir)</br> 
------>2(dir)</br> 
-->video1_dir(dir)</br>
-->video2_dir(dir)</br>

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
URL: https://pan.baidu.com/s/1CCUryYf5pD1twUKHdhNNXw  
Code: 2g2q 

Download from Google Cloud:  
https://drive.google.com/file/d/1OYzIk4xeireMiDUyZXdIeZV2rRsbvC2F/view?usp=sharing

### Guidences for use
1. Download the dataset.zip file.
2. Decompress the dataset.zip and move the dataset directory into this project. Make surethe directory structure looks like this:
dataset(dir)</br>
-->IF_Dataset(dir)</br>
-->IF_train.csv(file)</br>
-->IF_test.csv(file)</br>
1. Use the IF-Dataset through reading csv files.
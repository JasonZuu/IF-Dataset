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

### samples of data


## How to use
### Access to data
IF-Dataset can be downloaded from the Baidu Cloud and the Google Could.

Download from Baidu Cloud:  
URL: https://pan.baidu.com/s/1CCUryYf5pD1twUKHdhNNXw  
Code: 2g2q 

Download from Google Cloud: 

### Guidences for use
1. Download the dataset.zip file.
2. Decompress the dataset.zip and move the dataset directory into this project. Make surethe directory structure looks like this:
dataset(dir)</br>
-->IF_Dataset(dir)</br>
-->IF_train.csv(file)</br>
-->IF_test.csv(file)</br>
3. Use the IF-Dataset through reading those csv files.
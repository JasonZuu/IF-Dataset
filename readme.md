## Basic Description
To our best knowledge, IF-Dataset is the first dataset of irrelevant faces recognition in Chinese short-form video. 
IF-Datast includes 43965 images of irrelevant faces and 89924 images of relevant faces, with 133889 face images in total. 
ID-Dataset contains the face image as well as five statistical features of each face. The statistical features are described as follows:  
![avatar](features_description.PNG)

## Structure of the test directory
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
## How to use
Firstly, download dataset.zip form Baidu Cloud.  
URL: https://pan.baidu.com/s/1CCUryYf5pD1twUKHdhNNXw 
Code: 2g2q

Then, decompress the dataset.zip and move the IF_train.csv and IF_test files into the dataset directory. The directory structure is supposed to be like this:

dataset(dir)</br>
-->IF_Dataset(dir)</br>
-->IF_train.csv(file)</br>
-->IF_test.csv(file)</br>

Finally, you can use the IF-Dataset by accessing the structure.csv.
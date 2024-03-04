**PAXRAY: A Projected dataset for the segmentation of Anatomical structures in X-RAY data** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the medical industry. 

The dataset consists of 852 images with 161742 labeled objects belonging to 165 different classes including *lung_overall*, *lung_left_lobeupper*, *lung_left_lobelower*, and other: *lung_right_lobeupper*, *lung_right_lobemiddle*, *lung_right_lobelower*, *mediastinum_overall*, *mediastinum_lower*, *mediastinum_upper*, *mediastinum_anterior*, *mediastinum_middle*, *mediastinum_posterior*, *heart*, *airways*, *esophagus*, *aorta*, *aorta_arch*, *bones*, *spine*, *t1*, *t2*, *t3*, *t4*, *t5*, *t6*, *t7*, *t8*, *t9*, and 137 more.

Images in the Paxray dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 3 splits in the dataset: *train* (598 images), *test* (180 images), and *val* (74 images). Additionally, every image has following tags: ***im_id*** and ***view*** (frontal or lateral). Explore it in supervisely labeling tool. The dataset was released in 2022 by the GE joint research group.

Here is a visualized example for randomly selected sample classes:

[Dataset classes](https://github.com/dataset-ninja/paxray/raw/main/visualizations/classes_preview.webm)

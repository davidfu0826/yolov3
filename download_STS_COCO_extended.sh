#!/bin/bash
# Download STS_COCO dataset with 33 classes
gsutil cp gs://swedish-traffic-sign-europe/STS_COCO_dataset_v1_part1.zip .
unzip -q STS_COCO_dataset_v1_part1.zip 
rm STS_COCO_dataset_v1_part1.zip 

gsutil cp gs://swedish-traffic-sign-europe/STS_COCO_dataset_v1_part2.zip .
unzip -q STS_COCO_dataset_v1_part2.zip 
rm STS_COCO_dataset_v1_part2.zip 

gsutil cp gs://swedish-traffic-sign-europe/STS_COCO_dataset_v1_part3.zip .
unzip -q STS_COCO_dataset_v1_part3.zip 
rm STS_COCO_dataset_v1_part3.zip 

gsutil cp gs://swedish-traffic-sign-europe/STS_COCO_dataset_v1_part4.zip .
unzip -q STS_COCO_dataset_v1_part4.zip 
rm STS_COCO_dataset_v1_part4.zip 

gsutil cp gs://swedish-traffic-sign-europe/STS_COCO_dataset_v1_part5_extended.zip .
unzip -q STS_COCO_dataset_v1_part5_extended.zip 
rm STS_COCO_dataset_v1_part5_extended.zip 
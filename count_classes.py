import argparse
import glob
import os
from typing import List, Tuple

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def two_stacked_horizontal_histogram(
                        first_arr: List[str], second_arr: List[str],
                        title: str = "Results",
                        xlabel: str = "Frequency",
                        ylabel: str = "Classes",
                        legend: Tuple[str,str] = ('Detected', 'Missed')) -> None:
    """Plots two stacked histograms given two arrays
    """
    s1=pd.Series(first_arr, name="original")
    s2=pd.Series(second_arr, name="mirrored")

    df = pd.concat([s1, s2])

    plt.figure(figsize=(15, 15))

    total_counts = df.value_counts() 
    original_counts = s1.value_counts().reindex(total_counts.index)

    #Plot 1 - background - "total" (top) series
    ax = sns.barplot(y = total_counts.index, x = total_counts, color = "red", alpha=0.5)

    # Add values on top of the bar
    for p in ax.patches:
        x = p.get_x() + p.get_width() + 0.9
        y = p.get_y() + p.get_height()/2 + 0.2
        ax.annotate(int(p.get_width()), (x, y))

    #Plot 2 - overlay - "bottom" series
    bottom_plot = sns.barplot(y = total_counts.index, x = original_counts, color = "#0000F3", alpha=0.5)

    bottom_plot.axes.set_title(title, fontsize=30)
    bottom_plot.set_xlabel(xlabel, fontsize=20)
    bottom_plot.set_ylabel(ylabel, fontsize=20)

    topbar = plt.Rectangle((0,0),1,1, fc="#ff7777", edgecolor = 'none')
    bottombar = plt.Rectangle((0,0),1,1, fc='#965596',  edgecolor = 'none')
    l = plt.legend([bottombar, topbar], legend, loc='center right', ncol = 2, prop={'size':16})
    l.draw_frame(False)

    plt.xlabel('Frequency')
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example usage: python count_classes.py --annot darknet_dataset\labels\ ")
    parser.add_argument('--true-positives', type=str, default='true_positives.txt', help='path to output file true_positives.txt (created from detect.py --save-txt)')  
    parser.add_argument('--annot', type=str, help='path to annotation files directory (Darknet format)', required=True)
    parser.add_argument('--names', type=str, default='data/traffic_sign.names', help='*.names path')
    opt = parser.parse_args()
    
    path_tp = opt.true_positives
    names = opt.names
    #txt_files = glob.glob(path_to_folder + "/*.txt")
    #print(txt_files)
    
    idx_to_name = dict()
    with open(names) as f:
        for i, line in enumerate(f.readlines()):
            idx_to_name[i] = line.replace("\n", "") # Class
    
    #predictions = list()
    with open(path_tp) as f:
        lines = f.readlines()
        tps = [int(float(line.replace("\n", ""))) for line in lines]
        predictions = [idx_to_name[tp] for tp in tps]
    #for txt_file in txt_files:
    #    with open(txt_file) as f:
    #        for line in f.readlines():
    #            class_idx = int(line.split(" ")[4])
    #            class_name = idx_to_name[class_idx]
    #            predictions.append(class_name)
    #print(predictions)
    
    annotation_dir = opt.annot
    label_list = list()
    for annot_txt in glob.glob(annotation_dir + os.sep + "*.txt"):
        with open(annot_txt) as f:
            labels = [line.split(" ")[0] for line in f.readlines()]
            for label_id in labels:
                label_list.append(idx_to_name[int(label_id)])
    #label_list += predictions
    #false_positives = list()
    for pred in predictions:
        #try:
        label_list.remove(pred)
        #except:
        #    predictions.remove(pred)
        #    false_positives.append(pred)
    
    
    two_stacked_horizontal_histogram(predictions, label_list)      
    #plt.figure()
    #plt.title("Distribution of predictions")  
    #sns.countplot(y=label_list)
    #sns.countplot(y=predictions)
    #plt.show()

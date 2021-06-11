import os
import re
import shutil

pattern  = re.compile(r"\d{4}")
f = open("C:\\Users\\arjun.harish\\PycharmProjects\\comparator\\missing_files\\bb_coords.txt","r")
text = f.read()
filenames = pattern.findall(text)

# path1 = "C:\\Users\\arjun.harish\\PycharmProjects\\comparator\\switch_on_task\\dataset\\dataset_processed\\train_img2"
# for file in os.listdir(path1):
#     if file.split(".")[0] in filenames:
#         target = "C:\\Users\\arjun.harish\\PycharmProjects" \
#                  "\\comparator\\switch_on_task\\dataset\\dataset_final\\train_img2\\" + file
#         original = os.path.join(path1,file)
#         shutil.copyfile(original, target)

path1 = "C:\\Users\\arjun.harish\\PycharmProjects\\comparator\\missing_files\\groundtruth"
for file in os.listdir(path1):
    if file.split("_")[0] in filenames:
        target = "C:\\Users\\arjun.harish\\PycharmProjects" \
                 "\\comparator\\switch_on_task\\dataset\\dataset_final\\ground_truth\\" + file
        original = os.path.join(path1,file)
        shutil.copyfile(original, target)

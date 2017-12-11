
import os

root_dir = os.getcwd()
label_list_dir = os.path.join(root_dir, "vkitti_1.3.1_scenegt_binary/")
rgb_list_dir = os.path.join(root_dir, "vkitti_1.3.1_rgb/")

seqs = ["0001", "0002", "0006", "0018"]

variations = "morning"

for seq in seqs:
    label_var_dir = os.path.join(label_list_dir, seq, "morning")
    rgb_var_dir = os.path.join(rgb_list_dir, seq, "morning")
    
    out_txt_file = "all.txt"
    fid = open(out_txt_file, 'a')

    label_img_list = os.listdir(label_var_dir)
    label_img_list.sort()

    rgb_img_list = os.listdir(rgb_var_dir)
    rgb_img_list.sort()

    for i in range(len(label_img_list)):
        label_img_path = os.path.join(label_var_dir, label_img_list[i].strip("\n"))
        rgb_img_path = os.path.join(rgb_var_dir, rgb_img_list[i].strip("\n"))

        fid.write(rgb_img_path + " " + label_img_path+"\n")

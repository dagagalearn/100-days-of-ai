# Challenge from DeepSeek!
dataset_info = ("ImageNet",2012,150.0)
file_list = ["train_images.zip","val_images.zip","labels.csv"]
print("Dataset Info:", dataset_info)
print("File List:",file_list)
file_list.append("normalization_params.json")
file_list.remove("val_images.zip")
file_list.insert(0,"config.yaml")
if "labels.csv" in file_list:
    print("Yes labels.csv is in the files!")
else:
    print("Nah!")
print(file_list)
name, version, size_gb = dataset_info
print(f"Dataset {name} (v{version}) is {size_gb} GB currently has {len(file_list)} files ready.")

def check_file_ready(file_list, filename):
    if filename in file_list:
        return True,len(file_list)
    else:
        return False
print(check_file_ready(file_list,"config.yaml"))

import os

output_name = "README.md"
black_list = [".git", ".DS_Store", "index.py", output_name]
format_order = ["#[words](link)", "- [words](link)"]

def prepare_file_list(dir, black_list, format_order, acc_result):

    for subdir in os.listdir(dir):

        if subdir not in black_list:
            acc_result += format_order[0].replace("words",subdir).replace("link", "{}/{}".format(dir, subdir))+"\n\n"
            
            try:
                acc_result = prepare_file_list(subdir, black_list, format_order[1:], acc_result)
            except:
                pass
    
    return acc_result

with open(output_name, "w") as f:
    f.write(prepare_file_list(".", black_list, format_order, ""))
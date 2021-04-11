import json

i_filename = "./list.py"
o_filename = "./tmp/word_count";
with open(i_filename) as file:
    content = file.readlines()
    with open(o_filename, 'w') as o_file:
        result = {
            i_filename: len(content)
        }
        json.dump(result, o_file)

with open(o_filename) as file:
    pre_result = json.load(file)
    print(pre_result)

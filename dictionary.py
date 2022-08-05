word_dict={}
id = 1

# data.txtからデータを1行ずつ取得して出力
with open("dictionary_data.txt") as file:
    for data in file:
        word_dict[id] = data.rstrip("\n")
        id += 1
file.close()

for id in word_dict:
    print(str(id) + ": " + word_dict[id])

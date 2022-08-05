import sys

def hasWordID(arg_list):
    """
    単語IDが存在するかを調べる

    Parameters
    ----------
    args : list
        sys.argvで読み込むlist
    
    Returns
    -------
    bool
        単語IDが存在するときTure
    """
    if len(arg_list) >= 4:
        return True
    else :
        return False

# definition and input        
arg_list  = sys.argv #コマンドライン引数のリスト [user_name  data_file   *ID(任意)]
word_dict = {}
id = 1

# file input to word_dict
# dictionary_data.txtからデータを1行ずつ取得
user_name = arg_list[1]
file_name = arg_list[2]
with open(file_name) as file:
    for data in file:
        word_dict[id] = data.rstrip("\n")
        id += 1
file.close()

# output
print("ユーザー名: " + user_name)
if hasWordID(arg_list):
    arg = int(arg_list[3]) #指定されたID
    print(str(arg) + ": " + word_dict[arg])
else :
    for id in word_dict:
        print(str(id) + ": " + word_dict[id])

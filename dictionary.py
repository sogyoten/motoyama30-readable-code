import sys

def hasArgument(arg_list):
    """
    引数が存在するかを調べる

    Parameters
    ----------
    args : list
        sys.argvで読み込むlist
    
    Returns
    -------
    bool
        引数が存在するときTure
    """
    if len(arg_list) >= 2:
        return True
    else :
        return False

# definition and input        
arg_list = sys.argv #コマンドライン引数のリスト
word_dict = {}
id = 1

# file input to word_dict
# dictionary_data.txtからデータを1行ずつ取得
with open("dictionary_data.txt") as file:
    for data in file:
        word_dict[id] = data.rstrip("\n")
        id += 1
file.close()

# output
if hasArgument(arg_list):
    arg = int(arg_list[1]) #指定されたID
    print(str(arg) + ": " + word_dict[arg])
else :
    for id in word_dict:
        print(str(id) + ": " + word_dict[id])

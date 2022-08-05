# data.txtからデータを1行ずつ取得して出力
with open("data.txt") as file:
    for line in file:
        print(line)
    file.close()

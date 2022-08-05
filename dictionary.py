# data.txtからデータを1行ずつ取得して出力
with open("data.txt") as file:
    for data in file:
        print(data.rstrip("\n"))
file.close()

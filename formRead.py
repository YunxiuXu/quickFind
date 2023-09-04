import pandas as pd

# 使用read_excel函数读取Excel文件
df = pd.read_excel('./forms/method.xlsx', engine='openpyxl')  # 如果你的文件是.xlsx格式
# 或
# df = pd.read_excel('你的文件路径.xls', engine='xlrd')  # 如果你的文件是.xls格式




def preprocess_string(s):
    # 移除所有空格
    s = s.replace(' ', '')
    # 将中文括号替换为英文括号
    s = s.replace('（', '(').replace('）', ')')
    return s

# 给定要搜索的字符串并进行预处理
search_string = "你要搜索的字符串"


# 遍历每个单元格并搜索字符串
for row in df.iterrows():
    for col_name, cell_value in row[1].items():
        if isinstance(cell_value, str):
            cell_value_processed = preprocess_string(cell_value)
            if search_string in cell_value_processed:
                print(f"在行 {row[0] + 1}，列 {col_name} 找到匹配字符串: {cell_value}")


def searchByString(input):
    input = preprocess_string(input)

    # 遍历每个单元格并搜索字符串
    for row in df.iterrows():
        for col_name, cell_value in row[1].items():
            if isinstance(cell_value, str):
                cell_value_processed = preprocess_string(cell_value)
                if input in cell_value_processed:
                    #print(f"在行 {row[0] + 1}，列 {col_name} 找到匹配字符串: {cell_value}")
                    return cell_value
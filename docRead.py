import pandas as pd

# 使用read_excel函数读取Excel文件
df = pd.read_excel('./forms/instrumentExcel.xlsx', engine='openpyxl')  # 如果你的文件是.xlsx格式


def searchDoc(input):
    # 在 "列名" 列中搜索 "字符串内容"
    result = df[df['管理编号'].astype(str).str.contains(input)]
    if(result.empty == False):
        print(result)
        instrumet_name = result["仪器设备名称"].iloc[0]
        type = result["型号/规格"].iloc[0]
        No = result["管理编号"].iloc[0]

        result = str(instrumet_name + "\n" + type + "\n" + No)
        return result
    else:
        return None
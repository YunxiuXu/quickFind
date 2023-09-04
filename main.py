import tkinter as tk
import formRead
import docRead


def on_button_click():
    """处理按钮点击事件"""
    content = entry.get()
    output = formRead.searchByString(content)
    if(output == None):
        content = ""
        output = "无结果"
    output_label.config(text=content + " " + output )

    #entry.delete(0, tk.END)  # 清空当前文本内容
    #entry.insert(0, output)  # 插入新的文本内容，转为大写

    entry2.delete(0, tk.END)  # 清空当前文本内容
    entry2.insert(0, output)  # 插入新的文本内容，转为大写

    print(output)


def on_button_click_instrument():
    """处理按钮点击事件"""
    content = entryInstrumentInput.get()
    output = docRead.searchDoc(content)
    if(output == None):
        content = ""
        output = "无结果"
    output_labelInstrument.config(text=content + " " + output )


    entryInstrumentOutput.delete(0, tk.END)  # 清空当前文本内容
    entryInstrumentOutput.insert(0, output)  # 插入新的文本内容，转为大写

    print(output)

# 创建根窗口
root = tk.Tk()
root.title("悬浮窗口")
# 使窗口始终保持在前面
root.attributes("-topmost", True)
# 设置窗口大小和位置
root.geometry("200x400+100+100")

# 创建一个输入框并将其放置在窗口中
entry = tk.Entry(root)
entry.pack(pady=10)

# 创建一个按钮并将其放置在窗口中，绑定事件函数
button = tk.Button(root, text="search方法", command=on_button_click)
button.pack(pady=10)


entry2 = tk.Entry(root)
entry2.pack(pady=10)


# 创建一个标签来显示打印的内容
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

#############

entryInstrumentInput = tk.Entry(root)
entryInstrumentInput.pack(pady=10)

# 创建一个按钮并将其放置在窗口中，绑定事件函数
button2 = tk.Button(root, text="search设备", command=on_button_click_instrument)
button2.pack(pady=10)


entryInstrumentOutput = tk.Entry(root)
entryInstrumentOutput.pack(pady=10)

# 创建一个标签来显示打印的内容
output_labelInstrument = tk.Label(root, text="")
output_labelInstrument.pack(pady=10)

# 进入主循环
root.mainloop()

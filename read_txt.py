# 指定文件路径
file_path = './documents/mark_informs.txt'
 

# 用于存储解析后的数据（这里只是打印出来，但你可以根据需要修改）
parsed_data = []

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # 读取所有行到列表中
    i = 0
    while i < len(lines):
        # 检查当前行是否以'text:'开头
        if lines[i].startswith('text:'):
            # 提取text的值
            text = lines[i].split(':')[1].strip()
            # 读取下一行并提取x的值
            x = int(lines[i+1].split(':')[1].strip())
            # 读取再下一行并提取y的值
            y = int(lines[i+2].split(':')[1].strip())
            # 打印或存储解析后的数据
            print(f'text: {text}, x: {x}, y: {y}')
            # 如果需要，可以将它们添加到列表中
            parsed_data.append({'text': text,'x': x, 'y': y})
            # 移动到下一块数据的开始
            i += 3  # 跳过当前块的三行
        else:
            # 如果当前行不以'text:'开头，可能是文件格式有误或空行，我们简单地跳过它
            i += 1
            
print(len(parsed_data))
print(parsed_data[0]['text'])
# 如果你将数据存储在了parsed_data列表中，现在你可以使用它
# 例如，打印所有存储的数据：
# for item in parsed_data:
#     print(item)
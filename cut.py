import os
import sys

def split_markdown_file(file_path):
    # 检查文件路径是否存在
    if not os.path.exists(file_path):
        print("File does not exist: " + file_path)
        return

    # 读取原Markdown文件的内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 创建一个与原文件同名的文件夹
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    dir_path = os.path.join(os.path.dirname(file_path), base_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # 初始化
    current_file = None
    current_title = None
    title_count = 0  # 新增计数器

    for line in lines:
        # 检测一级标题
        if line.startswith('# '):
            if current_file:
                current_file.close()
            title_count += 1  # 更新计数器
            title_name = line[2:].strip().replace(' ', '_').replace('/', '_')
            file_name = f"{title_count:02d}_{title_name}.md"  # 使用计数器作为文件名的前缀
            current_file = open(os.path.join(dir_path, file_name), 'w', encoding='utf-8')
            print('- '+title_name+': '+file_path[:-3]+'/'+file_name)
        if current_file:
            current_file.write(line)

    # 关闭最后一个文件
    if current_file:
        current_file.close()

if __name__ == '__main__': 
    file_path = '算法/深度广度优先搜索.md'
    split_markdown_file(file_path)
#scp -r site/* ubuntu@43.143.162.24:/home/ubuntu/web
import csv
import random

def split_csv(input_file, output_file1, output_file2, ratio):
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # 读取表头
        data = list(reader)  # 读取数据

    random.shuffle(data)  # 随机打乱数据

    split_index = int(len(data) * ratio)  # 计算分割索引

    data1 = data[:split_index]  # 第一个文件的数据
    data2 = data[split_index:]  # 第二个文件的数据

    with open(output_file1, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # 写入表头
        writer.writerows(data1)  # 写入第一个文件的数据

    with open(output_file2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # 写入表头
        writer.writerows(data2)  # 写入第二个文件的数据

# 使用示例
input_file = 'PEDV_mix_DL_and_inactive_2_zaijiayidui_del.csv'  # 输入文件名
output_file1 = 'PEDV_mix_DL_and_inactive_2_zaijiayidui_del_train_4.csv'  # 第一个输出文件名
output_file2 = 'PEDV_mix_DL_and_inactive_2_zaijiayidui_del_test_4.csv'  # 第二个输出文件名
ratio = 0.9  # 分割比例

split_csv(input_file, output_file1, output_file2, ratio)

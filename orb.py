#!/usr/bin/env python
# -*- coding: utf-8 -*-
def read_and_calculate(input_file_name, output_file_name):
    with open(input_file_name) as f:
        f_lines = f.readlines()
        flag = True
        temp = '0'
        file = open(output_file_name, 'w+')
        for f_line in f_lines:
            f_line_temp = f_line.strip().split(" ")
            if flag:
                # 存储第一个
                temp = float(f_line_temp[0])
                f_line_temp[0] = '0'
                flag = False
            else:
                f_line_temp[0] = str(float(f_line_temp[0]) - float(temp))
            file.write("{}\n".format(" ".join(f_line_temp)))
        file.flush()




if __name__ == '__main__':
    input_file_name = '/home/yangtx/guji/Trajectory.txt'
    output_file_name = '/home/yangtx/guji/test3/first.txt'
    read_and_calculate(input_file_name, output_file_name)

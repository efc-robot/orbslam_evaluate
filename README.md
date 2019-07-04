#运行脚本文件，并把结果输出到test3文件夹里


bash test.sh test3


#first.txt是optitrack数据坐标,second.txt是orbslam的数据坐标

脚本里offset可设为0
max_difference为两个数据集时间戳匹配的最大差值（这里的0.0042偏小）
first_result.txt和second_result.txt为二者根据匹配时间戳出来的数据集

#!/bin/bash
PWD=$1
FIRSTLINE=$(sed -n 1p ./$PWD/first.txt)
OFFSETVALUE=${FIRSTLINE%% *}
python associate.py --offset $OFFSETVALUE  --first --max_difference 0.0042 ./$PWD/first.txt ./$PWD/second.txt > ./$PWD/first_result.txt
python associate.py --offset $OFFSETVALUE --max_difference 0.0042 ./$PWD/first.txt ./$PWD/second.txt > ./$PWD/second_result.txt
python evaluate_ate.py --scale 0.8 --plot ./$PWD/0.png  ./$PWD/second.txt ./$PWD/first.txt
python evaluate_ate.py --scale 0.8 --plot ./$PWD/1.png  ./$PWD/second_result.txt ./$PWD/first_result.txt

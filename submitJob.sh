#!/bin/bash

# 生成任务列表
for i in {1..500}; do 
    echo "modelELN2p1hpNo1${i}.C"; 
done > tasks.txt

# 并行执行任务
cat tasks.txt | parallel -j14 --timeout 600 root -l -b -q {} >> output.txt 2>&1

# cat tasks.txt | parallel -j14 --timeout 600 root -l -b -q {} >> output.txt 2>/dev/null


# 等待所有任务完成
wait

# 处理输出部分, 使用awk处理output.txt，寻找fchisq并检查其值

awk '
  /fchisq/ && $3 < 60 {
    print prev; 
    print $0; 
    getline; 
    print;
  } 
  {prev = $0}
' output.txt > GoodResults.txt
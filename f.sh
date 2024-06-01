#!/bin/bash  
  
# 检查参数数量  
if [ "$#" -ne 1 ]; then  
    echo "Usage: $0 <json_string>"  
    exit 1  
fi  
  
# 调用 Python 脚本处理 JSON 数据  
python 1.py "$1"
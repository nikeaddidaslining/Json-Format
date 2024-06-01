import json  
import sys  
  
# 从命令行参数读取 JSON 数据  
if len(sys.argv) < 2:  
    print("Usage: python process_json.py <json_string>")  
    sys.exit(1)  
  
json_str = sys.argv[1]  
  
try:  
    # 解析 JSON 数据  
    data = json.loads(json_str)  
    # 打印格式化后的 JSON 数据  
    print(json.dumps(data, indent=5, ensure_ascii=False))  
except json.JSONDecodeError as e:  
    print(f"JSON 解析错误: {e}")
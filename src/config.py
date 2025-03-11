import json
import os

def load_config():
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建配置文件的相对路径
    config_path = os.path.join(current_dir, 'conf', 'config.json')

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)
        return config
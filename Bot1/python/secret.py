import os
import json

def alter_config(path):
    with open(path,'r', encoding='utf-8') as f:
        configs = json.load(f)
    configs["token"] = os.environ["NjI1NzQ4NzM3NTgyNDMyMjk3.XYkD7A.dW_a04Hp8UNXLANbr4LxCH88oOo"]
    with open('config.json','w') as f:
        f.write(json.dumps(configs,indent=3))

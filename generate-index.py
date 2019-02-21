# -*- coding: utf-8 -*-
import os
import json
import logging

TEMPLATE_ROOT = "templates"
TEMPLATE_INDEX = os.path.join(TEMPLATE_ROOT, "index.json")

template_list = []

dirs = os.listdir(TEMPLATE_ROOT)
for template_name in dirs:
    template_dir = os.path.join(TEMPLATE_ROOT, template_name)
    template_config = os.path.join(template_dir, "config.json")
    if (os.path.isdir(template_dir) and os.path.isfile(template_config)):
        template_list.append(template_name)
        print(template_name)

index_obj = {"default": template_list[0], "templates": template_list}

with open(TEMPLATE_INDEX, "r") as f:
    try:
        index_obj["default"] = json.loads(f.read(), encoding='utf-8')["default"]
    except Exception:
        logging.warn("default is missing.")
print(index_obj)

with open(TEMPLATE_INDEX, "w") as f:
    json.dump(index_obj, f, ensure_ascii=False, sort_keys=True, indent=4);

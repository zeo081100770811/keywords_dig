#!/bin/bash

# 设置Python虚拟环境路径（根据实际情况修改）
VENV_PATH="/Users/zeo/venv"

# 激活虚拟环境
source $VENV_PATH/bin/activate

# 切换到脚本所在目录
cd "$(dirname "$0")"

# 运行Python脚本
python keywords_dig_scheduler.py

# 退出虚拟环境
deactivate

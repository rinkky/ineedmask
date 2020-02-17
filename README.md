循环检测京东自营口罩，并自动下单

## 环境

- Windows/Linux/Mac OS
- python3
- chrome浏览器
- chromedriver
- 安装依赖 `pip install -r requirements.txt`

## 用法

### 检测并自动下单

运行`python3 run.py`.

### 仅检测，不自动下单（速度更快）

运行`python3 run.py noorder`. (需配合提醒功能)

### 提醒功能

如需提醒，请在`alert/__init__.py`中自行添加提醒代码

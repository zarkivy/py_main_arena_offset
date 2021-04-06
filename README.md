# Get main_arena offset of a given libc with python 

##

## 简介

一键获取 libc 的 `main_arena` 偏移量

python 版本方便集成于 exploit 中

感谢 m4x 学长：[shell版](https://github.com/bash-c/main_arena_offset)

##

## 安装

```sh
git clone https://github.com/IZAY01/py_main_arena_offset
cd py_main_arena_offset
sudo python3 setup.py develop
```
依赖于 objdump，请确保你的 Linux 中已安装 binutils 包

## 

## 示例

```python
from pymao import *

libc = "./libc-2.27.so"
main_arena_offset = gmao( libc )
# or main_arena_offset = get_main_arena_offset( libc ) 
```


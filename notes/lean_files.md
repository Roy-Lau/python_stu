# python 文件处理

### 文件打开方法

> file = open(name[,mode[buf]])

- `name`: 文件路径
- `mode`: 打开方式

	| mode 		| 说明 		| 注意 |
	|-----------|-----------|------|
	|`'r'`		|只读方式打开| 文件必须存在
	|`'w'`		|只写方式打开| 文件不存在则创建文件，文件存在则清空文件内容
	|`'a'`		|追加方式打开| 文件不存在则创建文件
	|`'r+/'w+'`	|读写方式打开|
	|`'a+'`		|追加和读写方式打开|
	|`'rb','wb','ab','rb+','wb+','ab+'`| 二进制方式打开 |


- `buf`: 缓冲区`buffering`大小

### 文件读取方式

- `file.read([size])`: 读取文件(_读取`[size]`个字节，默认读取全部_)
- `file.readline([size])`: 读取一行
- `file.readlines([size])`: 读取完文件，返回每一行所组成的列表
- **`iter(file)`:** 使用迭代器读取文件


### 文件写入方式

- `file.write(str)`: 将字符串写入文件
- `file.writelines(sequence_of_strings)`: 写多行到文件,参数为可迭代的对象(`sequence_of_strings`:字符串組成的列表)

### 文件指针操作

> `file.seek(offset[,whence])` : 移动文件指针

- `offset` : 偏移量，可为负数
- `whence` : 偏移相对位置

### 文件指针定位方式

- `os.SEEK_SET` : 相对文件起始位置
- `os.SEEK_CUR` : 相对文件当前位置
- `os.SEEK_END` : 相对文件结尾位置

### 文件属性

- `file.fileno()` : 文件描述符
- `file.mode` : 文件打开权限
- `file.encoding` : 文件编码格式
- `file.closed` : 文件是否关闭

### 标准文件

- `sys.stdin` : 文件标准输入
- `sys.stdout` : 文件标准输出
- `sys.stderr` : 文件标准错误

### 使用os模块打开文件

> `os.open(filename,flag,[,mode])` : 打开文件

`flag`: 打开方式

  - `os.O_CREAT` : 创建文件
  - `os.O_RDONLY` : 只读方式打开
  - `os.O_WRONLY` : 只写方式打开
  - `os.O_RDWR` : 读写方式打开

> `os.read(fd,buffersize)` : 读取文件

> `os.write(fd,string)` : 写入文件

> `os.lseek(fd,pos,how)` : 文件指针操作

> `os.close(fd)` : 关闭文件


### `os`模块方法介绍

| `os` 方法 	| 说明
|-----------|------
| `access(path,mode)` | 判断该文件权限：`F_OK`存在，权限:`R_OK`,`W_OK`,`X_OK`
| `listdir(path)` | 返回当前目录下所有文件组成的列表
| `remove(path)` | 删除文件
| `rename(old,new)` | 修改文件或目录名
| `mkdir(path[,mode])` | 创建目录
| `makedirs(path,[,mode])` | 创建多级目录
| `removedirs(path)` | 删除多级目录
| `rmdir(path)` | 删除目录（目录必须为空目录）

#### `os.path` 模块方法介绍

| `os.path` 方法 | 说明
|----------------|--------
|`exits(path)`| 当前路径是否存在
|`isdir(s)`| 是否是一个目录
|`isfile(path)`| 是否是一个文件
|`getsize(filename)`| 返回文件大小
|`dirname(p)`| 返回路径的目录
|`basename(p)`| 返回路径的文件名
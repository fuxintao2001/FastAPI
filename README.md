# FastAPI

一个最小可运行的 FastAPI 项目。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
uvicorn main:app --reload
```

## 测试接口

访问 `http://127.0.0.1:8000/`，返回示例：

```json
{"message": "Hello FastAPI"}
```

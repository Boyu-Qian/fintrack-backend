# fintrack-backend

## CI/CD

项目已配置 GitHub Actions（`.github/workflows/ci.yml`）作为 CI 流程，会在推送或提交 PR 到 `main` 分支时自动触发。流水线针对 `user-service` 与 `transaction-service`：

- 使用 Python 3.11 安装各自的依赖；
- 运行 `python -m compileall` 做语法检查；
- 如存在 `tests/` 目录，则执行 `pytest`。

如需在本地复现，可分别在服务目录下执行：

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest  # 如果项目已有测试
```

This is the backend for my fintrack project. You can see the project here: www.fintrack.site

This project is built with Python/Flask and PostgreSQL. I am currently working on Observability function(Grafana, Prometheus and OpenTelemetry.)

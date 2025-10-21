# fintrack-backend

## CI/CD

GitHub Actions (`.github/workflows/ci.yml`) is set up as the CI pipeline and runs automatically whenever code is pushed or a PR is opened against the `main` branch. The workflow covers both `user-service` and `transaction-service`:

- Install each service’s dependencies with Python 3.11.
- Run `python -m compileall` for syntax checks.
- Execute `pytest` if a `tests/` directory exists.

To reproduce the pipeline locally, run the following inside each service directory:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest
```

This is the backend for my fintrack project. You can see the project here: www.fintrack.site

This project is built with Python/Flask and PostgreSQL. I am currently working on Observability function(Grafana, Prometheus and OpenTelemetry.)

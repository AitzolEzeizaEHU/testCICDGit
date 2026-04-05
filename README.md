# testCICDGit

[![CI](https://github.com/AitzolEzeizaEHU/testCICDGit/actions/workflows/ci.yml/badge.svg)](https://github.com/AitzolEzeizaEHU/testCICDGit/actions/workflows/ci.yml)

Simple Python demo project showing:

- pytest-based tests
- Ruff lint and format checks
- GitHub Actions CI on pushes and pull requests

## Run locally

```powershell
uv pip install --system -e ".[dev]"
ruff check .
ruff format --check .
pytest -v
```
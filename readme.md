
<!-- bandit -r --ini .bandit to see if any issue-->
# Starting a new Python project with pdm

PDM setup

## Testing

[ptw](https://pypi.org/project/pytest-watch/)
[pytestmon](https://pypi.org/project/pytest-testmon/)

### Code coverage

#### From command line

```shell
pdm run pytest --cov=. --cov-report=xml tests
```

#### Pdm script

```toml
[tool.pdm.scripts]
cov = {shell = "pdm run pytest --cov=. --cov-report=xml tests"}
```

## Config

### Debugging in vscode using __pypackages__

Add to your .bashrc or .zshrc

```bash
if [ -n "$PYTHONPATH" ]; then
    export PYTHONPATH='/Users/pat/.asdf/installs/python/3.9.0/lib/python3.9/site-packages/pdm/pep582':$PYTHONPATH
else
    export PYTHONPATH='/Users/pat/.asdf/installs/python/3.9.0/lib/python3.9/site-packages/pdm/pep582'
fi
```

Add to .vscode/settings.json

``` json
    "python.autoComplete.extraPaths": ["${workspaceFolder}/__pypackages__/3.9/lib"],
    "python.analysis.extraPaths": ["${workspaceFolder}/__pypackages__/3.9/lib"]
```

### bandit rc

To work around this issue: Use of assert detected. The enclosed code will be removed when compiling to optimized byte code.

Create the following .bandit config at the root of the project:

``` yaml
[bandit]
exclude = tests/
targets = project/
```

To test bandit works, simply add assert True in both project.py and test_project.py. Then run:

``` bash
bandit -r --ini .bandit
```

Observe the config is ignored and warnings keep being reported for both project.py and test_project.py.

Explicitly tell vscode to run bandit with its config:

``` json
{
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.banditEnabled": true,
    "python.linting.banditArgs": [
        "-r",
        "--ini",
        ".bandit"
    ],
}
```

# Example Datadog Metrics
This is a simple example project that publishes metrics with the datadog metric API. 

It uses poetry to manage the dependencies, pyenv for the python version and direnv to
add the datadog api key to the environment. 

## Requirements
Install and configure:
* [poetry](https://python-poetry.org/)
* [pyenv](https://github.com/pyenv/pyenv)
* [direnv](https://direnv.net/)

Copy `.envrc.example` to `.envrc` and set the `DD_API_KEY` to your preferred API key. 
You may need to run `direnv allow` after this.

## Runninng It

```bash
poetry install

poetry run publish
```


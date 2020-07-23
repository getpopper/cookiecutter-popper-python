# {{ cookiecutter['project name'] }}

{{ cookiecutter['author(s)'] }}

{{ cookiecutter['description']}}

## Requirements

- `popper`

## Reproducing the results

```
popper run -f wf.yml
```

{% if cookiecutter.license != "No license file" -%}

## Project strucutre
```
{% if cookiecutter.license != "No license file" -%}
├── LICENSE
{%- endif %}
├── README.md                   <- The top-level README.
├── data                        <- Data used in workflow.
├── paper                       <- Generated papaer as PDF, LaTeX.
├── containers                  <- Definitions of containers used in workflow
|   ├── exploration.dockerfile  <- Default dockerfile used in workflow.
|   └── explotation_env.yml     <- Defines conda environment used by container.
├── results         
|   └── figures                 <- Graphics created during workflow.
└── src                         <- Source code for this project.
{%- if cookiecutter['jupyter notebooks'] == "Yes" %}
    ├── notebooks               <- Jupyter notebooks.
{% endif -%}
    ├── data                    <- Scripts to download or generate data.
    ├── models                  <- Scripts used to generate models.
    └── visualization           <- Scripts to generate graphics.

```

## License

This project is distributed under the  {{ cookiecutter.license }} license.
{%- endif %}
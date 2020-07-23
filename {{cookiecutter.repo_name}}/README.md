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
## License

This project is distributed under the  {{ cookiecutter.license }} license.
{%- endif %}
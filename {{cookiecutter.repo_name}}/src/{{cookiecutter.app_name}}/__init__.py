from pkg_resources import get_distribution
__version__ = get_distribution('{{ cookiecutter.project_name }}').version


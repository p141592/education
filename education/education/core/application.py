import typer

from apps.material import app as material
from apps.plan import app as plan

__version__ = "0.1.0"
NAME = "cs_education"


app = typer.Typer(
    name=NAME,
    help="Инструменты для работы с обучением"
)


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(None, "--version", "-v"),
):
    if version:
        typer.echo(f"{NAME} version: {__version__}")
        raise typer.Exit()


app.add_typer(material)
app.add_typer(plan)
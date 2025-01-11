"""Command-line interface for the pyprefab package."""
import shutil
from pathlib import Path
from typing import Optional

import typer
from jinja2 import Environment, FileSystemLoader
from rich import print
from rich.panel import Panel

app = typer.Typer(help='Generate python project scaffolding based on pyprefab.')

def validate_project_name(name: str) -> bool:
    """Validate project name follows Python package naming conventions."""
    return name.isidentifier() and name.islower()

@app.command()
def create(
    name: str = typer.Argument(..., help='Name of the project'),
    author: str = typer.Option(..., '--author', help='Project author'),
    description: str = typer.Option('', '--description', help='Project description'),
    project_dir: Optional[Path] = typer.Option(
        None, '--directory', help='Directory that will contain the project (defaults to current directory)'
    ),
):
    """Generate a new Python project from templates."""
    if not validate_project_name(name):
        typer.secho(
            f'Error: {name} is not a valid Python package name',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    templates_dir = Path(__file__).parent / 'templates'
    target_dir = project_dir or Path.cwd() / name

    try:
        # Create project directory
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Template context
        context = {
            'project_name': name,
            'author': author,
            'description': description,
        }

        # Process templates
        env = Environment(loader=FileSystemLoader(templates_dir))
        for template_file in templates_dir.rglob('*'):
            if template_file.is_file():
                template = env.get_template(template_file.name)
                output = template.render(**context)
                
                rel_path = template_file.relative_to(templates_dir)
                dest_file = target_dir / rel_path.with_suffix('').name
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                dest_file.write_text(output)

        print(Panel.fit(
            f'✨ Created new project [bold green]{name}[/] in {target_dir}\n'
            f'Author: [blue]{author}[/]\n'
            f'Description: {description}',
            title='Project Created Successfully',
            border_style='green',
        ))

    except Exception as e:
        typer.secho(f'Error creating project: {str(e)}', fg=typer.colors.RED)
        if target_dir.exists():
            shutil.rmtree(target_dir)
        raise typer.Exit(1)

def main():
    app()

if __name__ == '__main__':
    main()
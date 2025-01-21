"""Command-line interface for the pyprefab package."""

import shutil
from pathlib import Path
from typing import Optional

import structlog
import typer
from jinja2 import Environment, FileSystemLoader
from rich import print
from rich.panel import Panel

logger = structlog.get_logger()

app = typer.Typer(help='Generate python project scaffolding based on pyprefab.')


def validate_project_name(name: str) -> bool:
    """Validate project name follows Python package naming conventions."""
    return name.isidentifier() and name.islower()


def render_templates(context: dict, templates_dir: Path, target_dir: Path):
    """Render Jinja templates to target directory."""
    # Process templates
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    # For rendering path names
    path_env = Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )

    for template_file in templates_dir.rglob('*'):
        if template_file.is_file():
            rel_path = template_file.relative_to(templates_dir)
            template = env.get_template(str(rel_path))
            output = template.render(**context)

            # Process path parts through Jinja
            path_parts = []
            for part in rel_path.parts:
                # Render each path component through Jinja
                rendered_part = path_env.from_string(part).render(**context)
                if rendered_part.endswith('.j2'):
                    rendered_part = rendered_part[:-3]
                path_parts.append(rendered_part)

            # Create destination path preserving structure
            dest_file = target_dir.joinpath(*path_parts)
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            with open(dest_file, 'w', newline='\n') as f:
                f.write(output)


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

        # Write Jinja templates to project directory
        render_templates(context, templates_dir, target_dir)

        print(
            Panel.fit(
                f'✨ Created new project [bold green]{name}[/] in {target_dir}\n'
                f'Author: [blue]{author}[/]\n'
                f'Description: {description}',
                title='Project Created Successfully',
                border_style='green',
            )
        )

    except Exception as e:
        typer.secho(f'Error creating project: {str(e)}', fg=typer.colors.RED)
        if target_dir.exists():
            shutil.rmtree(target_dir)
        raise typer.Exit(1)


def main():
    app()


if __name__ == '__main__':
    main()

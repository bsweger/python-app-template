# Changelog

All notable changes to `pyprefab` are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com), and the project uses [Semantic Versioning](https://semver.org/).

## [0.5.0] - [2025-02-10]

### Added

- Sphinx-based project documentation (published on GitHub pages)
- New CLI `--docs` option to include skeleton documentation in created package

### Fixed

- Add escape character to quotation marks in author name and project description

## [0.4.0] - [2025-01-26]

### Added

- New templates for GitHub workflows: ci (linting, tests, and coverage), publishing to TestPyPI, and publishing to PyPI
- Project changelog
- New CHANGELOG.md template
- New CONTRIBUTING.md template

### Changed

- Add CLI prompts as an alternate to passing command options
- `--directory` option renamed to `--dir`
- Prompt user when specified project directory is not empty
- List created package components on README.md

### Fixed

- Correct CLI example on README.md

## [0.3.2] - [2025-01-13](https://github.com/bsweger/pyprefab/compare/v0.3.1...v0.3.2)

### Changed

- Rename CLI command to `pyprefab`

## [0.3.1] - [2025-01-13](https://github.com/bsweger/pyprefab/compare/v0.3.0...v0.3.1)

### Added

- New templates for generating Python package boilerplate: .gitignore, README.md, app.py

### Changed

- Rename project to `pyprefab`

### Removed

- Removed sample `hello_world` module in favor of template-driven boilerplate

## [0.3.0] - [2025-01-12](https://github.com/bsweger/pyprefab/compare/v0.2.1...v0.3.0)

### Added

- Added `pyproject.toml` template as the first piece of template-driven Python boilerplate

### Removed

- Removed artifacts from prior iteration of `pyprefab` that pre-dates the template-drive approach

# Release Guide for ClipClean

This document outlines the process for releasing ClipClean to PyPI and creating executable distributions.

## Prerequisites

1. **PyPI Account**: Create accounts on [PyPI](https://pypi.org/) and [Test PyPI](https://test.pypi.org/)
2. **API Tokens**: Generate API tokens for both PyPI and Test PyPI
3. **GitHub Repository**: Set up repository secrets for automated publishing

## Setting Up GitHub Secrets

Add these secrets to your GitHub repository (Settings > Secrets and variables > Actions):

- `PYPI_API_TOKEN`: Your PyPI API token (starts with `pypi-`)

## Manual Release Process

### 1. Prepare Release

```bash
# Update version in pyproject.toml and clipclean/__init__.py
# Update CHANGELOG.md if you have one
# Commit all changes

git add .
git commit -m "Prepare v1.0.0 release"
git tag v1.0.0
git push origin main --tags
```

### 2. Build and Test Locally

```bash
# Install build dependencies
pip install build twine

# Build the package
python -m build

# Check the package
twine check dist/*

# Test upload to Test PyPI
twine upload --repository testpypi dist/*

# Test install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ clipclean
```

### 3. Upload to PyPI

```bash
# Upload to PyPI
twine upload dist/*
```

### 4. Create Executable (Windows)

On Windows machine or using GitHub Actions:

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller clipclean.spec

# Test the executable
dist/clipclean.exe
```

## Automated Release (GitHub Actions)

### 1. Create Release on GitHub

1. Go to your repository on GitHub
2. Click "Releases" > "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `ClipClean v1.0.0`
5. Describe the changes
6. Click "Publish release"

This will automatically:
- Build and upload to PyPI
- Create Windows and macOS executables
- Attach executables to the release

### 2. Verify Release

- Check PyPI: https://pypi.org/project/clipclean/
- Test installation: `pip install clipclean`
- Download and test executables from GitHub release

## Version Management

Update version numbers in:
1. `pyproject.toml` - `version = "1.0.0"`
2. `clipclean/__init__.py` - `__version__ = "1.0.0"`

## Testing Checklist

Before release, ensure:
- [ ] All tests pass: `python test_cleaning.py`
- [ ] Package installs correctly: `pip install -e .`
- [ ] Command works: `clipclean`
- [ ] GUI launches and functions properly
- [ ] Dark/light mode switching works
- [ ] Text cleaning works as expected
- [ ] Settings persistence works

## Troubleshooting

### PyInstaller Issues

If executable creation fails:
- Ensure all dependencies are installed
- Check for missing hidden imports
- Test on clean virtual environment

### PyPI Upload Issues

- Verify API token is correct
- Check package name isn't taken
- Ensure version number is unique
- Validate package metadata

## File Checklist

Ensure these files are included:
- [ ] `README.md` - Complete documentation
- [ ] `LICENSE` - MIT license
- [ ] `pyproject.toml` - Package configuration
- [ ] `MANIFEST.in` - Include additional files
- [ ] `.github/workflows/` - CI/CD workflows
- [ ] `clipclean.spec` - PyInstaller configuration
- [ ] `assets/` - Icons and resources
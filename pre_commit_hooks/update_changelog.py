from pathlib import Path
from git_changelog.cli import build_and_render


def create_empty_changelog(filename: str = "CHANGELOG.md"):
    txt = """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->

    """
    with open(filename, "w") as f:
        f.write(txt)


def main():
    filename = "CHANGELOG.md"
    if not Path(filename).exists():
        create_empty_changelog(filename)

    build_and_render(
        repository=".",
        output=filename,
        convention="basic",
        template="keepachangelog",
        bump_latest=True,
        in_place=True,
        version_regex='<a href="[^"]+">(?P<version>[^<]+)',
    )

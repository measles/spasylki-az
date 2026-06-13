"""Different automations useful for development."""

import os

import nox

CONTAINER_ENGINE = os.getenv("CONTAINER_ENGINE", "podman")
nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["lint"]


def _image_exist(image_name: str, session: nox.Session) -> bool:
    """Check if specified image exists.

    :param image_name: Image name to look for
    :type image_name: str
    :param session: current nox session
    :type session: nox.Session
    :return: True if image exists, False otherwise
    :rtype: bool
    """
    try:
        session.run(CONTAINER_ENGINE, "image", "exists", image_name)
        return True
    except nox.command.CommandFailed:
        return False


#
# Image operations
#
@nox.session(python=False)
def update_requirements(session: nox.Session) -> None:
    """Update the requirements.txt file with a data from uv.lock."""
    session.run(
        "uv",
        "export",
        "--format",
        "requirements.txt",
        "--output-file",
        "requirements.txt",
    )


@nox.session(python=False, requires=["update_requirements"])
def build(session: nox.Session) -> None:
    """Build an image."""
    session.run(CONTAINER_ENGINE, "build", "-f", "Dockerfile", "-t", "spasylki-az")


@nox.session(python=False)
def run(session: nox.Session) -> None:
    """Run the container.

    If image does not exist, builds one."""
    if not _image_exist("spasylki-az", session):
        session.run("nox", "-s", "build", external=True)
    session.run(
        CONTAINER_ENGINE,
        "run",
        "-it",
        "-p",
        "8080:8080",
        "--env",
        "PORT=8080",
        "spasylki-az:latest",
    )


#
# Formatting and linting
#
@nox.session(python=False)
def black(session: nox.Session) -> None:
    """Format code with black."""
    session.run("black", "noxfile.py", "src")


@nox.session(python=False)
def isort(session: nox.Session) -> None:
    """Sort imports with isort."""
    session.run("isort", "noxfile.py", "src")


@nox.session(python=False)
def mypy(session: nox.Session) -> None:
    """Check types with mypy."""
    session.run("mypy", "--strict", "noxfile.py", "src")


@nox.session(python=False)
def ruff(session: nox.Session) -> None:
    """Check code with ruff."""
    session.run("ruff", "check", "noxfile.py", "src")


@nox.session(python=False)
def pylint(session: nox.Session) -> None:
    """Check code with pylint."""
    session.run("pylint", "noxfile.py", "src")


@nox.session(python=False, requires=["black", "isort", "mypy", "ruff", "pylint"])
def lint(session: nox.Session) -> None:
    """Run all code fomaters and linters. Let it all burn!"""
    session.log("Code is formated and all checks are passed.")

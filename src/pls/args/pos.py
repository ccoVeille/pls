import argparse
from pathlib import Path

from pls.exceptions import ArgException


def _directory(path_str: str) -> Path:
    """
    Parse the given path into a ``Path`` instance. The path is considered valid
    if it points to an existing directory.

    :param path_str: the path supplied as a CLI argument
    :return: the ``Path`` instance wrapping the supplied path
    :raise: ``ArgException``, if the path is invalid
    """

    path = Path(path_str).resolve()
    if not path.exists():
        raise ArgException(
            f"Path [repr.path]{path_str}[/] does not exist.", arg_name="directory"
        )
    if not path.is_dir():
        raise ArgException(
            f"Path [repr.path]{path_str}[/] is not a directory.", arg_name="directory"
        )
    return path


def add_args(parser: argparse.ArgumentParser):
    """
    Add the positional arguments to the given parser.

    :param parser: the parser to which to add the arguments
    """

    parser.add_argument(
        "directory",
        type=_directory,
        nargs=argparse.OPTIONAL,
        default=Path.cwd(),
        help="the directory whose contents are to be listed",
    )
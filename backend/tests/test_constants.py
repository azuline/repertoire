import os

import pytest

from src.constants import _get_data_path


def test_get_data_path_create(isolated_dir):
    data_path = isolated_dir / "data_path"
    os.environ["DATA_PATH"] = str(data_path)
    assert _get_data_path() == data_path
    assert data_path.is_dir()


def test_get_data_path_exists(isolated_dir):
    data_path = isolated_dir / "data_path"
    data_path.mkdir()
    os.environ["DATA_PATH"] = str(data_path)
    assert _get_data_path() == data_path
    assert data_path.is_dir()


def test_get_data_path_unset(isolated_dir):
    if "DATA_PATH" in os.environ:
        del os.environ["DATA_PATH"]
    with pytest.raises(SystemExit):
        _get_data_path()


def test_get_data_path_is_file(isolated_dir):
    data_path = isolated_dir / "data_path"
    data_path.touch()
    os.environ["DATA_PATH"] = str(data_path)
    with pytest.raises(SystemExit):
        _get_data_path()


def test_get_data_path_readonly(isolated_dir):
    data_path = isolated_dir / "data_path"
    data_path.mkdir(0o400)
    os.environ["DATA_PATH"] = str(data_path)
    with pytest.raises(SystemExit):
        _get_data_path()

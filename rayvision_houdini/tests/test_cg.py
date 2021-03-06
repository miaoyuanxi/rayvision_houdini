# -*- coding=utf-8 -*-
"""The plugin of the pytest.

The pytest plugin hooks do not need to be imported into any test code, it will
load automatically when running pytest.

References:
    https://docs.pytest.org/en/2.7.3/plugins.html

"""

import pytest

from rayvision_utils.exception.exception import FileNameContainsChineseError
from rayvision_utils.exception.exception import VersionNotMatchError
from rayvision_utils.exception.exception import CGFileNotExistsError
from rayvision_houdini.cg import Houdini


def test_init(houdini, tmpdir):
    """Test houdini init."""
    houdini.cg_file = str(tmpdir.join("资源名不能带中文.hip"))
    with pytest.raises(FileNameContainsChineseError):
        houdini.init()


def test_get_save_version(houdini, cg_file_h):
    """Test get_save_version function."""
    # result = houdini.get_save_version(cg_file_h["cg_file"])
    with pytest.raises(CGFileNotExistsError):
        houdini.get_save_version(cg_file_h["cg_file"])


def test_find_location(houdini, mocker, tmpdir):
    """Test find_location action """
    mocker_cg_file = mocker.patch.object(Houdini, 'find_location')
    mocker_cg_file.return_value = tmpdir.join('muti_layer_test.hip')
    assert houdini.find_location() == str(tmpdir.join('muti_layer_test.hip'))


def test_valid(houdini):
    """Valid the software and name"""
    houdini.name = ""
    houdini.version = "2015"
    with pytest.raises(VersionNotMatchError):
        houdini.valid()

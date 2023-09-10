##
#  @file
#  Testcases for foundation core functionalities.
#
#  @copyright
#  Copyright (c) 2023, Codevience. All rights reserved.<BR>
#
#  SPDX-License-Identifier: BSD-2-Clause-Patent
#
#  @par reference
#
##
"""
Collection of testcases for core functionality.
"""


def test_import_package_function() -> None:
    """
    Check the Python package import.

    Note:
        Need to make sure the package is in import path.
            - Add the path into "PYTHONPATH" environment variable.

    Args:
        None

    Raises:
        None.

    Returns:
        None.
    """
    try:
        import pycommon
        print(pycommon.__version__)
    except ModuleNotFoundError:
        assert False

    assert True

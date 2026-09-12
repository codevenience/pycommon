##
#  @file
#  Sub-package for HTTP-related constants.
#
#  @copyright
#  Copyright (c) 2026, Codevenience Organization. All rights reserved.<BR>
#
#  SPDX-License-Identifier: BSD-3-Clause
#
#  @par reference
#
##
"""
Generic definitions for HyperText Transfer Protocol (HTTP).
"""
from typing import List

from pycommon.const.http import http_status_code

__all__: List[str] = [
    'http_status_code',
]

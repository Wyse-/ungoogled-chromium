#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (c) 2017 The ungoogled-chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Simple buildkit CLI launcher allowing invocation from anywhere.

Pass in -h or --help for usage information.
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import buildkit.cli
sys.path.pop(0)

buildkit.cli.main()

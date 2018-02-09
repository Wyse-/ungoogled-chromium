#!/usr/bin/env python3

# Copyright (c) 2018 The ungoogled-chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

if __name__ == '__main__':
    from pylint import epylint as lint
    import pathlib

    lint.lint(filename=str(pathlib.Path(__file__).parent.parent / 'buildkit'), options=[
        '--disable=locally-disabled',
        '--jobs=4',
        '--ignore=third_party'])

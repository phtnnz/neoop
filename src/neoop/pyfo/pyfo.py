#!/usr/bin/env python

# Copyright 2026 Martin Junius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ChangeLog
# Version 0.1 / 2026-06-26
#       Python interface for find_orb command line

VERSION     = "0.1 / 2026-06-26"
AUTHOR      = "Martin Junius"
NAME        = "neoop.pyfo.pyfo"
DESCRIPTION = "Compute ephemeris using Project Pluto's find_orb"

from typing import Self
import os

from icecream import ic
# Disable debugging
ic.disable()

# AstroPy

# NEOOP
from neoop.neo.config import config



class FindOrb:
    def __init__(self) -> None:
        # Check and find find_orb dir
        find_orb_dir = config.find_orb_dir
        if not os.path.isdir(find_orb_dir):
            raise FileNotFoundError(f"dir {find_orb_dir} not found")
        self._fo_dir = os.path.abspath(find_orb_dir)
        self._fo_exe = os.path.join(self._fo_dir, config.fo_exe)
        if not os.path.isfile(self._fo_exe):
            raise FileNotFoundError(f"file {self._fo_exe} not found")
        self._fo_mpc80 = os.path.join(self._fo_dir, config.fo_mpc80)
        self._fo_json = os.path.join(self._fo_dir, config.fo_json)
        ic(self._fo_dir, self._fo_exe, self._fo_mpc80, self._fo_json)        


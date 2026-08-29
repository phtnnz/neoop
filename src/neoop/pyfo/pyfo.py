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
import subprocess

from icecream import ic
# Disable debugging
ic.disable()

# AstroPy
from astropy.table import QTable
import astropy.units as u

# NEOOP
from neoop.neo.config import config
from neoop.mpc.observations import Obs
from neoop.neo.local import LocalCircumstances
from neoop.utils.verbose import verbose, error



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
        self._fo_txt = os.path.join(self._fo_dir, config.fo_txt)
        self._fo_debug = os.path.join(self._fo_dir, config.fo_debug)
        ic(self._fo_dir, self._fo_exe, self._fo_mpc80, self._fo_json)        


    def write_obs(self, obs: Obs) -> None:
        obs.write_mpcformat(self._fo_mpc80)


    def run_find_orb(self, local: LocalCircumstances) -> None:
        # For compatibility with sbpy.data.Ephem
        start = local.epochs.get("start")
        step  = local.epochs.get("step")
        stop  = local.epochs.get("stop")
        if stop:
            number = int((stop - start) / step) + 1
        else:
            number = 10
        ic(start, step, stop, number)

        # Example command line
        # .\fo64 DATAFILE  -C M49  -e ephem.txt  -E 3,5,10,27,28,29,35,36  "EPHEM_START=2026 Aug 24 22:00" EPHEM_STEPS=12 EPHEM_STEP_SIZE=5m
        args = [self._fo_exe, self._fo_mpc80, "-C", local.code, "-e", self._fo_txt, *config.fo_args,
                f"EPHEM_START={start.iso}", f"EPHEM_STEPS={number}", f"EPHEM_STEP_SIZE={int(step.to(u.min).value)}m"
                ]
        ic(args)
        verbose("run", " ".join(args))
        try:
            subprocess.run(args=args, shell=False, cwd=self._fo_dir, check=True)
        except subprocess.CalledProcessError as e:
            error(f"running fo failed: {e}, see {self._fo_debug}")


    def read_ephem(self) -> QTable:
        ...



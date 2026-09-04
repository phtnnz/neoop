#!/usr/bin/env python

# Copyright 2025-2026 Martin Junius
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
# Version 0.1 / 2026-06-25
#       Get observations from MPC database
# Version 0.2 / 2026-09-01
#       Also get NEOCP observations from MPC

VERSION     = "0.2 / 2026-09-01"
AUTHOR      = "Martin Junius"
NAME        = "neoop.mpc.observations"
DESCRIPTION = "Retrieve MPC observations data"

import re
from dataclasses import dataclass
from typing import Self
import requests

from icecream import ic
# Disable debugging
ic.disable()

# AstroPy
from astropy.time import Time
from astropy.table import Row
from astropy.table import Table, QTable
import astropy.units as u

from astroquery.mpc import MPC

# NEOOP
from neoop.neo.config import config
from neoop.utils.verbose import verbose, error

# Requests timeout
TIMEOUT = config.requests_timeout



@dataclass
class Obs:
    table: QTable = None

    def get_observations(self, obj: str, mpcformat: bool=False) -> None:
        try:
            table = MPC.get_observations(obj, get_mpcformat=mpcformat)
        except ValueError:
            error(f"retrieving MPC observations for {obj}, use {obj}:NEOCP?")

        # table is already a QTable
        self.table = table


    def get_observations_neocp(self, obj: str, mpcformat: bool=False) -> None:
        if not mpcformat:
            raise NotImplementedError("mpcformat=True not implemented for NEOCP observations")
        # verbose(f"query {config.neocp_obs_url}")
        content = mpc_query_neocp_obs(config.neocp_obs_url, obj)
        table = parse_neocp_obs(content)
        self.table = table


    @classmethod
    def from_object(cls, obj: str, mpcformat: bool=False, neocp: bool=False) -> Self:
        obs = cls()
        if neocp:
            obs.get_observations_neocp(obj, mpcformat)
        else:
            obs.get_observations(obj, mpcformat)
        return obs
    

    def __getitem__(self, item) -> any:
        return self.table[item]
    

    def __len__(self) -> int:
        return len(self.table)


    def get_last_row_from_mpc(self) -> Row:
        # # Handle masked entries
        # for i in range(-1, -10, -1):
        #     mag = obs["mag"][i].unmasked
        #     if mag > Magnitude(0):
        #         break
        return self.table[-1]


    def get_last_obs(self) -> Time:
            jd = self.table[-1].get("epoch")
            time = Time(jd, format="jd")
            time.format = "iso"
            return time


    def write_mpcformat(self, filename: str) -> None:
        ic(self.table.columns)
        if not "obs" in self.table.columns:
            raise IndexError("table not in mpc80 format (single 'obs' column)")
        with open(filename, "w") as file:
            for line in self.table["obs"]:
                print(line, file=file)



def mpc_query_neocp_obs(url: str, target: str) -> str:

    # Example query:
    # https://cgi.minorplanetcenter.net/cgi-bin/showobsorbs.cgi?Obj=ST26H93&obs=y
    data = { 
        "Obj": target,
        "obs": "y"
    }

    ic(url, data)
    response = requests.get(url, params=data, timeout=TIMEOUT)
    ic(response.status_code)
    if response.status_code != 200:
        error(f"query to {url} failed")

    return response.text



def parse_neocp_obs(content: str) -> QTable:
    qt = QTable()
    qt["obs"] = ""

    for line in content.splitlines():
        # Skip HTML
        if "<pre>" in line or "</pre>" in line:
            continue
        qt.add_row([line])
    ic(qt)
    return qt

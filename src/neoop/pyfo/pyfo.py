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
import json

from icecream import ic
# Disable debugging
ic.disable()

# AstroPy
from astropy.table import QTable
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import Angle, AltAz
import astropy.units as u
from astropy.units import Quantity, Magnitude
import numpy as np

# NEOOP
from neoop.neo.config import config
from neoop.mpc.observations import Obs
from neoop.neo.local import LocalCircumstances
from neoop.utils.verbose import verbose, error



class FindOrb:
    def __init__(self, local: LocalCircumstances) -> None:
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
        self.local = local
        ic(self._fo_dir, self._fo_exe, self._fo_mpc80, self._fo_json)        


    def write_obs(self, obs: Obs) -> None:
        obs.write_mpcformat(self._fo_mpc80)


    def run_find_orb(self) -> None:
        # For compatibility with sbpy.data.Ephem
        start = self.local.epochs.get("start")
        step  = self.local.epochs.get("step")
        stop  = self.local.epochs.get("stop")
        if stop:
            number = int((stop - start) / step) + 1
        else:
            number = 10
        ic(start, step, stop, number)

        # Example command line
        # .\fo64 DATAFILE  -C M49  -e ephem.txt  -E 3,5,10,27,28,29,35,36  "EPHEM_START=2026 Aug 24 22:00" EPHEM_STEPS=12 EPHEM_STEP_SIZE=5m
        args = [self._fo_exe, self._fo_mpc80, "-C", self.local.code, "-e", self._fo_txt, *config.fo_args,
                f"EPHEM_START={start.iso}", f"EPHEM_STEPS={number}", f"EPHEM_STEP_SIZE={int(step.to(u.min).value)}m"
                ]
        ic(args)
        verbose("run", " ".join(args))
        try:
            subprocess.run(args=args, shell=False, cwd=self._fo_dir, check=True)
        except subprocess.CalledProcessError as e:
            error(f"running fo failed: {e}, see {self._fo_debug}")


    def read_ephem(self, target: str, nautical: bool=True) -> QTable:
        with open(self._fo_json, 'r') as file:
            data = json.load(file)
            eph = data.get("ephemeris")
            if not eph:
                error(f"missing 'ephemeris' key in {self._fo_json}")
            n_steps = eph.get("n_steps")
            entries = eph.get("entries")

            qt = QTable()
            qt["Targetname"]  = target
            qt["Obstime"]     = Time("2000-01-01 00:00")
            qt["RA"]          = 0 * u.hourangle
            qt["DEC"]         = 0 * u.degree
            # qt["Sky"]         = 0 * u.mag
            # qt["SNR"]         = 0.0
            # qt["Exp_time"]    = 0 * u.s
            qt["Mag"]         = 0 * u.mag
            qt["Motion"]      = 0 * u.arcsec / u.min
            qt["PA"]          = 0 * u.degree
            qt["Alt"]         = 0 * u.degree
            qt["Az"]          = 0 * u.degree
            qt["Moon_alt"]    = 0 * u.degree
            qt["Moon_az"]     = 0 * u.degree
            qt["Moon_dist"]   = 0 * u.degree

            for idx in range(0, n_steps):
                key = str(idx)
                entry = entries.get(key)
                ic(entry)

                # Example entry:
                # { "JD": 2461282.125000001, "ISO_time": "2026-08-29T15:00:00Z", "RA": 328.36496886613, 
                #   "RA60": "21 53 27.593", "Dec": -48.29541971139, "Dec60": "-48 17 43.51",
                #   "delta": 0.140281546550, "r": 1.121276583889, "elong": 140.25456, "SkyBr": 3.49, "RGB": "e2ffff", 
                #   "SNR": 0.00, "ExpT": null, "OptExpT": 4.3, "mag": 17.642, "motion_rate": 2.587680, "motionPA": 213.7115, 
                #   "alt": 5.0700, "az": 140.8945, "Mal": -40.1759, "Maz": 111.5655 },
                time   = Time(entry["ISO_time"])

                # Skip ephemeris outside nautical dusk ... dawn
                if nautical:
                    if time < self.local.naut_dusk or time > self.local.naut_dawn:
                        continue

                ra     = Angle(entry["RA"], unit=u.deg)
                dec    = Angle(entry["Dec"], unit=u.deg)
                # sky    = Magnitude(entry["SkyBr"], unit=u.mag) if entry["SkyBr"] else Magnitude(0, unit=u.mag)
                # snr    = float(entry["SNR"]) if entry["SNR"] else 0.0
                # exp    = Quantity(entry["OptExpT"], unit=u.s) 
                mag    = Magnitude(entry["mag"], unit=u.mag)
                motion = Quantity(entry["motion_rate"], unit=u.arcsec / u.min)
                pa     = Angle(entry["motionPA"], unit=u.deg)
                alt    = Angle(entry["alt"], unit=u.deg)
                az     = Angle(entry["az"], unit=u.deg)
                m_alt  = Angle(entry["Mal"], unit=u.deg)
                m_az   = Angle(entry["Maz"], unit=u.deg)

                altaz = AltAz(alt=alt, az=az)
                m_altaz = AltAz(alt=m_alt, az=m_az)
                m_dist = altaz.separation(m_altaz)
                ic(altaz, m_altaz, m_dist)

                # Alternatively, use the spherical law of cosines
                # cos_d = np.sin(alt)*np.sin(m_alt) + np.cos(alt)*np.cos(m_alt)*np.cos(az - m_az)
                # m_dist = np.acos(cos_d)

                # qt.add_row( [target, time, ra, dec, sky, snr, exp, mag, motion, pa, alt, az, m_alt, m_az, m_dist ] )
                qt.add_row( [target, time, ra, dec, mag, motion, pa, alt, az, m_alt, m_az, m_dist ] )

            ic(qt)
            self.table = qt
            return qt


    def read_ephem_txt(self) -> str:
        with open(self._fo_txt, "r") as file:
            self.text = file.read()
        return self.text
    

    @classmethod
    def from_obs(cls, local: LocalCircumstances, target: str, obs: Obs, nautical: bool=True) -> Self:
        fo = cls(local)
        fo.write_obs(obs)
        fo.run_find_orb()
        fo.read_ephem(target, nautical)
        return fo

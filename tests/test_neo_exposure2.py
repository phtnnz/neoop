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
# Version 0.1 / 2026-06-30
#       Test neoop.neo.exposure

from icecream import ic
import astropy.units as u
from astropy.units import Quantity, Magnitude
from neoop.neo.classes import Exposure

ic.enable()

ic("--------------------")
mag = Magnitude(19.0)
motion = 15 * u.arcsec/u.min
ic(mag, motion)
exp = Exposure.from_motion_mag(motion, mag)
print("Test1:", exp, "\n")

ic("--------------------")
mag = Magnitude(19.5)
motion = 15 * u.arcsec/u.min
ic(mag, motion)
exp = Exposure.from_motion_mag(motion, mag)
print("Test1:", exp, "\n")

ic("--------------------")
mag = Magnitude(20.0)
motion = 15 * u.arcsec/u.min
ic(mag, motion)
exp = Exposure.from_motion_mag(motion, mag)
print("Test1:", exp, "\n")

ic("--------------------")
mag = Magnitude(20.0)
motion = 30 * u.arcsec/u.min
ic(mag, motion)
exp = Exposure.from_motion_mag(motion, mag)
print("Test1:", exp, "\n")


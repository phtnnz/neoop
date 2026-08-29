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
# Version 0.1 / 2026-08-26
#       Test neoop.pyfo.pyfo

from icecream import ic

from neoop.mpc.observations import Obs
from neoop.neo.local import LocalCircumstances
from neoop.pyfo.pyfo import FindOrb

ic.enable()
obj = "2026 NT2"

# Observer location and local circumstances
local = LocalCircumstances.from_location("M49")
ic(local)

obs = Obs.from_object(obj, mpcformat=True)
ic(obs)

fo = FindOrb.from_obs(local, obj, obs)
txt = fo.read_ephem_txt()
ic(txt)

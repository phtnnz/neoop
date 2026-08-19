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
# Version 0.1 / 2026-08-19
#       Test neoop.mpc.neocp

from icecream import ic

from neoop.mpc.ephemdata import EphemDataList
from neoop.neo.local import LocalCircumstances
from neoop.utils.verbose import verbose
import neoop.mpc.neocp

verbose.enable()
ic.enable()

# Change for currently listed NEOCP object!
obj = "ZTF10FV"

# Observer location and local circumstances
local = LocalCircumstances.from_location("M49")
ic(local)

edata_list = EphemDataList.from_single_neocp(local, obj, 1)
ic(edata_list)
edata_list.verbose_ephem()

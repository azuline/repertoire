# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_from_id 1'] = GenericRepr("T(id=1, path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")

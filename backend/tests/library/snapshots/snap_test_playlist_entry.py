# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_from_id_success 1'] = GenericRepr('T(id=1, track_id=1, playlist_id=1, position=1, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))')

snapshots['test_from_playlist_and_track_success 1'] = [
    GenericRepr('T(id=1, track_id=1, playlist_id=1, position=1, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))')
]

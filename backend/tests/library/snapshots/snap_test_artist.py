# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_all 1'] = [
    GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
    GenericRepr("T(id=4, name='Abakus', favorite=False, num_releases=1)"),
    GenericRepr("T(id=5, name='Bacchus', favorite=True, num_releases=1)")
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)")

snapshots['test_releases 1'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, runtime=2258, release_date=datetime.date(2014, 7, 8), image_path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")
]

snapshots['test_top_genres 1'] = [
    {
        'genre': GenericRepr("T(id=12, name='Folk', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=13, name='Rock', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=14, name='Country', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=15, name='World', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    }
]

snapshots['test_update_fields 1'] = GenericRepr("T(id=2, name='New Name', favorite=True, num_releases=1)")

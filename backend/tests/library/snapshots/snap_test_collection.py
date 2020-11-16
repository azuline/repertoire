# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_release 1'] = GenericRepr("T(id=3, name='1', starred=False, type=<CollectionType.RATING: 5>, num_releases=1, last_updated_on=None)")

snapshots['test_add_release 2'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, runtime=2258, release_date=datetime.date(2014, 7, 8), image_path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")
]

snapshots['test_all 1'] = [
    GenericRepr("T(id=1, name='Inbox', starred=False, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=2, name='Favorite', starred=False, type=<CollectionType.SYSTEM: 1>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=3, name='1', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=4, name='2', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=5, name='3', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=6, name='4', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=7, name='5', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=8, name='6', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=9, name='7', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=10, name='8', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=11, name='9', starred=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=12, name='Folk', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=13, name='Rock', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=14, name='Country', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=15, name='World', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=16, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=17, name='Electronic', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=18, name='House', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=19, name='Ambient', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=20, name='MyLabel', starred=False, type=<CollectionType.LABEL: 3>, num_releases=0, last_updated_on=None)")
]

snapshots['test_all_filter_type 1'] = [
    GenericRepr("T(id=1, name='Inbox', starred=False, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=2, name='Favorite', starred=False, type=<CollectionType.SYSTEM: 1>, num_releases=0, last_updated_on=None)")
]

snapshots['test_del_release 1'] = GenericRepr("T(id=12, name='Folk', starred=False, type=<CollectionType.GENRE: 4>, num_releases=0, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_del_release 2'] = [
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=16, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_releases 1'] = [
    GenericRepr("T(id=3, title='Departure', release_type=<ReleaseType.EP: 3>, added_on=datetime.datetime(2020, 10, 19, 8, 29, 34), release_year=2016, num_tracks=11, in_inbox=True, runtime=3513, release_date=None, image_path=PosixPath('/data/cover_art/d832df509b44cb7c560e2579453178016c391cd2ab8d6eab3de2bbbdf75c4ac0.jpg'))")
]

snapshots['test_top_genres 1'] = [
    {
        'genre': GenericRepr("T(id=16, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=17, name='Electronic', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=18, name='House', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=19, name='Ambient', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    }
]

snapshots['test_update_fields 1'] = GenericRepr("T(id=13, name='New Name', starred=True, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

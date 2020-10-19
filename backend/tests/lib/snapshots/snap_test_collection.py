# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_all 1'] = [
    GenericRepr("T(id=1, name='Inbox', favorite=False, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=2, name='Favorite', favorite=False, type=<CollectionType.SYSTEM: 1>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=3, name='1', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=4, name='2', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=5, name='3', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=6, name='4', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=7, name='5', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=8, name='6', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=9, name='7', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=10, name='8', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=11, name='9', favorite=False, type=<CollectionType.RATING: 5>, num_releases=0, last_updated_on=None)"),
    GenericRepr("T(id=12, name='Folk', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=13, name='Rock', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=14, name='Country', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=15, name='World', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=16, name='Downtempo', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=17, name='Electronic', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=18, name='House', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=19, name='Ambient', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')")
]

snapshots['test_all_filter_type 1'] = [
    GenericRepr("T(id=1, name='Inbox', favorite=False, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on='2020-10-19 00:25:34')"),
    GenericRepr("T(id=2, name='Favorite', favorite=False, type=<CollectionType.SYSTEM: 1>, num_releases=0, last_updated_on=None)")
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=16, name='Downtempo', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on='2020-10-19 00:25:34')")

snapshots['test_releases 1'] = [
    GenericRepr("T(id=3, title='Departure', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 8, 29, 34), release_year=2016, release_date=None, image_path=PosixPath('/data/cover_art/d832df509b44cb7c560e2579453178016c391cd2ab8d6eab3de2bbbdf75c4ac0.jpg'), num_tracks=None)")
]

snapshots['test_top_genres 1'] = [
    {
        'genre': GenericRepr("T(id=16, name='Downtempo', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=17, name='Electronic', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=18, name='House', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=19, name='Ambient', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    }
]

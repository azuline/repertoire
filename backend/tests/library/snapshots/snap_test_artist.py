# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_all 1'] = [
    GenericRepr("T(id=5, name='Bacchus', starred=True, num_releases=1)"),
    GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
    GenericRepr("T(id=4, name='Abakus', starred=False, num_releases=1)")
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)")

snapshots['test_releases 1'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, in_favorites=False, runtime=2258, release_date=datetime.date(2014, 7, 8), image_id=1)")
]

snapshots['test_top_genres 1'] = [
    {
        'genre': GenericRepr("T(id=3, name='Folk', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=4, name='Rock', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=5, name='Country', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=6, name='World', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 1
    }
]

snapshots['test_update_fields 1'] = GenericRepr("T(id=2, name='New Name', starred=True, num_releases=1)")

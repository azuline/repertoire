# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_release 1'] = GenericRepr("T(id=2, name='Favorites', starred=True, type=<CollectionType.SYSTEM: 1>, num_releases=1, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))")

snapshots['test_add_release 2'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=FakeDatetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, in_favorites=True, rating=6, runtime=2258, release_date=FakeDate(2014, 7, 8), image_id=1)")
]

snapshots['test_del_release 1'] = GenericRepr("T(id=3, name='Folk', starred=False, type=<CollectionType.GENRE: 4>, num_releases=0, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))")

snapshots['test_del_release 2'] = [
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=7, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_releases 1'] = [
    GenericRepr("T(id=3, title='Departure', release_type=<ReleaseType.EP: 3>, added_on=FakeDatetime(2020, 10, 19, 8, 29, 34), release_year=2016, num_tracks=11, in_inbox=True, in_favorites=False, rating=None, runtime=3513, release_date=None, image_id=2)")
]

snapshots['test_search_all 1'] = [
    GenericRepr("T(id=2, name='Favorites', starred=True, type=<CollectionType.SYSTEM: 1>, num_releases=0, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))"),
    GenericRepr("T(id=1, name='Inbox', starred=True, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))"),
    GenericRepr("T(id=11, name='MyLabel', starred=False, type=<CollectionType.LABEL: 3>, num_releases=0, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=10, name='Ambient', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=5, name='Country', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=7, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=8, name='Electronic', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=3, name='Folk', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=9, name='House', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=4, name='Rock', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=6, name='World', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))")
]

snapshots['test_top_genres 1'] = [
    {
        'genre': GenericRepr("T(id=7, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=8, name='Electronic', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=9, name='House', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
        'num_matches': 1
    },
    {
        'genre': GenericRepr("T(id=10, name='Ambient', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=FakeDatetime(2020, 10, 19, 0, 25, 34))"),
        'num_matches': 1
    }
]

snapshots['test_update_fields 1'] = GenericRepr("T(id=4, name='New Name', starred=True, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))")

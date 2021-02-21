# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_entries 1'] = [
    GenericRepr('T(id=3, track_id=3, playlist_id=2, position=1, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))'),
    GenericRepr('T(id=4, track_id=4, playlist_id=2, position=2, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))'),
    GenericRepr('T(id=5, track_id=13, playlist_id=2, position=3, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))'),
    GenericRepr('T(id=6, track_id=14, playlist_id=2, position=4, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))'),
    GenericRepr('T(id=7, track_id=14, playlist_id=2, position=5, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))'),
    GenericRepr('T(id=8, track_id=15, playlist_id=2, position=6, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34))')
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=2, name='AAAAAA', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=6, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_search 1'] = [
    GenericRepr("T(id=1, name='Favorites', starred=True, type=<PlaylistType.SYSTEM: 1>, num_tracks=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=3, name='BBBBBB', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=0, last_updated_on=None)"),
    GenericRepr("T(id=2, name='AAAAAA', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=6, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")
]

snapshots['test_search_filter_type 1'] = [
    GenericRepr("T(id=3, name='BBBBBB', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=0, last_updated_on=None)"),
    GenericRepr("T(id=2, name='AAAAAA', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=6, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")
]

snapshots['test_search_filter_type_multiple 1'] = [
    GenericRepr("T(id=1, name='Favorites', starred=True, type=<PlaylistType.SYSTEM: 1>, num_tracks=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))"),
    GenericRepr("T(id=3, name='BBBBBB', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=0, last_updated_on=None)"),
    GenericRepr("T(id=2, name='AAAAAA', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=6, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")
]

snapshots['test_top_genres 1'] = [
    {
        'genre': GenericRepr("T(id=7, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 4
    },
    {
        'genre': GenericRepr("T(id=8, name='Electronic', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 4
    },
    {
        'genre': GenericRepr("T(id=9, name='House', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 4
    },
    {
        'genre': GenericRepr("T(id=10, name='Ambient', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 4
    },
    {
        'genre': GenericRepr("T(id=3, name='Folk', starred=False, type=<CollectionType.GENRE: 4>, num_releases=None, last_updated_on=None)"),
        'num_matches': 2
    }
]

snapshots['test_update_fields 1'] = GenericRepr("T(id=2, name='New Name', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=6, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

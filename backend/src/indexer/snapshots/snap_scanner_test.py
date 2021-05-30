# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_catalog_file 1'] = {
    'disc_number': '1',
    'duration': 2,
    'id': 1,
    'release_id': 2,
    'sha256': None,
    'sha256_initial': b'\x99\xae\x85\x16\xec,\xe5\x88\x88\xe7r)\xd8\xb0\xcc\xa2R\xc0Be\xb9\xcb\x9c\x86T\xe0\xf1\xc6\xac\xce\xda\xa0',
    'title': 'Track 1 (Artist AB Remix)',
    'track_number': '1'
}

snapshots['test_catalog_file 2'] = [
    {
        'artist': GenericRepr("T(id=3, name='Artist A', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=4, name='Artist C', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.FEATURE: 2>')
    },
    {
        'artist': GenericRepr("T(id=5, name='Artist AB', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.REMIXER: 3>')
    },
    {
        'artist': GenericRepr("T(id=6, name='Artist BC', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.REMIXER: 3>')
    },
    {
        'artist': GenericRepr("T(id=7, name='Artist CD', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    },
    {
        'artist': GenericRepr("T(id=8, name='Artist DE', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    },
    {
        'artist': GenericRepr("T(id=9, name='Artist EF', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    },
    {
        'artist': GenericRepr("T(id=10, name='Artist FG', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    },
    {
        'artist': GenericRepr("T(id=11, name='Artist GH', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.CONDUCTOR: 6>')
    },
    {
        'artist': GenericRepr("T(id=12, name='Artist HI', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.CONDUCTOR: 6>')
    },
    {
        'artist': GenericRepr("T(id=13, name='Artist IJ', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.DJMIXER: 7>')
    },
    {
        'artist': GenericRepr("T(id=14, name='Artist JK', num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.DJMIXER: 7>')
    }
]

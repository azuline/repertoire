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
    'sha256': b'\xb9\x91\x8c\xb7\xfd-_\xd1QU\x9d\x15\x98GK\x8bA,\xf3PX\xbc3E\xc1\x15\xa1\x14\x90\xd0\x80\xbc',
    'title': 'Track 1 (Artist AB Remix)',
    'track_number': '1'
}

snapshots['test_catalog_file 2'] = [
    {
        'artist': GenericRepr("T(id=3, name='Artist A', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=4, name='Artist C', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.FEATURE: 2>')
    },
    {
        'artist': GenericRepr("T(id=5, name='Artist AB', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.REMIXER: 3>')
    },
    {
        'artist': GenericRepr("T(id=6, name='Artist BC', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.REMIXER: 3>')
    },
    {
        'artist': GenericRepr("T(id=7, name='Artist CD', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    },
    {
        'artist': GenericRepr("T(id=8, name='Artist DE', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    },
    {
        'artist': GenericRepr("T(id=9, name='Artist EF', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    },
    {
        'artist': GenericRepr("T(id=10, name='Artist FG', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    },
    {
        'artist': GenericRepr("T(id=11, name='Artist GH', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.CONDUCTOR: 6>')
    },
    {
        'artist': GenericRepr("T(id=12, name='Artist HI', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.CONDUCTOR: 6>')
    },
    {
        'artist': GenericRepr("T(id=13, name='Artist IJ', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.DJMIXER: 7>')
    },
    {
        'artist': GenericRepr("T(id=14, name='Artist JK', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.DJMIXER: 7>')
    }
]

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
    'sha256_initial': b"\xed\xa5;\xe3\xb5\x0cR\xf0\x80E\x11&;\xaf\xbc\xab\xba\xc5\x18\xbf\xe4\\'y\xd3>EU\x15h\xd1\x05",
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

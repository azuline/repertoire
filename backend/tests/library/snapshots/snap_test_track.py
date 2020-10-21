# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_artist 1'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', favorite=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    },
    {
        'artist': GenericRepr("T(id=4, name='Abakus', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_new_role 1'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.REMIXER: 3>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', favorite=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    }
]

snapshots['test_artists 1'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', favorite=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    }
]

snapshots['test_del_artist 1'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')")

snapshots['test_update_fields 1'] = GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='New Title', release_id=2, duration=213, track_number='X Æ', disc_number='A-12')")

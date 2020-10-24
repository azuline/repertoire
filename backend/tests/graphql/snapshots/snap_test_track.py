# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_artist_to_track 1'] = (
    True,
    {
        'data': {
            'addArtistToTrack': {
                '__typename': 'Track',
                'artists': [
                    {
                        'artist': {
                            'id': 2
                        },
                        'role': 'MAIN'
                    },
                    {
                        'artist': {
                            'id': 3
                        },
                        'role': 'MAIN'
                    }
                ],
                'discNumber': '1',
                'duration': 213,
                'id': 1,
                'release': {
                    'id': 2
                },
                'title': 'Our Apartment',
                'trackNumber': '1'
            }
        }
    }
)

snapshots['test_add_artist_to_track 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', favorite=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_to_track_already_exists 1'] = (
    True,
    {
        'data': {
            'addArtistToTrack': {
                '__typename': 'Error',
                'error': 'ALREADY_EXISTS',
                'message': 'Artist is already on track.'
            }
        }
    }
)

snapshots['test_add_artist_to_track_already_exists 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_to_track_bad_artist 1'] = (
    True,
    {
        'data': {
            'addArtistToTrack': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Artist does not exist.'
            }
        }
    }
)

snapshots['test_add_artist_to_track_bad_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_to_track_bad_track 1'] = (
    True,
    {
        'data': {
            'addArtistToTrack': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Track does not exist.'
            }
        }
    }
)

snapshots['test_add_artist_to_track_no_auth 1'] = (
    True,
    {
        'data': {
            'addArtistToTrack': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_del_artist_from_track 1'] = (
    True,
    {
        'data': {
            'delArtistFromTrack': {
                '__typename': 'Track',
                'artists': [
                ],
                'discNumber': '1',
                'duration': 213,
                'id': 1,
                'release': {
                    'id': 2
                },
                'title': 'Our Apartment',
                'trackNumber': '1'
            }
        }
    }
)

snapshots['test_del_artist_from_track 2'] = [
]

snapshots['test_del_artist_from_track_bad_artist 1'] = (
    True,
    {
        'data': {
            'delArtistFromTrack': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Artist does not exist.'
            }
        }
    }
)

snapshots['test_del_artist_from_track_bad_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', favorite=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_del_artist_from_track_bad_track 1'] = (
    True,
    {
        'data': {
            'delArtistFromTrack': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Track does not exist.'
            }
        }
    }
)

snapshots['test_del_artist_from_track_doesnt_exist 1'] = (
    True,
    {
        'data': {
            'delArtistFromTrack': {
                '__typename': 'Error',
                'error': 'DOES_NOT_EXIST',
                'message': 'Artist is not on track.'
            }
        }
    }
)

snapshots['test_del_artist_from_track_no_auth 1'] = (
    True,
    {
        'data': {
            'delArtistFromTrack': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_track 1'] = (
    True,
    {
        'data': {
            'track': {
                '__typename': 'Track',
                'artists': [
                    {
                        'artist': {
                            'id': 2
                        },
                        'role': 'MAIN'
                    },
                    {
                        'artist': {
                            'id': 3
                        },
                        'role': 'COMPOSER'
                    }
                ],
                'discNumber': '1',
                'duration': 153,
                'id': 10,
                'release': {
                    'id': 2
                },
                'title': 'Going to Georgia',
                'trackNumber': '10'
            }
        }
    }
)

snapshots['test_track_no_auth 1'] = (
    True,
    {
        'data': {
            'track': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_track_not_found 1'] = (
    True,
    {
        'data': {
            'track': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Track 999 not found.'
            }
        }
    }
)

snapshots['test_update_track 1'] = (
    True,
    {
        'data': {
            'updateTrack': {
                '__typename': 'Track',
                'artists': [
                    {
                        'artist': {
                            'id': 2
                        },
                        'role': 'MAIN'
                    }
                ],
                'discNumber': '899',
                'duration': 252,
                'id': 2,
                'release': {
                    'id': 3
                },
                'title': 'aa',
                'trackNumber': '999'
            }
        }
    }
)

snapshots['test_update_track 2'] = GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='aa', release_id=3, duration=252, track_number='999', disc_number='899')")

snapshots['test_update_track_bad_release_id 1'] = (
    True,
    {
        'data': {
            'updateTrack': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Release does not exist.'
            }
        }
    }
)

snapshots['test_update_track_bad_release_id 2'] = GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')")

snapshots['test_update_track_no_auth 1'] = (
    True,
    {
        'data': {
            'updateTrack': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_update_track_not_found 1'] = (
    True,
    {
        'data': {
            'updateTrack': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Track 99999 does not exist.'
            }
        }
    }
)

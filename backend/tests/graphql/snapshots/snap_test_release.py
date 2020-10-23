# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_release 1'] = (
    True,
    {
        'data': {
            'release': {
                '__typename': 'Release',
                'addedOn': 1603096174,
                'artists': [
                    {
                        'id': 4
                    },
                    {
                        'id': 5
                    }
                ],
                'collages': [
                ],
                'genres': [
                    {
                        'id': 16
                    },
                    {
                        'id': 17
                    },
                    {
                        'id': 18
                    },
                    {
                        'id': 19
                    }
                ],
                'id': 3,
                'imagePath': '/data/cover_art/d832df509b44cb7c560e2579453178016c391cd2ab8d6eab3de2bbbdf75c4ac0.jpg',
                'inInbox': True,
                'labels': [
                ],
                'numTracks': 11,
                'releaseDate': None,
                'releaseType': 'EP',
                'releaseYear': 2016,
                'title': 'Departure',
                'tracks': [
                    {
                        'id': 11
                    },
                    {
                        'id': 12
                    },
                    {
                        'id': 13
                    },
                    {
                        'id': 14
                    },
                    {
                        'id': 15
                    },
                    {
                        'id': 16
                    },
                    {
                        'id': 17
                    },
                    {
                        'id': 18
                    },
                    {
                        'id': 19
                    },
                    {
                        'id': 20
                    },
                    {
                        'id': 21
                    }
                ]
            }
        }
    }
)

snapshots['test_release_no_auth 1'] = (
    True,
    {
        'data': {
            'release': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_release_not_found 1'] = (
    True,
    {
        'data': {
            'release': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Release 999 not found.'
            }
        }
    }
)

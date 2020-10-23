# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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

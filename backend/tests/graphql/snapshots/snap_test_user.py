# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_new_token_no_auth 1'] = (
    True,
    {
        'data': {
            'newToken': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 9,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'newToken'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_user 1'] = (
    True,
    {
        'data': {
            'user': {
                'id': 1,
                'username': 'admin'
            }
        }
    }
)

snapshots['test_user_no_auth 1'] = (
    True,
    {
        'data': {
            'user': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 9,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'user'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

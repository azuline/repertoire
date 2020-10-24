# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_new_token_no_auth 1'] = (
    True,
    {
        'data': {
            'newToken': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_user 1'] = (
    True,
    {
        'data': {
            'user': {
                '__typename': 'User',
                'id': 1
            }
        }
    }
)

snapshots['test_user_no_auth 1'] = (
    True,
    {
        'data': {
            'user': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

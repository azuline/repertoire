# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_update_user 1'] = (
    True,
    {
        'data': {
            'updateUser': {
                'id': 1,
                'nickname': 'not admin'
            }
        }
    }
)

snapshots['test_user 1'] = (
    True,
    {
        'data': {
            'user': {
                'id': 1,
                'nickname': 'admin'
            }
        }
    }
)

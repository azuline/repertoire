# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_update_config_bad_crontab 1'] = {
    'data': {
        'updateConfig': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': '1 1 * 2 * 7 3 is not a valid crontab.',
            'path': [
                'updateConfig'
            ]
        }
    ]
}

snapshots['test_update_config_bad_directory 1'] = {
    'data': {
        'updateConfig': {
            'indexCrontab': '0 0 * * *',
            'musicDirectories': [
                {
                    'directory': '/not_a_directory_lol',
                    'existsOnDisk': False
                }
            ]
        }
    }
}

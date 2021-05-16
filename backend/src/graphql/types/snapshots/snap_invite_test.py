# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_invite 1'] = {
    'data': {
        'createInvite': {
            'createdAt': 1577840461,
            'createdBy': {
                'id': 1
            },
            'id': 5,
            'usedBy': None
        }
    }
}

snapshots['test_invite 1'] = {
    'data': {
        'invite': {
            'createdAt': 1577840461,
            'createdBy': {
                'id': 1
            },
            'id': 1,
            'usedBy': None
        }
    }
}

snapshots['test_invite_not_found 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Invite 999999 does not exist.',
            'path': [
                'invite'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_invites 1'] = {
    'data': {
        'invites': {
            'results': [
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 1
                    },
                    'id': 1,
                    'usedBy': None
                },
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 2
                    },
                    'id': 2,
                    'usedBy': None
                }
            ],
            'total': 2
        }
    }
}

snapshots['test_invites_created_by 1'] = {
    'data': {
        'invites': {
            'results': [
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 1
                    },
                    'id': 1,
                    'usedBy': None
                }
            ],
            'total': 1
        }
    }
}

snapshots['test_invites_filter_expired 1'] = {
    'data': {
        'invites': {
            'results': [
                {
                    'createdAt': 1577667661,
                    'createdBy': {
                        'id': 1
                    },
                    'id': 3,
                    'usedBy': None
                },
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 1
                    },
                    'id': 1,
                    'usedBy': None
                },
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 2
                    },
                    'id': 2,
                    'usedBy': None
                }
            ],
            'total': 3
        }
    }
}

snapshots['test_invites_filter_used 1'] = {
    'data': {
        'invites': {
            'results': [
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 1
                    },
                    'id': 1,
                    'usedBy': None
                },
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 2
                    },
                    'id': 2,
                    'usedBy': None
                },
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 1
                    },
                    'id': 4,
                    'usedBy': {
                        'id': 2
                    }
                }
            ],
            'total': 3
        }
    }
}

snapshots['test_invites_pagination 1'] = {
    'data': {
        'invites': {
            'results': [
                {
                    'createdAt': 1577840461,
                    'createdBy': {
                        'id': 2
                    },
                    'id': 2,
                    'usedBy': None
                }
            ],
            'total': 2
        }
    }
}

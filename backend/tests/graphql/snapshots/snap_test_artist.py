# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_artist 1'] = (
    True,
    {
        'data': {
            'artist': {
                '__typename': 'Artist',
                'favorite': False,
                'id': 4,
                'name': 'Abakus',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 3
                    }
                ],
                'topGenres': [
                    {
                        'genre': {
                            'id': 16
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 17
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 18
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 19
                        },
                        'numMatches': 1
                    }
                ]
            }
        }
    }
)

snapshots['test_artist_from_name 1'] = (
    True,
    {
        'data': {
            'artistFromName': {
                '__typename': 'Artist',
                'favorite': False,
                'id': 4,
                'name': 'Abakus',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 3
                    }
                ],
                'topGenres': [
                    {
                        'genre': {
                            'id': 16
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 17
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 18
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 19
                        },
                        'numMatches': 1
                    }
                ]
            }
        }
    }
)

snapshots['test_artist_from_name_no_auth 1'] = (
    True,
    {
        'data': {
            'artistFromName': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_artist_from_name_not_found 1'] = (
    True,
    {
        'data': {
            'artistFromName': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Artist "Random Artist name" does not exist.'
            }
        }
    }
)

snapshots['test_artist_no_auth 1'] = (
    True,
    {
        'data': {
            'artist': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_artist_no_auth_not_found 1'] = (
    True,
    {
        'data': {
            'artist': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Artist 999999 does not exist.'
            }
        }
    }
)

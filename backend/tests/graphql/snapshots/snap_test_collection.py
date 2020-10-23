# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_collection 1'] = (
    True,
    {
        'data': {
            'collection': {
                '__typename': 'Collection',
                'favorite': False,
                'id': 12,
                'lastUpdatedOn': 1603067134,
                'name': 'Folk',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2
                    }
                ],
                'topGenres': [
                    {
                        'genre': {
                            'id': 12
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 13
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 14
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 15
                        },
                        'numMatches': 1
                    }
                ],
                'type': 'GENRE'
            }
        }
    }
)

snapshots['test_collection_from_name_and_type 1'] = (
    True,
    {
        'data': {
            'collectionFromNameAndType': {
                '__typename': 'Collection',
                'favorite': False,
                'id': 12,
                'lastUpdatedOn': 1603067134,
                'name': 'Folk',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2
                    }
                ],
                'topGenres': [
                    {
                        'genre': {
                            'id': 12
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 13
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 14
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 15
                        },
                        'numMatches': 1
                    }
                ],
                'type': 'GENRE'
            }
        }
    }
)

snapshots['test_collection_from_name_and_type_no_auth 1'] = (
    True,
    {
        'data': {
            'collectionFromNameAndType': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_collection_from_name_and_type_not_found 1'] = (
    True,
    {
        'data': {
            'collectionFromNameAndType': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Collection "AAFEFOPAIEFPAJF" of type COLLAGE not found.'
            }
        }
    }
)

snapshots['test_collection_no_auth 1'] = (
    True,
    {
        'data': {
            'collection': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_collection_not_found 1'] = (
    True,
    {
        'data': {
            'collection': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Collection 999999 not found.'
            }
        }
    }
)

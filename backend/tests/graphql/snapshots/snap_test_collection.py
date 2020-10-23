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

snapshots['test_collections 1'] = (
    True,
    {
        'data': {
            'collections': {
                '__typename': 'Collections',
                'results': [
                    {
                        'favorite': False,
                        'id': 1,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Inbox',
                        'numReleases': 2,
                        'releases': [
                            {
                                'id': 2
                            },
                            {
                                'id': 3
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
                            },
                            {
                                'genre': {
                                    'id': 16
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'favorite': False,
                        'id': 2,
                        'lastUpdatedOn': None,
                        'name': 'Favorite',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'favorite': False,
                        'id': 3,
                        'lastUpdatedOn': None,
                        'name': '1',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 4,
                        'lastUpdatedOn': None,
                        'name': '2',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 5,
                        'lastUpdatedOn': None,
                        'name': '3',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 6,
                        'lastUpdatedOn': None,
                        'name': '4',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 7,
                        'lastUpdatedOn': None,
                        'name': '5',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 8,
                        'lastUpdatedOn': None,
                        'name': '6',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 9,
                        'lastUpdatedOn': None,
                        'name': '7',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 10,
                        'lastUpdatedOn': None,
                        'name': '8',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'favorite': False,
                        'id': 11,
                        'lastUpdatedOn': None,
                        'name': '9',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
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
                    },
                    {
                        'favorite': False,
                        'id': 13,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Rock',
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
                    },
                    {
                        'favorite': False,
                        'id': 14,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Country',
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
                    },
                    {
                        'favorite': False,
                        'id': 15,
                        'lastUpdatedOn': 1603067134,
                        'name': 'World',
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
                    },
                    {
                        'favorite': False,
                        'id': 16,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Downtempo',
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
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'favorite': False,
                        'id': 17,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Electronic',
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
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'favorite': False,
                        'id': 18,
                        'lastUpdatedOn': 1603067134,
                        'name': 'House',
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
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'favorite': False,
                        'id': 19,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Ambient',
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
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'favorite': False,
                        'id': 20,
                        'lastUpdatedOn': None,
                        'name': 'MyLabel',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'topGenres': [
                        ],
                        'type': 'LABEL'
                    }
                ]
            }
        }
    }
)

snapshots['test_collections_no_auth 1'] = (
    True,
    {
        'data': {
            'collections': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_collections_type_param 1'] = (
    True,
    {
        'data': {
            'collections': {
                '__typename': 'Collections',
                'results': [
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
                    }
                ]
            }
        }
    }
)

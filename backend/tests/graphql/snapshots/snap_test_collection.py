# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_release_to_collection 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': {
                'id': 2,
                'lastUpdatedOn': None,
                'name': 'Favorites',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2
                    }
                ],
                'starred': True,
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
                'type': 'SYSTEM'
            }
        }
    }
)

snapshots['test_add_release_to_collection 2'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, in_favorites=True, runtime=2258, release_date=datetime.date(2014, 7, 8), image_id=1)")
]

snapshots['test_add_release_to_collection_already_exists 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release is already in collection.',
                'path': [
                    'addReleaseToCollection'
                ],
                'type': 'AlreadyExists'
            }
        ]
    }
)

snapshots['test_add_release_to_collection_already_exists 2'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, in_favorites=False, runtime=2258, release_date=datetime.date(2014, 7, 8), image_id=1)")
]

snapshots['test_add_release_to_collection_bad_collection 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection 999 does not exist.',
                'path': [
                    'addReleaseToCollection'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_add_release_to_collection_bad_release 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Releasse 9999 does not exist.',
                'path': [
                    'addReleaseToCollection'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_add_release_to_collection_bad_release 2'] = [
]

snapshots['test_collection 1'] = (
    True,
    {
        'data': {
            'collection': {
                'id': 12,
                'lastUpdatedOn': 1603067134,
                'name': 'Folk',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2
                    }
                ],
                'starred': False,
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
                'id': 12,
                'lastUpdatedOn': 1603067134,
                'name': 'Folk',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2
                    }
                ],
                'starred': False,
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

snapshots['test_collection_from_name_and_type_not_found 1'] = (
    True,
    {
        'data': {
            'collectionFromNameAndType': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection "AAFEFOPAIEFPAJF" of type COLLAGE not found.',
                'path': [
                    'collectionFromNameAndType'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_collection_not_found 1'] = (
    True,
    {
        'data': {
            'collection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection 999999 not found.',
                'path': [
                    'collection'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_collections 1'] = (
    True,
    {
        'data': {
            'collections': {
                'results': [
                    {
                        'id': 2,
                        'lastUpdatedOn': None,
                        'name': 'Favorites',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': True,
                        'topGenres': [
                        ],
                        'type': 'SYSTEM'
                    },
                    {
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
                        'starred': True,
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
                        'id': 20,
                        'lastUpdatedOn': None,
                        'name': 'MyLabel',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'LABEL'
                    },
                    {
                        'id': 19,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Ambient',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 14,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Country',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 16,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Downtempo',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 17,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Electronic',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 12,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Folk',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 18,
                        'lastUpdatedOn': 1603067134,
                        'name': 'House',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 13,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Rock',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 15,
                        'lastUpdatedOn': 1603067134,
                        'name': 'World',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 3,
                        'lastUpdatedOn': None,
                        'name': '1',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 4,
                        'lastUpdatedOn': None,
                        'name': '2',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 5,
                        'lastUpdatedOn': None,
                        'name': '3',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 6,
                        'lastUpdatedOn': None,
                        'name': '4',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 7,
                        'lastUpdatedOn': None,
                        'name': '5',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 8,
                        'lastUpdatedOn': None,
                        'name': '6',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 9,
                        'lastUpdatedOn': None,
                        'name': '7',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 10,
                        'lastUpdatedOn': None,
                        'name': '8',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    },
                    {
                        'id': 11,
                        'lastUpdatedOn': None,
                        'name': '9',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ],
                        'type': 'RATING'
                    }
                ]
            }
        }
    }
)

snapshots['test_collections_type_param 1'] = (
    True,
    {
        'data': {
            'collections': {
                'results': [
                    {
                        'id': 2,
                        'lastUpdatedOn': None,
                        'name': 'Favorites',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': True,
                        'topGenres': [
                        ],
                        'type': 'SYSTEM'
                    },
                    {
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
                        'starred': True,
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
                        'id': 19,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Ambient',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 14,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Country',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 16,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Downtempo',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 17,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Electronic',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 12,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Folk',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 18,
                        'lastUpdatedOn': 1603067134,
                        'name': 'House',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3
                            }
                        ],
                        'starred': False,
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
                        'id': 13,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Rock',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                        'id': 15,
                        'lastUpdatedOn': 1603067134,
                        'name': 'World',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2
                            }
                        ],
                        'starred': False,
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
                ]
            }
        }
    }
)

snapshots['test_create_collection 1'] = (
    True,
    {
        'data': {
            'createCollection': {
                'id': 21,
                'lastUpdatedOn': None,
                'name': 'NewCollection',
                'numReleases': 0,
                'releases': [
                ],
                'starred': True,
                'topGenres': [
                ],
                'type': 'COLLAGE'
            }
        }
    }
)

snapshots['test_create_collection 2'] = GenericRepr("T(id=21, name='NewCollection', starred=True, type=<CollectionType.COLLAGE: 2>, num_releases=0, last_updated_on=None)")

snapshots['test_create_collection_duplicate 1'] = (
    True,
    {
        'data': {
            'createCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection "Folk" already exists.',
                'path': [
                    'createCollection'
                ],
                'type': 'Duplicate'
            }
        ]
    }
)

snapshots['test_del_release_from_collection 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': {
                'id': 1,
                'lastUpdatedOn': 1603067134,
                'name': 'Inbox',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 3
                    }
                ],
                'starred': True,
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
                'type': 'SYSTEM'
            }
        }
    }
)

snapshots['test_del_release_from_collection 2'] = [
    GenericRepr("T(id=3, title='Departure', release_type=<ReleaseType.EP: 3>, added_on=datetime.datetime(2020, 10, 19, 8, 29, 34), release_year=2016, num_tracks=12, in_inbox=True, in_favorites=False, runtime=3515, release_date=None, image_id=2)")
]

snapshots['test_del_release_from_collection_bad_collection 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection 999 does not exist.',
                'path': [
                    'delReleaseFromCollection'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_del_release_from_collection_bad_release 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release 9999 does not exist.',
                'path': [
                    'delReleaseFromCollection'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_del_release_from_collection_bad_release 2'] = [
]

snapshots['test_del_release_from_collection_doesnt_exist 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release is not in collection.',
                'path': [
                    'delReleaseFromCollection'
                ],
                'type': 'DoesNotExist'
            }
        ]
    }
)

snapshots['test_update_collection 1'] = (
    True,
    {
        'data': {
            'updateCollection': {
                'id': 12,
                'lastUpdatedOn': 1603067134,
                'name': 'NewCollection',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2
                    }
                ],
                'starred': True,
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

snapshots['test_update_collection 2'] = GenericRepr("T(id=12, name='NewCollection', starred=True, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_collection_duplicate 1'] = (
    True,
    {
        'data': {
            'updateCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection "Folk" already exists.',
                'path': [
                    'updateCollection'
                ],
                'type': 'Duplicate'
            }
        ]
    }
)

snapshots['test_update_collection_duplicate 2'] = GenericRepr("T(id=16, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_collection_immutable 1'] = (
    True,
    {
        'data': {
            'updateCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'System and rating collections cannot be modified.',
                'path': [
                    'updateCollection'
                ],
                'type': 'Immutable'
            }
        ]
    }
)

snapshots['test_update_collection_immutable 2'] = GenericRepr("T(id=1, name='Inbox', starred=True, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_collection_not_found 1'] = (
    True,
    {
        'data': {
            'updateCollection': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Collection 99999 does not exist.',
                'path': [
                    'updateCollection'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

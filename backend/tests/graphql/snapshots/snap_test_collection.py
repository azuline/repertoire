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
                'collection': {
                    'id': 2,
                    'lastUpdatedOn': None,
                    'name': 'Favorites',
                    'numReleases': 1,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        }
                    ],
                    'starred': True,
                    'topGenres': [
                        {
                            'genre': {
                                'id': 3
                            },
                            'numMatches': 1
                        },
                        {
                            'genre': {
                                'id': 4
                            },
                            'numMatches': 1
                        },
                        {
                            'genre': {
                                'id': 5
                            },
                            'numMatches': 1
                        },
                        {
                            'genre': {
                                'id': 6
                            },
                            'numMatches': 1
                        }
                    ],
                    'type': 'SYSTEM'
                },
                'release': {
                    'addedOn': 1603067134,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Aaron West and the Roaring Twenties'
                        }
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 3,
                            'name': 'Folk'
                        },
                        {
                            'id': 4,
                            'name': 'Rock'
                        },
                        {
                            'id': 5,
                            'name': 'Country'
                        },
                        {
                            'id': 6,
                            'name': 'World'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': True,
                    'inInbox': True,
                    'labels': [
                    ],
                    'numTracks': 10,
                    'releaseDate': '2014-07-08',
                    'releaseType': 'ALBUM',
                    'releaseYear': 2014,
                    'runtime': 2258,
                    'title': 'We Don’t Have Each Other',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Our Apartment'
                        },
                        {
                            'id': 2,
                            'title': 'Grapefruit'
                        },
                        {
                            'id': 3,
                            'title': 'St. Joe Keeps Us Safe'
                        },
                        {
                            'id': 4,
                            'title': 'Runnin’ Scared'
                        },
                        {
                            'id': 5,
                            'title': 'Divorce and the American South'
                        },
                        {
                            'id': 6,
                            'title': 'The Thunderbird Inn'
                        },
                        {
                            'id': 7,
                            'title': 'Get Me Out of Here Alive'
                        },
                        {
                            'id': 8,
                            'title': 'You Ain’t No Saint'
                        },
                        {
                            'id': 9,
                            'title': 'Carolina Coast'
                        },
                        {
                            'id': 10,
                            'title': 'Going to Georgia'
                        }
                    ]
                }
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
                'id': 3,
                'lastUpdatedOn': 1603067134,
                'name': 'Folk',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 4
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 5
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 6
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
                'id': 3,
                'lastUpdatedOn': 1603067134,
                'name': 'Folk',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 4
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 5
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 6
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
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            },
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': True,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'id': 11,
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
                        'id': 10,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Ambient',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 5,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Country',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 7,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Downtempo',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 8,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Electronic',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 3,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Folk',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 9,
                        'lastUpdatedOn': 1603067134,
                        'name': 'House',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 4,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Rock',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 6,
                        'lastUpdatedOn': 1603067134,
                        'name': 'World',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
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
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            },
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': True,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'id': 10,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Ambient',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 5,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Country',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 7,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Downtempo',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 8,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Electronic',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 3,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Folk',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 9,
                        'lastUpdatedOn': 1603067134,
                        'name': 'House',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Departure'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 4,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Rock',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 1
                            }
                        ],
                        'type': 'GENRE'
                    },
                    {
                        'id': 6,
                        'lastUpdatedOn': 1603067134,
                        'name': 'World',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'We Don’t Have Each Other'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 1
                            },
                            {
                                'genre': {
                                    'id': 6
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
                'id': 12,
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

snapshots['test_create_collection 2'] = GenericRepr("T(id=12, name='NewCollection', starred=True, type=<CollectionType.COLLAGE: 2>, num_releases=0, last_updated_on=None)")

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
                'collection': {
                    'id': 1,
                    'lastUpdatedOn': 1603067134,
                    'name': 'Inbox',
                    'numReleases': 1,
                    'releases': [
                        {
                            'id': 3,
                            'title': 'Departure'
                        }
                    ],
                    'starred': True,
                    'topGenres': [
                        {
                            'genre': {
                                'id': 7
                            },
                            'numMatches': 1
                        },
                        {
                            'genre': {
                                'id': 8
                            },
                            'numMatches': 1
                        },
                        {
                            'genre': {
                                'id': 9
                            },
                            'numMatches': 1
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 1
                        }
                    ],
                    'type': 'SYSTEM'
                },
                'release': {
                    'addedOn': 1603067134,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Aaron West and the Roaring Twenties'
                        }
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 3,
                            'name': 'Folk'
                        },
                        {
                            'id': 4,
                            'name': 'Rock'
                        },
                        {
                            'id': 5,
                            'name': 'Country'
                        },
                        {
                            'id': 6,
                            'name': 'World'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                    ],
                    'numTracks': 10,
                    'releaseDate': '2014-07-08',
                    'releaseType': 'ALBUM',
                    'releaseYear': 2014,
                    'runtime': 2258,
                    'title': 'We Don’t Have Each Other',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Our Apartment'
                        },
                        {
                            'id': 2,
                            'title': 'Grapefruit'
                        },
                        {
                            'id': 3,
                            'title': 'St. Joe Keeps Us Safe'
                        },
                        {
                            'id': 4,
                            'title': 'Runnin’ Scared'
                        },
                        {
                            'id': 5,
                            'title': 'Divorce and the American South'
                        },
                        {
                            'id': 6,
                            'title': 'The Thunderbird Inn'
                        },
                        {
                            'id': 7,
                            'title': 'Get Me Out of Here Alive'
                        },
                        {
                            'id': 8,
                            'title': 'You Ain’t No Saint'
                        },
                        {
                            'id': 9,
                            'title': 'Carolina Coast'
                        },
                        {
                            'id': 10,
                            'title': 'Going to Georgia'
                        }
                    ]
                }
            }
        }
    }
)

snapshots['test_del_release_from_collection 2'] = [
    GenericRepr("T(id=3, title='Departure', release_type=<ReleaseType.EP: 3>, added_on=datetime.datetime(2020, 10, 19, 8, 29, 34), release_year=2016, num_tracks=11, in_inbox=True, in_favorites=False, runtime=3513, release_date=None, image_id=2)")
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
                'id': 3,
                'lastUpdatedOn': 1603067134,
                'name': 'NewCollection',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'starred': True,
                'topGenres': [
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 4
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 5
                        },
                        'numMatches': 1
                    },
                    {
                        'genre': {
                            'id': 6
                        },
                        'numMatches': 1
                    }
                ],
                'type': 'GENRE'
            }
        }
    }
)

snapshots['test_update_collection 2'] = GenericRepr("T(id=3, name='NewCollection', starred=True, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

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

snapshots['test_update_collection_duplicate 2'] = GenericRepr("T(id=7, name='Downtempo', starred=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

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
                'message': 'System collections cannot be modified.',
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

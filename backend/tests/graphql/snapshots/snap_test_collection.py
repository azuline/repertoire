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
                '__typename': 'Collection',
                'favorite': False,
                'id': 2,
                'lastUpdatedOn': None,
                'name': 'Favorite',
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
                'type': 'SYSTEM'
            }
        }
    }
)

snapshots['test_add_release_to_collection 2'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, release_date=datetime.date(2014, 7, 8), image_path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")
]

snapshots['test_add_release_to_collection_already_exists 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': {
                '__typename': 'Error',
                'error': 'ALREADY_EXISTS',
                'message': 'Release is already in collection.'
            }
        }
    }
)

snapshots['test_add_release_to_collection_already_exists 2'] = [
    GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, release_date=datetime.date(2014, 7, 8), image_path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")
]

snapshots['test_add_release_to_collection_bad_collection 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Collection does not exist.'
            }
        }
    }
)

snapshots['test_add_release_to_collection_bad_release 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Releasse 9999 does not exist.'
            }
        }
    }
)

snapshots['test_add_release_to_collection_bad_release 2'] = [
]

snapshots['test_add_release_to_collection_no_auth 1'] = (
    True,
    {
        'data': {
            'addReleaseToCollection': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

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
                '__typename': 'Collection',
                'favorite': True,
                'id': 21,
                'lastUpdatedOn': None,
                'name': 'NewCollection',
                'numReleases': 0,
                'releases': [
                ],
                'topGenres': [
                ],
                'type': 'COLLAGE'
            }
        }
    }
)

snapshots['test_create_collection 2'] = GenericRepr("T(id=21, name='NewCollection', favorite=True, type=<CollectionType.COLLAGE: 2>, num_releases=0, last_updated_on=None)")

snapshots['test_create_collection_duplicate 1'] = (
    True,
    {
        'data': {
            'createCollection': {
                '__typename': 'Error',
                'error': 'DUPLICATE',
                'message': 'Collection "Folk" already exists.'
            }
        }
    }
)

snapshots['test_del_release_from_collection 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': {
                '__typename': 'Collection',
                'favorite': False,
                'id': 1,
                'lastUpdatedOn': 1603067134,
                'name': 'Inbox',
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
                'type': 'SYSTEM'
            }
        }
    }
)

snapshots['test_del_release_from_collection 2'] = [
    GenericRepr("T(id=3, title='Departure', release_type=<ReleaseType.EP: 3>, added_on=datetime.datetime(2020, 10, 19, 8, 29, 34), release_year=2016, num_tracks=11, in_inbox=True, release_date=None, image_path=PosixPath('/data/cover_art/d832df509b44cb7c560e2579453178016c391cd2ab8d6eab3de2bbbdf75c4ac0.jpg'))")
]

snapshots['test_del_release_from_collection_bad_collection 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Collection does not exist.'
            }
        }
    }
)

snapshots['test_del_release_from_collection_bad_release 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Release 9999 does not exist.'
            }
        }
    }
)

snapshots['test_del_release_from_collection_bad_release 2'] = [
]

snapshots['test_del_release_from_collection_doesnt_exist 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': {
                '__typename': 'Error',
                'error': 'DOES_NOT_EXIST',
                'message': 'Release is not in collection.'
            }
        }
    }
)

snapshots['test_del_release_from_collection_no_auth 1'] = (
    True,
    {
        'data': {
            'delReleaseFromCollection': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_dreate_collection_no_auth 1'] = (
    True,
    {
        'data': {
            'createCollection': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_update_collection 1'] = (
    True,
    {
        'data': {
            'updateCollection': {
                '__typename': 'Collection',
                'favorite': True,
                'id': 12,
                'lastUpdatedOn': 1603067134,
                'name': 'NewCollection',
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

snapshots['test_update_collection 2'] = GenericRepr("T(id=12, name='NewCollection', favorite=True, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_collection_duplicate 1'] = (
    True,
    {
        'data': {
            'updateCollection': {
                '__typename': 'Error',
                'error': 'DUPLICATE',
                'message': 'Collection "Folk" already exists.'
            }
        }
    }
)

snapshots['test_update_collection_duplicate 2'] = GenericRepr("T(id=16, name='Downtempo', favorite=False, type=<CollectionType.GENRE: 4>, num_releases=1, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_collection_immutable 1'] = (
    True,
    {
        'data': {
            'updateCollection': {
                '__typename': 'Error',
                'error': 'IMMUTABLE',
                'message': 'Collection "Inbox" cannot be updated.'
            }
        }
    }
)

snapshots['test_update_collection_immutable 2'] = GenericRepr("T(id=1, name='Inbox', favorite=False, type=<CollectionType.SYSTEM: 1>, num_releases=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_collection_no_auth 1'] = (
    True,
    {
        'data': {
            'updateCollection': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_update_collection_not_found 1'] = (
    True,
    {
        'data': {
            'updateCollection': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Collection 99999 does not exist.'
            }
        }
    }
)

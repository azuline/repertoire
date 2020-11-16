# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_artist_to_release 1'] = (
    True,
    {
        'data': {
            'addArtistToRelease': {
                'addedOn': 1603067134,
                'artists': [
                    {
                        'id': 2
                    },
                    {
                        'id': 3
                    }
                ],
                'collages': [
                ],
                'genres': [
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
                    }
                ],
                'hasCover': True,
                'id': 2,
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
                        'id': 1
                    },
                    {
                        'id': 2
                    },
                    {
                        'id': 3
                    },
                    {
                        'id': 4
                    },
                    {
                        'id': 5
                    },
                    {
                        'id': 6
                    },
                    {
                        'id': 7
                    },
                    {
                        'id': 8
                    },
                    {
                        'id': 9
                    },
                    {
                        'id': 10
                    }
                ]
            }
        }
    }
)

snapshots['test_add_artist_to_release 2'] = [
    GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
    GenericRepr("T(id=3, name='John Darnielle', starred=False, num_releases=1)")
]

snapshots['test_add_artist_to_release_already_exists 1'] = (
    True,
    {
        'data': {
            'addArtistToRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist is already on release.',
                'path': [
                    'addArtistToRelease'
                ],
                'type': 'AlreadyExists'
            }
        ]
    }
)

snapshots['test_add_artist_to_release_already_exists 2'] = [
    GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)")
]

snapshots['test_add_artist_to_release_bad_artist 1'] = (
    True,
    {
        'data': {
            'addArtistToRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist 9999 does not exist.',
                'path': [
                    'addArtistToRelease'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_add_artist_to_release_bad_artist 2'] = [
    GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)")
]

snapshots['test_add_artist_to_release_bad_release 1'] = (
    True,
    {
        'data': {
            'addArtistToRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release 999 does not exist.',
                'path': [
                    'addArtistToRelease'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_add_artist_to_release_no_auth 1'] = (
    True,
    {
        'data': {
            'addArtistToRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'addArtistToRelease'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_create_release 1'] = {
    'data': {
        'createRelease': {
            'artists': [
                {
                    'id': 2
                },
                {
                    'id': 3
                }
            ],
            'collages': [
            ],
            'genres': [
            ],
            'hasCover': False,
            'id': 4,
            'inInbox': False,
            'labels': [
            ],
            'numTracks': 0,
            'releaseDate': '2020-10-23',
            'releaseType': 'ALBUM',
            'releaseYear': 2020,
            'runtime': 0,
            'title': 'aa',
            'tracks': [
            ]
        }
    }
}

snapshots['test_create_release_bad_artists 1'] = (
    True,
    {
        'data': {
            'createRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist(s) 9999 do not exist.',
                'path': [
                    'createRelease'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_create_release_bad_date 1'] = (
    True,
    {
        'data': {
            'createRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid release date.',
                'path': [
                    'createRelease'
                ],
                'type': 'ParseError'
            }
        ]
    }
)

snapshots['test_create_release_no_auth 1'] = (
    True,
    {
        'data': {
            'createRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'createRelease'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_del_artist_from_release 1'] = (
    True,
    {
        'data': {
            'delArtistFromRelease': {
                'addedOn': 1603067134,
                'artists': [
                ],
                'collages': [
                ],
                'genres': [
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
                    }
                ],
                'hasCover': True,
                'id': 2,
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
                        'id': 1
                    },
                    {
                        'id': 2
                    },
                    {
                        'id': 3
                    },
                    {
                        'id': 4
                    },
                    {
                        'id': 5
                    },
                    {
                        'id': 6
                    },
                    {
                        'id': 7
                    },
                    {
                        'id': 8
                    },
                    {
                        'id': 9
                    },
                    {
                        'id': 10
                    }
                ]
            }
        }
    }
)

snapshots['test_del_artist_from_release 2'] = [
]

snapshots['test_del_artist_from_release_bad_artist 1'] = (
    True,
    {
        'data': {
            'delArtistFromRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist 9999 does not exist.',
                'path': [
                    'delArtistFromRelease'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_del_artist_from_release_bad_artist 2'] = [
    GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)")
]

snapshots['test_del_artist_from_release_bad_release 1'] = (
    True,
    {
        'data': {
            'delArtistFromRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release 999 does not exist.',
                'path': [
                    'delArtistFromRelease'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_del_artist_from_release_doesnt_exist 1'] = (
    True,
    {
        'data': {
            'delArtistFromRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist is not on release.',
                'path': [
                    'delArtistFromRelease'
                ],
                'type': 'DoesNotExist'
            }
        ]
    }
)

snapshots['test_del_artist_from_release_no_auth 1'] = (
    True,
    {
        'data': {
            'delArtistFromRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'delArtistFromRelease'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_release 1'] = (
    True,
    {
        'data': {
            'release': {
                'addedOn': 1603096174,
                'artists': [
                    {
                        'id': 4
                    },
                    {
                        'id': 5
                    }
                ],
                'collages': [
                ],
                'genres': [
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
                ],
                'hasCover': True,
                'id': 3,
                'inInbox': True,
                'labels': [
                ],
                'numTracks': 11,
                'releaseDate': None,
                'releaseType': 'EP',
                'releaseYear': 2016,
                'runtime': 3513,
                'title': 'Departure',
                'tracks': [
                    {
                        'id': 11
                    },
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
                    },
                    {
                        'id': 20
                    },
                    {
                        'id': 21
                    }
                ]
            }
        }
    }
)

snapshots['test_release_no_auth 1'] = (
    True,
    {
        'data': {
            'release': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'release'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_release_not_found 1'] = (
    True,
    {
        'data': {
            'release': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release 999 not found.',
                'path': [
                    'release'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_releases 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 0,
                        'artists': [
                        ],
                        'collages': [
                        ],
                        'genres': [
                        ],
                        'hasCover': False,
                        'id': 1,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': 0,
                        'runtime': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    },
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                        ],
                        'hasCover': True,
                        'id': 3,
                        'inInbox': True,
                        'labels': [
                        ],
                        'numTracks': 11,
                        'releaseDate': None,
                        'releaseType': 'EP',
                        'releaseYear': 2016,
                        'runtime': 3513,
                        'title': 'Departure',
                        'tracks': [
                            {
                                'id': 11
                            },
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
                            },
                            {
                                'id': 20
                            },
                            {
                                'id': 21
                            }
                        ]
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_releases_filter_artists 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_filter_collections 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_filter_types 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_no_auth 1'] = (
    True,
    {
        'data': {
            'releases': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'releases'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_releases_pagination 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                        ],
                        'hasCover': True,
                        'id': 3,
                        'inInbox': True,
                        'labels': [
                        ],
                        'numTracks': 11,
                        'releaseDate': None,
                        'releaseType': 'EP',
                        'releaseYear': 2016,
                        'runtime': 3513,
                        'title': 'Departure',
                        'tracks': [
                            {
                                'id': 11
                            },
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
                            },
                            {
                                'id': 20
                            },
                            {
                                'id': 21
                            }
                        ]
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_releases_search 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_sort 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                        ],
                        'hasCover': True,
                        'id': 3,
                        'inInbox': True,
                        'labels': [
                        ],
                        'numTracks': 11,
                        'releaseDate': None,
                        'releaseType': 'EP',
                        'releaseYear': 2016,
                        'runtime': 3513,
                        'title': 'Departure',
                        'tracks': [
                            {
                                'id': 11
                            },
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
                            },
                            {
                                'id': 20
                            },
                            {
                                'id': 21
                            }
                        ]
                    },
                    {
                        'addedOn': 0,
                        'artists': [
                        ],
                        'collages': [
                        ],
                        'genres': [
                        ],
                        'hasCover': False,
                        'id': 1,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': 0,
                        'runtime': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_releases_sort_desc 1'] = (
    True,
    {
        'data': {
            'releases': {
                'results': [
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                            }
                        ],
                        'hasCover': True,
                        'id': 2,
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
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    },
                    {
                        'addedOn': 0,
                        'artists': [
                        ],
                        'collages': [
                        ],
                        'genres': [
                        ],
                        'hasCover': False,
                        'id': 1,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': 0,
                        'runtime': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
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
                        ],
                        'hasCover': True,
                        'id': 3,
                        'inInbox': True,
                        'labels': [
                        ],
                        'numTracks': 11,
                        'releaseDate': None,
                        'releaseType': 'EP',
                        'releaseYear': 2016,
                        'runtime': 3513,
                        'title': 'Departure',
                        'tracks': [
                            {
                                'id': 11
                            },
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
                            },
                            {
                                'id': 20
                            },
                            {
                                'id': 21
                            }
                        ]
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_update_release 1'] = (
    True,
    {
        'data': {
            'updateRelease': {
                'addedOn': 1603067134,
                'artists': [
                    {
                        'id': 2
                    }
                ],
                'collages': [
                ],
                'genres': [
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
                    }
                ],
                'hasCover': True,
                'id': 2,
                'inInbox': True,
                'labels': [
                ],
                'numTracks': 10,
                'releaseDate': '2020-10-23',
                'releaseType': 'SINGLE',
                'releaseYear': 2020,
                'runtime': 2258,
                'title': 'aa',
                'tracks': [
                    {
                        'id': 1
                    },
                    {
                        'id': 2
                    },
                    {
                        'id': 3
                    },
                    {
                        'id': 4
                    },
                    {
                        'id': 5
                    },
                    {
                        'id': 6
                    },
                    {
                        'id': 7
                    },
                    {
                        'id': 8
                    },
                    {
                        'id': 9
                    },
                    {
                        'id': 10
                    }
                ]
            }
        }
    }
)

snapshots['test_update_release 2'] = GenericRepr("T(id=2, title='aa', release_type=<ReleaseType.SINGLE: 2>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2020, num_tracks=10, in_inbox=True, runtime=2258, release_date=datetime.date(2020, 10, 23), image_path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")

snapshots['test_update_release_bad_date 1'] = (
    True,
    {
        'data': {
            'updateRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid release date.',
                'path': [
                    'updateRelease'
                ],
                'type': 'ParseError'
            }
        ]
    }
)

snapshots['test_update_release_bad_date 2'] = GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, runtime=2258, release_date=datetime.date(2014, 7, 8), image_path=PosixPath('/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg'))")

snapshots['test_update_release_no_auth 1'] = (
    True,
    {
        'data': {
            'updateRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Invalid authorization token.',
                'path': [
                    'updateRelease'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_update_release_not_found 1'] = (
    True,
    {
        'data': {
            'updateRelease': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Release 99999 does not exist.',
                'path': [
                    'updateRelease'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

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
                'artist': {
                    'id': 3,
                    'name': 'John Darnielle',
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
                    ]
                },
                'release': {
                    'addedOn': 1603067134,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Aaron West and the Roaring Twenties'
                        },
                        {
                            'id': 3,
                            'name': 'John Darnielle'
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

snapshots['test_create_release 1'] = {
    'data': {
        'createRelease': {
            'artists': [
                {
                    'id': 2,
                    'name': 'Aaron West and the Roaring Twenties'
                },
                {
                    'id': 3,
                    'name': 'John Darnielle'
                }
            ],
            'collages': [
            ],
            'genres': [
            ],
            'id': 4,
            'imageId': None,
            'inFavorites': False,
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

snapshots['test_del_artist_from_release 1'] = (
    True,
    {
        'data': {
            'delArtistFromRelease': {
                'artist': {
                    'id': 2,
                    'name': 'Aaron West and the Roaring Twenties',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': False,
                    'topGenres': [
                    ]
                },
                'release': {
                    'addedOn': 1603067134,
                    'artists': [
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

snapshots['test_release 1'] = (
    True,
    {
        'data': {
            'release': {
                'addedOn': 1603096174,
                'artists': [
                    {
                        'id': 4,
                        'name': 'Abakus'
                    },
                    {
                        'id': 5,
                        'name': 'Bacchus'
                    }
                ],
                'collages': [
                ],
                'genres': [
                    {
                        'id': 7,
                        'name': 'Downtempo'
                    },
                    {
                        'id': 8,
                        'name': 'Electronic'
                    },
                    {
                        'id': 9,
                        'name': 'House'
                    },
                    {
                        'id': 10,
                        'name': 'Ambient'
                    }
                ],
                'id': 3,
                'imageId': 2,
                'inFavorites': False,
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
                        'id': 11,
                        'title': 'Airwaves'
                    },
                    {
                        'id': 12,
                        'title': 'Liberated from the Negative'
                    },
                    {
                        'id': 13,
                        'title': 'Hope'
                    },
                    {
                        'id': 14,
                        'title': 'Dreamer'
                    },
                    {
                        'id': 15,
                        'title': 'Stay with Me'
                    },
                    {
                        'id': 16,
                        'title': 'Still a Soul in There'
                    },
                    {
                        'id': 17,
                        'title': 'Lost Myself'
                    },
                    {
                        'id': 18,
                        'title': 'The Beginning'
                    },
                    {
                        'id': 19,
                        'title': 'Let Go'
                    },
                    {
                        'id': 20,
                        'title': 'Storm'
                    },
                    {
                        'id': 21,
                        'title': 'Kite'
                    }
                ]
            }
        }
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

snapshots['test_release_years 1'] = (
    True,
    {
        'data': {
            'releaseYears': [
                2016,
                2014
            ]
        }
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
                        'id': 1,
                        'imageId': None,
                        'inFavorites': False,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': None,
                        'runtime': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
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
                    },
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4,
                                'name': 'Abakus'
                            },
                            {
                                'id': 5,
                                'name': 'Bacchus'
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
                            {
                                'id': 7,
                                'name': 'Downtempo'
                            },
                            {
                                'id': 8,
                                'name': 'Electronic'
                            },
                            {
                                'id': 9,
                                'name': 'House'
                            },
                            {
                                'id': 10,
                                'name': 'Ambient'
                            }
                        ],
                        'id': 3,
                        'imageId': 2,
                        'inFavorites': False,
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
                                'id': 11,
                                'title': 'Airwaves'
                            },
                            {
                                'id': 12,
                                'title': 'Liberated from the Negative'
                            },
                            {
                                'id': 13,
                                'title': 'Hope'
                            },
                            {
                                'id': 14,
                                'title': 'Dreamer'
                            },
                            {
                                'id': 15,
                                'title': 'Stay with Me'
                            },
                            {
                                'id': 16,
                                'title': 'Still a Soul in There'
                            },
                            {
                                'id': 17,
                                'title': 'Lost Myself'
                            },
                            {
                                'id': 18,
                                'title': 'The Beginning'
                            },
                            {
                                'id': 19,
                                'title': 'Let Go'
                            },
                            {
                                'id': 20,
                                'title': 'Storm'
                            },
                            {
                                'id': 21,
                                'title': 'Kite'
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
                ],
                'total': 1
            }
        }
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
                                'id': 4,
                                'name': 'Abakus'
                            },
                            {
                                'id': 5,
                                'name': 'Bacchus'
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
                            {
                                'id': 7,
                                'name': 'Downtempo'
                            },
                            {
                                'id': 8,
                                'name': 'Electronic'
                            },
                            {
                                'id': 9,
                                'name': 'House'
                            },
                            {
                                'id': 10,
                                'name': 'Ambient'
                            }
                        ],
                        'id': 3,
                        'imageId': 2,
                        'inFavorites': False,
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
                                'id': 11,
                                'title': 'Airwaves'
                            },
                            {
                                'id': 12,
                                'title': 'Liberated from the Negative'
                            },
                            {
                                'id': 13,
                                'title': 'Hope'
                            },
                            {
                                'id': 14,
                                'title': 'Dreamer'
                            },
                            {
                                'id': 15,
                                'title': 'Stay with Me'
                            },
                            {
                                'id': 16,
                                'title': 'Still a Soul in There'
                            },
                            {
                                'id': 17,
                                'title': 'Lost Myself'
                            },
                            {
                                'id': 18,
                                'title': 'The Beginning'
                            },
                            {
                                'id': 19,
                                'title': 'Let Go'
                            },
                            {
                                'id': 20,
                                'title': 'Storm'
                            },
                            {
                                'id': 21,
                                'title': 'Kite'
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
                                'id': 4,
                                'name': 'Abakus'
                            },
                            {
                                'id': 5,
                                'name': 'Bacchus'
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
                            {
                                'id': 7,
                                'name': 'Downtempo'
                            },
                            {
                                'id': 8,
                                'name': 'Electronic'
                            },
                            {
                                'id': 9,
                                'name': 'House'
                            },
                            {
                                'id': 10,
                                'name': 'Ambient'
                            }
                        ],
                        'id': 3,
                        'imageId': 2,
                        'inFavorites': False,
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
                                'id': 11,
                                'title': 'Airwaves'
                            },
                            {
                                'id': 12,
                                'title': 'Liberated from the Negative'
                            },
                            {
                                'id': 13,
                                'title': 'Hope'
                            },
                            {
                                'id': 14,
                                'title': 'Dreamer'
                            },
                            {
                                'id': 15,
                                'title': 'Stay with Me'
                            },
                            {
                                'id': 16,
                                'title': 'Still a Soul in There'
                            },
                            {
                                'id': 17,
                                'title': 'Lost Myself'
                            },
                            {
                                'id': 18,
                                'title': 'The Beginning'
                            },
                            {
                                'id': 19,
                                'title': 'Let Go'
                            },
                            {
                                'id': 20,
                                'title': 'Storm'
                            },
                            {
                                'id': 21,
                                'title': 'Kite'
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
                        'id': 1,
                        'imageId': None,
                        'inFavorites': False,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': None,
                        'runtime': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
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
                    },
                    {
                        'addedOn': 0,
                        'artists': [
                        ],
                        'collages': [
                        ],
                        'genres': [
                        ],
                        'id': 1,
                        'imageId': None,
                        'inFavorites': False,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': None,
                        'runtime': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4,
                                'name': 'Abakus'
                            },
                            {
                                'id': 5,
                                'name': 'Bacchus'
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
                            {
                                'id': 7,
                                'name': 'Downtempo'
                            },
                            {
                                'id': 8,
                                'name': 'Electronic'
                            },
                            {
                                'id': 9,
                                'name': 'House'
                            },
                            {
                                'id': 10,
                                'name': 'Ambient'
                            }
                        ],
                        'id': 3,
                        'imageId': 2,
                        'inFavorites': False,
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
                                'id': 11,
                                'title': 'Airwaves'
                            },
                            {
                                'id': 12,
                                'title': 'Liberated from the Negative'
                            },
                            {
                                'id': 13,
                                'title': 'Hope'
                            },
                            {
                                'id': 14,
                                'title': 'Dreamer'
                            },
                            {
                                'id': 15,
                                'title': 'Stay with Me'
                            },
                            {
                                'id': 16,
                                'title': 'Still a Soul in There'
                            },
                            {
                                'id': 17,
                                'title': 'Lost Myself'
                            },
                            {
                                'id': 18,
                                'title': 'The Beginning'
                            },
                            {
                                'id': 19,
                                'title': 'Let Go'
                            },
                            {
                                'id': 20,
                                'title': 'Storm'
                            },
                            {
                                'id': 21,
                                'title': 'Kite'
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
)

snapshots['test_update_release 2'] = GenericRepr("T(id=2, title='aa', release_type=<ReleaseType.SINGLE: 2>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2020, num_tracks=10, in_inbox=True, in_favorites=False, rating=1, runtime=2258, release_date=datetime.date(2020, 10, 23), image_id=1)")

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

snapshots['test_update_release_bad_date 2'] = GenericRepr("T(id=2, title='We Don’t Have Each Other', release_type=<ReleaseType.ALBUM: 1>, added_on=datetime.datetime(2020, 10, 19, 0, 25, 34), release_year=2014, num_tracks=10, in_inbox=True, in_favorites=False, rating=6, runtime=2258, release_date=datetime.date(2014, 7, 8), image_id=1)")

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

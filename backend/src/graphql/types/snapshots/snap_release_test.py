# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_add_artist_to_release 1'] = {
    'data': {
        'addArtistToRelease': {
            'artist': {
                'id': 5,
                'name': 'Artist4',
                'numReleases': 2,
                'releases': [
                    {
                        'id': 2,
                        'title': 'Release1'
                    },
                    {
                        'id': 4,
                        'title': 'Release3'
                    }
                ],
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 11
                        },
                        'numMatches': 2
                    },
                    {
                        'genre': {
                            'id': 12
                        },
                        'numMatches': 2
                    }
                ]
            },
            'release': {
                'addedOn': 1577840461,
                'artists': [
                    {
                        'id': 2,
                        'name': 'Artist1'
                    },
                    {
                        'id': 3,
                        'name': 'Artist2'
                    },
                    {
                        'id': 5,
                        'name': 'Artist4'
                    }
                ],
                'collages': [
                    {
                        'id': 5,
                        'name': 'Collage1'
                    },
                    {
                        'id': 6,
                        'name': 'Collage2'
                    }
                ],
                'genres': [
                    {
                        'id': 11,
                        'name': 'Genre1'
                    },
                    {
                        'id': 12,
                        'name': 'Genre2'
                    }
                ],
                'id': 2,
                'imageId': 1,
                'inFavorites': False,
                'inInbox': False,
                'labels': [
                    {
                        'id': 8,
                        'name': 'Label1'
                    }
                ],
                'numTracks': 3,
                'releaseDate': '1970-02-05',
                'releaseType': 'ALBUM',
                'releaseYear': 1970,
                'runtime': 3,
                'title': 'Release1',
                'tracks': [
                    {
                        'id': 1,
                        'title': 'Track0'
                    },
                    {
                        'id': 2,
                        'title': 'Track1'
                    },
                    {
                        'id': 3,
                        'title': 'Track2'
                    }
                ]
            }
        }
    }
}

snapshots['test_add_artist_to_release_already_exists 1'] = {
    'data': None,
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

snapshots['test_add_artist_to_release_bad_artist 1'] = {
    'data': None,
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

snapshots['test_add_artist_to_release_bad_release 1'] = {
    'data': None,
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

snapshots['test_create_release 1'] = {
    'data': {
        'createRelease': {
            'addedOn': 1577840461,
            'artists': [
                {
                    'id': 2,
                    'name': 'Artist1'
                },
                {
                    'id': 3,
                    'name': 'Artist2'
                }
            ],
            'collages': [
            ],
            'genres': [
            ],
            'id': 7,
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
            'title': 'NewRelease',
            'tracks': [
            ]
        }
    }
}

snapshots['test_create_release_bad_artists 1'] = {
    'data': None,
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

snapshots['test_create_release_bad_date 1'] = {
    'data': None,
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

snapshots['test_del_artist_from_release 1'] = {
    'data': {
        'delArtistFromRelease': {
            'artist': {
                'id': 2,
                'name': 'Artist1',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 5,
                        'title': 'Release4'
                    }
                ],
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 13
                        },
                        'numMatches': 1
                    }
                ]
            },
            'release': {
                'addedOn': 1577840461,
                'artists': [
                    {
                        'id': 3,
                        'name': 'Artist2'
                    }
                ],
                'collages': [
                    {
                        'id': 5,
                        'name': 'Collage1'
                    },
                    {
                        'id': 6,
                        'name': 'Collage2'
                    }
                ],
                'genres': [
                    {
                        'id': 11,
                        'name': 'Genre1'
                    },
                    {
                        'id': 12,
                        'name': 'Genre2'
                    }
                ],
                'id': 2,
                'imageId': 1,
                'inFavorites': False,
                'inInbox': False,
                'labels': [
                    {
                        'id': 8,
                        'name': 'Label1'
                    }
                ],
                'numTracks': 3,
                'releaseDate': '1970-02-05',
                'releaseType': 'ALBUM',
                'releaseYear': 1970,
                'runtime': 3,
                'title': 'Release1',
                'tracks': [
                    {
                        'id': 1,
                        'title': 'Track0'
                    },
                    {
                        'id': 2,
                        'title': 'Track1'
                    },
                    {
                        'id': 3,
                        'title': 'Track2'
                    }
                ]
            }
        }
    }
}

snapshots['test_del_artist_from_release_bad_artist 1'] = {
    'data': None,
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

snapshots['test_del_artist_from_release_bad_release 1'] = {
    'data': None,
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

snapshots['test_del_artist_from_release_doesnt_exist 1'] = {
    'data': None,
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

snapshots['test_release 1'] = {
    'data': {
        'release': {
            'addedOn': 1577840461,
            'artists': [
                {
                    'id': 2,
                    'name': 'Artist1'
                },
                {
                    'id': 3,
                    'name': 'Artist2'
                }
            ],
            'collages': [
                {
                    'id': 5,
                    'name': 'Collage1'
                },
                {
                    'id': 6,
                    'name': 'Collage2'
                }
            ],
            'genres': [
                {
                    'id': 11,
                    'name': 'Genre1'
                },
                {
                    'id': 12,
                    'name': 'Genre2'
                }
            ],
            'id': 2,
            'imageId': 1,
            'inFavorites': False,
            'inInbox': False,
            'labels': [
                {
                    'id': 8,
                    'name': 'Label1'
                }
            ],
            'numTracks': 3,
            'releaseDate': '1970-02-05',
            'releaseType': 'ALBUM',
            'releaseYear': 1970,
            'runtime': 3,
            'title': 'Release1',
            'tracks': [
                {
                    'id': 1,
                    'title': 'Track0'
                },
                {
                    'id': 2,
                    'title': 'Track1'
                },
                {
                    'id': 3,
                    'title': 'Track2'
                }
            ]
        }
    }
}

snapshots['test_release_not_found 1'] = {
    'data': None,
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

snapshots['test_release_years 1'] = {
    'data': {
        'releaseYears': [
            2010,
            2000,
            1990,
            1980,
            1970
        ]
    }
}

snapshots['test_releases 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 0,
                    'artists': [
                        {
                            'id': 1,
                            'name': 'Unknown Artist'
                        }
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
                    'releaseType': 'OTHER',
                    'releaseYear': None,
                    'runtime': 0,
                    'title': 'Unknown Release',
                    'tracks': [
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 3,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'ALBUM',
                    'releaseYear': 1980,
                    'runtime': 7,
                    'title': 'Release2',
                    'tracks': [
                        {
                            'id': 4,
                            'title': 'Track3'
                        },
                        {
                            'id': 5,
                            'title': 'Track4'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 5,
                            'name': 'Artist4'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 4,
                    'imageId': 2,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'COMPILATION',
                    'releaseYear': 1990,
                    'runtime': 18,
                    'title': 'Release3',
                    'tracks': [
                        {
                            'id': 6,
                            'title': 'Track5'
                        },
                        {
                            'id': 7,
                            'title': 'Track6'
                        },
                        {
                            'id': 8,
                            'title': 'Track7'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        },
                        {
                            'id': 6,
                            'name': 'Artist5'
                        }
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 5,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 5,
                    'releaseDate': None,
                    'releaseType': 'UNKNOWN',
                    'releaseYear': 2000,
                    'runtime': 50,
                    'title': 'Release4',
                    'tracks': [
                        {
                            'id': 9,
                            'title': 'Track8'
                        },
                        {
                            'id': 10,
                            'title': 'Track9'
                        },
                        {
                            'id': 11,
                            'title': 'Track10'
                        },
                        {
                            'id': 12,
                            'title': 'Track11'
                        },
                        {
                            'id': 13,
                            'title': 'Track12'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 6,
                    'imageId': 3,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'EP',
                    'releaseYear': 2010,
                    'runtime': 27,
                    'title': 'Release5',
                    'tracks': [
                        {
                            'id': 14,
                            'title': 'Track13'
                        },
                        {
                            'id': 15,
                            'title': 'Track14'
                        }
                    ]
                }
            ],
            'total': 6
        }
    }
}

snapshots['test_releases_filter_artists 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        },
                        {
                            'id': 6,
                            'name': 'Artist5'
                        }
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 5,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 5,
                    'releaseDate': None,
                    'releaseType': 'UNKNOWN',
                    'releaseYear': 2000,
                    'runtime': 50,
                    'title': 'Release4',
                    'tracks': [
                        {
                            'id': 9,
                            'title': 'Track8'
                        },
                        {
                            'id': 10,
                            'title': 'Track9'
                        },
                        {
                            'id': 11,
                            'title': 'Track10'
                        },
                        {
                            'id': 12,
                            'title': 'Track11'
                        },
                        {
                            'id': 13,
                            'title': 'Track12'
                        }
                    ]
                }
            ],
            'total': 2
        }
    }
}

snapshots['test_releases_filter_collections 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 3,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'ALBUM',
                    'releaseYear': 1980,
                    'runtime': 7,
                    'title': 'Release2',
                    'tracks': [
                        {
                            'id': 4,
                            'title': 'Track3'
                        },
                        {
                            'id': 5,
                            'title': 'Track4'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 5,
                            'name': 'Artist4'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 4,
                    'imageId': 2,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'COMPILATION',
                    'releaseYear': 1990,
                    'runtime': 18,
                    'title': 'Release3',
                    'tracks': [
                        {
                            'id': 6,
                            'title': 'Track5'
                        },
                        {
                            'id': 7,
                            'title': 'Track6'
                        },
                        {
                            'id': 8,
                            'title': 'Track7'
                        }
                    ]
                }
            ],
            'total': 3
        }
    }
}

snapshots['test_releases_filter_types 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 3,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'ALBUM',
                    'releaseYear': 1980,
                    'runtime': 7,
                    'title': 'Release2',
                    'tracks': [
                        {
                            'id': 4,
                            'title': 'Track3'
                        },
                        {
                            'id': 5,
                            'title': 'Track4'
                        }
                    ]
                }
            ],
            'total': 2
        }
    }
}

snapshots['test_releases_pagination 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 3,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'ALBUM',
                    'releaseYear': 1980,
                    'runtime': 7,
                    'title': 'Release2',
                    'tracks': [
                        {
                            'id': 4,
                            'title': 'Track3'
                        },
                        {
                            'id': 5,
                            'title': 'Track4'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 5,
                            'name': 'Artist4'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 4,
                    'imageId': 2,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'COMPILATION',
                    'releaseYear': 1990,
                    'runtime': 18,
                    'title': 'Release3',
                    'tracks': [
                        {
                            'id': 6,
                            'title': 'Track5'
                        },
                        {
                            'id': 7,
                            'title': 'Track6'
                        },
                        {
                            'id': 8,
                            'title': 'Track7'
                        }
                    ]
                }
            ],
            'total': 6
        }
    }
}

snapshots['test_releases_search 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                }
            ],
            'total': 1
        }
    }
}

snapshots['test_releases_sort 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 3,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'ALBUM',
                    'releaseYear': 1980,
                    'runtime': 7,
                    'title': 'Release2',
                    'tracks': [
                        {
                            'id': 4,
                            'title': 'Track3'
                        },
                        {
                            'id': 5,
                            'title': 'Track4'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 5,
                            'name': 'Artist4'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 4,
                    'imageId': 2,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'COMPILATION',
                    'releaseYear': 1990,
                    'runtime': 18,
                    'title': 'Release3',
                    'tracks': [
                        {
                            'id': 6,
                            'title': 'Track5'
                        },
                        {
                            'id': 7,
                            'title': 'Track6'
                        },
                        {
                            'id': 8,
                            'title': 'Track7'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        },
                        {
                            'id': 6,
                            'name': 'Artist5'
                        }
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 5,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 5,
                    'releaseDate': None,
                    'releaseType': 'UNKNOWN',
                    'releaseYear': 2000,
                    'runtime': 50,
                    'title': 'Release4',
                    'tracks': [
                        {
                            'id': 9,
                            'title': 'Track8'
                        },
                        {
                            'id': 10,
                            'title': 'Track9'
                        },
                        {
                            'id': 11,
                            'title': 'Track10'
                        },
                        {
                            'id': 12,
                            'title': 'Track11'
                        },
                        {
                            'id': 13,
                            'title': 'Track12'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 6,
                    'imageId': 3,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'EP',
                    'releaseYear': 2010,
                    'runtime': 27,
                    'title': 'Release5',
                    'tracks': [
                        {
                            'id': 14,
                            'title': 'Track13'
                        },
                        {
                            'id': 15,
                            'title': 'Track14'
                        }
                    ]
                },
                {
                    'addedOn': 0,
                    'artists': [
                        {
                            'id': 1,
                            'name': 'Unknown Artist'
                        }
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
                    'releaseType': 'OTHER',
                    'releaseYear': None,
                    'runtime': 0,
                    'title': 'Unknown Release',
                    'tracks': [
                    ]
                }
            ],
            'total': 6
        }
    }
}

snapshots['test_releases_sort_desc 1'] = {
    'data': {
        'releases': {
            'results': [
                {
                    'addedOn': 0,
                    'artists': [
                        {
                            'id': 1,
                            'name': 'Unknown Artist'
                        }
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
                    'releaseType': 'OTHER',
                    'releaseYear': None,
                    'runtime': 0,
                    'title': 'Unknown Release',
                    'tracks': [
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 6,
                    'imageId': 3,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'EP',
                    'releaseYear': 2010,
                    'runtime': 27,
                    'title': 'Release5',
                    'tracks': [
                        {
                            'id': 14,
                            'title': 'Track13'
                        },
                        {
                            'id': 15,
                            'title': 'Track14'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        },
                        {
                            'id': 6,
                            'name': 'Artist5'
                        }
                    ],
                    'collages': [
                    ],
                    'genres': [
                        {
                            'id': 13,
                            'name': 'Genre3'
                        }
                    ],
                    'id': 5,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 5,
                    'releaseDate': None,
                    'releaseType': 'UNKNOWN',
                    'releaseYear': 2000,
                    'runtime': 50,
                    'title': 'Release4',
                    'tracks': [
                        {
                            'id': 9,
                            'title': 'Track8'
                        },
                        {
                            'id': 10,
                            'title': 'Track9'
                        },
                        {
                            'id': 11,
                            'title': 'Track10'
                        },
                        {
                            'id': 12,
                            'title': 'Track11'
                        },
                        {
                            'id': 13,
                            'title': 'Track12'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 5,
                            'name': 'Artist4'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 4,
                    'imageId': 2,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 9,
                            'name': 'Label2'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'COMPILATION',
                    'releaseYear': 1990,
                    'runtime': 18,
                    'title': 'Release3',
                    'tracks': [
                        {
                            'id': 6,
                            'title': 'Track5'
                        },
                        {
                            'id': 7,
                            'title': 'Track6'
                        },
                        {
                            'id': 8,
                            'title': 'Track7'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        {
                            'id': 4,
                            'name': 'Artist3'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 3,
                    'imageId': None,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 2,
                    'releaseDate': None,
                    'releaseType': 'ALBUM',
                    'releaseYear': 1980,
                    'runtime': 7,
                    'title': 'Release2',
                    'tracks': [
                        {
                            'id': 4,
                            'title': 'Track3'
                        },
                        {
                            'id': 5,
                            'title': 'Track4'
                        }
                    ]
                },
                {
                    'addedOn': 1577840461,
                    'artists': [
                        {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        {
                            'id': 3,
                            'name': 'Artist2'
                        }
                    ],
                    'collages': [
                        {
                            'id': 5,
                            'name': 'Collage1'
                        },
                        {
                            'id': 6,
                            'name': 'Collage2'
                        }
                    ],
                    'genres': [
                        {
                            'id': 11,
                            'name': 'Genre1'
                        },
                        {
                            'id': 12,
                            'name': 'Genre2'
                        }
                    ],
                    'id': 2,
                    'imageId': 1,
                    'inFavorites': False,
                    'inInbox': False,
                    'labels': [
                        {
                            'id': 8,
                            'name': 'Label1'
                        }
                    ],
                    'numTracks': 3,
                    'releaseDate': '1970-02-05',
                    'releaseType': 'ALBUM',
                    'releaseYear': 1970,
                    'runtime': 3,
                    'title': 'Release1',
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Track0'
                        },
                        {
                            'id': 2,
                            'title': 'Track1'
                        },
                        {
                            'id': 3,
                            'title': 'Track2'
                        }
                    ]
                }
            ],
            'total': 6
        }
    }
}

snapshots['test_update_release 1'] = {
    'data': {
        'updateRelease': {
            'addedOn': 1577840461,
            'artists': [
                {
                    'id': 2,
                    'name': 'Artist1'
                },
                {
                    'id': 3,
                    'name': 'Artist2'
                }
            ],
            'collages': [
                {
                    'id': 5,
                    'name': 'Collage1'
                },
                {
                    'id': 6,
                    'name': 'Collage2'
                }
            ],
            'genres': [
                {
                    'id': 11,
                    'name': 'Genre1'
                },
                {
                    'id': 12,
                    'name': 'Genre2'
                }
            ],
            'id': 2,
            'imageId': 1,
            'inFavorites': False,
            'inInbox': False,
            'labels': [
                {
                    'id': 8,
                    'name': 'Label1'
                }
            ],
            'numTracks': 3,
            'releaseDate': '2020-10-23',
            'releaseType': 'SINGLE',
            'releaseYear': 2020,
            'runtime': 3,
            'title': 'aa',
            'tracks': [
                {
                    'id': 1,
                    'title': 'Track0'
                },
                {
                    'id': 2,
                    'title': 'Track1'
                },
                {
                    'id': 3,
                    'title': 'Track2'
                }
            ]
        }
    }
}

snapshots['test_update_release_bad_date 1'] = {
    'data': None,
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

snapshots['test_update_release_not_found 1'] = {
    'data': None,
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

# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_artist 1'] = (
    True,
    {
        'data': {
            'artist': {
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
            'artistFromName': None
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
                    'artistFromName'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_artist_from_name_not_found 1'] = (
    True,
    {
        'data': {
            'artistFromName': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist "Random Artist name" does not exist.',
                'path': [
                    'artistFromName'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_artist_no_auth 1'] = (
    True,
    {
        'data': {
            'artist': None
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
                    'artist'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_artist_not_found 1'] = (
    True,
    {
        'data': {
            'artist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist 999999 does not exist.',
                'path': [
                    'artist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_artists 1'] = (
    True,
    {
        'data': {
            'artists': {
                'results': [
                    {
                        'favorite': False,
                        'id': 2,
                        'name': 'Aaron West and the Roaring Twenties',
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
                        ]
                    },
                    {
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
                    },
                    {
                        'favorite': True,
                        'id': 5,
                        'name': 'Bacchus',
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
                ]
            }
        }
    }
)

snapshots['test_artists_no_auth 1'] = (
    True,
    {
        'data': {
            'artists': None
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
                    'artists'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_create_artist 1'] = (
    True,
    {
        'data': {
            'createArtist': {
                'favorite': True,
                'id': 6,
                'name': 'New Artist',
                'numReleases': 0,
                'releases': [
                ],
                'topGenres': [
                ]
            }
        }
    }
)

snapshots['test_create_artist 2'] = GenericRepr("T(id=6, name='New Artist', favorite=True, num_releases=0)")

snapshots['test_create_artist_duplicate 1'] = (
    True,
    {
        'data': {
            'createArtist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist "Abakus" already exists.',
                'path': [
                    'createArtist'
                ],
                'type': 'Duplicate'
            }
        ]
    }
)

snapshots['test_create_artist_no_auth 1'] = (
    True,
    {
        'data': {
            'createArtist': None
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
                    'createArtist'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_update_artist 1'] = (
    True,
    {
        'data': {
            'updateArtist': {
                'favorite': True,
                'id': 4,
                'name': 'New Name',
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

snapshots['test_update_artist 2'] = GenericRepr("T(id=4, name='New Name', favorite=True, num_releases=1)")

snapshots['test_update_artist_doesnt_exist 1'] = (
    True,
    {
        'data': {
            'updateArtist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist 999 does not exist.',
                'path': [
                    'updateArtist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_update_artist_duplicate 1'] = (
    True,
    {
        'data': {
            'updateArtist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Artist "Bacchus" already exists.',
                'path': [
                    'updateArtist'
                ],
                'type': 'Duplicate'
            }
        ]
    }
)

snapshots['test_update_artist_duplicate 2'] = GenericRepr("T(id=4, name='Abakus', favorite=False, num_releases=1)")

snapshots['test_update_artist_no_auth 1'] = (
    True,
    {
        'data': {
            'updateArtist': None
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
                    'updateArtist'
                ],
                'type': 'NotAuthorized'
            }
        ]
    }
)

snapshots['test_update_artist_no_auth 2'] = GenericRepr("T(id=4, name='Abakus', favorite=False, num_releases=1)")

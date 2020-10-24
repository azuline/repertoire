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

snapshots['test_artist_not_found 1'] = (
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

snapshots['test_artists 1'] = (
    True,
    {
        'data': {
            'artists': {
                '__typename': 'Artists',
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
            'artists': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_create_artist 1'] = (
    True,
    {
        'data': {
            'createArtist': {
                '__typename': 'Artist',
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
            'createArtist': {
                '__typename': 'Error',
                'error': 'DUPLICATE',
                'message': 'Artist "Abakus" already exists.'
            }
        }
    }
)

snapshots['test_create_artist_no_auth 1'] = (
    True,
    {
        'data': {
            'createArtist': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_update_artist 1'] = (
    True,
    {
        'data': {
            'updateArtist': {
                '__typename': 'Artist',
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
            'updateArtist': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Artist 999 does not exist.'
            }
        }
    }
)

snapshots['test_update_artist_duplicate 1'] = (
    True,
    {
        'data': {
            'updateArtist': {
                '__typename': 'Error',
                'error': 'DUPLICATE',
                'message': 'Artist "Bacchus" already exists.'
            }
        }
    }
)

snapshots['test_update_artist_duplicate 2'] = GenericRepr("T(id=4, name='Abakus', favorite=False, num_releases=1)")

snapshots['test_update_artist_no_auth 1'] = (
    True,
    {
        'data': {
            'updateArtist': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_update_artist_no_auth 2'] = GenericRepr("T(id=4, name='Abakus', favorite=False, num_releases=1)")

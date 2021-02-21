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
                'id': 4,
                'name': 'Abakus',
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
                'id': 4,
                'name': 'Abakus',
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
                ]
            }
        }
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
                        'id': 5,
                        'name': 'Bacchus',
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
                        ]
                    },
                    {
                        'id': 2,
                        'name': 'Aaron West and the Roaring Twenties',
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
                    {
                        'id': 4,
                        'name': 'Abakus',
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
                        ]
                    },
                    {
                        'id': 3,
                        'name': 'John Darnielle',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ]
                    },
                    {
                        'id': 1,
                        'name': 'Unknown Artist',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 1,
                                'title': 'Unknown Release'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                        ]
                    }
                ]
            }
        }
    }
)

snapshots['test_create_artist 1'] = (
    True,
    {
        'data': {
            'createArtist': {
                'id': 6,
                'name': 'New Artist',
                'numReleases': 0,
                'releases': [
                ],
                'starred': True,
                'topGenres': [
                ]
            }
        }
    }
)

snapshots['test_create_artist 2'] = GenericRepr("T(id=6, name='New Artist', starred=True, num_releases=0)")

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

snapshots['test_update_artist 1'] = (
    True,
    {
        'data': {
            'updateArtist': {
                'id': 4,
                'name': 'New Name',
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
                ]
            }
        }
    }
)

snapshots['test_update_artist 2'] = GenericRepr("T(id=4, name='New Name', starred=True, num_releases=1)")

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

snapshots['test_update_artist_duplicate 2'] = GenericRepr("T(id=4, name='Abakus', starred=False, num_releases=1)")

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
                'name': 'Artist3',
                'numReleases': 2,
                'releases': [
                    {
                        'id': 3,
                        'title': 'Release2'
                    },
                    {
                        'id': 5,
                        'title': 'Release4'
                    }
                ],
                'starred': False,
                'topGenres': [
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
                    },
                    {
                        'genre': {
                            'id': 11
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
                'message': 'Artist "Abakus" does not exist.',
                'path': [
                    'artistFromName'
                ],
                'type': 'NotFound'
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
                        'id': 2,
                        'name': 'Artist1',
                        'numReleases': 2,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'Release1'
                            },
                            {
                                'id': 5,
                                'title': 'Release4'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
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
                            },
                            {
                                'genre': {
                                    'id': 11
                                },
                                'numMatches': 1
                            }
                        ]
                    },
                    {
                        'id': 3,
                        'name': 'Artist2',
                        'numReleases': 2,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'Release1'
                            },
                            {
                                'id': 3,
                                'title': 'Release2'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 2
                            }
                        ]
                    },
                    {
                        'id': 4,
                        'name': 'Artist3',
                        'numReleases': 2,
                        'releases': [
                            {
                                'id': 3,
                                'title': 'Release2'
                            },
                            {
                                'id': 5,
                                'title': 'Release4'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
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
                            },
                            {
                                'genre': {
                                    'id': 11
                                },
                                'numMatches': 1
                            }
                        ]
                    },
                    {
                        'id': 5,
                        'name': 'Artist4',
                        'numReleases': 1,
                        'releases': [
                            {
                                'id': 4,
                                'title': 'Release3'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
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
                        'id': 6,
                        'name': 'Artist5',
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
                                    'id': 11
                                },
                                'numMatches': 1
                            }
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
                ],
                'total': 6
            }
        }
    }
)

snapshots['test_artists_pagination 1'] = (
    True,
    {
        'data': {
            'artists': {
                'results': [
                    {
                        'id': 3,
                        'name': 'Artist2',
                        'numReleases': 2,
                        'releases': [
                            {
                                'id': 2,
                                'title': 'Release1'
                            },
                            {
                                'id': 3,
                                'title': 'Release2'
                            }
                        ],
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 2
                            }
                        ]
                    }
                ],
                'total': 6
            }
        }
    }
)

snapshots['test_artists_search 1'] = (
    True,
    {
        'data': {
            'artists': {
                'results': [
                ],
                'total': 0
            }
        }
    }
)

snapshots['test_create_artist 1'] = (
    True,
    {
        'data': {
            'createArtist': {
                'id': 7,
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

snapshots['test_create_artist_duplicate 1'] = (
    True,
    {
        'data': {
            'createArtist': {
                'id': 7,
                'name': 'Abakus',
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

snapshots['test_update_artist 1'] = (
    True,
    {
        'data': {
            'updateArtist': {
                'id': 4,
                'name': 'New Name',
                'numReleases': 2,
                'releases': [
                    {
                        'id': 3,
                        'title': 'Release2'
                    },
                    {
                        'id': 5,
                        'title': 'Release4'
                    }
                ],
                'starred': True,
                'topGenres': [
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
                    },
                    {
                        'genre': {
                            'id': 11
                        },
                        'numMatches': 1
                    }
                ]
            }
        }
    }
)

snapshots['test_update_artist 2'] = GenericRepr("T(id=4, name='New Name', starred=True, num_releases=2)")

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
            'updateArtist': {
                'id': 4,
                'name': 'Bacchus',
                'numReleases': 2,
                'releases': [
                    {
                        'id': 3,
                        'title': 'Release2'
                    },
                    {
                        'id': 5,
                        'title': 'Release4'
                    }
                ],
                'starred': True,
                'topGenres': [
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
                    },
                    {
                        'genre': {
                            'id': 11
                        },
                        'numMatches': 1
                    }
                ]
            }
        }
    }
)

snapshots['test_update_artist_duplicate 2'] = GenericRepr("T(id=4, name='Bacchus', starred=True, num_releases=2)")

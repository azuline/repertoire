# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_artist_to_track 1'] = {
    'data': {
        'addArtistToTrack': {
            'track': {
                'artists': [
                    {
                        'artist': {
                            'id': 2,
                            'name': 'Artist1'
                        },
                        'role': 'MAIN'
                    },
                    {
                        'artist': {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        'role': 'MAIN'
                    },
                    {
                        'artist': {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        'role': 'PRODUCER'
                    }
                ],
                'discNumber': '1',
                'duration': 0,
                'id': 1,
                'release': {
                    'id': 2,
                    'title': 'Release1'
                },
                'title': 'Track0',
                'trackNumber': '0'
            },
            'trackArtist': {
                'artist': {
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
                'role': 'MAIN'
            }
        }
    }
}

snapshots['test_add_artist_to_track 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Artist1', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='Artist2', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='Artist2', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    }
]

snapshots['test_add_artist_to_track_already_exists 1'] = {
    'data': {
        'addArtistToTrack': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Artist already on track with this role.',
            'path': [
                'addArtistToTrack'
            ],
            'type': 'AlreadyExists'
        }
    ]
}

snapshots['test_add_artist_to_track_already_exists 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Artist1', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='Artist2', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    }
]

snapshots['test_add_artist_to_track_bad_artist 1'] = {
    'data': {
        'addArtistToTrack': None
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
                'addArtistToTrack'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_add_artist_to_track_bad_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Artist1', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='Artist2', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    }
]

snapshots['test_add_artist_to_track_bad_track 1'] = {
    'data': {
        'addArtistToTrack': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Track does not exist.',
            'path': [
                'addArtistToTrack'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_del_artist_from_track 1'] = {
    'data': {
        'delArtistFromTrack': {
            'track': {
                'artists': [
                    {
                        'artist': {
                            'id': 3,
                            'name': 'Artist2'
                        },
                        'role': 'PRODUCER'
                    }
                ],
                'discNumber': '1',
                'duration': 0,
                'id': 1,
                'release': {
                    'id': 2,
                    'title': 'Release1'
                },
                'title': 'Track0',
                'trackNumber': '0'
            },
            'trackArtist': {
                'artist': {
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
                'role': 'MAIN'
            }
        }
    }
}

snapshots['test_del_artist_from_track 2'] = [
    {
        'artist': GenericRepr("T(id=3, name='Artist2', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    }
]

snapshots['test_del_artist_from_track_bad_artist 1'] = {
    'data': {
        'delArtistFromTrack': None
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
                'delArtistFromTrack'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_del_artist_from_track_bad_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Artist1', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='Artist2', starred=False, num_releases=2)"),
        'role': GenericRepr('<ArtistRoles.PRODUCER: 4>')
    }
]

snapshots['test_del_artist_from_track_bad_track 1'] = {
    'data': {
        'delArtistFromTrack': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Track does not exist.',
            'path': [
                'delArtistFromTrack'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_del_artist_from_track_doesnt_exist 1'] = {
    'data': {
        'delArtistFromTrack': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'No artist on track with this role.',
            'path': [
                'delArtistFromTrack'
            ],
            'type': 'DoesNotExist'
        }
    ]
}

snapshots['test_track 1'] = {
    'data': {
        'track': {
            'artists': [
                {
                    'artist': {
                        'id': 2,
                        'name': 'Artist1'
                    },
                    'role': 'MAIN'
                },
                {
                    'artist': {
                        'id': 4,
                        'name': 'Artist3'
                    },
                    'role': 'FEATURE'
                },
                {
                    'artist': {
                        'id': 6,
                        'name': 'Artist5'
                    },
                    'role': 'REMIXER'
                }
            ],
            'discNumber': '1',
            'duration': 9,
            'id': 10,
            'release': {
                'id': 5,
                'title': 'Release4'
            },
            'title': 'Track9',
            'trackNumber': '9'
        }
    }
}

snapshots['test_track_not_found 1'] = {
    'data': {
        'track': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Track 999 not found.',
            'path': [
                'track'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_tracks 1'] = {
    'data': {
        'tracks': {
            'results': [
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 0,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track0',
                    'trackNumber': '0'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 1,
                    'id': 2,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track1',
                    'trackNumber': '1'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 2,
                    'id': 3,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track2',
                    'trackNumber': '2'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '3',
                    'duration': 3,
                    'id': 4,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track3',
                    'trackNumber': '3'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '4',
                    'duration': 4,
                    'id': 5,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track4',
                    'trackNumber': '4'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 5,
                    'id': 6,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track5',
                    'trackNumber': '5'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 6,
                    'id': 7,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track6',
                    'trackNumber': '6'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 7,
                    'id': 8,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track7',
                    'trackNumber': '7'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 10,
                    'id': 11,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track10',
                    'trackNumber': '10'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 11,
                    'id': 12,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track11',
                    'trackNumber': '11'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 12,
                    'id': 13,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track12',
                    'trackNumber': '12'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 8,
                    'id': 9,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track8',
                    'trackNumber': '8'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 9,
                    'id': 10,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track9',
                    'trackNumber': '9'
                },
                {
                    'artists': [
                    ],
                    'discNumber': '13',
                    'duration': 13,
                    'id': 14,
                    'release': {
                        'id': 6,
                        'title': 'Release5'
                    },
                    'title': 'Track13',
                    'trackNumber': '13'
                },
                {
                    'artists': [
                    ],
                    'discNumber': '14',
                    'duration': 14,
                    'id': 15,
                    'release': {
                        'id': 6,
                        'title': 'Release5'
                    },
                    'title': 'Track14',
                    'trackNumber': '14'
                }
            ],
            'total': 15
        }
    }
}

snapshots['test_tracks_filter_artists 1'] = {
    'data': {
        'tracks': {
            'results': [
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 0,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track0',
                    'trackNumber': '0'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 1,
                    'id': 2,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track1',
                    'trackNumber': '1'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 2,
                    'id': 3,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track2',
                    'trackNumber': '2'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 10,
                    'id': 11,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track10',
                    'trackNumber': '10'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 11,
                    'id': 12,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track11',
                    'trackNumber': '11'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 12,
                    'id': 13,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track12',
                    'trackNumber': '12'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 8,
                    'id': 9,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track8',
                    'trackNumber': '8'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 9,
                    'id': 10,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track9',
                    'trackNumber': '9'
                }
            ],
            'total': 8
        }
    }
}

snapshots['test_tracks_filter_playlists 1'] = {
    'data': {
        'tracks': {
            'results': [
            ],
            'total': 0
        }
    }
}

snapshots['test_tracks_pagination 1'] = {
    'data': {
        'tracks': {
            'results': [
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 2,
                    'id': 3,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track2',
                    'trackNumber': '2'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '3',
                    'duration': 3,
                    'id': 4,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track3',
                    'trackNumber': '3'
                }
            ],
            'total': 15
        }
    }
}

snapshots['test_tracks_search 1'] = {
    'data': {
        'tracks': {
            'results': [
            ],
            'total': 0
        }
    }
}

snapshots['test_tracks_sort 1'] = {
    'data': {
        'tracks': {
            'results': [
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 0,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track0',
                    'trackNumber': '0'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 1,
                    'id': 2,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track1',
                    'trackNumber': '1'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 10,
                    'id': 11,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track10',
                    'trackNumber': '10'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 11,
                    'id': 12,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track11',
                    'trackNumber': '11'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 12,
                    'id': 13,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track12',
                    'trackNumber': '12'
                },
                {
                    'artists': [
                    ],
                    'discNumber': '13',
                    'duration': 13,
                    'id': 14,
                    'release': {
                        'id': 6,
                        'title': 'Release5'
                    },
                    'title': 'Track13',
                    'trackNumber': '13'
                },
                {
                    'artists': [
                    ],
                    'discNumber': '14',
                    'duration': 14,
                    'id': 15,
                    'release': {
                        'id': 6,
                        'title': 'Release5'
                    },
                    'title': 'Track14',
                    'trackNumber': '14'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 2,
                    'id': 3,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track2',
                    'trackNumber': '2'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '3',
                    'duration': 3,
                    'id': 4,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track3',
                    'trackNumber': '3'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '4',
                    'duration': 4,
                    'id': 5,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track4',
                    'trackNumber': '4'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 5,
                    'id': 6,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track5',
                    'trackNumber': '5'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 6,
                    'id': 7,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track6',
                    'trackNumber': '6'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 7,
                    'id': 8,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track7',
                    'trackNumber': '7'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 8,
                    'id': 9,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track8',
                    'trackNumber': '8'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 9,
                    'id': 10,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track9',
                    'trackNumber': '9'
                }
            ],
            'total': 15
        }
    }
}

snapshots['test_tracks_sort_desc 1'] = {
    'data': {
        'tracks': {
            'results': [
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 9,
                    'id': 10,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track9',
                    'trackNumber': '9'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 8,
                    'id': 9,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track8',
                    'trackNumber': '8'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 7,
                    'id': 8,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track7',
                    'trackNumber': '7'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 6,
                    'id': 7,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track6',
                    'trackNumber': '6'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 5,
                                'name': 'Artist4'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 5,
                    'id': 6,
                    'release': {
                        'id': 4,
                        'title': 'Release3'
                    },
                    'title': 'Track5',
                    'trackNumber': '5'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '4',
                    'duration': 4,
                    'id': 5,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track4',
                    'trackNumber': '4'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        }
                    ],
                    'discNumber': '3',
                    'duration': 3,
                    'id': 4,
                    'release': {
                        'id': 3,
                        'title': 'Release2'
                    },
                    'title': 'Track3',
                    'trackNumber': '3'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 2,
                    'id': 3,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track2',
                    'trackNumber': '2'
                },
                {
                    'artists': [
                    ],
                    'discNumber': '14',
                    'duration': 14,
                    'id': 15,
                    'release': {
                        'id': 6,
                        'title': 'Release5'
                    },
                    'title': 'Track14',
                    'trackNumber': '14'
                },
                {
                    'artists': [
                    ],
                    'discNumber': '13',
                    'duration': 13,
                    'id': 14,
                    'release': {
                        'id': 6,
                        'title': 'Release5'
                    },
                    'title': 'Track13',
                    'trackNumber': '13'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 12,
                    'id': 13,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track12',
                    'trackNumber': '12'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 11,
                    'id': 12,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track11',
                    'trackNumber': '11'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 4,
                                'name': 'Artist3'
                            },
                            'role': 'FEATURE'
                        },
                        {
                            'artist': {
                                'id': 6,
                                'name': 'Artist5'
                            },
                            'role': 'REMIXER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 10,
                    'id': 11,
                    'release': {
                        'id': 5,
                        'title': 'Release4'
                    },
                    'title': 'Track10',
                    'trackNumber': '10'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 1,
                    'id': 2,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track1',
                    'trackNumber': '1'
                },
                {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Artist1'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'Artist2'
                            },
                            'role': 'PRODUCER'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 0,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'Release1'
                    },
                    'title': 'Track0',
                    'trackNumber': '0'
                }
            ],
            'total': 15
        }
    }
}

snapshots['test_update_track 1'] = {
    'data': {
        'updateTrack': {
            'artists': [
                {
                    'artist': {
                        'id': 2,
                        'name': 'Artist1'
                    },
                    'role': 'MAIN'
                },
                {
                    'artist': {
                        'id': 3,
                        'name': 'Artist2'
                    },
                    'role': 'PRODUCER'
                }
            ],
            'discNumber': '899',
            'duration': 1,
            'id': 2,
            'release': {
                'id': 3,
                'title': 'Release2'
            },
            'title': 'aa',
            'trackNumber': '999'
        }
    }
}

snapshots['test_update_track 2'] = GenericRepr("T(id=2, filepath=PosixPath('/home/azul/devel/repertoire/backend/music/track2.flac'), sha256=b'\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01', title='aa', release_id=3, duration=1, track_number='999', disc_number='899')")

snapshots['test_update_track_bad_release_id 1'] = {
    'data': {
        'updateTrack': None
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
                'updateTrack'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_update_track_bad_release_id 2'] = GenericRepr("T(id=2, filepath=PosixPath('/home/azul/devel/repertoire/backend/music/track2.flac'), sha256=b'\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01\\x01', title='Track1', release_id=2, duration=1, track_number='1', disc_number='1')")

snapshots['test_update_track_not_found 1'] = {
    'data': {
        'updateTrack': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Track 99999 does not exist.',
            'path': [
                'updateTrack'
            ],
            'type': 'NotFound'
        }
    ]
}

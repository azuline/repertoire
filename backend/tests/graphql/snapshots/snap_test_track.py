# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_artist_to_track 1'] = (
    True,
    {
        'data': {
            'addArtistToTrack': {
                'track': {
                    'artists': [
                        {
                            'artist': {
                                'id': 2,
                                'name': 'Aaron West and the Roaring Twenties'
                            },
                            'role': 'MAIN'
                        },
                        {
                            'artist': {
                                'id': 3,
                                'name': 'John Darnielle'
                            },
                            'role': 'MAIN'
                        }
                    ],
                    'discNumber': '1',
                    'duration': 213,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    },
                    'title': 'Our Apartment',
                    'trackNumber': '1'
                },
                'trackArtist': {
                    'artist': {
                        'id': 3,
                        'name': 'John Darnielle',
                        'numReleases': 0,
                        'releases': [
                        ],
                        'starred': False,
                        'topGenres': [
                        ]
                    },
                    'role': 'MAIN'
                }
            }
        }
    }
)

snapshots['test_add_artist_to_track 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_to_track_already_exists 1'] = (
    True,
    {
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
)

snapshots['test_add_artist_to_track_already_exists 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_to_track_bad_artist 1'] = (
    True,
    {
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
)

snapshots['test_add_artist_to_track_bad_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_to_track_bad_track 1'] = (
    True,
    {
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
)

snapshots['test_del_artist_from_track 1'] = (
    True,
    {
        'data': {
            'delArtistFromTrack': {
                'track': {
                    'artists': [
                    ],
                    'discNumber': '1',
                    'duration': 213,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    },
                    'title': 'Our Apartment',
                    'trackNumber': '1'
                },
                'trackArtist': {
                    'artist': {
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
                    'role': 'MAIN'
                }
            }
        }
    }
)

snapshots['test_del_artist_from_track 2'] = [
]

snapshots['test_del_artist_from_track_bad_artist 1'] = (
    True,
    {
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
)

snapshots['test_del_artist_from_track_bad_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_del_artist_from_track_bad_track 1'] = (
    True,
    {
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
)

snapshots['test_del_artist_from_track_doesnt_exist 1'] = (
    True,
    {
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
)

snapshots['test_track 1'] = (
    True,
    {
        'data': {
            'track': {
                'artists': [
                    {
                        'artist': {
                            'id': 2,
                            'name': 'Aaron West and the Roaring Twenties'
                        },
                        'role': 'MAIN'
                    },
                    {
                        'artist': {
                            'id': 3,
                            'name': 'John Darnielle'
                        },
                        'role': 'COMPOSER'
                    }
                ],
                'discNumber': '1',
                'duration': 153,
                'id': 10,
                'release': {
                    'id': 2,
                    'title': 'We Don’t Have Each Other'
                },
                'title': 'Going to Georgia',
                'trackNumber': '10'
            }
        }
    }
)

snapshots['test_track_not_found 1'] = (
    True,
    {
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
)

snapshots['test_tracks 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 213,
                        'id': 1,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Our Apartment',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            },
                            {
                                'artist': {
                                    'id': 3,
                                    'name': 'John Darnielle'
                                },
                                'role': 'COMPOSER'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 153,
                        'id': 10,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Going to Georgia',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 210,
                        'id': 3,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'St. Joe Keeps Us Safe',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 193,
                        'id': 4,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Runnin’ Scared',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 259,
                        'id': 5,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Divorce and the American South',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 199,
                        'id': 6,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'The Thunderbird Inn',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 212,
                        'id': 7,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Get Me Out of Here Alive',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 265,
                        'id': 8,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'You Ain’t No Saint',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 302,
                        'id': 9,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Carolina Coast',
                        'trackNumber': '9'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 312,
                        'id': 19,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Let Go',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 382,
                        'id': 18,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'The Beginning',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 271,
                        'id': 11,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Airwaves',
                        'trackNumber': '11'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 268,
                        'id': 20,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Storm',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 320,
                        'id': 21,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Kite',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 304,
                        'id': 12,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Liberated from the Negative',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 262,
                        'id': 13,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Hope',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 412,
                        'id': 14,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Dreamer',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 307,
                        'id': 15,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Stay with Me',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 372,
                        'id': 16,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Still a Soul in There',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 303,
                        'id': 17,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Lost Myself',
                        'trackNumber': '9'
                    }
                ],
                'total': 21
            }
        }
    }
)

snapshots['test_tracks_filter_artists 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 213,
                        'id': 1,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Our Apartment',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            },
                            {
                                'artist': {
                                    'id': 3,
                                    'name': 'John Darnielle'
                                },
                                'role': 'COMPOSER'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 153,
                        'id': 10,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Going to Georgia',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 210,
                        'id': 3,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'St. Joe Keeps Us Safe',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 193,
                        'id': 4,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Runnin’ Scared',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 259,
                        'id': 5,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Divorce and the American South',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 199,
                        'id': 6,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'The Thunderbird Inn',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 212,
                        'id': 7,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Get Me Out of Here Alive',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 265,
                        'id': 8,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'You Ain’t No Saint',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 302,
                        'id': 9,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Carolina Coast',
                        'trackNumber': '9'
                    }
                ],
                'total': 10
            }
        }
    }
)

snapshots['test_tracks_filter_playlists 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 213,
                        'id': 1,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Our Apartment',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    }
                ],
                'total': 2
            }
        }
    }
)

snapshots['test_tracks_pagination 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 210,
                        'id': 3,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'St. Joe Keeps Us Safe',
                        'trackNumber': '3'
                    }
                ],
                'total': 21
            }
        }
    }
)

snapshots['test_tracks_search 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 213,
                        'id': 1,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Our Apartment',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 193,
                        'id': 4,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Runnin’ Scared',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 302,
                        'id': 9,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Carolina Coast',
                        'trackNumber': '9'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 265,
                        'id': 8,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'You Ain’t No Saint',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 199,
                        'id': 6,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'The Thunderbird Inn',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 210,
                        'id': 3,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'St. Joe Keeps Us Safe',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 212,
                        'id': 7,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Get Me Out of Here Alive',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 259,
                        'id': 5,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Divorce and the American South',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            },
                            {
                                'artist': {
                                    'id': 3,
                                    'name': 'John Darnielle'
                                },
                                'role': 'COMPOSER'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 153,
                        'id': 10,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Going to Georgia',
                        'trackNumber': '10'
                    }
                ],
                'total': 10
            }
        }
    }
)

snapshots['test_tracks_sort 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 271,
                        'id': 11,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Airwaves',
                        'trackNumber': '11'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 302,
                        'id': 9,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Carolina Coast',
                        'trackNumber': '9'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 259,
                        'id': 5,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Divorce and the American South',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 412,
                        'id': 14,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Dreamer',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 212,
                        'id': 7,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Get Me Out of Here Alive',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            },
                            {
                                'artist': {
                                    'id': 3,
                                    'name': 'John Darnielle'
                                },
                                'role': 'COMPOSER'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 153,
                        'id': 10,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Going to Georgia',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 262,
                        'id': 13,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Hope',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 320,
                        'id': 21,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Kite',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 312,
                        'id': 19,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Let Go',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 304,
                        'id': 12,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Liberated from the Negative',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 303,
                        'id': 17,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Lost Myself',
                        'trackNumber': '9'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 213,
                        'id': 1,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Our Apartment',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 193,
                        'id': 4,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Runnin’ Scared',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 210,
                        'id': 3,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'St. Joe Keeps Us Safe',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 307,
                        'id': 15,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Stay with Me',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 372,
                        'id': 16,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Still a Soul in There',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 268,
                        'id': 20,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Storm',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 382,
                        'id': 18,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'The Beginning',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 199,
                        'id': 6,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'The Thunderbird Inn',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 265,
                        'id': 8,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'You Ain’t No Saint',
                        'trackNumber': '8'
                    }
                ],
                'total': 21
            }
        }
    }
)

snapshots['test_tracks_sort_desc 1'] = (
    True,
    {
        'data': {
            'tracks': {
                'results': [
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 265,
                        'id': 8,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'You Ain’t No Saint',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 199,
                        'id': 6,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'The Thunderbird Inn',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 382,
                        'id': 18,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'The Beginning',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 268,
                        'id': 20,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Storm',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 372,
                        'id': 16,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Still a Soul in There',
                        'trackNumber': '8'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 307,
                        'id': 15,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Stay with Me',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 210,
                        'id': 3,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'St. Joe Keeps Us Safe',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 193,
                        'id': 4,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Runnin’ Scared',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 213,
                        'id': 1,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Our Apartment',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 303,
                        'id': 17,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Lost Myself',
                        'trackNumber': '9'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 304,
                        'id': 12,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Liberated from the Negative',
                        'trackNumber': '4'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 312,
                        'id': 19,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Let Go',
                        'trackNumber': '1'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 320,
                        'id': 21,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Kite',
                        'trackNumber': '3'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 262,
                        'id': 13,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Hope',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 252,
                        'id': 2,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Grapefruit',
                        'trackNumber': '2'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            },
                            {
                                'artist': {
                                    'id': 3,
                                    'name': 'John Darnielle'
                                },
                                'role': 'COMPOSER'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 153,
                        'id': 10,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Going to Georgia',
                        'trackNumber': '10'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 212,
                        'id': 7,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Get Me Out of Here Alive',
                        'trackNumber': '7'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 412,
                        'id': 14,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Dreamer',
                        'trackNumber': '6'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 259,
                        'id': 5,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Divorce and the American South',
                        'trackNumber': '5'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 2,
                                    'name': 'Aaron West and the Roaring Twenties'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '1',
                        'duration': 302,
                        'id': 9,
                        'release': {
                            'id': 2,
                            'title': 'We Don’t Have Each Other'
                        },
                        'title': 'Carolina Coast',
                        'trackNumber': '9'
                    },
                    {
                        'artists': [
                            {
                                'artist': {
                                    'id': 4,
                                    'name': 'Abakus'
                                },
                                'role': 'MAIN'
                            }
                        ],
                        'discNumber': '0',
                        'duration': 271,
                        'id': 11,
                        'release': {
                            'id': 3,
                            'title': 'Departure'
                        },
                        'title': 'Airwaves',
                        'trackNumber': '11'
                    }
                ],
                'total': 21
            }
        }
    }
)

snapshots['test_update_track 1'] = (
    True,
    {
        'data': {
            'updateTrack': {
                'artists': [
                    {
                        'artist': {
                            'id': 2,
                            'name': 'Aaron West and the Roaring Twenties'
                        },
                        'role': 'MAIN'
                    }
                ],
                'discNumber': '899',
                'duration': 252,
                'id': 2,
                'release': {
                    'id': 3,
                    'title': 'Departure'
                },
                'title': 'aa',
                'trackNumber': '999'
            }
        }
    }
)

snapshots['test_update_track 2'] = GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='aa', release_id=3, duration=252, track_number='999', disc_number='899')")

snapshots['test_update_track_bad_release_id 1'] = (
    True,
    {
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
)

snapshots['test_update_track_bad_release_id 2'] = GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')")

snapshots['test_update_track_not_found 1'] = (
    True,
    {
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
)

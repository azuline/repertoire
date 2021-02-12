# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_track_to_playlist 1'] = (
    True,
    {
        'data': {
            'addTrackToPlaylist': {
                'playlist': {
                    'id': 2,
                    'lastUpdatedOn': 1603067134,
                    'name': 'AAAAAA',
                    'numTracks': 6,
                    'starred': False,
                    'topGenres': [
                        {
                            'genre': {
                                'id': 3
                            },
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 4
                            },
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 5
                            },
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 6
                            },
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 7
                            },
                            'numMatches': 3
                        }
                    ],
                    'tracks': [
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
                        }
                    ],
                    'type': 'PLAYLIST'
                },
                'track': {
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
            }
        }
    }
)

snapshots['test_add_track_to_playlist 2'] = [
    GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')"),
    GenericRepr('T(id=3, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/03. St. Joe Keeps Us Safe.m4a\'), sha256=b\'\\x9c",\\xae\\xc4\\xb1\\x88\\x19\\xeb\\xefK\\xfa\\xf7Z\\xc3\\x19r+\\xfa?\\x96`\\xda\\xa3Ss+\\x13\\x9a\\xabV\\x96\', title=\'St. Joe Keeps Us Safe\', release_id=2, duration=210, track_number=\'3\', disc_number=\'1\')'),
    GenericRepr("T(id=4, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/04. Runnin’ Scared.m4a'), sha256=b'\\x9e\\x00\\xa1\\x88z\\x87\\xe8\\xa6+wh\\xf76\\xfb0\\x06\\xf6\\x8b\\xb1@\\x07\\xa7B$\\x1e\\xd7%\\xb9!!P\\xd4', title='Runnin’ Scared', release_id=2, duration=193, track_number='4', disc_number='1')"),
    GenericRepr("T(id=13, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/05. Hope.m4a'), sha256=b'\\x1b\\xa2^\\xb9;j\\xe9\\x9ffK\\xa58r\\x83\\xeb\\xdaf\\r\\xf4\\xf5\\xf8\\xad\\x13d\\x91\\x99\\xd3\\xe7odK\\xb4', title='Hope', release_id=3, duration=262, track_number='5', disc_number='0')"),
    GenericRepr("T(id=14, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/06. Dreamer.m4a'), sha256=b'\\xd2\\xd2\\xef\\x07\\xd1\\xde\\xf3 \\x82\\x9aC(\\xf1U\\x83L\\x81mI\\xec\\x17\\xad\\xa0\\xf4\\xcc\\xf0\\xd0n+H3\\xc4', title='Dreamer', release_id=3, duration=412, track_number='6', disc_number='0')"),
    GenericRepr("T(id=15, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/07. Stay with Me.m4a'), sha256=b'\\xe0K\\x14\\xc0\\\\\\xc2h\\xdb\\x85\\xd0KA\\x94kb\\x9a*UOA\\x8aB\\x8e\\xd2\\x08\\xa5&\\x95\\x04\\xf0\\x0e[', title='Stay with Me', release_id=3, duration=307, track_number='7', disc_number='0')")
]

snapshots['test_add_track_to_playlist_already_exists 1'] = (
    True,
    {
        'data': {
            'addTrackToPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Track is already in playlist.',
                'path': [
                    'addTrackToPlaylist'
                ],
                'type': 'AlreadyExists'
            }
        ]
    }
)

snapshots['test_add_track_to_playlist_already_exists 2'] = [
    GenericRepr('T(id=3, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/03. St. Joe Keeps Us Safe.m4a\'), sha256=b\'\\x9c",\\xae\\xc4\\xb1\\x88\\x19\\xeb\\xefK\\xfa\\xf7Z\\xc3\\x19r+\\xfa?\\x96`\\xda\\xa3Ss+\\x13\\x9a\\xabV\\x96\', title=\'St. Joe Keeps Us Safe\', release_id=2, duration=210, track_number=\'3\', disc_number=\'1\')'),
    GenericRepr("T(id=4, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/04. Runnin’ Scared.m4a'), sha256=b'\\x9e\\x00\\xa1\\x88z\\x87\\xe8\\xa6+wh\\xf76\\xfb0\\x06\\xf6\\x8b\\xb1@\\x07\\xa7B$\\x1e\\xd7%\\xb9!!P\\xd4', title='Runnin’ Scared', release_id=2, duration=193, track_number='4', disc_number='1')"),
    GenericRepr("T(id=13, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/05. Hope.m4a'), sha256=b'\\x1b\\xa2^\\xb9;j\\xe9\\x9ffK\\xa58r\\x83\\xeb\\xdaf\\r\\xf4\\xf5\\xf8\\xad\\x13d\\x91\\x99\\xd3\\xe7odK\\xb4', title='Hope', release_id=3, duration=262, track_number='5', disc_number='0')"),
    GenericRepr("T(id=14, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/06. Dreamer.m4a'), sha256=b'\\xd2\\xd2\\xef\\x07\\xd1\\xde\\xf3 \\x82\\x9aC(\\xf1U\\x83L\\x81mI\\xec\\x17\\xad\\xa0\\xf4\\xcc\\xf0\\xd0n+H3\\xc4', title='Dreamer', release_id=3, duration=412, track_number='6', disc_number='0')"),
    GenericRepr("T(id=15, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/07. Stay with Me.m4a'), sha256=b'\\xe0K\\x14\\xc0\\\\\\xc2h\\xdb\\x85\\xd0KA\\x94kb\\x9a*UOA\\x8aB\\x8e\\xd2\\x08\\xa5&\\x95\\x04\\xf0\\x0e[', title='Stay with Me', release_id=3, duration=307, track_number='7', disc_number='0')")
]

snapshots['test_add_track_to_playlist_bad_playlist 1'] = (
    True,
    {
        'data': {
            'addTrackToPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist 999 does not exist.',
                'path': [
                    'addTrackToPlaylist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_add_track_to_playlist_bad_track 1'] = (
    True,
    {
        'data': {
            'addTrackToPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Track 9999 does not exist.',
                'path': [
                    'addTrackToPlaylist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_add_track_to_playlist_bad_track 2'] = [
    GenericRepr('T(id=3, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/03. St. Joe Keeps Us Safe.m4a\'), sha256=b\'\\x9c",\\xae\\xc4\\xb1\\x88\\x19\\xeb\\xefK\\xfa\\xf7Z\\xc3\\x19r+\\xfa?\\x96`\\xda\\xa3Ss+\\x13\\x9a\\xabV\\x96\', title=\'St. Joe Keeps Us Safe\', release_id=2, duration=210, track_number=\'3\', disc_number=\'1\')'),
    GenericRepr("T(id=4, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/04. Runnin’ Scared.m4a'), sha256=b'\\x9e\\x00\\xa1\\x88z\\x87\\xe8\\xa6+wh\\xf76\\xfb0\\x06\\xf6\\x8b\\xb1@\\x07\\xa7B$\\x1e\\xd7%\\xb9!!P\\xd4', title='Runnin’ Scared', release_id=2, duration=193, track_number='4', disc_number='1')"),
    GenericRepr("T(id=13, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/05. Hope.m4a'), sha256=b'\\x1b\\xa2^\\xb9;j\\xe9\\x9ffK\\xa58r\\x83\\xeb\\xdaf\\r\\xf4\\xf5\\xf8\\xad\\x13d\\x91\\x99\\xd3\\xe7odK\\xb4', title='Hope', release_id=3, duration=262, track_number='5', disc_number='0')"),
    GenericRepr("T(id=14, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/06. Dreamer.m4a'), sha256=b'\\xd2\\xd2\\xef\\x07\\xd1\\xde\\xf3 \\x82\\x9aC(\\xf1U\\x83L\\x81mI\\xec\\x17\\xad\\xa0\\xf4\\xcc\\xf0\\xd0n+H3\\xc4', title='Dreamer', release_id=3, duration=412, track_number='6', disc_number='0')"),
    GenericRepr("T(id=15, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/07. Stay with Me.m4a'), sha256=b'\\xe0K\\x14\\xc0\\\\\\xc2h\\xdb\\x85\\xd0KA\\x94kb\\x9a*UOA\\x8aB\\x8e\\xd2\\x08\\xa5&\\x95\\x04\\xf0\\x0e[', title='Stay with Me', release_id=3, duration=307, track_number='7', disc_number='0')")
]

snapshots['test_create_playlist 1'] = (
    True,
    {
        'data': {
            'createPlaylist': {
                'id': 4,
                'lastUpdatedOn': None,
                'name': 'NewPlaylist',
                'numTracks': 0,
                'starred': True,
                'topGenres': [
                ],
                'tracks': [
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_create_playlist 2'] = GenericRepr("T(id=4, name='NewPlaylist', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=0, last_updated_on=None)")

snapshots['test_create_playlist_duplicate 1'] = (
    True,
    {
        'data': {
            'createPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist "AAAAAA" already exists.',
                'path': [
                    'createPlaylist'
                ],
                'type': 'Duplicate'
            }
        ]
    }
)

snapshots['test_del_track_from_playlist 1'] = (
    True,
    {
        'data': {
            'delTrackFromPlaylist': {
                'playlist': {
                    'id': 1,
                    'lastUpdatedOn': 1603067134,
                    'name': 'Favorites',
                    'numTracks': 1,
                    'starred': True,
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
                    ],
                    'tracks': [
                        {
                            'id': 1,
                            'title': 'Our Apartment'
                        }
                    ],
                    'type': 'SYSTEM'
                },
                'track': {
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
            }
        }
    }
)

snapshots['test_del_track_from_playlist 2'] = [
    GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')")
]

snapshots['test_del_track_from_playlist_bad_playlist 1'] = (
    True,
    {
        'data': {
            'delTrackFromPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist 999 does not exist.',
                'path': [
                    'delTrackFromPlaylist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_del_track_from_playlist_bad_track 1'] = (
    True,
    {
        'data': {
            'delTrackFromPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Track 9999 does not exist.',
                'path': [
                    'delTrackFromPlaylist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_del_track_from_playlist_bad_track 2'] = [
    GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')"),
    GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')")
]

snapshots['test_del_track_from_playlist_doesnt_exist 1'] = (
    True,
    {
        'data': {
            'delTrackFromPlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Track is not in playlist.',
                'path': [
                    'delTrackFromPlaylist'
                ],
                'type': 'DoesNotExist'
            }
        ]
    }
)

snapshots['test_playlist 1'] = (
    True,
    {
        'data': {
            'playlist': {
                'id': 2,
                'lastUpdatedOn': 1603067134,
                'name': 'AAAAAA',
                'numTracks': 5,
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 7
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 8
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 9
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 2
                    }
                ],
                'tracks': [
                    {
                        'id': 3,
                        'title': 'St. Joe Keeps Us Safe'
                    },
                    {
                        'id': 4,
                        'title': 'Runnin’ Scared'
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
                    }
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_playlist_from_name_and_type 1'] = (
    True,
    {
        'data': {
            'playlistFromNameAndType': {
                'id': 2,
                'lastUpdatedOn': 1603067134,
                'name': 'AAAAAA',
                'numTracks': 5,
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 7
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 8
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 9
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 3
                    },
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 2
                    }
                ],
                'tracks': [
                    {
                        'id': 3,
                        'title': 'St. Joe Keeps Us Safe'
                    },
                    {
                        'id': 4,
                        'title': 'Runnin’ Scared'
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
                    }
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_playlist_from_name_and_type_not_found 1'] = (
    True,
    {
        'data': {
            'playlistFromNameAndType': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist "AAFEFOPAIEFPAJF" of type SYSTEM not found.',
                'path': [
                    'playlistFromNameAndType'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_playlist_not_found 1'] = (
    True,
    {
        'data': {
            'playlist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist 999999 not found.',
                'path': [
                    'playlist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_playlists 1'] = (
    True,
    {
        'data': {
            'playlists': {
                'results': [
                    {
                        'id': 1,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Favorites',
                        'numTracks': 2,
                        'starred': True,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 2
                            }
                        ],
                        'tracks': [
                            {
                                'id': 1,
                                'title': 'Our Apartment'
                            },
                            {
                                'id': 2,
                                'title': 'Grapefruit'
                            }
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'id': 3,
                        'lastUpdatedOn': None,
                        'name': 'BBBBBB',
                        'numTracks': 0,
                        'starred': True,
                        'topGenres': [
                        ],
                        'tracks': [
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'id': 2,
                        'lastUpdatedOn': 1603067134,
                        'name': 'AAAAAA',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 2
                            }
                        ],
                        'tracks': [
                            {
                                'id': 3,
                                'title': 'St. Joe Keeps Us Safe'
                            },
                            {
                                'id': 4,
                                'title': 'Runnin’ Scared'
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
                            }
                        ],
                        'type': 'PLAYLIST'
                    }
                ]
            }
        }
    }
)

snapshots['test_playlists_type_param 1'] = (
    True,
    {
        'data': {
            'playlists': {
                'results': [
                    {
                        'id': 1,
                        'lastUpdatedOn': 1603067134,
                        'name': 'Favorites',
                        'numTracks': 2,
                        'starred': True,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 4
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 5
                                },
                                'numMatches': 2
                            },
                            {
                                'genre': {
                                    'id': 6
                                },
                                'numMatches': 2
                            }
                        ],
                        'tracks': [
                            {
                                'id': 1,
                                'title': 'Our Apartment'
                            },
                            {
                                'id': 2,
                                'title': 'Grapefruit'
                            }
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'id': 3,
                        'lastUpdatedOn': None,
                        'name': 'BBBBBB',
                        'numTracks': 0,
                        'starred': True,
                        'topGenres': [
                        ],
                        'tracks': [
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'id': 2,
                        'lastUpdatedOn': 1603067134,
                        'name': 'AAAAAA',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 3
                            },
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 2
                            }
                        ],
                        'tracks': [
                            {
                                'id': 3,
                                'title': 'St. Joe Keeps Us Safe'
                            },
                            {
                                'id': 4,
                                'title': 'Runnin’ Scared'
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
                            }
                        ],
                        'type': 'PLAYLIST'
                    }
                ]
            }
        }
    }
)

snapshots['test_update_playlist 1'] = (
    True,
    {
        'data': {
            'updatePlaylist': {
                'id': 3,
                'lastUpdatedOn': None,
                'name': 'NewPlaylist',
                'numTracks': 0,
                'starred': True,
                'topGenres': [
                ],
                'tracks': [
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_update_playlist 2'] = GenericRepr("T(id=3, name='NewPlaylist', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=0, last_updated_on=None)")

snapshots['test_update_playlist_duplicate 1'] = (
    True,
    {
        'data': {
            'updatePlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist "BBBBBB" already exists.',
                'path': [
                    'updatePlaylist'
                ],
                'type': 'Duplicate'
            }
        ]
    }
)

snapshots['test_update_playlist_duplicate 2'] = GenericRepr("T(id=2, name='AAAAAA', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=5, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_playlist_immutable 1'] = (
    True,
    {
        'data': {
            'updatePlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'System playlists cannot be modified.',
                'path': [
                    'updatePlaylist'
                ],
                'type': 'Immutable'
            }
        ]
    }
)

snapshots['test_update_playlist_immutable 2'] = GenericRepr("T(id=1, name='Favorites', starred=True, type=<PlaylistType.SYSTEM: 1>, num_tracks=2, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

snapshots['test_update_playlist_not_found 1'] = (
    True,
    {
        'data': {
            'updatePlaylist': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist 99999 does not exist.',
                'path': [
                    'updatePlaylist'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

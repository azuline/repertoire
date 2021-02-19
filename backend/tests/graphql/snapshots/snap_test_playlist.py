# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_create_playlist 1'] = (
    True,
    {
        'data': {
            'createPlaylist': {
                'entries': [
                ],
                'id': 4,
                'lastUpdatedOn': None,
                'name': 'NewPlaylist',
                'numTracks': 0,
                'starred': True,
                'topGenres': [
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

snapshots['test_playlist 1'] = (
    True,
    {
        'data': {
            'playlist': {
                'entries': [
                    {
                        'id': 3,
                        'track': {
                            'id': 3,
                            'title': 'St. Joe Keeps Us Safe'
                        }
                    },
                    {
                        'id': 4,
                        'track': {
                            'id': 4,
                            'title': 'Runnin’ Scared'
                        }
                    },
                    {
                        'id': 5,
                        'track': {
                            'id': 13,
                            'title': 'Hope'
                        }
                    },
                    {
                        'id': 6,
                        'track': {
                            'id': 14,
                            'title': 'Dreamer'
                        }
                    },
                    {
                        'id': 7,
                        'track': {
                            'id': 14,
                            'title': 'Dreamer'
                        }
                    },
                    {
                        'id': 8,
                        'track': {
                            'id': 15,
                            'title': 'Stay with Me'
                        }
                    }
                ],
                'id': 2,
                'lastUpdatedOn': 1603067134,
                'name': 'AAAAAA',
                'numTracks': 6,
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 7
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 8
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 9
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 2
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
                'entries': [
                    {
                        'id': 3,
                        'track': {
                            'id': 3,
                            'title': 'St. Joe Keeps Us Safe'
                        }
                    },
                    {
                        'id': 4,
                        'track': {
                            'id': 4,
                            'title': 'Runnin’ Scared'
                        }
                    },
                    {
                        'id': 5,
                        'track': {
                            'id': 13,
                            'title': 'Hope'
                        }
                    },
                    {
                        'id': 6,
                        'track': {
                            'id': 14,
                            'title': 'Dreamer'
                        }
                    },
                    {
                        'id': 7,
                        'track': {
                            'id': 14,
                            'title': 'Dreamer'
                        }
                    },
                    {
                        'id': 8,
                        'track': {
                            'id': 15,
                            'title': 'Stay with Me'
                        }
                    }
                ],
                'id': 2,
                'lastUpdatedOn': 1603067134,
                'name': 'AAAAAA',
                'numTracks': 6,
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 7
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 8
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 9
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 4
                    },
                    {
                        'genre': {
                            'id': 3
                        },
                        'numMatches': 2
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
                        'entries': [
                            {
                                'id': 1,
                                'track': {
                                    'id': 1,
                                    'title': 'Our Apartment'
                                }
                            },
                            {
                                'id': 2,
                                'track': {
                                    'id': 2,
                                    'title': 'Grapefruit'
                                }
                            }
                        ],
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
                        'type': 'SYSTEM'
                    },
                    {
                        'entries': [
                        ],
                        'id': 3,
                        'lastUpdatedOn': None,
                        'name': 'BBBBBB',
                        'numTracks': 0,
                        'starred': True,
                        'topGenres': [
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 3,
                                'track': {
                                    'id': 3,
                                    'title': 'St. Joe Keeps Us Safe'
                                }
                            },
                            {
                                'id': 4,
                                'track': {
                                    'id': 4,
                                    'title': 'Runnin’ Scared'
                                }
                            },
                            {
                                'id': 5,
                                'track': {
                                    'id': 13,
                                    'title': 'Hope'
                                }
                            },
                            {
                                'id': 6,
                                'track': {
                                    'id': 14,
                                    'title': 'Dreamer'
                                }
                            },
                            {
                                'id': 7,
                                'track': {
                                    'id': 14,
                                    'title': 'Dreamer'
                                }
                            },
                            {
                                'id': 8,
                                'track': {
                                    'id': 15,
                                    'title': 'Stay with Me'
                                }
                            }
                        ],
                        'id': 2,
                        'lastUpdatedOn': 1603067134,
                        'name': 'AAAAAA',
                        'numTracks': 6,
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 2
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
                        'entries': [
                            {
                                'id': 1,
                                'track': {
                                    'id': 1,
                                    'title': 'Our Apartment'
                                }
                            },
                            {
                                'id': 2,
                                'track': {
                                    'id': 2,
                                    'title': 'Grapefruit'
                                }
                            }
                        ],
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
                        'type': 'SYSTEM'
                    },
                    {
                        'entries': [
                        ],
                        'id': 3,
                        'lastUpdatedOn': None,
                        'name': 'BBBBBB',
                        'numTracks': 0,
                        'starred': True,
                        'topGenres': [
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 3,
                                'track': {
                                    'id': 3,
                                    'title': 'St. Joe Keeps Us Safe'
                                }
                            },
                            {
                                'id': 4,
                                'track': {
                                    'id': 4,
                                    'title': 'Runnin’ Scared'
                                }
                            },
                            {
                                'id': 5,
                                'track': {
                                    'id': 13,
                                    'title': 'Hope'
                                }
                            },
                            {
                                'id': 6,
                                'track': {
                                    'id': 14,
                                    'title': 'Dreamer'
                                }
                            },
                            {
                                'id': 7,
                                'track': {
                                    'id': 14,
                                    'title': 'Dreamer'
                                }
                            },
                            {
                                'id': 8,
                                'track': {
                                    'id': 15,
                                    'title': 'Stay with Me'
                                }
                            }
                        ],
                        'id': 2,
                        'lastUpdatedOn': 1603067134,
                        'name': 'AAAAAA',
                        'numTracks': 6,
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 7
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 8
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 4
                            },
                            {
                                'genre': {
                                    'id': 3
                                },
                                'numMatches': 2
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
                'entries': [
                ],
                'id': 3,
                'lastUpdatedOn': None,
                'name': 'NewPlaylist',
                'numTracks': 0,
                'starred': True,
                'topGenres': [
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

snapshots['test_update_playlist_duplicate 2'] = GenericRepr("T(id=2, name='AAAAAA', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=6, last_updated_on=datetime.datetime(2020, 10, 19, 0, 25, 34))")

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

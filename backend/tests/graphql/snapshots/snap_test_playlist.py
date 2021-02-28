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
                'id': 5,
                'lastUpdatedOn': 1577840461,
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

snapshots['test_create_playlist_duplicate 1'] = (
    True,
    {
        'data': {
            'createPlaylist': {
                'entries': [
                ],
                'id': 5,
                'lastUpdatedOn': 1577840461,
                'name': 'AAAAAA',
                'numTracks': 0,
                'starred': True,
                'topGenres': [
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_playlist 1'] = (
    True,
    {
        'data': {
            'playlist': {
                'entries': [
                    {
                        'id': 1,
                        'track': {
                            'id': 1,
                            'title': 'Track0'
                        }
                    },
                    {
                        'id': 2,
                        'track': {
                            'id': 2,
                            'title': 'Track1'
                        }
                    },
                    {
                        'id': 3,
                        'track': {
                            'id': 3,
                            'title': 'Track2'
                        }
                    },
                    {
                        'id': 4,
                        'track': {
                            'id': 4,
                            'title': 'Track3'
                        }
                    },
                    {
                        'id': 5,
                        'track': {
                            'id': 5,
                            'title': 'Track4'
                        }
                    }
                ],
                'id': 2,
                'lastUpdatedOn': 1577840461,
                'name': 'Playlist1',
                'numTracks': 5,
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 9
                        },
                        'numMatches': 5
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 5
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
                'message': 'Playlist "AAAAAA" of type PLAYLIST not found.',
                'path': [
                    'playlistFromNameAndType'
                ],
                'type': 'NotFound'
            }
        ]
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
                        ],
                        'id': 1,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Favorites',
                        'numTracks': 0,
                        'starred': True,
                        'topGenres': [
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'entries': [
                            {
                                'id': 1,
                                'track': {
                                    'id': 1,
                                    'title': 'Track0'
                                }
                            },
                            {
                                'id': 2,
                                'track': {
                                    'id': 2,
                                    'title': 'Track1'
                                }
                            },
                            {
                                'id': 3,
                                'track': {
                                    'id': 3,
                                    'title': 'Track2'
                                }
                            },
                            {
                                'id': 4,
                                'track': {
                                    'id': 4,
                                    'title': 'Track3'
                                }
                            },
                            {
                                'id': 5,
                                'track': {
                                    'id': 5,
                                    'title': 'Track4'
                                }
                            }
                        ],
                        'id': 2,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist1',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 5
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 5
                            }
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 6,
                                'track': {
                                    'id': 6,
                                    'title': 'Track5'
                                }
                            },
                            {
                                'id': 7,
                                'track': {
                                    'id': 7,
                                    'title': 'Track6'
                                }
                            },
                            {
                                'id': 8,
                                'track': {
                                    'id': 8,
                                    'title': 'Track7'
                                }
                            }
                        ],
                        'id': 3,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist2',
                        'numTracks': 3,
                        'starred': False,
                        'topGenres': [
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
                            }
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 9,
                                'track': {
                                    'id': 6,
                                    'title': 'Track5'
                                }
                            },
                            {
                                'id': 10,
                                'track': {
                                    'id': 7,
                                    'title': 'Track6'
                                }
                            },
                            {
                                'id': 11,
                                'track': {
                                    'id': 8,
                                    'title': 'Track7'
                                }
                            },
                            {
                                'id': 12,
                                'track': {
                                    'id': 9,
                                    'title': 'Track8'
                                }
                            },
                            {
                                'id': 13,
                                'track': {
                                    'id': 10,
                                    'title': 'Track9'
                                }
                            }
                        ],
                        'id': 4,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist3',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
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
                                    'id': 11
                                },
                                'numMatches': 2
                            }
                        ],
                        'type': 'PLAYLIST'
                    }
                ],
                'total': 4
            }
        }
    }
)

snapshots['test_playlists_filter 1'] = (
    True,
    {
        'data': {
            'playlists': {
                'results': [
                ],
                'total': 0
            }
        }
    }
)

snapshots['test_playlists_pagination 1'] = (
    True,
    {
        'data': {
            'playlists': {
                'results': [
                    {
                        'entries': [
                            {
                                'id': 6,
                                'track': {
                                    'id': 6,
                                    'title': 'Track5'
                                }
                            },
                            {
                                'id': 7,
                                'track': {
                                    'id': 7,
                                    'title': 'Track6'
                                }
                            },
                            {
                                'id': 8,
                                'track': {
                                    'id': 8,
                                    'title': 'Track7'
                                }
                            }
                        ],
                        'id': 3,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist2',
                        'numTracks': 3,
                        'starred': False,
                        'topGenres': [
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
                            }
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 9,
                                'track': {
                                    'id': 6,
                                    'title': 'Track5'
                                }
                            },
                            {
                                'id': 10,
                                'track': {
                                    'id': 7,
                                    'title': 'Track6'
                                }
                            },
                            {
                                'id': 11,
                                'track': {
                                    'id': 8,
                                    'title': 'Track7'
                                }
                            },
                            {
                                'id': 12,
                                'track': {
                                    'id': 9,
                                    'title': 'Track8'
                                }
                            },
                            {
                                'id': 13,
                                'track': {
                                    'id': 10,
                                    'title': 'Track9'
                                }
                            }
                        ],
                        'id': 4,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist3',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
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
                                    'id': 11
                                },
                                'numMatches': 2
                            }
                        ],
                        'type': 'PLAYLIST'
                    }
                ],
                'total': 4
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
                        ],
                        'id': 1,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Favorites',
                        'numTracks': 0,
                        'starred': True,
                        'topGenres': [
                        ],
                        'type': 'SYSTEM'
                    },
                    {
                        'entries': [
                            {
                                'id': 1,
                                'track': {
                                    'id': 1,
                                    'title': 'Track0'
                                }
                            },
                            {
                                'id': 2,
                                'track': {
                                    'id': 2,
                                    'title': 'Track1'
                                }
                            },
                            {
                                'id': 3,
                                'track': {
                                    'id': 3,
                                    'title': 'Track2'
                                }
                            },
                            {
                                'id': 4,
                                'track': {
                                    'id': 4,
                                    'title': 'Track3'
                                }
                            },
                            {
                                'id': 5,
                                'track': {
                                    'id': 5,
                                    'title': 'Track4'
                                }
                            }
                        ],
                        'id': 2,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist1',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
                            {
                                'genre': {
                                    'id': 9
                                },
                                'numMatches': 5
                            },
                            {
                                'genre': {
                                    'id': 10
                                },
                                'numMatches': 5
                            }
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 6,
                                'track': {
                                    'id': 6,
                                    'title': 'Track5'
                                }
                            },
                            {
                                'id': 7,
                                'track': {
                                    'id': 7,
                                    'title': 'Track6'
                                }
                            },
                            {
                                'id': 8,
                                'track': {
                                    'id': 8,
                                    'title': 'Track7'
                                }
                            }
                        ],
                        'id': 3,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist2',
                        'numTracks': 3,
                        'starred': False,
                        'topGenres': [
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
                            }
                        ],
                        'type': 'PLAYLIST'
                    },
                    {
                        'entries': [
                            {
                                'id': 9,
                                'track': {
                                    'id': 6,
                                    'title': 'Track5'
                                }
                            },
                            {
                                'id': 10,
                                'track': {
                                    'id': 7,
                                    'title': 'Track6'
                                }
                            },
                            {
                                'id': 11,
                                'track': {
                                    'id': 8,
                                    'title': 'Track7'
                                }
                            },
                            {
                                'id': 12,
                                'track': {
                                    'id': 9,
                                    'title': 'Track8'
                                }
                            },
                            {
                                'id': 13,
                                'track': {
                                    'id': 10,
                                    'title': 'Track9'
                                }
                            }
                        ],
                        'id': 4,
                        'lastUpdatedOn': 1577840461,
                        'name': 'Playlist3',
                        'numTracks': 5,
                        'starred': False,
                        'topGenres': [
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
                                    'id': 11
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
                    {
                        'id': 6,
                        'track': {
                            'id': 6,
                            'title': 'Track5'
                        }
                    },
                    {
                        'id': 7,
                        'track': {
                            'id': 7,
                            'title': 'Track6'
                        }
                    },
                    {
                        'id': 8,
                        'track': {
                            'id': 8,
                            'title': 'Track7'
                        }
                    }
                ],
                'id': 3,
                'lastUpdatedOn': 1577840461,
                'name': 'NewPlaylist',
                'numTracks': 3,
                'starred': True,
                'topGenres': [
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
                    }
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_update_playlist 2'] = GenericRepr("T(id=3, name='NewPlaylist', starred=True, type=<PlaylistType.PLAYLIST: 2>, num_tracks=3, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))")

snapshots['test_update_playlist_duplicate 1'] = (
    True,
    {
        'data': {
            'updatePlaylist': {
                'entries': [
                    {
                        'id': 1,
                        'track': {
                            'id': 1,
                            'title': 'Track0'
                        }
                    },
                    {
                        'id': 2,
                        'track': {
                            'id': 2,
                            'title': 'Track1'
                        }
                    },
                    {
                        'id': 3,
                        'track': {
                            'id': 3,
                            'title': 'Track2'
                        }
                    },
                    {
                        'id': 4,
                        'track': {
                            'id': 4,
                            'title': 'Track3'
                        }
                    },
                    {
                        'id': 5,
                        'track': {
                            'id': 5,
                            'title': 'Track4'
                        }
                    }
                ],
                'id': 2,
                'lastUpdatedOn': 1577840461,
                'name': 'BBBBBB',
                'numTracks': 5,
                'starred': False,
                'topGenres': [
                    {
                        'genre': {
                            'id': 9
                        },
                        'numMatches': 5
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 5
                    }
                ],
                'type': 'PLAYLIST'
            }
        }
    }
)

snapshots['test_update_playlist_duplicate 2'] = GenericRepr("T(id=2, name='BBBBBB', starred=False, type=<PlaylistType.PLAYLIST: 2>, num_tracks=5, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))")

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

snapshots['test_update_playlist_immutable 2'] = GenericRepr("T(id=1, name='Favorites', starred=True, type=<PlaylistType.SYSTEM: 1>, num_tracks=0, last_updated_on=FakeDatetime(2020, 1, 1, 1, 1, 1))")

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

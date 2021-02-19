# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_playlist_entry 1'] = (
    True,
    {
        'data': {
            'createPlaylistEntry': {
                'id': 9,
                'playlist': {
                    'id': 1,
                    'name': 'Favorites'
                },
                'position': 3,
                'track': {
                    'id': 10,
                    'title': 'Going to Georgia'
                }
            }
        }
    }
)

snapshots['test_create_playlist_entry_bad_playlist 1'] = (
    True,
    {
        'data': {
            'createPlaylistEntry': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist 9999 does not exist.',
                'path': [
                    'createPlaylistEntry'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_create_playlist_entry_bad_track 1'] = (
    True,
    {
        'data': {
            'createPlaylistEntry': None
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
                    'createPlaylistEntry'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_delete_entries 1'] = (
    True,
    {
        'data': {
            'delPlaylistEntries': {
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
                    'numTracks': 4,
                    'starred': False,
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
                        },
                        {
                            'genre': {
                                'id': 7
                            },
                            'numMatches': 2
                        }
                    ],
                    'type': 'PLAYLIST'
                },
                'track': {
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
                }
            }
        }
    }
)

snapshots['test_delete_entry 1'] = (
    True,
    {
        'data': {
            'delPlaylistEntry': {
                'playlist': {
                    'entries': [
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
                    'duration': 213,
                    'id': 1,
                    'release': {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    },
                    'title': 'Our Apartment',
                    'trackNumber': '1'
                }
            }
        }
    }
)

snapshots['test_delete_entry_invalid 1'] = (
    True,
    {
        'data': {
            'delPlaylistEntry': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist entry 99999 does not exist.',
                'path': [
                    'delPlaylistEntry'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_resolve_playlist_entries 1'] = (
    True,
    {
        'data': {
            'playlist': {
                'entries': [
                    {
                        'id': 1,
                        'playlist': {
                            'id': 1,
                            'name': 'Favorites'
                        },
                        'position': 1,
                        'track': {
                            'id': 1,
                            'title': 'Our Apartment'
                        }
                    },
                    {
                        'id': 2,
                        'playlist': {
                            'id': 1,
                            'name': 'Favorites'
                        },
                        'position': 2,
                        'track': {
                            'id': 2,
                            'title': 'Grapefruit'
                        }
                    }
                ]
            }
        }
    }
)

snapshots['test_update_playlist_entry 1'] = (
    True,
    {
        'data': {
            'updatePlaylistEntry': {
                'id': 5,
                'playlist': {
                    'id': 2,
                    'name': 'AAAAAA'
                },
                'position': 1,
                'track': {
                    'id': 13,
                    'title': 'Hope'
                }
            }
        }
    }
)

snapshots['test_update_playlist_entry_bad_entry 1'] = (
    True,
    {
        'data': {
            'updatePlaylistEntry': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Playlist entry 99999 does not exist.',
                'path': [
                    'updatePlaylistEntry'
                ],
                'type': 'NotFound'
            }
        ]
    }
)

snapshots['test_update_playlist_entry_bad_position 1'] = (
    True,
    {
        'data': {
            'updatePlaylistEntry': None
        },
        'errors': [
            {
                'locations': [
                    {
                        'column': 13,
                        'line': 3
                    }
                ],
                'message': 'Position 9999 out of bounds.',
                'path': [
                    'updatePlaylistEntry'
                ]
            }
        ]
    }
)

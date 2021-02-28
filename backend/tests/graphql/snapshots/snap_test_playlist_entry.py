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
                'id': 14,
                'playlist': {
                    'id': 1,
                    'name': 'Favorites'
                },
                'position': 1,
                'track': {
                    'id': 10,
                    'title': 'Track9'
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
                'track': {
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
                    'numTracks': 4,
                    'starred': False,
                    'topGenres': [
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
                        }
                    ],
                    'type': 'PLAYLIST'
                },
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
                    'name': 'Playlist1'
                },
                'position': 1,
                'track': {
                    'id': 5,
                    'title': 'Track4'
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

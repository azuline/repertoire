# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_release 1'] = (
    True,
    {
        'data': {
            'release': {
                '__typename': 'Release',
                'addedOn': 1603096174,
                'artists': [
                    {
                        'id': 4
                    },
                    {
                        'id': 5
                    }
                ],
                'collages': [
                ],
                'genres': [
                    {
                        'id': 16
                    },
                    {
                        'id': 17
                    },
                    {
                        'id': 18
                    },
                    {
                        'id': 19
                    }
                ],
                'id': 3,
                'imagePath': '/data/cover_art/d832df509b44cb7c560e2579453178016c391cd2ab8d6eab3de2bbbdf75c4ac0.jpg',
                'inInbox': True,
                'labels': [
                ],
                'numTracks': 11,
                'releaseDate': None,
                'releaseType': 'EP',
                'releaseYear': 2016,
                'title': 'Departure',
                'tracks': [
                    {
                        'id': 11
                    },
                    {
                        'id': 12
                    },
                    {
                        'id': 13
                    },
                    {
                        'id': 14
                    },
                    {
                        'id': 15
                    },
                    {
                        'id': 16
                    },
                    {
                        'id': 17
                    },
                    {
                        'id': 18
                    },
                    {
                        'id': 19
                    },
                    {
                        'id': 20
                    },
                    {
                        'id': 21
                    }
                ]
            }
        }
    }
)

snapshots['test_release_no_auth 1'] = (
    True,
    {
        'data': {
            'release': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_release_not_found 1'] = (
    True,
    {
        'data': {
            'release': {
                '__typename': 'Error',
                'error': 'NOT_FOUND',
                'message': 'Release 999 not found.'
            }
        }
    }
)

snapshots['test_releases 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'addedOn': 0,
                        'artists': [
                        ],
                        'collages': [
                        ],
                        'genres': [
                        ],
                        'id': 1,
                        'imagePath': None,
                        'inInbox': False,
                        'labels': [
                        ],
                        'numTracks': 0,
                        'releaseDate': None,
                        'releaseType': 'UNKNOWN',
                        'releaseYear': 0,
                        'title': 'Unknown Release',
                        'tracks': [
                        ]
                    },
                    {
                        'addedOn': 1603067134,
                        'artists': [
                            {
                                'id': 2
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
                            {
                                'id': 12
                            },
                            {
                                'id': 13
                            },
                            {
                                'id': 14
                            },
                            {
                                'id': 15
                            }
                        ],
                        'id': 2,
                        'imagePath': '/data/cover_art/fb21f22d84bb812bb8bd1988ee89c3a91f1d41e92cf988ef774423e9d85e3292.jpg',
                        'inInbox': True,
                        'labels': [
                        ],
                        'numTracks': 10,
                        'releaseDate': '2014-07-08',
                        'releaseType': 'ALBUM',
                        'releaseYear': 2014,
                        'title': 'We Don’t Have Each Other',
                        'tracks': [
                            {
                                'id': 1
                            },
                            {
                                'id': 2
                            },
                            {
                                'id': 3
                            },
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            },
                            {
                                'id': 6
                            },
                            {
                                'id': 7
                            },
                            {
                                'id': 8
                            },
                            {
                                'id': 9
                            },
                            {
                                'id': 10
                            }
                        ]
                    },
                    {
                        'addedOn': 1603096174,
                        'artists': [
                            {
                                'id': 4
                            },
                            {
                                'id': 5
                            }
                        ],
                        'collages': [
                        ],
                        'genres': [
                            {
                                'id': 16
                            },
                            {
                                'id': 17
                            },
                            {
                                'id': 18
                            },
                            {
                                'id': 19
                            }
                        ],
                        'id': 3,
                        'imagePath': '/data/cover_art/d832df509b44cb7c560e2579453178016c391cd2ab8d6eab3de2bbbdf75c4ac0.jpg',
                        'inInbox': True,
                        'labels': [
                        ],
                        'numTracks': 11,
                        'releaseDate': None,
                        'releaseType': 'EP',
                        'releaseYear': 2016,
                        'title': 'Departure',
                        'tracks': [
                            {
                                'id': 11
                            },
                            {
                                'id': 12
                            },
                            {
                                'id': 13
                            },
                            {
                                'id': 14
                            },
                            {
                                'id': 15
                            },
                            {
                                'id': 16
                            },
                            {
                                'id': 17
                            },
                            {
                                'id': 18
                            },
                            {
                                'id': 19
                            },
                            {
                                'id': 20
                            },
                            {
                                'id': 21
                            }
                        ]
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_releases_filter_artists 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_filter_collections 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_filter_types 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_no_auth 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Error',
                'error': 'NOT_AUTHENTICATED',
                'message': 'Please authenticate ^.~'
            }
        }
    }
)

snapshots['test_releases_pagination 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 3,
                        'title': 'Departure'
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_releases_search 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'total': 1
            }
        }
    }
)

snapshots['test_releases_sort 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 3,
                        'title': 'Departure'
                    },
                    {
                        'id': 1,
                        'title': 'Unknown Release'
                    },
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    }
                ],
                'total': 3
            }
        }
    }
)

snapshots['test_releases_sort_desc 1'] = (
    True,
    {
        'data': {
            'releases': {
                '__typename': 'Releases',
                'results': [
                    {
                        'id': 2,
                        'title': 'We Don’t Have Each Other'
                    },
                    {
                        'id': 1,
                        'title': 'Unknown Release'
                    },
                    {
                        'id': 3,
                        'title': 'Departure'
                    }
                ],
                'total': 3
            }
        }
    }
)

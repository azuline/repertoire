# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_add_release_to_collection 1'] = {
    'data': {
        'addReleaseToCollection': {
            'collection': {
                'id': 1,
                'lastUpdatedOn': 1577840461,
                'name': 'Inbox',
                'numReleases': 1,
                'releases': [
                    {
                        'id': 2,
                        'title': 'Release1'
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
                    }
                ],
                'type': 'SYSTEM'
            },
            'release': {
                'addedOn': 1577840461,
                'artists': [
                    {
                        'id': 2,
                        'name': 'Artist1'
                    },
                    {
                        'id': 3,
                        'name': 'Artist2'
                    }
                ],
                'collages': [
                    {
                        'id': 3,
                        'name': 'Collage1'
                    },
                    {
                        'id': 4,
                        'name': 'Collage2'
                    }
                ],
                'genres': [
                    {
                        'id': 9,
                        'name': 'Genre1'
                    },
                    {
                        'id': 10,
                        'name': 'Genre2'
                    }
                ],
                'id': 2,
                'imageId': 1,
                'inFavorites': False,
                'inInbox': True,
                'labels': [
                    {
                        'id': 6,
                        'name': 'Label1'
                    }
                ],
                'numTracks': 3,
                'releaseDate': '1970-02-05',
                'releaseType': 'ALBUM',
                'releaseYear': 1970,
                'runtime': 3,
                'title': 'Release1',
                'tracks': [
                    {
                        'id': 1,
                        'title': 'Track0'
                    },
                    {
                        'id': 2,
                        'title': 'Track1'
                    },
                    {
                        'id': 3,
                        'title': 'Track2'
                    }
                ]
            }
        }
    }
}

snapshots['test_add_release_to_collection_already_exists 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Release is already in collection.',
            'path': [
                'addReleaseToCollection'
            ],
            'type': 'AlreadyExists'
        }
    ]
}

snapshots['test_add_release_to_collection_bad_collection 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection 999 does not exist.',
            'path': [
                'addReleaseToCollection'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_add_release_to_collection_bad_release 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Release 9999 does not exist.',
            'path': [
                'addReleaseToCollection'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_collection 1'] = {
    'data': {
        'collection': {
            'id': 3,
            'lastUpdatedOn': 1577840461,
            'name': 'Collage1',
            'numReleases': 3,
            'releases': [
                {
                    'id': 2,
                    'title': 'Release1'
                },
                {
                    'id': 3,
                    'title': 'Release2'
                },
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
                    'numMatches': 3
                },
                {
                    'genre': {
                        'id': 10
                    },
                    'numMatches': 3
                }
            ],
            'type': 'COLLAGE'
        }
    }
}

snapshots['test_collection_from_name_and_type 1'] = {
    'data': {
        'collectionFromNameAndType': {
            'id': 9,
            'lastUpdatedOn': 1577840461,
            'name': 'Genre1',
            'numReleases': 3,
            'releases': [
                {
                    'id': 2,
                    'title': 'Release1'
                },
                {
                    'id': 3,
                    'title': 'Release2'
                },
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
                    'numMatches': 3
                },
                {
                    'genre': {
                        'id': 10
                    },
                    'numMatches': 3
                }
            ],
            'type': 'GENRE'
        }
    }
}

snapshots['test_collection_from_name_and_type_not_found 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection "AAFEFOPAIEFPAJF" of type COLLAGE not found.',
            'path': [
                'collectionFromNameAndType'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_collection_from_name_type_user 1'] = {
    'data': {
        'collectionFromNameAndType': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection "Genre1" of type GENRE not found.',
            'path': [
                'collectionFromNameAndType'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_collection_from_name_type_user_not_found 1'] = {
    'data': {
        'collectionFromNameAndType': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection "AAFEFOPAIEFPAJF" of type COLLAGE not found.',
            'path': [
                'collectionFromNameAndType'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_collection_not_found 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection 999999 not found.',
            'path': [
                'collection'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_collections 1'] = {
    'data': {
        'collections': {
            'results': [
                {
                    'id': 2,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Favorites',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': True,
                    'topGenres': [
                    ],
                    'type': 'SYSTEM'
                },
                {
                    'id': 1,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Inbox',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': True,
                    'topGenres': [
                    ],
                    'type': 'SYSTEM'
                },
                {
                    'id': 3,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Collage1',
                    'numReleases': 3,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
                        },
                        {
                            'id': 3,
                            'title': 'Release2'
                        },
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
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 3
                        }
                    ],
                    'type': 'COLLAGE'
                },
                {
                    'id': 4,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Collage2',
                    'numReleases': 1,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
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
                    ],
                    'type': 'COLLAGE'
                },
                {
                    'id': 5,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Collage3',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': False,
                    'topGenres': [
                    ],
                    'type': 'COLLAGE'
                },
                {
                    'id': 6,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Label1',
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
                    ],
                    'type': 'LABEL'
                },
                {
                    'id': 7,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Label2',
                    'numReleases': 2,
                    'releases': [
                        {
                            'id': 4,
                            'title': 'Release3'
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
                    ],
                    'type': 'LABEL'
                },
                {
                    'id': 8,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Label3',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': False,
                    'topGenres': [
                    ],
                    'type': 'LABEL'
                },
                {
                    'id': 9,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre1',
                    'numReleases': 3,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
                        },
                        {
                            'id': 3,
                            'title': 'Release2'
                        },
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
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 3
                        }
                    ],
                    'type': 'GENRE'
                },
                {
                    'id': 10,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre2',
                    'numReleases': 3,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
                        },
                        {
                            'id': 3,
                            'title': 'Release2'
                        },
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
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 3
                        }
                    ],
                    'type': 'GENRE'
                },
                {
                    'id': 11,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre3',
                    'numReleases': 2,
                    'releases': [
                        {
                            'id': 5,
                            'title': 'Release4'
                        },
                        {
                            'id': 6,
                            'title': 'Release5'
                        }
                    ],
                    'starred': False,
                    'topGenres': [
                        {
                            'genre': {
                                'id': 11
                            },
                            'numMatches': 2
                        }
                    ],
                    'type': 'GENRE'
                }
            ],
            'total': 11
        }
    }
}

snapshots['test_collections_filter 1'] = {
    'data': {
        'collections': {
            'results': [
                {
                    'id': 9,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre1',
                    'numReleases': 3,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
                        },
                        {
                            'id': 3,
                            'title': 'Release2'
                        },
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
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 3
                        }
                    ],
                    'type': 'GENRE'
                }
            ],
            'total': 1
        }
    }
}

snapshots['test_collections_pagination 1'] = {
    'data': {
        'collections': {
            'results': [
                {
                    'id': 5,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Collage3',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': False,
                    'topGenres': [
                    ],
                    'type': 'COLLAGE'
                },
                {
                    'id': 6,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Label1',
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
                    ],
                    'type': 'LABEL'
                }
            ],
            'total': 11
        }
    }
}

snapshots['test_collections_type_param 1'] = {
    'data': {
        'collections': {
            'results': [
                {
                    'id': 2,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Favorites',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': True,
                    'topGenres': [
                    ],
                    'type': 'SYSTEM'
                },
                {
                    'id': 1,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Inbox',
                    'numReleases': 0,
                    'releases': [
                    ],
                    'starred': True,
                    'topGenres': [
                    ],
                    'type': 'SYSTEM'
                },
                {
                    'id': 9,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre1',
                    'numReleases': 3,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
                        },
                        {
                            'id': 3,
                            'title': 'Release2'
                        },
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
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 3
                        }
                    ],
                    'type': 'GENRE'
                },
                {
                    'id': 10,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre2',
                    'numReleases': 3,
                    'releases': [
                        {
                            'id': 2,
                            'title': 'Release1'
                        },
                        {
                            'id': 3,
                            'title': 'Release2'
                        },
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
                            'numMatches': 3
                        },
                        {
                            'genre': {
                                'id': 10
                            },
                            'numMatches': 3
                        }
                    ],
                    'type': 'GENRE'
                },
                {
                    'id': 11,
                    'lastUpdatedOn': 1577840461,
                    'name': 'Genre3',
                    'numReleases': 2,
                    'releases': [
                        {
                            'id': 5,
                            'title': 'Release4'
                        },
                        {
                            'id': 6,
                            'title': 'Release5'
                        }
                    ],
                    'starred': False,
                    'topGenres': [
                        {
                            'genre': {
                                'id': 11
                            },
                            'numMatches': 2
                        }
                    ],
                    'type': 'GENRE'
                }
            ]
        }
    }
}

snapshots['test_create_collection 1'] = {
    'data': {
        'createCollection': {
            'id': 12,
            'lastUpdatedOn': 1577840461,
            'name': 'NewCollection',
            'numReleases': 0,
            'releases': [
            ],
            'starred': True,
            'topGenres': [
            ],
            'type': 'COLLAGE'
        }
    }
}

snapshots['test_create_collection_duplicate 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection "Collage1" already exists.',
            'path': [
                'createCollection'
            ],
            'type': 'Duplicate'
        }
    ]
}

snapshots['test_del_release_from_collection 1'] = {
    'data': {
        'delReleaseFromCollection': {
            'collection': {
                'id': 3,
                'lastUpdatedOn': 1577840461,
                'name': 'Collage1',
                'numReleases': 2,
                'releases': [
                    {
                        'id': 3,
                        'title': 'Release2'
                    },
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
                        'numMatches': 2
                    },
                    {
                        'genre': {
                            'id': 10
                        },
                        'numMatches': 2
                    }
                ],
                'type': 'COLLAGE'
            },
            'release': {
                'addedOn': 1577840461,
                'artists': [
                    {
                        'id': 2,
                        'name': 'Artist1'
                    },
                    {
                        'id': 3,
                        'name': 'Artist2'
                    }
                ],
                'collages': [
                    {
                        'id': 4,
                        'name': 'Collage2'
                    }
                ],
                'genres': [
                    {
                        'id': 9,
                        'name': 'Genre1'
                    },
                    {
                        'id': 10,
                        'name': 'Genre2'
                    }
                ],
                'id': 2,
                'imageId': 1,
                'inFavorites': False,
                'inInbox': False,
                'labels': [
                    {
                        'id': 6,
                        'name': 'Label1'
                    }
                ],
                'numTracks': 3,
                'releaseDate': '1970-02-05',
                'releaseType': 'ALBUM',
                'releaseYear': 1970,
                'runtime': 3,
                'title': 'Release1',
                'tracks': [
                    {
                        'id': 1,
                        'title': 'Track0'
                    },
                    {
                        'id': 2,
                        'title': 'Track1'
                    },
                    {
                        'id': 3,
                        'title': 'Track2'
                    }
                ]
            }
        }
    }
}

snapshots['test_del_release_from_collection_bad_collection 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection 999 does not exist.',
            'path': [
                'delReleaseFromCollection'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_del_release_from_collection_bad_release 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Release 9999 does not exist.',
            'path': [
                'delReleaseFromCollection'
            ],
            'type': 'NotFound'
        }
    ]
}

snapshots['test_del_release_from_collection_doesnt_exist 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Release is not in collection.',
            'path': [
                'delReleaseFromCollection'
            ],
            'type': 'DoesNotExist'
        }
    ]
}

snapshots['test_update_collection 1'] = {
    'data': {
        'updateCollection': {
            'id': 3,
            'lastUpdatedOn': 1577840461,
            'name': 'NewCollection',
            'numReleases': 3,
            'releases': [
                {
                    'id': 2,
                    'title': 'Release1'
                },
                {
                    'id': 3,
                    'title': 'Release2'
                },
                {
                    'id': 4,
                    'title': 'Release3'
                }
            ],
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
            'type': 'COLLAGE'
        }
    }
}

snapshots['test_update_collection_duplicate 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection "Collage3" already exists.',
            'path': [
                'updateCollection'
            ],
            'type': 'Duplicate'
        }
    ]
}

snapshots['test_update_collection_immutable 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'System collections cannot be modified.',
            'path': [
                'updateCollection'
            ],
            'type': 'Immutable'
        }
    ]
}

snapshots['test_update_collection_not_found 1'] = {
    'data': None,
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'Collection 99999 does not exist.',
            'path': [
                'updateCollection'
            ],
            'type': 'NotFound'
        }
    ]
}

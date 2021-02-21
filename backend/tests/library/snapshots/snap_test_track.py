# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_add_artist 1'] = GenericRepr("T(id=10, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/10. Going to Georgia.m4a'), sha256=b'\\x03\\xdb>|\\xc9H\\x7fGm\\x84\\xac\\xec`\\xf5/\\xe8\\xf4\\xf7\\xd2\\xbf\\x97Bh\\x14\\xd0\\x83:\\xe2\\x9b5(\\x17', title='Going to Georgia', release_id=2, duration=153, track_number='10', disc_number='1')")

snapshots['test_add_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    },
    {
        'artist': GenericRepr("T(id=4, name='Abakus', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_add_artist_new_role 1'] = GenericRepr("T(id=10, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/10. Going to Georgia.m4a'), sha256=b'\\x03\\xdb>|\\xc9H\\x7fGm\\x84\\xac\\xec`\\xf5/\\xe8\\xf4\\xf7\\xd2\\xbf\\x97Bh\\x14\\xd0\\x83:\\xe2\\x9b5(\\x17', title='Going to Georgia', release_id=2, duration=153, track_number='10', disc_number='1')")

snapshots['test_add_artist_new_role 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.REMIXER: 3>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    }
]

snapshots['test_artists 1'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    },
    {
        'artist': GenericRepr("T(id=3, name='John Darnielle', starred=False, num_releases=0)"),
        'role': GenericRepr('<ArtistRoles.COMPOSER: 5>')
    }
]

snapshots['test_create 1'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_del_artist 1'] = GenericRepr("T(id=10, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/10. Going to Georgia.m4a'), sha256=b'\\x03\\xdb>|\\xc9H\\x7fGm\\x84\\xac\\xec`\\xf5/\\xe8\\xf4\\xf7\\xd2\\xbf\\x97Bh\\x14\\xd0\\x83:\\xe2\\x9b5(\\x17', title='Going to Georgia', release_id=2, duration=153, track_number='10', disc_number='1')")

snapshots['test_del_artist 2'] = [
    {
        'artist': GenericRepr("T(id=2, name='Aaron West and the Roaring Twenties', starred=False, num_releases=1)"),
        'role': GenericRepr('<ArtistRoles.MAIN: 1>')
    }
]

snapshots['test_from_id_success 1'] = GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')")

snapshots['test_search_all 1'] = [
    GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')"),
    GenericRepr("T(id=10, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/10. Going to Georgia.m4a'), sha256=b'\\x03\\xdb>|\\xc9H\\x7fGm\\x84\\xac\\xec`\\xf5/\\xe8\\xf4\\xf7\\xd2\\xbf\\x97Bh\\x14\\xd0\\x83:\\xe2\\x9b5(\\x17', title='Going to Georgia', release_id=2, duration=153, track_number='10', disc_number='1')"),
    GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')"),
    GenericRepr('T(id=3, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/03. St. Joe Keeps Us Safe.m4a\'), sha256=b\'\\x9c",\\xae\\xc4\\xb1\\x88\\x19\\xeb\\xefK\\xfa\\xf7Z\\xc3\\x19r+\\xfa?\\x96`\\xda\\xa3Ss+\\x13\\x9a\\xabV\\x96\', title=\'St. Joe Keeps Us Safe\', release_id=2, duration=210, track_number=\'3\', disc_number=\'1\')'),
    GenericRepr("T(id=4, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/04. Runnin’ Scared.m4a'), sha256=b'\\x9e\\x00\\xa1\\x88z\\x87\\xe8\\xa6+wh\\xf76\\xfb0\\x06\\xf6\\x8b\\xb1@\\x07\\xa7B$\\x1e\\xd7%\\xb9!!P\\xd4', title='Runnin’ Scared', release_id=2, duration=193, track_number='4', disc_number='1')"),
    GenericRepr("T(id=5, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/05. Divorce and the American South.m4a'), sha256=b'=\\xb4_\\x13\\r\\x83`x\\xf3\\xba\\xf5\\xc9\\xa6\\x80\\x9ax\\xa2\\x14\\xc2\\xa8\\x1f\\x9f\\xa7}xr]*?\\xa4\\x90\\xe0', title='Divorce and the American South', release_id=2, duration=259, track_number='5', disc_number='1')"),
    GenericRepr("T(id=6, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/06. The Thunderbird Inn.m4a'), sha256=b'\\xa9G206\\xd9\\x99\\x83GI\\x8a\\xa3f-V\\x01;\\xdd\\x02\\r\\xfd\\x9f\\xb1\\x03\\x8a\\xb1?\\xc5\\xf99\\x91;', title='The Thunderbird Inn', release_id=2, duration=199, track_number='6', disc_number='1')"),
    GenericRepr('T(id=7, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/07. Get Me Out of Here Alive.m4a\'), sha256=b\'sT+\\xbe\\xcd\\x04h>XD@V}\\xae\\x8a\\xe2\\x01\\x91\\x84\\x1e=]\\x0c\\x93bS"\\x8a\\xfd\\xde\\xabB\', title=\'Get Me Out of Here Alive\', release_id=2, duration=212, track_number=\'7\', disc_number=\'1\')'),
    GenericRepr("T(id=8, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/08. You Ain’t No Saint.m4a'), sha256=b'~\\x95\\xadd&n\\x12(\\x0bs\\xed3\\xbf\\xfa\\xa0\\xfc0\\xaez\\xec\\xe7Z\\xa7\\xb5\\x0b\\x81D\\x94\\xdb\\xd0\\xb1\\x11', title='You Ain’t No Saint', release_id=2, duration=265, track_number='8', disc_number='1')"),
    GenericRepr("T(id=9, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/09. Carolina Coast.m4a'), sha256=b'\\x95\\xc3\\xe0:\\x8d#\\x1c\\x8b\\x06\\xc4\\x0e\\xbfp\\xd4\\r\\xd1_Z\\xde\\x1f\\xf5\\xaf1\\xd0Z\\xe0i\\xa3\\x04\\x1f\\xc8\\x83', title='Carolina Coast', release_id=2, duration=302, track_number='9', disc_number='1')"),
    GenericRepr("T(id=19, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/01. Let Go.m4a'), sha256=b'\\x9e)\\x10\\xb0\\xd2\\x04\\x91\\xf0\\x9d\\x1c\\xee\\xe7\\x83\\xae\\xdd_\\xae\\x04\\x00\\x9ec:\\xb6\\xd1\\x86\\x11.\\x07b\\xe8l$', title='Let Go', release_id=3, duration=312, track_number='1', disc_number='0')"),
    GenericRepr("T(id=18, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/10. The Beginning.m4a'), sha256=b'\\xbcX-\\x8b\\xa0\\xebnM\\xac\\x9a\\xd6\\xaelM\\t\\xe3\\x16\\xf1|`\\xbd>\\x81\\xd0J\\xc9)3 \\x852\\x85', title='The Beginning', release_id=3, duration=382, track_number='10', disc_number='0')"),
    GenericRepr("T(id=11, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/11. Airwaves.m4a'), sha256=b'Mq(rg[E\\xe2J\\xe1\\xeb(\\x06\\xf8|\\xdfd\\xe0*\\xda\\xe8w\\x82\\t\\x1f\\x94\\x96\\x1f\\xbcb=\\x14', title='Airwaves', release_id=3, duration=271, track_number='11', disc_number='0')"),
    GenericRepr("T(id=20, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/02. Storm.m4a'), sha256=b'\\x08\\x1b\\xda6\\x8aY\\x934\\xac\\x108\\xd8\\xfd\\x96X\\xe0j\\x1fl5\\xd4\\xa2}\\xc7#\\xd2\\xd6\\x91\\x97\\x0f\\xf4\\x8a', title='Storm', release_id=3, duration=268, track_number='2', disc_number='0')"),
    GenericRepr("T(id=21, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/03. Kite.m4a'), sha256=b'\\xf6BY\\x94\\x88\\xe7\\xee\\x9cA\\xd0\\xbf\\xb8tD\\xa8\\xda\\xf0\\tLm\\xa6\\xdb\\xdd\\xc9\\x15\\xffmS\\xe6\\x07\\xe3\\xd0', title='Kite', release_id=3, duration=320, track_number='3', disc_number='0')"),
    GenericRepr('T(id=12, filepath=PosixPath(\'/tmp/repertoire-library/Abakus/2016. Departure/04. Liberated from the Negative.m4a\'), sha256=b"\\xb3~\\xbf\'m\\xb0=r\\xa4b\\xc3\\x15-\\xda\\xbb\\xde\\t\\x8bmF\\x17\\xa6/\\x12\\x97\\xb7i\\r%ckl", title=\'Liberated from the Negative\', release_id=3, duration=304, track_number=\'4\', disc_number=\'0\')'),
    GenericRepr("T(id=13, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/05. Hope.m4a'), sha256=b'\\x1b\\xa2^\\xb9;j\\xe9\\x9ffK\\xa58r\\x83\\xeb\\xdaf\\r\\xf4\\xf5\\xf8\\xad\\x13d\\x91\\x99\\xd3\\xe7odK\\xb4', title='Hope', release_id=3, duration=262, track_number='5', disc_number='0')"),
    GenericRepr("T(id=14, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/06. Dreamer.m4a'), sha256=b'\\xd2\\xd2\\xef\\x07\\xd1\\xde\\xf3 \\x82\\x9aC(\\xf1U\\x83L\\x81mI\\xec\\x17\\xad\\xa0\\xf4\\xcc\\xf0\\xd0n+H3\\xc4', title='Dreamer', release_id=3, duration=412, track_number='6', disc_number='0')"),
    GenericRepr("T(id=15, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/07. Stay with Me.m4a'), sha256=b'\\xe0K\\x14\\xc0\\\\\\xc2h\\xdb\\x85\\xd0KA\\x94kb\\x9a*UOA\\x8aB\\x8e\\xd2\\x08\\xa5&\\x95\\x04\\xf0\\x0e[', title='Stay with Me', release_id=3, duration=307, track_number='7', disc_number='0')"),
    GenericRepr('T(id=16, filepath=PosixPath(\'/tmp/repertoire-library/Abakus/2016. Departure/08. Still a Soul in There.m4a\'), sha256=b"9\\xc1\\xf7\\xb7\\xd5\\xca\\xd0GR\\x15\'\\xf0\\xb4\\xe0\\xc9\\x13C\\\\\\x91\\xd9\\x81\\x05\\xb4\\xf9\\xfcl\\x9a\\xbc\\xa1\\xef]\\xbc", title=\'Still a Soul in There\', release_id=3, duration=372, track_number=\'8\', disc_number=\'0\')'),
    GenericRepr("T(id=17, filepath=PosixPath('/tmp/repertoire-library/Abakus/2016. Departure/09. Lost Myself.m4a'), sha256=b'\\xd3c\\x96C\\xd7;\\xef\\x86B8?\\xda\\xe0)\\x96\\x1b1\\x97A\\xe3\\xe9a@h\\x18\\xf9b\\xc9\\\\l\\xb5\\xd3', title='Lost Myself', release_id=3, duration=303, track_number='9', disc_number='0')")
]

snapshots['test_search_page 1'] = [
    GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')"),
    GenericRepr("T(id=10, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/10. Going to Georgia.m4a'), sha256=b'\\x03\\xdb>|\\xc9H\\x7fGm\\x84\\xac\\xec`\\xf5/\\xe8\\xf4\\xf7\\xd2\\xbf\\x97Bh\\x14\\xd0\\x83:\\xe2\\x9b5(\\x17', title='Going to Georgia', release_id=2, duration=153, track_number='10', disc_number='1')")
]

snapshots['test_search_page_2 1'] = [
    GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')"),
    GenericRepr('T(id=3, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/03. St. Joe Keeps Us Safe.m4a\'), sha256=b\'\\x9c",\\xae\\xc4\\xb1\\x88\\x19\\xeb\\xefK\\xfa\\xf7Z\\xc3\\x19r+\\xfa?\\x96`\\xda\\xa3Ss+\\x13\\x9a\\xabV\\x96\', title=\'St. Joe Keeps Us Safe\', release_id=2, duration=210, track_number=\'3\', disc_number=\'1\')')
]

snapshots['test_search_search 1'] = [
    GenericRepr("T(id=2, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/02. Grapefruit.m4a'), sha256=b'\\xb8^\\xf2tc\\x9c\\x13\\x1e\\xb69\\xe9\\x84;Q\\xc0\\xe0(\\xa8p\\xe3o\\xb4\\xe1\\xd8a\\xe48\\xd6\\x82\\x1f\\xaev', title='Grapefruit', release_id=2, duration=252, track_number='2', disc_number='1')"),
    GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='Our Apartment', release_id=2, duration=213, track_number='1', disc_number='1')"),
    GenericRepr("T(id=4, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/04. Runnin’ Scared.m4a'), sha256=b'\\x9e\\x00\\xa1\\x88z\\x87\\xe8\\xa6+wh\\xf76\\xfb0\\x06\\xf6\\x8b\\xb1@\\x07\\xa7B$\\x1e\\xd7%\\xb9!!P\\xd4', title='Runnin’ Scared', release_id=2, duration=193, track_number='4', disc_number='1')"),
    GenericRepr("T(id=9, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/09. Carolina Coast.m4a'), sha256=b'\\x95\\xc3\\xe0:\\x8d#\\x1c\\x8b\\x06\\xc4\\x0e\\xbfp\\xd4\\r\\xd1_Z\\xde\\x1f\\xf5\\xaf1\\xd0Z\\xe0i\\xa3\\x04\\x1f\\xc8\\x83', title='Carolina Coast', release_id=2, duration=302, track_number='9', disc_number='1')"),
    GenericRepr("T(id=8, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/08. You Ain’t No Saint.m4a'), sha256=b'~\\x95\\xadd&n\\x12(\\x0bs\\xed3\\xbf\\xfa\\xa0\\xfc0\\xaez\\xec\\xe7Z\\xa7\\xb5\\x0b\\x81D\\x94\\xdb\\xd0\\xb1\\x11', title='You Ain’t No Saint', release_id=2, duration=265, track_number='8', disc_number='1')"),
    GenericRepr("T(id=6, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/06. The Thunderbird Inn.m4a'), sha256=b'\\xa9G206\\xd9\\x99\\x83GI\\x8a\\xa3f-V\\x01;\\xdd\\x02\\r\\xfd\\x9f\\xb1\\x03\\x8a\\xb1?\\xc5\\xf99\\x91;', title='The Thunderbird Inn', release_id=2, duration=199, track_number='6', disc_number='1')"),
    GenericRepr('T(id=3, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/03. St. Joe Keeps Us Safe.m4a\'), sha256=b\'\\x9c",\\xae\\xc4\\xb1\\x88\\x19\\xeb\\xefK\\xfa\\xf7Z\\xc3\\x19r+\\xfa?\\x96`\\xda\\xa3Ss+\\x13\\x9a\\xabV\\x96\', title=\'St. Joe Keeps Us Safe\', release_id=2, duration=210, track_number=\'3\', disc_number=\'1\')'),
    GenericRepr('T(id=7, filepath=PosixPath(\'/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/07. Get Me Out of Here Alive.m4a\'), sha256=b\'sT+\\xbe\\xcd\\x04h>XD@V}\\xae\\x8a\\xe2\\x01\\x91\\x84\\x1e=]\\x0c\\x93bS"\\x8a\\xfd\\xde\\xabB\', title=\'Get Me Out of Here Alive\', release_id=2, duration=212, track_number=\'7\', disc_number=\'1\')'),
    GenericRepr("T(id=5, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/05. Divorce and the American South.m4a'), sha256=b'=\\xb4_\\x13\\r\\x83`x\\xf3\\xba\\xf5\\xc9\\xa6\\x80\\x9ax\\xa2\\x14\\xc2\\xa8\\x1f\\x9f\\xa7}xr]*?\\xa4\\x90\\xe0', title='Divorce and the American South', release_id=2, duration=259, track_number='5', disc_number='1')"),
    GenericRepr("T(id=10, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/10. Going to Georgia.m4a'), sha256=b'\\x03\\xdb>|\\xc9H\\x7fGm\\x84\\xac\\xec`\\xf5/\\xe8\\xf4\\xf7\\xd2\\xbf\\x97Bh\\x14\\xd0\\x83:\\xe2\\x9b5(\\x17', title='Going to Georgia', release_id=2, duration=153, track_number='10', disc_number='1')")
]

snapshots['test_update_fields 1'] = GenericRepr("T(id=1, filepath=PosixPath('/tmp/repertoire-library/Aaron West and the Roaring Twenties/2014. We Don’t Have Each Other/01. Our Apartment.m4a'), sha256=b'u\\xca\\x14C!e\\xa9\\xee\\x87\\xeec\\xdfeN\\xf7\\x7fE\\xd0\\t\\xbb\\xe5}\\xa0a\\nE<H\\xc6\\xb2j\\x1a', title='New Title', release_id=3, duration=213, track_number='X Æ', disc_number='A-12')")

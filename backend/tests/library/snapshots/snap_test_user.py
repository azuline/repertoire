# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_create_user_success 1'] = GenericRepr("T(id=3, username='neW1')")

snapshots['test_from_id_success 1'] = GenericRepr("T(id=1, username='admin')")

snapshots['test_from_token_success 1'] = GenericRepr("T(id=1, username='admin')")

snapshots['test_from_username_success 1'] = GenericRepr("T(id=1, username='admin')")

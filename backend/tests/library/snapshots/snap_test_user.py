# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_create_user_success 1'] = GenericRepr("T(id=3, nickname='neW1')")

snapshots['test_from_id_success 1'] = GenericRepr("T(id=1, nickname='admin')")

snapshots['test_from_token_failure_but_correct_prefix 1'] = None

snapshots['test_from_token_success 1'] = GenericRepr("T(id=1, nickname='admin')")

snapshots['test_from_nickname_success 1'] = GenericRepr("T(id=1, nickname='admin')")

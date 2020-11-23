# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_graphql_endpoint 1'] = b'{"data":{"user":{"id":1,"username":"admin"}}}'

snapshots['test_graphql_endpoint_no_auth 1'] = b'\n<!doctype html>\n<title>401 Unauthorized</title>\n<h1>Unauthorized</h1>\nNo permission -- see authorization schemes\n        '

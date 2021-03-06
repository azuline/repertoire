#!/usr/bin/env bash

# This script set ups the environment for end to end testing.
#
# ASSUMPTIONS:
# - A working frontend is available at localhost:3000.
# - A working backend is available at localhost:5000.
# - The data path is `../data`.
# - The standard test library is in `../testlib`.
#
# STEPS:
# 1. Set the system's secret key to all 0s.
# 1. Create a new admin user with tokens of all 0s.
# 2. Index the testlib by invoking the backend indexer API endpoint (TODO).

printf 'Inserting a tester user...'

# TODO: try combining into one call?

# Wipe the old tester user.
sqlite3 ../data/db.sqlite3 <<EOF
DELETE FROM system__users WHERE token_prefix = X'000000000000000000000000'
EOF

# Create a new tester user.
sqlite3 ../data/db.sqlite3 <<EOF
INSERT INTO system__users (
    nickname,
    token_prefix,
    token_hash,
    csrf_token
) VALUES (
    'tester',
    X'000000000000000000000000',
    'pbkdf2:sha256:150000\$b26LpXBc\$ab7f9cf988532362beed5db5c974a3759aef479042364994df568c0284a5fee2',
    X'0000000000000000000000000000000000000000000000000000000000000000'
)
EOF

echo ' done!'

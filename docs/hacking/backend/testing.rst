.. _backend_testing:

Testing
=======

This document covers the backend's automated testing setup and philosophy.

We use the pytest test framework for our tests. Refer to
https://docs.pytest.org/en/stable/index.html for more details on pytest.

Test Types
----------

The backend tests are primarily unit tests, with the exception of the GraphQL
API tests, which are snapshot integration tests.

In the future, we may look towards adding some other types of tests, such as
fuzz test or property based tests.

Philosophy
----------

This section covers some of the philosophies of our test suite.

Mocking
^^^^^^^

Rather than use mocks, we prefer to run tests in an environment that matches a
live environment as much as possible. For this reason, each test runs in a
temporary directory with its own data directory, containing all application
configuration files and an up-to-date database.

We do this because only when tests match the live environment as much as
possible will they be useful.

Dependencies
^^^^^^^^^^^^

Unfortunately, the unit tests are not completely isolated to the code that runs
them. The dependency structure of many tests mimics the dependency structure of
the code that they test. What this means is that if a dependency of the code
that's tested breaks, the test will likely also break.

Our philosophy is that a test with the same dependency structure as the code it
tests is acceptable. Tests, however, should not depend on code that the code it
tests does not depend on.

However, sometimes dependencies are inevitable. For many of the inevitable
dependencies, we provide test fixtures. We hold the invariant that test
fixtures work properly, even though some of them depend on the code we are
testing.

In the event that a fixture breaks, many tests will fail, but we will have a
single known place to fix the tests.

As an example of a fixture, a lot of code depends on data present in the
database, and the tests must insert data as a part of their setup. For this, we
provide a factory fixture that abstracts over data insertion. All data
insertion that occurs during test setup should use the factory fixture.


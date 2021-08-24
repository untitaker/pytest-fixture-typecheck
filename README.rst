========================
pytest-fixture-typecheck
========================

.. image:: https://img.shields.io/pypi/v/pytest-fixture-typecheck
    :target: https://pypi.org/project/pytest-sentry/

.. image:: https://img.shields.io/pypi/l/pytest-fixture-typecheck
    :target: https://pypi.org/project/pytest-sentry/

``pytest-fixture-typecheck`` is a `pytest <https://pytest.org>`_ plugin that inserts runtime assertions that your fixture usages are properly typed.

Problem
=======

Pytest fixtures are magic that mypy does not understand. This typechecks just fine::

    @pytest.fixture
    def myint():
        return 42

    def test_basic(myint: str):
        assert myint == 42

This test passes but the type annotation is wrong.

With this pytest plugin it will pass typechecking all the same, but your test
will fail at least.

If your tests do not have type annotations, this plugin does nothing. Use mypy
to enforce that everything has type annotations.

License
=======

Licensed under public domain.

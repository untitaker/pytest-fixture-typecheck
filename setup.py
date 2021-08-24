from setuptools import setup

setup(
    name="pytest-fixture-typecheck",
    description="A pytest plugin to ensure test fixtures have the right type.",
    long_description=open("README.rst").read(),
    author="Markus Unterwaditzer",
    version="0.1.0",
    license="Public Domain",
    author_email="markus@unterwaditzer.net",
    url="https://github.com/untitaker/pytest-fixture-typecheck",
    py_modules=["pytest_sentry"],
    entry_points={"pytest11": ["fixture_typecheck = pytest_fixture_typecheck"]},
    install_requires=["pytest", "typeguard"],
)

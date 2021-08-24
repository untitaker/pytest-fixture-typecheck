import typeguard


def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        for fixturename, ty in item.obj.__annotations__.items():
            typeguard.check_type(fixturename, item.funcargs[fixturename], ty)

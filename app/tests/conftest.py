import asyncio
from typing import Any, Generator

import pytest


@pytest.fixture(scope="session")
def event_loop(request: Any) -> Generator:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

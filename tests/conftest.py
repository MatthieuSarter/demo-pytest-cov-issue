import os
from pathlib import Path
from typing import Generator

import pytest

@pytest.fixture()
def cwd_to_src() -> Generator[None, None, None]:
    cwd = Path.cwd()
    os.chdir(Path(__file__).parent.parent / "src")
    yield
    os.chdir(cwd)
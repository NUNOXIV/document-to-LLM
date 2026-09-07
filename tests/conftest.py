"""Ein check(), das nicht fehlschlagen kann, prueft nichts.

check() sammelt Fehlschlaege in test_units.failures, und der eigene Runner
(python tests/test_units.py) wertet die Liste am Ende aus. Unter pytest tat
das niemand: jeder check()-basierte Test war gruen, egal was er fand — auch
in CI. Diese Fixture leert die Liste vor jedem Test und laesst den Test
scheitern, wenn danach etwas darin steht.
"""
from __future__ import annotations

import pytest

import test_units


@pytest.fixture(autouse=True)
def checks_muessen_gelten():
    test_units.failures.clear()
    yield
    offen = list(test_units.failures)
    test_units.failures.clear()
    assert not offen, "check() fehlgeschlagen: " + ", ".join(offen)

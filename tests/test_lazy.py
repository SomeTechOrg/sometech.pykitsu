"""Groups and models must only be imported when used."""

import subprocess
import sys
import textwrap


def run(code: str) -> str:
    out = subprocess.run(
        [sys.executable, "-c", textwrap.dedent(code)], check=True, capture_output=True, text=True
    )
    return out.stdout.strip()


def test_import_and_client_load_no_group_nor_model() -> None:
    out = run(
        """
        import sys, pykitsu
        k = pykitsu.PyKitsu("http://kitsu.test")
        a = pykitsu.AsyncPyKitsu("http://kitsu.test")
        loaded = [m for m in sys.modules if m.startswith(("pykitsu.groups", "pykitsu.models"))]
        print(loaded, "pydantic" in sys.modules)
        """
    )
    assert out == "[] False"


def test_group_access_loads_only_that_group() -> None:
    out = run(
        """
        import sys, pykitsu
        k = pykitsu.PyKitsu("http://kitsu.test")
        k.shots
        assert k.shots is k.shots
        print(sorted(m for m in sys.modules if m.startswith("pykitsu.groups.") and "_models" not in m))
        """
    )
    assert out == "['pykitsu.groups.shots']"


def test_models_package_is_lazy() -> None:
    out = run(
        """
        import sys
        import pykitsu.models as m
        before = "pykitsu.models._core" in sys.modules
        from pykitsu.models import Shot
        print(before, "pykitsu.models._core" in sys.modules, Shot.__name__)
        """
    )
    assert out == "False True Shot"

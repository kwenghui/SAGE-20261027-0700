"""Sage's recorded behaviour must not change by accident.

tools/behaviour_digests.py runs the 11 characterisation checks (tens of
thousands of cases: real answers, random tables, fake data servers, every
chart path, the whole page) and reduces each to a digest. This test compares
them with tests/golden/behaviour_digests.json.

If it fails after an INTENDED change, review the change, then run
    python tools/behaviour_digests.py --update
and explain the behaviour change in the commit message.
"""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.behaviour_digests import GOLDEN, current_digests  # noqa: E402


class RecordedBehaviourIsUnchanged(unittest.TestCase):
    def test_every_characterisation_digest_matches_the_accepted_one(self):
        expected = json.loads(GOLDEN.read_text(encoding="utf-8"))
        actual = current_digests()
        changed = sorted(name for name in expected if actual.get(name) != expected[name])
        self.assertEqual(changed, [], "Behaviour changed; see tools/behaviour_digests.py")
        self.assertEqual(sorted(actual), sorted(expected))


if __name__ == "__main__":
    unittest.main()

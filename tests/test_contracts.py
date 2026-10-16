"""Executable checks for the implemented scaffold contracts."""
import unittest
from models import MapConfig
from search import run_search
from tests.fixtures import example_graph


class ContractTests(unittest.TestCase):
    def test_unknown_algorithm_is_rejected(self):
        with self.assertRaises(ValueError):
            run_search(example_graph(), 0, 2, "unknown")

    def test_missing_node_is_rejected(self):
        with self.assertRaises(ValueError):
            run_search(example_graph(), 0, 99, "ucs")

    def test_unknown_astar_heuristic_is_rejected(self):
        with self.assertRaises(ValueError):
            run_search(example_graph(), 0, 2, "astar", "unknown")

    def test_config_is_immutable(self):
        from dataclasses import FrozenInstanceError
        with self.assertRaises(FrozenInstanceError):
            MapConfig().seed = 99

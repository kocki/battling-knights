# Standard Library
import json

# 3rd-party
import pytest
from battle import battle


@pytest.mark.parametrize('file_name', [
    'base',
    'attack',
    'attack_with_item_1',
    'attack_with_item_2',
    'many_items',
    'skip_item',
])
def test_json(file_name):
    """Base example from challenge."""
    with open(f'test/jsons/{file_name}.json') as f:
        expected = json.loads(f.read())
    assert json.loads(battle(f'test/scenarios/{file_name}.txt')) == expected

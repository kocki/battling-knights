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
    'pickup_item_before_fight',
])
def test_board(file_name):
    """Base example from challenge."""
    with open(f'test/boards/{file_name}.txt') as f:
        expected = f.read().strip()
    assert battle(f'test/scenarios/{file_name}.txt', report=True).strip() == expected

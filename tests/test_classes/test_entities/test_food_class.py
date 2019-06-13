import random
import pytest
from src.classes.entities.food_class import Food


@pytest.fixture()
def food():
    return Food((3,5))


def test_food(food):
    assert food.position == (3.5)
    food_durability = food.__durability
    food.decomposition()
    assert food_durability - 5 == food.__durability

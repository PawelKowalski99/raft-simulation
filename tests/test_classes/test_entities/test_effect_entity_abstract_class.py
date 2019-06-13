from src.classes.entities.effect_entity_abstract_class import EffectEntityAbstract
import pytest
import random


class EffectEntityAbstractInstance(EffectEntityAbstract):
    def __init__(self, position):
        super().__init__(position)
        self.effect_value = random.randint(10, 20)


@pytest.fixture
def EffectEntityAbstractTestInstance():
    return EffectEntityAbstractInstance((3, 4))


def test_EntityAbstract(EffectEntityAbstractTestInstance):
    assert EffectEntityAbstractTestInstance.type == None
    assert EffectEntityAbstractTestInstance.symbol == None
    assert EffectEntityAbstractTestInstance.position == (3, 4)
    assert EffectEntityAbstractTestInstance.effect_value >= 10 or \
           EffectEntityAbstractTestInstance.effect_value <= 20

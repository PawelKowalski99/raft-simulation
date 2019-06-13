from src.classes.entities.entity_abstract_class import EntityAbstract
import pytest


class EntityAbstractInstance(EntityAbstract):
    def __init__(self, position):
        super().__init__(position)


@pytest.fixture
def entityAbstractTestInstance():
    return EntityAbstractInstance((3, 4))


def test_EntityAbstract(entityAbstractTestInstance):
    assert entityAbstractTestInstance.type == None
    assert entityAbstractTestInstance.symbol == None
    assert entityAbstractTestInstance.position == (3, 4)

from models.models_languague import LanguageModel

def test_languague_not_none():
    languague = LanguageModel().get__language()
    assert languague != None

def test_languague_has_element():
    languague = LanguageModel().get__language()
    assert len(languague) > 0

def test_languague_check_element_length():
    languague = LanguageModel().get__language()
    for lan in languague:
        assert len(lan) > 0
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message(message="message", key=908) == "egassem"
    assert encrypt_message(message="message2", key=2) == "2egass_em"
    assert encrypt_message(message="message3", key=3) == "sem_3egas"

    # tipo incorreto para key
    with pytest.raises(TypeError):
        encrypt_message(message="incorreto para key", key="")
    # tipo incorreto para message
    with pytest.raises(TypeError):
        encrypt_message(message=656, key=3)

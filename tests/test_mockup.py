from intro_pytest import hello_world, saved_world
import pytest
import os


def test_hello_world_3times():
    expected = "hello world hello world hello world"
    result = hello_world(3)
    assert result == expected


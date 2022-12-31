from game import *
import pytest

def test_leader():
	assert leader('me') == "CS50 will not kill me"
	with pytest.raises(ValueError):
		leader('game')

def test_no_of_games():
	assert no_of_games('you') == "You've done enough"
	with pytest.raises(NameError):
		no_of_games('game')

def test_user():
	assert user('should') == "I probably should have started earlier"
	with pytest.raises(ValueError):
		user('game')

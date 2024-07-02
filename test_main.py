import pytest
from main import UserSettings

@pytest.fixture
def settings():
    settings = UserSettings()
    settings.reset_settings()
    return settings

def test_singleton(settings):
    settings2 = UserSettings()
    assert id(settings) == id(settings2), "Singleton failed, instances are different."

def test_set_and_get_setting(settings):
    settings.set_setting("theme", "dark")
    assert settings.get_setting("theme") == "dark", "Failed to get the correct setting value."

def test_reset_settings(settings):
    settings.set_setting("theme", "dark")
    settings.reset_settings()
    assert settings.get_setting("theme") is None, "Failed to reset settings."

def test_display_settings(capsys, settings):
    settings.set_setting("theme", "dark")
    settings.display_settings()
    captured = capsys.readouterr()
    assert "theme: dark" in captured.out, "Failed to display settings correctly."

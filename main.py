import json

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UserSettings(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key, None)

    def reset_settings(self):
        self.settings.clear()

    def display_settings(self):
        if len(self.settings.items()) > 0:
            for key, value in self.settings.items():
                print(f"{key}: {value}")
        else:
            print('No settings availbale.')

    def save_settings(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.settings, file)
            print(f"Settings saved to {filename}.")
        except Exception as e:
            print(f"Error saving settings: {e}")

    def load_settings(self, filename):
        try:
            with open(filename, 'r') as file:
                self.settings = json.load(file)
            print(f"Settings loaded from {filename}.")
        except FileNotFoundError:
            print(f"Settings file {filename} not found.")
        except Exception as e:
            print(f"Error loading settings: {e}")


if __name__ == "__main__":
    settings = UserSettings()

    # Make some comments
    settings.set_setting("theme", "dark")
    settings.set_setting("language", "en")
    settings.set_setting("visibility", "contacts only")
    settings.set_setting("notifications", "enabled")

    print("Settings from settings:")
    settings.display_settings()

    settings.save_settings("user_settings.json")

    settings.reset_settings()
    print("\nSettings after reset:")
    settings.display_settings()

    settings.load_settings("user_settings.json")
    print("\nSettings after loading from file:")
    settings.display_settings()

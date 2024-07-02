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
        for key, value in self.settings.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    settings1 = UserSettings()
    settings2 = UserSettings()

    if id(settings1) == id(settings2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    # Пример использования настроек пользователя
    settings1.set_setting("theme", "dark")
    settings1.set_setting("language", "en")
    settings2.set_setting("notifications", "enabled")

    print("Settings from settings1:")
    settings1.display_settings()

    print("\nSettings from settings2 (should be the same as settings1):")
    settings2.display_settings()

    # Сброс всех настроек
    settings1.reset_settings()
    print("\nSettings after reset:")
    settings1.display_settings()

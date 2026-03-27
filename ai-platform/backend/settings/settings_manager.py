class SettingsManager:
    """Add missing settings keys without removing existing ones."""

    def __init__(self, current_settings: dict):
        self.settings = current_settings

    def add_settings(self, new_settings: dict):
        for key, value in new_settings.items():
            if key not in self.settings:
                self.settings[key] = value

    def get_settings(self):
        return self.settings

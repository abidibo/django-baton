from .utils import PlaywrightTestCase


class TestBatonTheme(PlaywrightTestCase):
    viewport = {"width": 1920, "height": 1280}

    def setUp(self):
        super().setUp()
        self.login()
        self.wait_baton_ready()

    def test_theme(self):
        theme = self.page.locator("html").get_attribute("data-bs-theme")
        self.assertIn(theme, ["light", "dark"])

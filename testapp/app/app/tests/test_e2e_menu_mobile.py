from .utils import PlaywrightTestCase


class TestBatonMenuMobile(PlaywrightTestCase):
    viewport = {"width": 480, "height": 600}

    def setUp(self):
        super().setUp()
        self.login()
        self.wait_baton_ready()

    # The mobile navbar is only translated off-screen (not display:none), so we
    # check its computed position rather than visibility.
    def _wait_navbar_hidden(self):
        self.page.wait_for_function(
            """() => {
                const el = document.querySelector('.sidebar-menu');
                const s = getComputedStyle(el);
                return (parseInt(s.left) || 0) + (parseInt(s.width) || 0) <= 0;
            }"""
        )

    def _wait_navbar_visible(self):
        self.page.wait_for_function(
            """() => {
                const el = document.querySelector('.sidebar-menu');
                return (parseInt(getComputedStyle(el).left) || 0) === 0;
            }"""
        )

    def _body_classes(self):
        return self.page.locator("body").get_attribute("class").split()

    def test_menu(self):
        page = self.page

        self.assertNotIn("menu-open", self._body_classes())
        self._wait_navbar_hidden()

        page.click(".navbar-toggler")
        self._wait_navbar_visible()
        self.assertIn("menu-open", self._body_classes())

        root_voices = page.locator(".depth-0 > li")

        page.click(".toggle-menu")
        self._wait_navbar_hidden()
        self.assertNotIn("menu-open", self._body_classes())

        page.click(".navbar-toggler")
        self._wait_navbar_visible()

        # system title voice
        self.assertEqual(root_voices.nth(0).inner_text(), "lock\nSYSTEM")
        self.assertTrue(root_voices.nth(0).is_visible())
        self.assertIn("title", root_voices.nth(0).get_attribute("class").split())
        self.assertEqual(root_voices.count(), 4)

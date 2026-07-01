from .utils import PlaywrightTestCase


class TestBatonIndexMobile(PlaywrightTestCase):
    viewport = {"width": 480, "height": 600}

    def setUp(self):
        super().setUp()
        self.login()
        self.wait_baton_ready()

    def test_navbar(self):
        page = self.page

        # toggler
        self.assertTrue(page.locator(".navbar-toggler").is_visible())

        # site title
        self.assertEqual(page.locator("#site-name a").inner_html(), "Baton Test App")

        # user dropdown
        user_dropdown = page.locator("#user-tools .dropdown-toggle")
        self.assertEqual(user_dropdown.inner_text().strip(), "admin")
        self.assertTrue(user_dropdown.is_visible())

        # user dropdown menu
        menu = page.locator("#user-tools .dropdown-menu a")
        self.assertEqual(menu.count(), 5)
        self.assertEqual(menu.nth(0).inner_html(), "View site")
        self.assertEqual(menu.nth(1).inner_html(), "Documentation")
        self.assertEqual(menu.nth(2).inner_html(), "Change password")
        self.assertEqual(menu.nth(3).inner_html(), "Log out")
        self.assertEqual(
            menu.nth(4)
            .inner_html()
            .replace("Light ", "")
            .replace("Dark ", ""),  # don't know system theme
            "theme",
        )

    def test_content(self):
        page = self.page

        page_title = page.locator("#content h1")
        self.assertEqual(page_title.inner_html(), "Baton administration")
        self.assertTrue(page_title.is_visible())

        self.assertTrue(page.locator("#recent-actions-module").is_visible())

        self.assertEqual(page.locator("#content-main .module").count(), 3)

    def test_footer(self):
        links = self.page.locator("#footer .col-sm-4 p")
        self.assertEqual(links.count(), 3)
        self.assertEqual(
            links.nth(0).locator("a").get_attribute("href"),
            "mailto:mail@otto.to.it",
        )
        self.assertEqual(links.nth(0).inner_text().strip(), "help Support")
        self.assertEqual(
            links.nth(1).inner_text().strip(), "Copyright © 2026 Otto srl"
        )
        self.assertEqual(
            links.nth(2).inner_text().strip(),
            "Baton Test App · Developed by Otto srl",
        )

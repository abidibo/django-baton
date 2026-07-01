from .utils import PlaywrightTestCase


class TestBatonIndex(PlaywrightTestCase):
    def setUp(self):
        super().setUp()
        self.login()
        self.wait_baton_ready()

    def test_navbar(self):
        site_name = self.page.locator("#site-name a")
        self.assertEqual(site_name.inner_html(), "Baton Test App")

    def test_content(self):
        page = self.page

        # page title
        page_title = page.locator("#content h1")
        self.assertEqual(page_title.inner_html(), "Baton administration")
        self.assertTrue(page_title.is_visible())

        # recent actions
        self.assertTrue(page.locator("#recent-actions-module").is_visible())

        self.assertEqual(page.locator("#content-main .module").count(), 3)

    def test_footer(self):
        links = self.page.locator("#footer .col-sm-4 p")
        self.assertEqual(links.count(), 3)
        # support
        self.assertEqual(
            links.nth(0).locator("a").get_attribute("href"),
            "mailto:mail@otto.to.it",
        )
        self.assertEqual(links.nth(0).inner_text().strip(), "help Support")
        # copyright
        self.assertEqual(
            links.nth(1).inner_text().strip(), "Copyright © 2026 Otto srl"
        )
        # powered by
        self.assertEqual(
            links.nth(2).inner_text().strip(),
            "Baton Test App · Developed by Otto srl",
        )

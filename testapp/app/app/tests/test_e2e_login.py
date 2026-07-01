from playwright.sync_api import expect

from .utils import PlaywrightTestCase


class TestBatonLogin(PlaywrightTestCase):
    def test_form(self):
        page = self.page
        page.goto(self.url("/admin/"))

        # login page header
        self.assertEqual(page.locator("#header").inner_text().strip(), "Baton Test App")

        expect(page.locator("#id_username")).to_be_visible()
        expect(page.locator("#id_password")).to_be_visible()
        expect(page.locator("input[type=submit]")).to_be_visible()

        page.fill("#id_username", "admin")
        page.fill("#id_password", "admin")
        page.click("input[type=submit]")

        page.wait_for_url("**/en/admin/")
        self.assertTrue(page.url.endswith("/en/admin/"))

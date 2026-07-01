from playwright.sync_api import expect

from .utils import PlaywrightTestCase


class TestBatonClIncludes(PlaywrightTestCase):
    def setUp(self):
        super().setUp()
        self.login("/admin/news/news/")
        self.wait_baton_ready()

    def test_includes(self):
        page = self.page
        include = page.locator(".baton-cl-include-above")
        expect(include).to_be_visible()

        # the element right after the include should be the changelist form
        sibling = include.locator("xpath=following-sibling::*[1]")
        self.assertEqual(sibling.get_attribute("id"), "changelist-form")

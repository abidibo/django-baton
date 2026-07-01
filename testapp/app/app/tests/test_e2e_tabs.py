from playwright.sync_api import expect

from .utils import PlaywrightTestCase


class TestBatonTabs(PlaywrightTestCase):
    viewport = {"width": 1920, "height": 2080}

    def setUp(self):
        super().setUp()
        self.login("/admin/news/news/1/change/")
        self.wait_baton_ready()

    def test_tabs(self):
        page = self.page

        # tabs number and labels
        tabs = page.locator(".nav-tabs .nav-item")
        expect(tabs).to_have_count(6)
        for i, label in enumerate(
            ["Dates", "Main", "Flags", "Attachments", "Videos", "Activities"]
        ):
            self.assertEqual(tabs.nth(i).inner_text(), label)

        # activating a tab reveals its fields
        input_date = page.locator("#id_date")
        self.assertFalse(input_date.is_visible())
        tabs.nth(0).click()  # Dates
        expect(input_date).to_be_visible()

        # tabs navigation
        input_share = page.locator("#id_share")
        description_att = page.locator(".tab-fs-attachments .description")
        self.assertFalse(input_share.is_visible())
        self.assertFalse(description_att.is_visible())

        tabs.nth(2).click()  # Flags
        expect(input_share).to_be_visible()
        self.assertFalse(description_att.is_visible())

        tabs.nth(3).click()  # Attachments
        expect(input_share).to_be_hidden()

        # fieldset description
        expect(description_att).to_be_visible()
        self.assertEqual(
            description_att.inner_text(), "Add as many attachments as you want"
        )

        # tabs groups && inlines
        self.assertTrue(page.locator("#id_attachments_summary_en").is_visible())
        inlines = page.locator(
            "#group-fs-attachments--inline-attachments .inline-related .module"
        ).first
        inline_title = inlines.locator("h2").first
        expect(inline_title).to_be_visible()
        self.assertEqual(inline_title.inner_text(), "Attachments")

        rows = inlines.locator(".dynamic-attachments")
        expect(rows).to_have_count(2)
        add_button = inlines.locator(".add-row a")
        expect(add_button).to_be_visible()
        add_button.click()
        expect(rows).to_have_count(3)

    def test_detect_tab_error(self):
        page = self.page

        tabs = page.locator(".nav-tabs .nav-item")
        tabs.nth(3).click()  # Attachments

        # fill a field on the extra inline row and save: the incomplete row
        # triggers a validation error, and baton should reopen the tab holding it
        page.locator("#id_attachments-1-caption").fill("test")
        page.click("input[type=submit][name=_continue]")

        self.wait_baton_ready()

        self.assertFalse(page.locator("#id_share").is_visible())
        description_att = page.locator(".tab-fs-attachments .description")
        expect(description_att).to_be_visible()
        self.assertEqual(
            description_att.inner_text(), "Add as many attachments as you want"
        )

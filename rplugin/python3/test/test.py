from unittest import TestCase

from open_plugin_page import OpenPluginPage


class TestExtractUrl(TestCase):

    def assertGHUrl(self, url, name):
        self.assertEqual(
                url, "http://github.com/" + name
            )

    def test_plugin_letters_only(self):
        plugin_name = "Plug 'scrooloose/nerdtree'"
        url = OpenPluginPage._extract_url(plugin_name)
        self.assertIsNotNone(url)
        self.assertGHUrl(url, 'scrooloose/nerdtree')

    def test_plugin_letters_and_numbers(self):
        plugin_name = "Plug 'Chiel92/vim-autoformat'  \" Easy code formatting"
        url = OpenPluginPage._extract_url(plugin_name)
        self.assertIsNotNone(url)
        self.assertGHUrl(url, 'Chiel92/vim-autoformat')

    def test_plugin_with_options(self):
        plugin_name = "Plug 'plasticboy/vim-markdown', { 'for': 'markdown' }"
        url = OpenPluginPage._extract_url(plugin_name)
        self.assertIsNotNone(url)
        self.assertGHUrl(url, 'plasticboy/vim-markdown')

    def test_plugin_with_branch_option(self):
        plugin_name = "Plug 'arkgast/nerdtree-execute', { 'branch': 'standard_linux_opener' }  \" Add execute menu to NerdTree"
        url = OpenPluginPage._extract_url(plugin_name)
        self.assertIsNotNone(url)
        self.assertGHUrl(url, 'arkgast/nerdtree-execute')

    def test_plugin_with_dot(self):
        plugin_name = "Plug 'junegunn/limelight.vim'  \" Focus blocks"
        url = OpenPluginPage._extract_url(plugin_name)
        self.assertIsNotNone(url)
        self.assertGHUrl(url, 'junegunn/limelight.vim')

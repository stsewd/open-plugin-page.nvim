import re
import webbrowser

import neovim


@neovim.plugin
class OpenPluginPage:

    def __init__(self, vim):
        self.vim = vim

    @neovim.command('OpenPluginPage')
    def command_handler(self):
        line = self.vim.current.line
        url = self._extract_url(line)
        if url:
            webbrowser.open_new_tab(url)
        else:
            return self.vim.err_write('[open-plugin-page] No match found\n')

    @staticmethod
    def _extract_url(line):
        plugin = OpenPluginPage._extract_plugin(line)
        if plugin:
            url = OpenPluginPage._get_url(plugin)
            return url
        else:
            return None

    @staticmethod
    def _extract_plugin(line):
        pattern = re.compile(
            r"^Plug\s'(?P<name>[-/a-zA-Z0-9._]+)'(\s*,\s*(?P<options>.*))?"
        )
        match = pattern.match(line)
        return match.group('name')

    @staticmethod
    def _get_url(plugin_name):
        user, *repo = plugin_name.split('/')
        if not repo:
            user, repo = 'vim-scripts', user
        else:
            repo = repo[0]
        return "https://github.com/{user}/{repo}".format(
            user=user,
            repo=repo
        )

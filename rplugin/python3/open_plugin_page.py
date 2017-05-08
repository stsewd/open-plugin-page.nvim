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
        pattern = re.compile(
                r"^Plug\s'(?P<name>[-/a-zA-Z0-9._]+)'(\s*,\s*(?P<options>.*))?"
            )
        match = pattern.match(line)
        if match:
            url = OpenPluginPage._get_url(match.group('name'))
            return url
        else:
            return None

    @staticmethod
    def _get_url(plugin_name):
        user, *repo = plugin_name.split('/')
        if not repo:
            repo = 'vim-scripts'
        else:
            repo = repo[0]
        return "http://github.com/{user}/{repo}".format(
                    user=user,
                    repo=repo
                )

# Open Plugin Page

Open the github repository of a neovim plugin

Note: For now only plugins managed by vim-plug are supported.

## Install

Install using [vim-plug](https://github.com/junegunn/vim-plug). Put
this on your `ìnit.vim`.

```
Plug 'stsewd/open-plugin-page.nvim', { 'for': 'vim', 'do': ':UpdateRemotePlugins' }
```

## Requirements

This plugin require Neovim with python3. If `:echo has("python3")` returns `1`,
then you're done; otherwise, you can enable the python3 interface with:

```
pip3 install --upgrade neovim
```

## Usage

Put the cursor over a plugin line

```vim
call plug#begin('~/.local/share/nvim/plugged')

Plug 'scrool[o]ose/nerdtree'

call plug#end()
```

Execute `:OpenPluginPage` and the plugin page will open in a new tab of your
web browser! 


## Configuration Example

```vim
" Use `gp` for open the github page of the current plugin under the cursor.
nnoremap <silent> gp :OpenPluginPage<CR>

```

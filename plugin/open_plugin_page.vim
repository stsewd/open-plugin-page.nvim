if exists('g:loaded_open_plugin_page')
  finish
endif

autocmd! BufNewFile,BufRead *init.vim 
       \ nnoremap <buffer> <Plug>(OpenPluginPage) :OpenPluginPage<CR>

let g:loaded_open_plugin_page = 1

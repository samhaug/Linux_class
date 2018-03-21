set nocompatible              " be iMproved, required
filetype off                  " required

"enable syntax highlighting
syntax enable


" show line numbers
set number
set number relativenumber

" set tabs to have 4 spaces
set ts=4

" indent when moving to the next line while writing code
set autoindent

" expand tabs into spaces
set expandtab

" when using the >> or << commands, shift lines by 4 spaces
set shiftwidth=4

" show a visual line under the cursor's current line
set cursorline
set cursorcolumn

" show the matching part of the pair for [] {} and ()
set showmatch

" enable all Python syntax highlighting features
let python_highlight_all = 1

" set position of vertical column
set colorcolumn=80

" options for vim folding that work well for python indents
set foldenable
set foldlevelstart=0
set foldnestmax=1 
nnoremap <space> za
vnoremap <space> zf
set foldmethod=indent

" contents of minimal .vimrc 
"execute pathogen#infect()
"syntax on
filetype plugin indent on

" nerdtree toggle
nnoremap <silent> <C-W> :NERDTreeToggle<CR>
"nnoremap <C-W> :NERDTreeToggle<CR>

set laststatus=2


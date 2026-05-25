# Build with LuaLaTeX (fontspec + unicode-math); biber for biblatex.
$pdf_mode  = 4;   # 4 = lualatex
$lualatex  = 'lualatex -interaction=nonstopmode -halt-on-error -synctex=1 %O %S';
$bibtex_use = 2;  # run biber as needed, clean its output on -c
$clean_ext = 'bbl run.xml synctex.gz';
@default_files = ('main.tex');

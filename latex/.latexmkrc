#!/usr/bin/env perl

use v5.10;
use experimental qw(smartmatch);

# tex options
$lualatex     = 'lualatex -shell-escape -synctex=1 -interaction=nonstopmode';
$pdflualatex  = $lualatex;
$biber        = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B';
$bibtex       = 'bibtex %O %B';
$makeindex    = 'mendex %O -o %D %S';
$max_repeat   = 5;
$pdf_mode     = 4;

$pvc_view_file_via_temporary = 0;

#!/usr/bin/python3

from shutil import rmtree
from os import mkdir
from os.path import exists, join
from paperscraper.load_dumps import QUERY_FN_DICT
from paperscraper.pdf import save_pdf_from_dump

if exists('papers'): rmtree('papers')
mkdir('papers')
query = ['CNT dispersant', 'carbon nanotube dispersion']
for key in QUERY_FN_DICT.keys():
  QUERY_FN_DICT[key](query, output_filepath = '%s_result.jsonl' % key)
  if not exists(join('papers', key)): mkdir(join('papers', key))
  save_pdf_from_dump('%s_result.jsonl' % key, pdf_path = join('papers', key), key_to_save = 'doi')


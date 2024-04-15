#!/usr/bin/python3

from paperscraper.load_dumps import QUERY_FN_DICT
from paperscraper.pdf import save_pdf_from_dump

query = ['CNT dispersant', 'carbon nanotube dispersion']
for key in QUERY_FN_DICT.keys():
  QUERY_FN_DICT[key](query, output_filepath = '%s_result.jsonl' % key)
  save_pdf_from_dump('%s_result.json' % key, pdf_path = key, key_to_save = 'doi')


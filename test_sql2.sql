select
  a.id_document,
  array_agg(c.id_label_en)::int[] as labels,
  array_agg(d.id_author)::int[] as authors,
  array_agg(e.id_pdf)::int[] as pdfs
from
  www.document a inner join
  www.document_label_en b on
  a.id_document=b.id_document inner join
  www.label_en c on
  b.id_label_en=c.id_label_en inner join
  www.author d on
  a.id_document=d.id_document inner join
  www.pdf e on
  a.id_document=e.id_document
group by a.id_document;

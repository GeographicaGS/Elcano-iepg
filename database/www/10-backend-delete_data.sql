/*

  Delete all data from www schema.

*/

\echo www.author
delete from www.author;
alter sequence www.author_id_author_seq restart with 1;

\echo
\echo www.document_label_en
delete from www.document_label_en;

\echo
\echo www.document_label_es
delete from www.document_label_es;

\echo
\echo www.pdf
delete from www.pdf;
alter sequence www.pdf_id_pdf_seq restart with 1;

\echo
\echo www.document
delete from www.document;
alter sequence www.document_id_document_seq restart with 1;

\echo
\echo www.highlight
delete from www.highlight;
alter sequence www.highlight_id_highlight_seq restart with 1;

\echo
\echo www.label_en
delete from www.label_en;
alter sequence www.label_en_id_label_en_seq restart with 1;

\echo
\echo www.label_es
delete from www.label_es;
alter sequence www.label_es_id_label_es_seq restart with 1;

\echo
\echo www.translation
delete from www.translation;

\echo
\echo www.wwwuser
delete from www.wwwuser;
alter sequence www.wwwuser_id_wwwuser_seq restart with 1;

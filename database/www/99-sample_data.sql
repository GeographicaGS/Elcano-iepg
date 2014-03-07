-- Sample data

insert into www.wwwuser(
  name,
  surname,
  password,
  email,
  admin,
  username,
  language,
  status)
values(
  'Alberto',
  'Asuero Arroyo',
  'eac9e8dd8575f4c7831f1f6a72607126',
  'alberto.asuero@geographica.gs',
  true,
  'alasarr',
  'es',
  1);

insert into www.label_en(label)
values('Economy');

insert into www.label_en(label)
values('Energy');

insert into www.label_en(label)
values('Military');

insert into www.label_en(label)
values('Fake Label EN 1');

insert into www.label_en(label)
values('Fake Label EN 2');

insert into www.label_en(label)
values('Fake Label EN 3');

insert into www.label_es(label)
values('Economía');

insert into www.label_es(label)
values('Energía');

insert into www.label_es(label)
values('Militar');

insert into www.label_es(label)
values('Fake Label ES 1');

insert into www.label_es(label)
values('Fake Label ES 2');

insert into www.label_es(label)
values('Fake Label ES 3');

insert into www.document(
  title_en,
  title_es,
  theme_en,
  theme_es,
  description_en,
  description_es,
  link_en,
  link_es,
  last_edit_id_user,
  last_edit_time,
  published)
values(
  'Title_en',
  'title_es',
  'theme_en',
  'theme_es',
  'description_en',
  'description_es',
  'link_en',
  'link_es',
  1,
  now(),
  true);

insert into www.document_label_en
values(1,1);

insert into www.document_label_en
values(1,2);

insert into www.document_label_es
values(1,1);

insert into www.document_label_es
values(1,2);

insert into www.pdf(id_document, lang, pdf_name)
values(1, 'EN', 'PDF EN 1');

insert into www.pdf(id_document, lang, pdf_name)
values(1, 'EN', 'PDF EN 2');

insert into www.pdf(id_document, lang, pdf_name)
values(1, 'ES', 'PDF ES 1');

insert into www.pdf(id_document, lang, pdf_name)
values(1, 'ES', 'PDF ES 1');

copy www.author from stdin with delimiter ',' null '@@null@@';
1,1,Iliana Olivié,Researcher,Investigadora,@iliana
2,1,@@null@@,IT Coordinator,Coordinadora IT,@ivanosca
\.

alter sequence www.author_id_author_seq restart with 3;

copy www.news_section from stdin with delimiter ',';
1,Blog,Blog
2,Media,En los medios
3,Events,Actividades
\.

alter sequence www.news_section_id_news_section_seq restart with 4;

insert into www.new(
  id_wwwuser,
  new_time,
  title_en,
  title_es,
  text_en,
  text_es,
  url_en,
  url_es,
  id_news_section)
values(
  1,
  now(),
  'Sample new',
  'Noticia de ejemplo',
  'Sample new text',
  'Texto de la noticia de ejemplo',
  'http://www.geographica.gs',
  'http://www.geographica.gs',
  1);

copy www.new_label_en from stdin with delimiter ',';
1,1
1,2
\.

copy www.new_label_es from stdin with delimiter ',';
1,1
1,2
\.

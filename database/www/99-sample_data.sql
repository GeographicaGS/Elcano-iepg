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

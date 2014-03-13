-- Sample data

-- Original administrator
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

-- News section
copy www.news_section from stdin with delimiter ',';
1,Blog,Blog
2,Media,En los medios
3,Events,Actividades
\.

alter sequence www.news_section_id_news_section_seq restart with 4;

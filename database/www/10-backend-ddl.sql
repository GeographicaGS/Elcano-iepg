/*

  Elcano backend schema.

*/

\i 00-config.sql

\c :dbname :user

create schema www authorization :user;

create table www.translation(
  key text,
  en text,
  es text
);

alter table www.translation
add constraint translation_pkey
primary key(key);


create table www.wwwuser(
  id_wwwuser serial,
  name varchar(128),
  surname varchar(255),
  password varchar(64),
  email varchar(255),
  admin boolean,
  username varchar(255),
  language varchar(2),
  status integer
);

alter table www.wwwuser
add constraint wwwuser_pkey
primary key(id_wwwuser);

alter table www.wwwuser
add constraint wwwuser_unique_email
unique(email);


create table www.highlight(
  id_highlight serial,
  title_en varchar(50),
  title_es varchar(50),  
  text_en varchar(500),
  text_es varchar(500),
  image_en varchar(500),
  image_es varchar(500),
  credit_img_en varchar(100),
  credit_img_es varchar(100),
  link_en varchar(500),
  link_es varchar(500),
  last_edit_user integer,
  last_edit_time timestamp,
  published boolean,
  publication_order integer
);

alter table www.highlight 
add constraint highlight_pkey
primary key(id_highlight);


create table www.author(
  id_author serial,
  id_document integer,
  name varchar(100),
  position_en varchar(250),
  position_es varchar(250),
  twitter_user varchar(50)
);

alter table www.author
add constraint author_pkey
primary key(id_author);


create table www.document(
  id_document serial,
  title_en varchar(150),
  title_es varchar(150),
  theme_en text,
  theme_es text,
  description_en text,
  description_es text,
  pdf_file_en varchar(500),
  pdf_file_es varchar(500),
  link_en varchar(500),
  link_es varchar(500),
  last_edit_id_user integer,
  last_edit_time timestamp,
  published boolean
);

alter table www.document
add constraint document_pkey
primary key(id_document);


create table www.label_en(
  id_label_en serial,
  label varchar(100)
);

alter table www.label_en
add constraint label_en_pkey
primary key(id_label_en);

alter table www.label_en
add constraint label_en_label_unique
unique(label);


create table www.label_es(
  id_label_es serial,
  label varchar(100)
);

alter table www.label_es
add constraint label_es_pkey
primary key(id_label_es);

alter table www.label_es
add constraint label_es_label_unique
unique(label);


create table www.document_label_en(
  id_document integer,
  id_label_en integer
);

alter table www.document_label_en
add constraint document_label_en_pkey
primary key (id_document, id_label_en);


create table www.document_label_es(
  id_document integer,
  id_label_es integer
);

alter table www.document_label_es
add constraint document_label_es_pkey
primary key (id_document, id_label_es);


-- Foreign keys

alter table www.document
add constraint document_user_fkey
foreign key (last_edit_id_user)
references www.wwwuser(id_wwwuser);

alter table www.highlight
add constraint highlight_wwwuser_fkey
foreign key (last_edit_user)
references www.wwwuser(id_wwwuser);

alter table www.document_label_en
add constraint document_label_en_document_fkey
foreign key (id_document)
references www.document(id_document);

alter table www.document_label_en
add constraint document_label_en_label_en_fkey
foreign key (id_label_en)
references www.label_en(id_label_en);

alter table www.document_label_es
add constraint document_label_es_document_fkey
foreign key (id_document)
references www.document(id_document);

alter table www.document_label_es
add constraint document_label_es_label_en_fkey
foreign key (id_label_es)
references www.label_es(id_label_es);

alter table www.author
add constraint author_document_fkey
foreign key (id_document)
references www.document(id_document);

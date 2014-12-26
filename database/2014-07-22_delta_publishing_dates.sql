alter table www.document add column publishing_date date;
alter table www.new add column publishing_date date;

update www.document set publishing_date=last_edit_time;
update www.new set publishing_date=new_time;

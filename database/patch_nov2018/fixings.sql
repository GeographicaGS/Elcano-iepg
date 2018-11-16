

BEGIN;

  UPDATE iepg_data_redux.master_country
    SET full_name_es_order = 'Uruguay',
        full_name_es = 'Uruguay',
        short_name_es_order = 'Uruguay',
        short_name_es1 = 'Uruguay',
        short_name_es2 = 'Uruguay'
  WHERE id_master_country = 'un858';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Spain maintains its 12th position in the Elcano Global Presence Index, although it has lost some measure of global presence in all of its dimensions (as have the other countries of the region). Spain’s strength continues to be the soft dimension (11th), as well as the economic (also 12th place). However, in the military sphere (17th), Spain’s international role is more passive.</p><p>Spain has recorded a noticeable increase in its global presence since 1990, supported by a steady growth both in its economic and mainly in its soft presence, within which tourism stands out, being the second country in the world with the greatest number of tourist per year.</p><p>Regarding to the economic dimension, after a strong growth in the 2000s, it had been registering a continuous decline since 2012, mainly due to the reduction of investments abroad and the decline in the growth of export of services, which have recovered in the last year pushed by the tourism sector.</p><p>If we look at its European projection, the importance of the soft dimension is strengthened, with a leading role in migration, tourism or scientific publications. Therefore, the loss of soft presence in the EU last year, along with the low growth of economic presence in recent years, makes it descend to the 7th position behind Italy.</p>'
   WHERE code='ES' AND language='en';

COMMIT;

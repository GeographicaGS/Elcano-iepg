\i 00-config.sql
\c :dbname :user :host :port

-- Sample data

-- Label EN
copy www.label_en from stdin with delimiter ',';
1,Economy
2,Energy
3,Politics
4,USA
5,BRICS
6,European Union
7,China
8,Russia
9,Japan
10,India
11,Spain
12,Crisis
\.

alter sequence www.label_en_id_label_en_seq restart with 13;


-- Label ES
copy www.label_es from stdin with delimiter ',';
1,Economía
2,Energía
3,Política
4,EEUU
5,BRICS
6,Unión Europea
7,China
8,Rusia
9,Japón
10,India
11,España
12,Crisis
\.

alter sequence www.label_es_id_label_es_seq restart with 13;


-- Documents
copy www.document from stdin with delimiter '^' null '@@@@';
1^English Title Doc 1^Freno al decrecimiento de la economía española^English Theme Doc 1^Este estudio analiza las fortalezas y debilidades de la economía española durante el último trimestre de 2013. En él se hace hincapié en varios factores de su evolución, que se puede considerar elativamente positiva: la mejoría de la demanda interna y del sector exterior, los cambios en la estructura del sistema financiero y la caída de la prima de riesgo. Los datos macroeconómicos provienen de instituciones y organismos económicos nacionales e internacionales, y también se tienen en cuenta las opiniones de analistas de referencia sobre la marcha de la economía. Desgraciadamente, también se encuentran desequilibrios pendientes de resolver e incertidumbres respecto a la influencia de posibles escenarios negativos en el exterior.^English Description Doc 1^La prima de riesgo y el sector financiero de España han sido varios de los elementos que, durante el último trimestre de 2013, han condicionado la economía española, debido a la gran importancia que tienen, a día de hoy, en la sostenibilidad de la financiación del Estado y en la mejora de la capacidad crediticia y de ahorro de empresas y familias. Pero es relevante analizar a las principales magnitudes que indican cuál es el estado actual de la economía española, así como qué evolución futura se puede esperar de la misma. Finalmente, se incide en la importancia de la buena marcha del sector exterior para la mejora de la economía de España y de su imagen internacional, que repercuten, a su vez, en factores como la liquidez disponible y el coste de la financiación de su deuda soberana en los mercados internacionales.^@@@@^http://www.realinstitutoelcano.org/^1^2014-02-23^false
2^Inside Spain^Spanish Title Doc 2^'A lively look at current affairs by a seasoned observer of Spanish political and economic life'.^Spanish Theme Doc 2^Section specially commissioned for our monthly bilingual Boletín/Newsletter written by William Chislett, former correspondent of The Times in Spain (1975-78) and the Financial Times in Mexico (1978-84), who has lived in Madrid since 1986. Chislett writes regularly for the Elcano Royal Institute, which has published his books The Internationalization of the Spanish Economy, Spanish Direct Investment in Latin America: Challenges and Opportunities, and Spain and the United States. The Quest for Mutual Rediscovery. (Note: publication of Inside Spain resumed in April 2012 after a break of four months).^Spanish description Doc 2^http://www.realinstitutoelcano.org/^@@@@^1^2014-01-10^false
3^Executive Summary and Conclusions of the Elcano Report "Towards the strategic renewal of Spain''s foreign policy^Spanish Title Doc 3^This report aims to provide a structured overview of the issues that need to be addressed in order to overhaul Spain’s foreign policy strategy. It is directed at all those who play leading roles in the defence and projection abroad of Spain’s values and interests. Its novelty lies in Spain’s lack of a tradition in drawing up papers such as this, since the usual practice has been to focus on the short term and to disregard the need for both public doctrine and planning. Nevertheless, it comes at a time when a more strategic outlook has begun to emerge in other fields, while there is a growing awareness that Spanish foreign policy has lacked any clear strategic guidelines since the country’s successful and full insertion in Europe and the world. The absence of clear guidelines has been aggravated during the crisis as a result of the declining resources available for foreign policy and of the public’s disillusion with the role Spain might play in the globalisation process. Furthermore, the large-scale changes and uncertainties on the international and European scenes make an exercise of this nature even more advisable.^Spanish Theme Doc 3^The paper is not rigidly prescriptive but rather provides general guidelines and some specific suggestions based on the overriding premise that a country’s collective values and ideas must necessarily be reflected in its foreign policy and external action (two terms here considered to be virtually interchangeable when looked at from a strategic perspective). It starts by identifying Spain’s fundamental values and interests, which determine the international action necessary to achieve them. It then looks at the country’s position in the complex world context, identifying the priorities to be pursued and where and how to do so, including an analysis of the means available and a proposal on designing foreign policy.\nSpain is currently experiencing difficulties but its contemporary history also provides a decisive story of political, social and economic success. The country’s collective vision may in turn require renewal, but the essential components of the Spanish model remain as follows: (i) democratic coexistence; (ii) security; (iii) sustainable prosperity; and (iv) culture and knowledge. This widely shared consensus provides a basis on which to build a sound foreign policy.\nThe world is increasingly multipolar in economic terms and apolar politically, and its societies are more dynamic and well informed, but also more unequal and older. The difficulties in coping with globalisation should encourage all nations to cooperate but current trends do not suggest the emergence or consolidation of effective multilateral systems. In this context, Europe is a region with specific difficulties due to its weaknesses in terms of demography, energy resources and the economy, and its diplomatic and military fragmentation. The construction of a united Europe provides the best response to these challenges, but the EU is vulnerable: its currency has unstable foundations, its legitimacy is questioned, its common foreign and security policy is still fragile, and it faces an unstable world that is relatively hostile to its values. This should encourage its member states to foster an ambitious process of political integration, but current trends suggest that progress will be slow.\nSpain’s place in this scenario is also difficult. The prospects for its international presence are less favourable than in the last quarter of the 20th century, when it managed to fully normalise its foreign policy. However, it is also true that, in contrast to its isolation in 1976, Spain today is well integrated in the world. In any event, Spain faces both significant risks and valuable opportunities. Its weaknesses and threats relate to its economy, politics, demography, energy and the environment, security, the competitiveness of its production model and the quality of its education and scientific-technological systems. In the specific field of foreign policy, the country has been unable to make better use of its geopolitical potential and its soft power, exerting less influence than warranted by its objective international presence. But Spain also has strengths and opportunities on account of its high level of socioeconomic development, political-institutional stability, sound external projection in the business world, strong appeal and a global language. In addition, it has a highly valuable geographic-historical position, is well integrated in the EU and the Atlantic space, and has an extensive external network as well as armed forces and a development cooperation system with the potential to play a leading international role.\nBased on the premise that Spain’s external action should help it achieve the essential aims of its aspirations as a country, this Report has identified six strategic objectives, three of which relate to fulfilling Spain’s own domestic aspirations (democracy, security, and competitiveness and talent) while the other three are more connected to foreign policy (European integration, international responsibility and influence).^Spanish Description Doc 3^@@@@^@@@@^1^2013-12-20^false
4^Impacts, policies, and status of latinamerican countries towards COP17 (ARI)^Impactos, políticas y posiciones de los países latinoamericanos rumbo a COP17 (ARI)^This ARI studies the main consequences of climate change for several key countries in Latinamerica. Mitigation plans area also presented, as well as views taken as a result of international negotiations regarding climate change. Advances made in COP16 (Cancún Agreements) are shown as well as preliminary international negotiation agreements towards COP17, to be held in Durban, South Africa.^En este ARI se estudian las principales consecuencias del cambio climático para algunos países clave de Latinoamérica. Se presentan además las políticas de mitigación, adaptación y las posiciones asumidas en las negociaciones internacionales sobre cambio climático. Derivados de los resultados alcanzados en COP16 –los Acuerdos de Cancún– se presentan también los avances más reseñables en las negociaciones internacionales rumbo a COP17, que se celebrará en Durban, Sudáfrica.^(EN) América Latina no se presenta a las negociaciones sobre cambio climático como un bloque. Los impactos en la región son muy variados, lo cual no sorprende por la extensión de la región, pero generalizando son problemas relacionados con el agua: sequía, inundaciones y lluvias torrenciales. El cambio climático por tanto afecta más a aquellos países cuyos sectores económicos dependen o usan intensivamente el agua, como pudieran ser la ganadería, la agricultura y el turismo.\nLas propuestas que han avanzados algunos países carecen de coordinación y obedecen más a los intereses particulares de cada país. Así, por ejemplo, Brasil impulsa el uso de biocombustibles como una forma de mitigación dada la evolución que ha tenido su programa de etanol, que se desarrolló por causas ajenas a las preocupaciones sobre cambio climático. México por su parte, ha tomado la eficiencia energética como bandera en las negociaciones. Esta es una propuesta que parece viable dado que logra beneficios que de cualquier forma los países persiguen individualmente. Estos beneficios incluyen la seguridad energética y la eficiencia en los mercados, así como el ahorro de energía. También fue uno de los promotores del Fondo Verde aprobado en Cancún. Ecuador, por su parte hace una propuesta sui generis: el pago por emisiones evitadas que implica para ellos el pago por no desarrollar sus yacimientos de hidrocarburos. Esta propuesta sería bien vista por otras regiones, como los países petroleros de Oriente Medio que reclaman una compensación por potenciales pérdidas de ingresos derivados del petróleo debido a la potencial transición hacia otros combustibles.^América Latina no se presenta a las negociaciones sobre cambio climático como un bloque. Los impactos en la región son muy variados, lo cual no sorprende por la extensión de la región, pero generalizando son problemas relacionados con el agua: sequía, inundaciones y lluvias torrenciales. El cambio climático por tanto afecta más a aquellos países cuyos sectores económicos dependen o usan intensivamente el agua, como pudieran ser la ganadería, la agricultura y el turismo.\nLas propuestas que han avanzados algunos países carecen de coordinación y obedecen más a los intereses particulares de cada país. Así, por ejemplo, Brasil impulsa el uso de biocombustibles como una forma de mitigación dada la evolución que ha tenido su programa de etanol, que se desarrolló por causas ajenas a las preocupaciones sobre cambio climático. México por su parte, ha tomado la eficiencia energética como bandera en las negociaciones. Esta es una propuesta que parece viable dado que logra beneficios que de cualquier forma los países persiguen individualmente. Estos beneficios incluyen la seguridad energética y la eficiencia en los mercados, así como el ahorro de energía. También fue uno de los promotores del Fondo Verde aprobado en Cancún. Ecuador, por su parte hace una propuesta sui generis: el pago por emisiones evitadas que implica para ellos el pago por no desarrollar sus yacimientos de hidrocarburos. Esta propuesta sería bien vista por otras regiones, como los países petroleros de Oriente Medio que reclaman una compensación por potenciales pérdidas de ingresos derivados del petróleo debido a la potencial transición hacia otros combustibles.^http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/especial+cambio+climatico/publicaciones+rie/ari+y+dt/ari130-2011#.Ux8kL1RdWLc^http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/especial+cambio+climatico/publicaciones+rie/ari+y+dt/ari130-2011#.Ux8kL1RdWLc^1^2014-01-02^false
5^Towards a United States of Europe?^¿Hacia unos Estados Unidos de Europa?^(EN) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel elit ligula. Vestibulum pellentesque ligula turpis, in sagittis metus hendrerit quis. Phasellus vel elementum turpis. Praesent pharetra, sapien a iaculis commodo, felis enim ullamcorper quam, ac sollicitudin tortor elit quis arcu. Nullam tellus enim, elementum eu ultricies tristique, congue id risus. Aliquam a ante porttitor, tincidunt augue ac, egestas arcu. Phasellus dapibus mattis convallis. Nulla sed nunc sed neque pellentesque ullamcorper. Aenean eu elit vel nisi molestie aliquet in in nisl. Proin et urna mi. Pellentesque mauris diam, suscipit et lorem ut, sodales commodo massa. Curabitur accumsan scelerisque posuere. Ut laoreet a orci ac semper. Suspendisse rutrum non leo a condimentum.^(ES) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel elit ligula. Vestibulum pellentesque ligula turpis, in sagittis metus hendrerit quis. Phasellus vel elementum turpis. Praesent pharetra, sapien a iaculis commodo, felis enim ullamcorper quam, ac sollicitudin tortor elit quis arcu. Nullam tellus enim, elementum eu ultricies tristique, congue id risus. Aliquam a ante porttitor, tincidunt augue ac, egestas arcu. Phasellus dapibus mattis convallis. Nulla sed nunc sed neque pellentesque ullamcorper. Aenean eu elit vel nisi molestie aliquet in in nisl. Proin et urna mi. Pellentesque mauris diam, suscipit et lorem ut, sodales commodo massa. Curabitur accumsan scelerisque posuere. Ut laoreet a orci ac semper. Suspendisse rutrum non leo a condimentum.^(EN) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu malesuada eros. Sed mi mauris, iaculis id diam vestibulum, posuere sodales ipsum. Nullam hendrerit gravida gravida. Vestibulum cursus, purus et ullamcorper blandit, nisi dui tempor ipsum, a tempus tellus ipsum eu tellus. Cras quis aliquet elit, non blandit urna. Nullam augue tellus, faucibus in lorem nec, luctus fringilla urna. Vivamus in varius arcu, luctus rutrum risus. Mauris in quam a dolor laoreet eleifend eget eu ante. Nam sed scelerisque massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur porta libero ultricies nibh blandit aliquam. Pellentesque nisi lacus, accumsan vitae tincidunt et, vehicula eu mauris. Sed porttitor eros vitae mi cursus convallis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur eleifend sem ac velit adipiscing, sit amet ultricies nisl dignissim. Curabitur lacus eros, auctor ut gravida eu, porta at velit.\nMauris a ligula accumsan, accumsan metus sed, aliquet nunc. Proin laoreet purus est, sed placerat elit imperdiet sed. Ut eget cursus odio. Duis et tempor nisl. Integer lacinia in dolor aliquet scelerisque. Suspendisse dapibus nisi purus, vitae elementum ipsum dapibus sit amet. Nulla non commodo nulla. Donec egestas, nisl vel vulputate molestie, libero leo pretium nulla, sit amet posuere lorem est sit amet odio. Nullam vitae diam bibendum, aliquam risus sed, faucibus arcu. Donec ac nisi at lectus consectetur imperdiet ac aliquam lorem. Mauris aliquet, lacus porttitor dictum tristique, felis tellus aliquam urna, et dignissim lacus mi quis mi. Ut nulla augue, volutpat non pretium eu, scelerisque id ipsum.\nMorbi eu lacus in mauris convallis scelerisque eu vel ipsum. Vestibulum magna lacus, molestie egestas lectus eget, fringilla dapibus purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc pharetra pulvinar nulla sit amet convallis. Phasellus a quam lorem. Nam convallis neque et nunc viverra, a faucibus metus hendrerit. Maecenas ut nulla ac massa iaculis tempus ac in dui. Proin eget orci non leo mollis suscipit. Ut a erat aliquam, tincidunt leo non, tincidunt mauris. Morbi a erat lorem. Praesent nisi lacus, tristique quis ante ac, posuere lacinia lectus. Donec eget suscipit nulla. Donec sed imperdiet augue.\nNulla feugiat et lacus eu vehicula. Donec ut scelerisque diam, ac suscipit ipsum. Sed a nisi vitae lorem commodo vulputate. Donec vitae enim porttitor, consectetur orci vel, semper elit. Nunc pharetra pellentesque arcu ut ullamcorper. Proin posuere enim ornare dui convallis tincidunt. Pellentesque lobortis nunc sed augue sagittis, vel condimentum nulla lobortis. Proin feugiat gravida dui non interdum. Vestibulum adipiscing accumsan justo, in aliquam lacus molestie eu. Pellentesque ullamcorper leo mauris, eu rhoncus nunc blandit sed. Nullam quis malesuada lorem. Morbi a semper urna, a pellentesque nunc. Maecenas vitae mi quis sem luctus volutpat et vel dui. Nam auctor faucibus leo, vitae adipiscing magna adipiscing ut. Aenean in nibh egestas tellus suscipit faucibus vel non urna.\nDuis nec vehicula lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis aliquam dui nec gravida suscipit. Phasellus molestie pulvinar sem, sit amet convallis odio blandit ac. Nulla ut sodales lectus, eu consequat enim. Nulla ornare nibh velit. Maecenas fringilla nunc eget lorem condimentum malesuada. Quisque aliquam vitae tortor nec hendrerit. Mauris at congue eros, vitae vulputate neque. Vivamus ac nibh non justo sagittis rhoncus. Sed venenatis diam erat, sit amet bibendum leo malesuada vel. Quisque metus lectus, faucibus nec massa at, porttitor aliquet eros. Nam odio diam, tincidunt non velit vel, feugiat convallis ligula.\nFusce libero augue, eleifend id felis at, mollis pulvinar lacus. Duis tempor est imperdiet, venenatis neque nec, venenatis sapien. Aliquam neque augue, convallis vel eros et, gravida aliquam mauris. In tincidunt eros quis tincidunt tempor. Suspendisse non condimentum massa. Sed feugiat, ipsum a tristique lobortis, odio sem bibendum sem, vitae cursus tortor neque non lorem. Phasellus id rutrum sem.^(ES) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu malesuada eros. Sed mi mauris, iaculis id diam vestibulum, posuere sodales ipsum. Nullam hendrerit gravida gravida. Vestibulum cursus, purus et ullamcorper blandit, nisi dui tempor ipsum, a tempus tellus ipsum eu tellus. Cras quis aliquet elit, non blandit urna. Nullam augue tellus, faucibus in lorem nec, luctus fringilla urna. Vivamus in varius arcu, luctus rutrum risus. Mauris in quam a dolor laoreet eleifend eget eu ante. Nam sed scelerisque massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur porta libero ultricies nibh blandit aliquam. Pellentesque nisi lacus, accumsan vitae tincidunt et, vehicula eu mauris. Sed porttitor eros vitae mi cursus convallis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur eleifend sem ac velit adipiscing, sit amet ultricies nisl dignissim. Curabitur lacus eros, auctor ut gravida eu, porta at velit.\nMauris a ligula accumsan, accumsan metus sed, aliquet nunc. Proin laoreet purus est, sed placerat elit imperdiet sed. Ut eget cursus odio. Duis et tempor nisl. Integer lacinia in dolor aliquet scelerisque. Suspendisse dapibus nisi purus, vitae elementum ipsum dapibus sit amet. Nulla non commodo nulla. Donec egestas, nisl vel vulputate molestie, libero leo pretium nulla, sit amet posuere lorem est sit amet odio. Nullam vitae diam bibendum, aliquam risus sed, faucibus arcu. Donec ac nisi at lectus consectetur imperdiet ac aliquam lorem. Mauris aliquet, lacus porttitor dictum tristique, felis tellus aliquam urna, et dignissim lacus mi quis mi. Ut nulla augue, volutpat non pretium eu, scelerisque id ipsum.\nMorbi eu lacus in mauris convallis scelerisque eu vel ipsum. Vestibulum magna lacus, molestie egestas lectus eget, fringilla dapibus purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc pharetra pulvinar nulla sit amet convallis. Phasellus a quam lorem. Nam convallis neque et nunc viverra, a faucibus metus hendrerit. Maecenas ut nulla ac massa iaculis tempus ac in dui. Proin eget orci non leo mollis suscipit. Ut a erat aliquam, tincidunt leo non, tincidunt mauris. Morbi a erat lorem. Praesent nisi lacus, tristique quis ante ac, posuere lacinia lectus. Donec eget suscipit nulla. Donec sed imperdiet augue.\nNulla feugiat et lacus eu vehicula. Donec ut scelerisque diam, ac suscipit ipsum. Sed a nisi vitae lorem commodo vulputate. Donec vitae enim porttitor, consectetur orci vel, semper elit. Nunc pharetra pellentesque arcu ut ullamcorper. Proin posuere enim ornare dui convallis tincidunt. Pellentesque lobortis nunc sed augue sagittis, vel condimentum nulla lobortis. Proin feugiat gravida dui non interdum. Vestibulum adipiscing accumsan justo, in aliquam lacus molestie eu. Pellentesque ullamcorper leo mauris, eu rhoncus nunc blandit sed. Nullam quis malesuada lorem. Morbi a semper urna, a pellentesque nunc. Maecenas vitae mi quis sem luctus volutpat et vel dui. Nam auctor faucibus leo, vitae adipiscing magna adipiscing ut. Aenean in nibh egestas tellus suscipit faucibus vel non urna.\nDuis nec vehicula lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis aliquam dui nec gravida suscipit. Phasellus molestie pulvinar sem, sit amet convallis odio blandit ac. Nulla ut sodales lectus, eu consequat enim. Nulla ornare nibh velit. Maecenas fringilla nunc eget lorem condimentum malesuada. Quisque aliquam vitae tortor nec hendrerit. Mauris at congue eros, vitae vulputate neque. Vivamus ac nibh non justo sagittis rhoncus. Sed venenatis diam erat, sit amet bibendum leo malesuada vel. Quisque metus lectus, faucibus nec massa at, porttitor aliquet eros. Nam odio diam, tincidunt non velit vel, feugiat convallis ligula.\nFusce libero augue, eleifend id felis at, mollis pulvinar lacus. Duis tempor est imperdiet, venenatis neque nec, venenatis sapien. Aliquam neque augue, convallis vel eros et, gravida aliquam mauris. In tincidunt eros quis tincidunt tempor. Suspendisse non condimentum massa. Sed feugiat, ipsum a tristique lobortis, odio sem bibendum sem, vitae cursus tortor neque non lorem. Phasellus id rutrum sem.^http://www.realinstitutoelcano.org/^http://www.realinstitutoelcano.org/^1^2014-02-01^false
6^Title Doc 6 (English)^Título Doc 6 (Español)^Theme Doc 6 (English)^Tema Doc 6 (Español)^Description Doc 6 (English)^Descripción Doc 6 (Español)^http://www.realinstitutoelcano.org^@@@@^1^2014-01-23^false
7^Title Doc 7 (English)^Título Doc 7 (Español)^Theme Doc 7 (English)^Tema Doc 7 (Español)^Description Doc 7 (English)^Descripción Doc 7 (Español)^@@@@^http://www.realinstitutoelcano.org^1^2014-01-21^false
8^Title Doc 8 (English)^Título Doc 8 (Español)^Theme Doc 8 (English)^Tema Doc 8 (Español)^Description Doc 8 (English)^Descripción Doc 8 (Español)^http://www.realinstitutoelcano.org^http://www.realinstitutoelcano.org^1^2014-01-26^false
\.

alter sequence www.document_id_document_seq restart with 9;


-- Authors
copy www.author from stdin with delimiter ',' null '@@@@';
1,1,Yerena Fernández,Titular Researcher,Investigadora principal,@@@@
2,1,@@@@,@@@@,@@@@,@jesuspardo
3,2,@@@@,@@@@,@@@@,@wchislett
4,3,@@@@,@@@@,@@@@,@imolina
5,4,@@@@,@@@@,@@@@,@rfuentesbracamontes
6,5,Iliana Olivié,Researcher,Investigadora,@iolivie
7,6,Iliana Olivié,Researcher,Investigadora,@iolivie
8,7,Iliana Olivié,Researcher,Investigadora,@iolivie
9,8,Iliana Olivié,Researcher,Investigadora,@iolivie
\.

alter sequence www.author_id_author_seq restart with 10;


-- PDF
copy www.pdf from stdin with delimiter ',' null '@@@@';
1,1,es,Freno al decrecimiento de la economía española (OIE),63906f4ae90203e39719f5e319c95136
2,2,en,Inside Spain - Elcano Newsletter 102,71713e60a8787b5687127a461c9249a7
3,2,en,Inside Spain - Elcano Newsletter 103,9abba230299e4fec187614caa57bf88e
4,3,en,Molina-Towards strategic renewal Spain foreign policy,7f630f2dceccffbd779147d76a3aaa0d
5,4,es,Impactos_Politicas_Posiciones_latinoamerica_cop17,e940df999f1269800fe615c86c2bb3f2
\.

alter sequence www.pdf_id_pdf_seq restart with 6;


-- Document - Label EN
copy www.document_label_en from stdin with delimiter ',';
1,1
1,11
1,12
2,11
3,3
3,11
4,2
4,3
5,1
5,3
5,6
6,7
6,8
7,2
7,4
8,11
8,10
\.


-- Document - Label ES
copy www.document_label_es from stdin with delimiter ',';
1,1
1,11
1,12
2,11
3,3
3,11
4,2
4,3
5,1
5,3
5,6
6,7
6,8
7,2
7,4
8,11
8,10
\.


-- Highlights
copy www.highlight from stdin with delimiter ',' null '@@';
1,How would be an United States of Europe like? Some ideas based on the EGPI,¿Cómo serían unos Estados Unidos de Europa? Algunas ideas en base al IEPG,Third edition of Elcano Global Presence Index (EGPI) comes now with global presence of the EU,La tercera edición del Índice Elcano de Presencia Global (IEPG) recoge ahora la presencia global de la UE,European Giant Robot,Robot Gigante Europeo,49c2c8029fb8892664028829d9022bb3,ecf9018ff475415e375efdff3bd09009,Gundam Inc.,Gundam Inc.,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/zonas_es/cooperacion+y+desarrollo/ari25-2013-olivie-gracia-united-states-of-europe-estados-unidos-europa-iepg-2012#.Ux80j1RdWLc,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/zonas_es/cooperacion+y+desarrollo/ari25-2013-olivie-gracia-united-states-of-europe-estados-unidos-europa-iepg-2012#.Ux80j1RdWLc,1,2014-01-10,false,@@
2,34st Wave of the BRIE,34ª oleada del BRIE,34st wave of Elcano Observatory: Spaniard's own perception is worst than that outside Spain,34ª oleada del Barómetro Elcano: la percepción exterior de España es mejor que la que tienen los propios españoles,Giant robot,Giant robot,1ba4f8e5ca2d5759d4d99ac1369feba5,9899aec9843e93ef1d88b459fccd202a,Gundam Inc.,Gundam Inc.,http://www.realinstitutoelcano.org/wps/portal/rielcano/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/barometro/oleadabrie34,http://www.realinstitutoelcano.org/wps/portal/rielcano/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/barometro/oleadabrie34,1,2013-11-23,false,@@
3,China: bracing itself for financial turbulence,China: preparativos para turbulencias financieras,'You should cross the river by feeling the stones' (chinese proverb),'Deberías cruzar el río sintiendo las piedras' (proverbio chino),Giant robot,Giant robot,e1469eab4849922c1e17fbf5969dc622,fcf463425c67646d4d40e1cab1b9d520,Gundam Inc.,Gundam Inc.,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/commentary-otero-china-bracing-itself-for-financial-turbulence#.Ux88p1RdWLc,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/commentary-otero-china-bracing-itself-for-financial-turbulence#.Ux88p1RdWLc,1,2014-02-01,false,@@
4,US-EU trade: what is at stake?,Comercio EEUU-UE: ¿qué nos jugamos?,The trade negotiations between the EU and the US are motivated more by geopolitical than economic considerations,Las negociaciones comerciales entre la UE y los EEUU están más motivados geopolítica que económicamente,Giant robot,Giant robot,1b15ec667a74e1bd88d03cf5da77f121,97b6efcadee943f12287a46f92d5faa1,Gundam Inc.,Gundam Inc.,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/ari13-2014-steinberg-us-eu-trade-negotiations#.Ux8_pFRdWLc,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/ari13-2014-steinberg-us-eu-trade-negotiations#.Ux8_pFRdWLc,1,2014-02-03,false,@@
5,Spain's banking crisis: a light in the tunnel,Crisis bancaria española: luz al final del tunel,The Spanish banking system is on the mend,El sistema bancario español en vías de recuperación,Giant robot,Giant robot,97d80f10b5da177d3b8d8664da70b0cf,6906ac978b6e490295f88ff11be633f6,Gundam Inc.,Gundam Inc.,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/ari11-2014-chislett-spain-banking-crisis-light-in-the-tunnel#.Ux9AUlRdWLc,http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/ari11-2014-chislett-spain-banking-crisis-light-in-the-tunnel#.Ux9AUlRdWLc,1,2014-01-28,false,@@
\.

alter sequence www.highlight_id_highlight_seq restart with 6;


-- News
copy www.new from stdin with delimiter '|' null '@@';
1|1|2014-01-02|New EGPI edition|Nueva edición IEPG|Elcano Royal Institute publish a new edition of the Elcano Global Presence Index.|El Real Instituto Elcano publica la nueva edición del Índice de Presencia Global.|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/p rensa/ruedasprensa/presentacion_iepg-2ed|2
2|1|2013-11-05|EGPI coverage in El País|El País dedica un reportaje al IEPG|Spanish newspaper El País covers extensively the results and conclusions of the last Elcano Global Presence Index edition.|El País repasa en un extenso artículo los resultados y conclusiones de la última edición del Índice Elcano de Presencia Global.|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|2
3|1|2014-03-04|Elcano Global Presence Index Presentation Event|Evento de presentación del Índice de Presencia Global Elcano|The Elcano Royal Institute will held in its premises the presentation event of the Elcano Global Presence Index, 2014 edition.|El Real Instituto Elcano presentará en su sede el Índice Elcano de Presencia Global, edición de 2014.|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|3
4|1|2014-02-15|Towards an United States of Europe? A view from the perspective of the Elcano Global Presence Index|¿Hacia unos Estados Unidos de Europa? Una visión desde el Índice Elcano de Presencia Global|Elcano Global Presence Index' conclusions points in a direction of desmitifying common obstacles perceived in an eventual creation of a true European federation.|Las conclusiones del Índice Elcano de Presencia Global apuntan a que una eventual federación europea sea posible en contra de lo que muchos creen.|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|1
5|1|2014-02-18|Ukraine in the EU: impact upon the Elcano Global Presence Index|Ucrania como miembro de la Unión Europea: impacto sobre el Índice Elcano de Presencia Global|In this article the impact upon the Elcano Global Presence Index of Ukraine joining the EU as a full-fledge member is analyzed.|En este artículo analizamos el impacto que puede tener sobre el Índice Elcano de Presencia Global el eventual ingreso de Ucrania como miembro de pleno derecho de la UE.|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|1
6|1|2014-03-23|New interactive tool for exploring the Elcano Global Presence Index|Nueva herramienta interactiva para explorar el Índice Elcano de Presencia Global|The brand new Elcano Global Presence Index web site includes a powerful interactive tool to browse the Index results.|El nuevo sitio web del Índice Elcano de Presencia Global incluye una poderosa herramienta interactiva para explorar los resultados del Índice.|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|http://www.realinstitutoelcano.org/wps/portal/rielcano/PrensaVista?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/prensa/ruedasprensa/presentacion_iepg-2ed|1
\.

alter sequence www.new_id_new_seq restart with 7;

copy www.new_label_en from stdin with delimiter '|' null '@@';
1|1
1|3
2|11
4|1
4|6
5|6
\.

copy www.new_label_es from stdin with delimiter '|' null '@@';
1|1
1|3
2|11
4|1
4|6
5|6
\.
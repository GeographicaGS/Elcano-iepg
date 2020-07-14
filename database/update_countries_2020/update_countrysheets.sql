
/*
  Update country comments.
*/

BEGIN;
-- USA
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Estados Unidos ocupa el primer puesto del Índice Elcano de Presencia Global en todos los años para los que se calcula. En 2019, también ocupa esta primera posición en todas las variables, con las excepciones de energía, manufacturas y turismo. Presenta, de los 130 países, las mayores cuotas de presencia en todas las dimensiones –18,8% en la económica; 28,2% en la militar; y 22,5% en la blanda–. Por otro lado, a diferencia de lo que ocurre en otros países desarrollados, la dimensión militar define en buena medida su proyección exterior, con una contribución de 25,5% en 2019.</p><p>A pesar de esta hegemonía, Estados Unidos pierde presencia global relativa en comparación con el resto de países –24,8% de cuota de presencia global en 1990 frente a 21,5% en 2019–. En un periodo de surgimiento de nuevos actores globales, diversas economías emergentes (particularmente petroleras o asiáticas) cosechan ganancias de cuota que reducen el protagonismo estadounidense. </p>'
 WHERE code='US' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>US tops the Elcano Global Presence Index in all years. In 2019, it also leads the ranking in all variables, with the exception of energy, manufactures and tourism. Of all 130 countries, it records the highest share of presence in all dimensions: 18.8% in the economic domain, 28.2% in the military and 22.5% in soft presence. Moreover, unlike other developed countries, its military dimension strongly defines its index value, with a contribution at 25.5% in 2019.</p><p></p>'
 WHERE code='US' AND language='en';

-- European Union
UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Si considerásemos a la Unión Europea un único país, ocuparía en 2019 el primer puesto en la clasificación de Presencia Global, con un registro similar al de Estados Unidos. Obtendría el mayor valor de presencia económica –con relevancia de la inversión en el exterior y las exportaciones de servicios– y un registro similar de presencia blanda –turismo, deportes y cooperación al desarrollo–, siendo superado por Estados Unidos tan sólo en la clasificación de presencia militar.</p><p>La crisis económica, con especial impacto dentro del espacio comunitario, ha condicionado la presencia de la Unión Europea en el resto del mundo. Por un lado, dentro de la dimensión económica, registra una pérdida de presencia hasta 2013, fundamentalmente debida al descenso de exportaciones de bienes y de inversión en el exterior –en parte consecuencia la depreciación del euro frente a otras monedas–. Por otro lado, se da una ralentización del crecimiento de su presencia blanda, afectada entre otras cosas por la reducción los flujos de cooperación internacional, así como al número de inmigrantes recibidos.</p><p>No obstante, en los últimos años se produce una recuperación en la evolución de dichas variables. Tanto la Unión Europea como Estados Unidos mantienen unos elevados niveles de presencia global, que les sitúa por el momento a mucha distancia de China, que ocuparía el tercer lugar.</p>'
WHERE code='XBEU' AND language='es';

UPDATE iepg_data_redux.iepg_comment
SET comment='<p>If the European Union were to be considered a single country, it would occupy the first place in the Global Presence ranking in 2019, with a record similar to that of the United States. The European Union would have the greatest value of economic presence –with relevance of foreign investment and exports of services– and also a similar record of soft presence –tourism, sports or development cooperation–, being surpassed by the United States only in the classification of military presence.</p><p>The economic crisis, which has especially hit the European Union, has had an impact on its presence in the rest of the world. On the one hand, within the economic dimension, there is a loss of presence until 2013, mainly due to the decline in exports of goods and foreign investment –in part due to the depreciation of the euro against other currencies–.
</p><p>On the other hand, there is a slowdown in the growth of its soft presence, affected among other things by the reduction of international cooperation flows, as well as the number of immigrants received.</p><p>However, in recent years there has been a recovery in the evolution of these variables. Both the European Union and the United States maintain high levels of global presence, which locates them still far from China, which would occupy the 3rd place.</p>'
WHERE code='XBEU' AND language='en';


-- China
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>El notable ascenso del gigante asiático en las últimas décadas tiene su reflejo en la clasificación del Índice Elcano de Presencia Global, donde escala diez posiciones desde 1990. Este crecimiento se debe en buena medida a la dimensión económica, donde se impulsa del 17º lugar en 1990 al 2º en 2019. A su vez, esto tiene su origen en el crecimiento de sus exportaciones manufactureras, pero también de bienes primarios, servicios e inversiones. Por ello, la naturaleza de su presencia global es principalmente económica, con un peso del 63,4% sobre el valor índice en 2019.</p>
 <p>Sin embargo, en los últimos años se producen aumentos sustanciales de presencia blanda, con un valor en 2019 que es 25 veces mayor que en 1990. Esto se explica con el comportamiento de indicadores como información, tecnología o ciencia, e incluso turismo o deportes.</p>
 <p>Con todo ello, su cuota de presencia pasa de 1,7% en 1990 a 8,0% en 2019, lejos de la de Estados Unidos pero ya superior a las de Francia, Reino Unido y Alemania.</p>'
 WHERE code='CN' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>China’s remarkable rise in recent decades is reflected in its classification in the Elcano Global Presence Index, where it has upscaled ten positions since 1990. This is mainly due to its economic presence, where it is now ranked 2nd (17th in 1990). This trend is driven by the export of manufactures, but also by primary goods, services and investments. Hence, the nature of its global presence is mainly economic, accounting for 63.4% of its index value in 2019.</p>
 <p>However, more recently China has also substantially increased its soft presence, with a record 25 times higher than in 1990; pushed by the increase in indicators such as information, technology or science, and even tourism or sports.</p>
 <p>As a result, its presence quota has gone up from 1.7% in 1990 to 8.0% in 2019. Although still far from the USA, China has overtaken France, the United Kingdom and Germany.</p>'
 WHERE code='CN' AND language='en';


-- Germany
UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Apoyada fundamentalmente en su proyección económica (69,1% de su presencia global), Alemania ha aumentado de forma continuada su presencia exterior desde mediados de los 90, tras su reunificación y la caída del bloque soviético. Se encuentra entre las cinco primeras posiciones en todas las variables económicas, con la única excepción de la de energía. Ocupa la 3ª posición en el ranking de presencia global, tras Estados Unidos y China, y por delante de Reino Unido.</p>
<p>Alemania ocupa el primer puesto en la clasificación del Índice Elcano de Presencia Europea lo que significa que es, de todos los estados miembros, el que tiene mayor proyección dentro de la UE. Es el resultado de ocupar el 1er puesto en manufacturas y tecnología y el 2º en bienes primarios, inversiones, migraciones, cultura, información, ciencia o educación. En definitiva, a diferencia de lo que ocurre en el conjunto de su proyección exterior, la presencia de Alemania en la Unión es, sobre todo, blanda (58,7% de su presencia europea).</p>'
WHERE code='DE' AND language='es';

UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Since the mid-1990s and following its reunification and the fall of the Soviet Union, Germany has recorded a steady growth in its external presence, on the basis of its economic dimension -that provides 69.1% of its global presence-. It is ranked among the five top positions in all economic variables; except energy. It is 3rd in the global presence ranking, after the US and China and before the United Kingdom. </p>
<p>Germany is ranked 1st in the Elcano European Presence Index, which means that, among all member states, it is the one with the highest projection within the EU. This is the result of being 1st in manufactures and technology and 2nd in primary goods, investments, migrations, culture, information, science or education. That is, unlike what happens with its total external projection, Germany’s presence in the Union is, mostly, soft (58.7% of its European presence).</p>'
WHERE code='DE' AND language='en';

-- UK
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Reino Unido se sitúa en la 4ª posición en el ranking de presencia global. Aunque ocupa posiciones elevadas en las tres dimensiones, es en la blanda, en la que es 3º, donde más destaca; y lo hace por su desempeño en deportes, educación, cultura o cooperación al desarrollo.</p>
 <p>El Reino Unido tiene mucha proyección, además, en algunos indicadores de presencia económica, particularmente en las exportaciones de servicios y en la inversión, dada la importancia de su economía de servicios a empresas, así como su función de hub financiero.</p>
 <p>En el Índice Elcano de Presencia Europea, Reino Unido se clasifica 2º, tras Alemania y por delante de Países Bajos. Es el estado miembro con mayor contribución de presencia blanda (cerca de 80%), lo que significa que su perfil económico se proyecta sobre todo fuera de la Unión. De hecho, es 3º en la variable de servicios y 4º en la de inversiones, pero encabeza el ranking europeo en deportes, cultura, información, ciencia y educación y se sitúa 2º en migraciones.</p>'
 WHERE code='GB' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>The United Kingdom occupies the 4th position in the global presence ranking. Although it outstands in all dimensions, it is particularly strong in the soft domain, where it is ranked 3rd. This is due to its performance in sports, education, culture or development cooperation.</p>
 <p>It also records a strong economic projection, particularly in services and investments, given the importance of its economic activity in business services and its condition of financial hub.</p>
 <p>The United Kingdom is 2nd in the Elcano European Presence Index, after Germany and before the Netherlands. It is the member state with the highest contribution of soft presence (nearly 80%), which means that its economic profile is mainly projected outside the Union’s borders. In fact, although being ranked 3rd in services and 4th in investments, it tops the European ranking in sports, culture, information, science and education, and is 2nd in migrations.</p>'
 WHERE code='GB' AND language='en';

 -- Japan
 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Japón ocupa el 5º lugar en la clasificación de presencia global. A pesar de mantenerse como la 3ª economía mundial, las consecuencias de la crisis de los noventa aún se reflejan en su presencia económica, en la que pasa de ocupar el 3er puesto en 1990, al 5º en 2019. Así, se recupera desde la 7ª posición en 2010 gracias, en buena medida, a las inversiones (que superan las de Francia o Alemania).</p>
  <p>También aumenta la dimensión militar que, a pesar de la desmilitarización tras la Segunda Guerra Mundial, contribuye crecientemente a la presencia japonesa –17,6% en 2019–; más que en otras economías desarrolladas.</p>
  <p>Aumenta su presencia blanda tanto en términos absolutos como relativos, aunque no lo suficiente para mantener la 3ª posición que ocupaba en 1990, situándose hoy en la 5ª, con cerca de 512 puntos. En este ámbito, sus principales fortalezas están en la tecnología, la ciencia y la cooperación al desarrollo.</p>'
  WHERE code='JP' AND language='es';

 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Japan is 5th in the global presence ranking. Despite being the 3rd world economy, the consequences of the nineties’ crisis still show in its economic presence records, where it has lost two positions since 1990. However, it is now ranked 5th, up from the 7th position in 2010; something which is mainly due to its performance in investments, where it has surpassed both Germany and France.</p>
  <p>The military dimension also grows –up to a contribution of 17.6% in 2019– and is higher than in other developed countries, despite the demilitarization following the World War II.</p>
  <p>The soft dimension increases both in absolute and relative terms, although not enough to maintain the 3rd position that it occupied in 1990. Japan is now ranked 5th, with almost 512 index value points. In this field, its main strengths are in technology, science and development cooperation.</p>'
  WHERE code='JP' AND language='en';

-- Rusia
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>La presencia global de la Unión Soviética cae fuertemente con la desintegración del bloque, al finalizar la Guerra Fría, y el desplome de su presencia militar, que en aquel momento era del 88,7% de su presencia total. Pese a ello, Rusia no pierde en ningún momento el 2º puesto en el ranking de presencia militar.</p>
 <p>La recuperación de su presencia global se sustenta en su dimensión económica y, concretamente, en la variable de energía; siendo el primer exportador mundial de gas y el segundo de petróleo. La dimensión blanda no es tan relevante, aunque el país destaque en deportes (debido a su éxito en el medallero olímpico), información o migraciones.</p>
 <p>Con todo ello, Rusia se sitúa hoy en la 7ª posición por presencia global, frente a la 2ª en 1990.</p>'
 WHERE code='RU' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>The Soviet Union’s external projection dramatically fell with the disintegration of the bloc, at the end of the Cold War, and the subsequent drop of its military presence; that accounted for 88.7% of its total presence in 1990. In spite of this, Russia never loses the 2nd position in the military presence ranking.</p>
 <p>The recovery of its global presence is grounded in its economic dimension and, more specifically, the energy variable; being Russia the world top exporter of gas and the second exporter of oil. The soft dimension is not particularly relevant. Although, the country outstands in sports (due to its performance in the Olympic Games), information or migrations.</p>
 <p>All in all, Russia is now 7th in global presence, down from the 2nd position in 1990. </p>'
 WHERE code='RU' AND language='en';

-- France
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Francia se enfrenta a una pérdida relativa de relevancia en la escena internacional. Tercero en 1995, se sitúa hoy en el 6º puesto del ranking del Índice Elcano de Presencia Global. Mantiene un perfil similar al de otras economías europeas, con una fuerte presencia blanda sobre todo en turismo, –siendo la primera potencia turística a nivel mundial–, cultura o cooperación al desarrollo.</p>
 <p>Es el 4º país en presencia en el espacio europeo, medida con el Índice Elcano de Presencia Europea, tras haber perdido en 2014 el 3er puesto que ahora ocupa Países Bajos. Como la mayoría de los estados miembros, su perfil en la UE es más blando (con una contribución de 59,6%) que económico (40,4%). Ocupa el 2º puesto del ranking europeo en servicios, deporte y tecnología, y el 3º en inversiones, migraciones, turismo y ciencia.</p>'
 WHERE code='FR' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>France faces a relative loss of relevance in the international scene. Third in 1995, it is now ranked 6th in the ranking of the Elcano Global Presence Index. Its profile is similar to that of other European countries, with a strong soft presence, particularly in tourism -being the first world tourism destination-, culture or development cooperation.</p>
 <p>It is 4th in the European sphere, when measured with the Elcano European Presence Index, after losing the 3rd position in 2014, which is now held by the Netherlands. As most member states, its profile within the EU is soft (with a contribution of 59.6%), rather than economic (40.4%). It is 2nd in the European ranking in services, sports and technology, and 3rd in investments, migrations, tourism and science.</p>'
 WHERE code='FR' AND language='en';

 -- Italy
 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Italia se mantiene, desde 2014, en el 10º puesto del ranking –frente al 7º puesto ocupado en 1990–. Esta tendencia se debe a la ralentización del crecimiento de su presencia económica, que tiene un escaso crecimiento desde los 90 en comparación con otros países del entorno. No obstante, continúa siendo uno de los países más industrializados, por lo que tiene relevancia dentro de las exportaciones de manufacturas e inversiones en el exterior. Al igual que ocurre con otras potencias europeas, mantiene registros elevados en la dimensión blanda –apoyada en cultura, tecnología, ciencia y turismo–.</p>
  <p>Por el contrario, dentro del espacio europeo su presencia es fundamentalmente blanda –estando entre los cinco primeros puestos en turismo, migraciones, deportes, información, tecnología y ciencia, y entre los diez primeros en cultura y educación– y ha sido precisamente esta dimensión la que mayores crecimientos había venido registrando.</p>'
  WHERE code='IT' AND language='es';

 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Italy holds the 10th place in the Elcano Global Presence Index ranking since 2014 –7th position in 1990–. This trend is due to the slower growth of its economic presence, which has registered a low increase compared to other neighboring countries. However, Italy is still one of the most industrialized countries, so its presence is fundamentally economic, supported by manufactured exports and investments. Similarly to other European countries Italy has a high score in the soft dimension –mainly because of culture, technology, science and tourism–.</p>
  <p>Within the European Union, Italy’s presence is of a soft nature. This dimension has registered the greatest growth –climbing positions up to being one of the top five European countries in tourism, migration, information, sports, technology and science and one of the top 10 ranks in education and culture–.</p>'
  WHERE code='IT' AND language='en';

  -- Canada
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Canadá ocupa en 2019 el 8º puesto del ranking de presencia global, a pesar del auge de China y de la reducción relativa de su peso económico en el mundo –pierde cuatro puestos en la clasificación mundial de PIB desde 1990–.</p>
   <p>Mantiene un perfil de presencia fundamentalmente económico –74,5% de su presencia global en 2019– vía sus inversiones en el exterior, los bienes primarios o la energía, dada su condición de cuarto productor de gas y petróleo a nivel mundial.</p>
   <p>En su dimensión blanda, poco relevante en su proyección exterior, se proyecta vía migraciones, cultura, ciencia y educación.</p>'
   WHERE code='CA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Canada is 8th in the global presence ranking; a position that it still holds despite the rise of China and despite its loss of economic weight –down four positions since 1990 in the GDP ranking–.</p>
   <p>It maintains a strong economic profile –74.5% of its global presence in 2019– via its investments abroad and its exports of primary goods or energy, given that it is the 4th largest gas and oil exporter.</p>
   <p>Its soft dimension, which is less determinant, is grounded in migrations, culture, science and education.</p>'
   WHERE code='CA' AND language='en';

  -- The Netherlands
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>A pesar del paulatino descenso de los Países Bajos en la clasificación mundial según el PIB, el país se mantiene en puestos elevados del Índice Elcano de Presencia Global. Se trata de una presencia de naturaleza fundamentalmente económica –esta dimensión representa en 2019 el 77% de su presencia global–. A su potencial exportador de bienes primarios se añade, por un lado, su condición de principal productor de gas en la Unión Europea y la posición estratégica del puerto de Rotterdam y, por otro , su posición estratégica en el sistema bancario y financiero europeo. Así, buena parte de su elevado registro puede explicarse por su condición de hub exportador e inversor.</p>
   <p>Este perfil se repite en el análisis de su presencia dentro del espacio europeo, donde ocupa el tercer puesto por detrás de Alemania y Reino Unido, por delante de Francia desde 2014.</p>'
   WHERE code='NL' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Despite the gradual decline in its world ranking by GDP, the Netherlands retains a high position in the Elcano Global Presence Index. Its economic dimension –which in 2019 accounted for 77% of its total value– continues to be the most important component.</p>
   <p>The importance of the Netherlands as exporter of primary goods is added, on the one hand, to its status as the main gas European producer and the strategic position of the port of Rotterdam and, on the other hand, its strategic position in the European banking and financial system. Thus, much of its position can be explained by its role as an export and investor hub. Its profile is replicated in Europe, where the Netherlands has the 3rd highest value after Germany and the United Kingdom, ahead of France since 2014.</p>'
   WHERE code='NL' AND language='en';

  -- South Korea
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Corea del Sur ocupa en 2019 la posición 11ª del ranking del Índice Elcano de Presencia Global. El país asiático ha registrado un importante crecimiento en su proyección exterior desde 1990, cuando ocupaba la 20ª posición.</p>
   <p>Este crecimiento ha estado especialmente apoyado en el aumento de exportaciones de manufacturas, y más recientemente del stock exterior de inversión extranjera, reflejando el proceso de internacionalización de las empresas coreanas. Dentro de la dimensión blanda destaca en ciencia y tecnología, lo que se vincula con el aumento de la complejidad tecnológica de sus exportaciones, así como en cultura, reflejo de la estrategia de diplomacia cultural exterior que viene desarrollando desde años. Respecto a la dimensión militar, registra un importante aumento de su equipamiento naval, que le sitúa por detrás de China y Japón, pero por delante de la India.</p>'
   WHERE code='KR' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>South Korea ranks 11th position in the 2019 edition of Elcano Global Presence Index. The Asian country has recorded significant growth in its external projection since 1990, when it occupied the 20th place.</p>
   <p>This growth has been mainly supported by the increase in manufacturing exports, and more recently in the foreign investment stock, reflecting the internationalization process of Korean companies. Within the soft dimension, it stands out in science and technology, which is linked to the increase in the technological complexity of its goods exports; as well as in culture, due to the foreign cultural diplomacy strategy that has been developing for years. Regarding the military dimension, it registers a significant increase in its naval equipment in recent years, behind China and Japan but ahead of India.</p>'
   WHERE code='KR' AND language='en';


  -- Spain
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>España ocupa la 12ª posición en el Índice Elcano de Presencia Global en 2019 recuperando una posición tras descender a la 13ª en 2015. Ello se debe a la mejora en su desempeño económico en el exterior (10ª posición en presencia económica), aunque su fortaleza sigue estando fundamentalmente en la dimensión blanda (11ª posición). En el plano militar, el papel internacional de España es más pasivo (14ª posición).</p>
   <p>En la década de los 90 aumentó notablemente su presencia global, debido al crecimiento tanto de la dimensión económica y, sobre todo, de la blanda. Destaca la variable de turismo, siendo el 2º país con mayor número de visitantes extranjeros. La dimensión económica se ve afectada por la crisis de finales de los 2000, aunque recientemente se produce una recuperación de las exportaciones de servicios, que se explica con el sector turístico.</p>
   <p>España es 6ª en el ranking del Índice Elcano de Presencia Europea. En el ámbito económico europeo destaca por sus exportaciones de bienes primarios, y dentro de la dimensión blanda el protagonismo es de las migraciones, el turismo o publicaciones científicas.</p>'
   WHERE code='ES' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Spain is 12th in the Elcano Global Presence Index in 2019, recovering a position after descending to 13th in 2015. This is due to the improvement in their economic performance abroad (10th position in economic presence), although its main strength is mainly in the soft dimension, (11th place) In the military sphere (15th), Spain’s international role is more passive (14th place).</p>
   <p>Spain’s global presence increased significantly during the 90s; a trend supported by the economic dimension and, mainly, by its soft presence. Tourism stands out, being the 2nd world destination. The economic dimension was affected by the late 2000s crisis. However, there has been a recent recovery of the services variable, due to the performance of tourism.</p>
   <p>Spain ranks 6th in the Elcano European Presence Index. In the European economic field Spain stands out for its exports of primary goods, and for its soft dimension, with a leading role in migration, tourism or scientific publications.</p>'
   WHERE code='ES' AND language='en';

  -- India
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>India ocupa la 13ª posición del ranking del Índice Elcano de Presencia Global. Se trata de un puesto relativamente bajo en comparación con su tamaño en términos de PIB (sexto puesto en la clasificación mundial), y también bajo respecto a su tamaño en términos de población (segundo puesto).</p>
   <p>Estos datos se explican con el modelo de desarrollo de India que, a diferencia del de China, ha estado orientado a la economía interna. Quizá por ello, dentro de su proyección exterior, tiene tanta relevancia la dimensión militar en comparación con lo que ocurre en el conjunto de la región asiática –29% de contribución de esta dimensión a su presencia global en 2019, superior a la registrada para el conjunto de Asia y Pacífico–.</p>
   <p>No obstante, en los últimos años, parece estar dándose un cambio de tendencia. India registra importantes crecimientos de presencia económica –con mayor protagonismo de los servicios, seguidos por manufacturas y bienes primarios–, así como en algunos indicadores de la dimensión blanda –cultura, ciencia y tecnología–. Ello le ha permitido ganar paulatinamente cuota de presencia global.</p>'
   WHERE code='IN' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>India occupies the 13th position in the Elcano Global Presence Index. This position is relatively low in comparison with its size in terms of GDP (sixth place in the world ranking) and specially with respect to its size in terms of population (second place). These data are consistent with the development model of India, which, unlike China, has been mainly inward-oriented. Perhaps for this reason, within its external projection, the military dimension is so relevant in comparison with that of other Asian countries –29% of its global presence in 2019, higher than that recorded for the whole Asia and the Pacific region–.</p>
   <p>However, this trend has changed recently. India records an important growth of economic presence –with prominence of services exports, followed by manufactures and primary goods– as well as in some indicators of the soft dimension –culture, science and technology–. This has allowed India to gradually gain global presence share.</p>'
   WHERE code='IN' AND language='en';

  ------------BLOCKS-------------------------------------
  -- Latin America
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>América Latina se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p>
   <p>Los países que forman parte de él son Argentina, Bahamas, Bolivia, Brasil, Chile, Colombia, Costa Rica, Cuba, Ecuador, El Salvador, Guatemala, Jamaica, Honduras, México, Nicaragua, Panamá, Paraguay, Perú, República Dominicana, Trinidad y Tobago, Uruguay y Venezuela. Representan en conjunto el 99,3% del PIB regional y 97,7% de la población latinoamericana (según datos de 2018 del Banco Mundial).</p>'
   WHERE code='XBLA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Latin America is constituted by the countries in the region whose global presence has been included in the calculation. The bloc’s global presence is obtained by adding the global presence of each country of which it is comprised.</p>
   <p>The countries that make up the bloc are Argentina, Bahamas, Bolivia, Brazil, Chile, Colombia, Costa Rica, Cuba, Ecuador, El Salvador, Guatemala, Jamaica, Honduras, Mexico, Nicaragua, Panama, Peru, the Dominican Republic, Trinidad and Tobago, Uruguay and Venezuela. They account for 99.3 % of the Latin America’s GDP and 97.7% of its population (according to World Bank data for 2018).</p>'
   WHERE code='XBLA' AND language='en';

  -- North America.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>América del Norte está formada por Estados Unidos y Canadá. De este modo, en el Índice Elcano de Presencia Global queda representado el 100% del PIB regional y de la población.</p>'
   WHERE code='XBNA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>North America comprises the United States of America and Canada. The bloc’s global presence is calculated by adding up the two countries’ global presences. Thus, 100% of the region’s GDP and population are represented in the Elcano Global Presence Index.</p>'
   WHERE code='XBNA' AND language='en';

  -- Asia Pacif.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Asia-Pacífico se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p>
   <p>Los países que forman parte de él son Australia, Bangladesh, Camboya, China, Filipinas, India, Indonesia, Japón, Malasia, Nueva Zelanda, Pakistán, Corea del Sur, Singapur, Tailandia, Vietnam, Myanmar, Nepal, Sri Lanka, Kazajistán, Turkmenistán y Uzbekistán. Representan el 99,7% y el 98,6% del PIB y de la población de la región, respectivamente (según datos de 2018 del Banco Mundial).</p>'
   WHERE code='XBAP' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Asia-Pacific is constituted by the countries in the region for which their global presence has been calculated. The global presence of the bloc is obtained by the pure sum of the global presence of each country that makes up the bloc.</p>
   <p>The countries comprising the bloc are Australia, Bangladesh, Cambodia, China, India, Indonesia, Japan, Malaysia, Nepal, New Zealand, Pakistan, the Philippines, South Korea, Singapore, Sri Lanka, Thailand, Vietnam, Myanmar, Kazakhstan, Turkmenistan and Uzbekistan. They account for 99.7% and 98.6% of the region’s GDP and population, respectively (according to World Bank data for 2018).</p>'
   WHERE code='XBAP' AND language='en';

  -- Europe
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Europa, como bloque, se compone de todos los países que forman parte de la región (sean o no estados miembros de la Unión Europea) para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la mera suma de la presencia global de cada país que conforma el bloque.</p>
   <p>Los países que forman parte del bloque Europa son Albania, Alemania, Austria, Azerbaiyán, Bélgica, Bielorrusia, Bosnia y Herzegovina, Bulgaria, Chipre, Croacia, Dinamarca, Eslovaquia, Eslovenia, España, Estonia, Finlandia, Francia, Georgia, Grecia, Hungría, Irlanda, Islandia, Italia, Letonia, Lituania, Luxemburgo, Macedonia del Norte, Malta, Noruega, Países Bajos, Polonia, Portugal, Reino Unido, República Checa, Rumanía, Rusia, Serbia, Suecia, Suiza, Turquía y Ucrania.</p>
   <p>Los países europeos considerados para el Índice Elcano de Presencia Global representan el 99,8% del PIB regional y el 99,3% de su población, según datos de 2018 del Banco Mundial.</p>'
   WHERE code='XBE2' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Europe, as a bloc, is considered to comprise all the countries in the region (regardless of whether they are member states of the European Union) whose global presence has been calculated. The bloc’s global presence is obtained by adding up the result for each of its constituent countries. The countries that make up the European bloc are Albania, Austria, Azerbaijan, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, the Czech Republic, Denmark, Estonia, Finland, France, Georgia, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, the Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, the Ukraine and the United Kingdom.</p>
   <p>The European countries considered for the Elcano Global Presence Index account for 99.8% of the region’s GDP and 99.3 % of its population (according to World Bank data for 2018).</p>'
   WHERE code='XBE2' AND language='en';

  -- Magreb and ME.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Magreb y Oriente Medio se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p>
   <p>Los países que forman parte de él son Afganistán, Arabia Saudí, Argelia, Baréin, Egipto, Emiratos Árabes Unidos, Irán, Irak, Israel, Jordania, Kuwait, Libia, Líbano, Marruecos, Siria, Omán, Túnez, Catar y Yemen. Representan el 98,5% del PIB regional y el 98,9% de su población (según datos de 2018 del Banco Mundial).</p>'
   WHERE code='XBMM' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>The Maghreb and the Middle East are made up of the countries forming the region whose global presence has been calculated. The bloc’s global presence is the result of the pure sum of the global presence of each country comprising it. The countries considered are Afghanistan, Algeria, Bahrein, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Libya, Lebanon, Morocco, Oman, Syria, Tunisia, the United Arab Emirates, Qatar and Yemen. They account for 98.5% of the s GDP and 98.9% of its population (according to World Bank data for 2018).</p>'
   WHERE code='XBMM' AND language='en';

  -- Africa Sub.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p><África Subsahariana se compone de los países de esta región para los que existe cálculo de presencia global, esto es: Angola, Botsuana, Burkina Faso, Camerún, Costa de Marfil, Etiopía, Gabón, Ghana, Guinea Ecuatorial, Kenia, Madagascar, Mali, Mauricio, Mozambique, Namibia, Nigeria, República Democrática del Congo, Senegal, Sudáfrica, Sudán, Tanzania, Uganda, Zambia y Zimbabue. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país. Los países considerados representan un 93,9% del PIB regional y un 85,2% de su población (según datos de 2018 del Banco Mundial).</p>'
   WHERE code='XBSA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Sub-Saharan Africa comprises the countries in the region whose global presence has been calculated: Angola, Botswana, Burkina Faso, Cameroon, Côte d’Ivoire, Equatorial Guinea, Ethiopia, Gabon, Ghana, Kenya, Madagascar, Mali, Mauritius, Mozambique, Namibia, Nigeria, the Democratic Republic of Congo, Senegal, South Africa, Sudan, Tanzania, Uganda, Zambia and Zimbabwe. The bloc’s global presence is obtained by adding the global presence of each country considered. The countries evaluated account for only 93.9% of the region’s GDP and 85.2% of its population (according to World Bank 2018 data).</p>'
   WHERE code='XBSA' AND language='en';

COMMIT;

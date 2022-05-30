
/*
  Update country comments.
*/

BEGIN;
-- USA
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Estados Unidos ocupa el primer puesto del Índice Elcano de Presencia Global en todos los años para los que se calcula. En 2021, también mantiene esta primera posición en todas las variables, con las excepciones de energía, manufacturas, ciencia y turismo. Presenta, de los 150 países, las mayores cuotas de presencia en todas las dimensiones –18,6% en la económica; 26,9% en la militar; y 22,9% en la blanda–. Por otro lado, a diferencia de lo que ocurre en otros países desarrollados, la dimensión militar define en buena medida su proyección exterior, con una contribución de 26,8% en 2021.</p><p>A pesar de esta hegemonía, Estados Unidos pierde presencia global relativa en comparación con el resto de países –24,8% de cuota de presencia global en 1990 frente a 21,3% en 2021–. En un periodo de surgimiento de nuevos actores globales, diversas economías emergentes (particularmente petroleras o asiáticas) cosechan ganancias de cuota que reducen el protagonismo estadounidense.</p>'
 WHERE code='US' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>US tops the Elcano Global Presence Index in all years. In 2021, it also leads the ranking in all variables, except for energy, manufactures and tourism. Of all 150 countries, it records the highest share of presence in all dimensions: 18.6% in the economic domain, 26.9% in the military and 22.9% in soft presence. Moreover, unlike other developed countries, its military dimension strongly defines its external projection, with a contribution at 26.8% in 2021.</p><p>Despite its hegemony, the US loses relative global presence when compared with other countries: from a 24.8% share of global presence in 1990 to 21.3% in 2021. In a period of emergence of new global players, several economies (particularly oil producers or Asian countries) reap gains of share that reduce the American role.</p>'
 WHERE code='US' AND language='en';

-- European Union
UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Si considerásemos a la Unión Europea un único país, tendría en 2021 un registro superior al de Estados Unidos y tres veces mayor que el de China, a pesar del Brexit y de la pandemia. Obtendría el mayor valor de presencia económica –con relevancia de la inversión en el exterior y las exportaciones de servicios– y de presencia blanda –turismo, educación, ciencia, deportes y cooperación al desarrollo–, siendo superado por Estados Unidos tan sólo en la clasificación de presencia militar.</p><p>La crisis económica de finales de los 2000, con especial impacto dentro del espacio comunitario, redujo la presencia de la Unión Europea en el resto del mundo. A partir de 2014 comenzó una leve tendencia de recuperación, drásticamente interrumpida con la pandemia y el Brexit. La pandemia ha tenido un fuerte impacto en su proyección blanda -especialmente por la interrupción del turismo- y, con la salida del Reino Unido, la Unión Europea ha perdido a un miembro caracterizado por una fuerte orientación extracomunitaria y un importante equipamiento militar.</p>'
WHERE code='XBEU' AND language='es';

UPDATE iepg_data_redux.iepg_comment
SET comment=E'<p>If the European Union were to be considered a single country, it would have a higher record than that of the United States and three times higher than that of China, despite both Brexit and the pandemic. The European Union would have the greatest value of economic presence –with relevant foreign investment and exports of services– and of soft presence –tourism, education, science, sports or development cooperation–, being surpassed by the United States only in the classification of military presence.</p>
<p>The late 2000s’ economic crisis, which has especially hit the European Union, has had an impact on its presence in the rest of the world, reducing its economic presence. A slight recovery trend began in 2014 but was drastically interrupted by the pandemic and Brexit. The pandemic has had a strong impact on its soft projection –especially through the interruption of tourism– and, with the exit of the United Kingdom, the European Union has lost a member characterized by a strong extra-EU orientation and high military equipment.</p>'
WHERE code='XBEU' AND language='en';


-- China
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>El notable ascenso del gigante asiático en las últimas décadas tiene su reflejo en la clasificación del Índice Elcano de Presencia Global, donde escala ocho posiciones desde 1990. Este crecimiento se debe en buena medida a la dimensión económica, donde se impulsa del 16º lugar en 1990 al 2º desde 2015. A su vez, esto tiene su origen en el crecimiento de sus exportaciones manufactureras, pero también de bienes primarios, servicios e inversiones. Por ello, la naturaleza de su presencia global es principalmente económica, con un peso del 62% sobre el valor índice en 2021.</p>
 <p>Sin embargo, en los últimos años se producen aumentos sustanciales de presencia blanda, con un valor en 2021 que es 23 veces mayor que en 1990. Esto se explica con el comportamiento de indicadores como información, tecnología o ciencia, e incluso turismo o deportes.</p>
 <p>Con todo ello, su cuota de presencia pasa de 2,1% en 1990 al 9% en 2021, lejos de la de Estados Unidos, pero ya superior a las de Francia, Reino Unido y Alemania.</p>'
 WHERE code='CN' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>China’s remarkable rise in recent decades is reflected in its classification in the Elcano Global Presence Index, where it has upscaled eight positions since 1990. This is mainly due to its economic presence, where it is now ranked 2nd (16th in 1990). This trend is driven by the export of manufactures, but also by primary goods, services and investments. Hence, the nature of its global presence is mainly economic, accounting for 62% of its index value in 2021.</p>
 <p>However, more recently China has also substantially increased its soft presence, with a record twenty-three times higher than in 1990; pushed by the increase in indicators such as information, technology or science, and even tourism or sports.</p>
 <p>As a result, its presence quota has gone up from 2.1% in 1990 to 9% in 2021. Although still far from the US, China has overtaken France, the United Kingdom and Germany.</p>'
 WHERE code='CN' AND language='en';


-- Germany
UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Apoyada fundamentalmente en su proyección económica (69,5% de su presencia global), Alemania ha aumentado de forma continuada su presencia exterior desde mediados de los 90, tras su reunificación y la caída del bloque soviético. Se encuentra entre las cinco primeras posiciones en todas las variables económicas, con la única excepción de la de energía. Ocupa la 3ª posición en el ranking de presencia global, tras Estados Unidos y China, y por delante de Reino Unido.</p>
<p>Alemania ocupa el primer puesto en la clasificación del Índice Elcano de Presencia Europea lo que significa que es, de todos los Estados miembros, el que tiene mayor proyección dentro de la UE. Es el resultado de ocupar el 1er puesto en manufacturas, servicios, migraciones, ciencia, tecnología y educación, y el 2º en bienes primarios, cultura, información o deportes. Este liderazgo se fortalece tras la salida del Reino Unido de la UE y la reconfiguración del espacio comunitario.</p>'
WHERE code='DE' AND language='es';

UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Since the mid-1990s and following its reunification and the fall of the Soviet Union, Germany has recorded a steady growth in its external presence, based on its economic dimension -that provides 69.5% of its global presence-. It is ranked among the five top positions in all economic variables; except for energy. It is 3rd in the global presence ranking, after the US and China and before the United Kingdom.</p>
<p>Germany is ranked 1st in the Elcano European Presence Index, which means that, among all member states, it is the one with the highest projection within the EU. This is the result of being 1st in manufactures, migrations, science, technology and education and 2nd in primary goods, culture, information or sports. This leadership has been strengthened after Brexit and the reconfiguration of the EU space.</p>'
WHERE code='DE' AND language='en';

-- UK
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Reino Unido se sitúa en la 5ª posición en el ranking de presencia global de 2021, tras haber sido superado por Japón. Aunque ocupa posiciones elevadas en las tres dimensiones, es en la blanda donde más destaca; y lo hace por su desempeño en deportes, educación, cultura o cooperación al desarrollo.</p>
 <p>El Reino Unido tiene mucha proyección, además, en algunos indicadores de presencia económica, particularmente en las exportaciones de servicios y en la inversión, dada la importancia de su economía de servicios a empresas, así como su función de hub financiero.</p>
 <p>Antes de su salida de la UE, Reino Unido ocupaba la 3ª posición del Índice Elcano de Presencia Europea, tras Alemania y Países Bajos.</p>'
 WHERE code='GB' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>The United Kingdom occupies the 5th position in the global presence ranking in 2021, being overtaken by Japan. Although it outstands in all dimensions, it is particularly strong in the soft domain due to its performance in sports, education, culture or development cooperation.</p>
 <p>It also records a strong economic projection, particularly in services and investments, given the importance of its economic activity in business services and its condition of financial hub.</p>
 <p>Prior to Brexit, the United Kingdom was ranked 3rd in the Elcano European Presence Index, after Germany and the Netherlands.</p>'
 WHERE code='GB' AND language='en';

 -- Japan
 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Japón ocupa en 2021 el 4º lugar en la clasificación de presencia global tras superar a Reino Unido. No obstante, y a pesar de mantenerse como la 3ª economía mundial, las consecuencias de la crisis de los noventa aún se reflejan en su presencia económica, en la que pasa de ocupar el 3er puesto en 1990, al 5º en 2021.</p>
  <p>En los últimos años mantiene un crecimiento de su proyección económica, gracias, en buena medida, a las inversiones (que superan las de Francia o Alemania).</p>
  <p>También aumenta la dimensión militar que, a pesar de la desmilitarización tras la Segunda Guerra Mundial, contribuye crecientemente a la presencia japonesa –23,1% en 2021–; más que en otras economías desarrolladas.</p>
  <p>Aumenta su presencia blanda tanto en términos absolutos como relativos, recuperando en 2021 la 3ª posición que ocupaba años atrás. En este ámbito, sus principales fortalezas están en la tecnología, la ciencia y la cooperación al desarrollo.</p>'
  WHERE code='JP' AND language='es';

 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Japan is 4th in the global presence ranking in 2021. Despite being the 3rd world economy, the consequences of the nineties’ crisis still show in its economic presence records, where it has lost two positions since 1990. However, it is now ranked 5th, up from the 7th position in 2010; something which is mainly due to its performance in investments, where it has surpassed both Germany and France.</p>
  <p>The military dimension also grows –up to a contribution of 23.1% in 2021– and is higher than in other developed countries, despite the demilitarization following the World War II.</p>
  <p>The soft dimension increases both in absolute and relative terms, recovering in 2021 the 3rd position held years ago. In this field, its main strengths are in technology, science and development cooperation.</p>'
  WHERE code='JP' AND language='en';

-- Rusia
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>La presencia global de la Unión Soviética cae fuertemente con la desintegración del bloque, al finalizar la Guerra Fría, y el desplome de su presencia militar, que en aquel momento era del 89,4% de su presencia total. Pese a ello, Rusia no pierde en ningún momento el 2º puesto en el ranking de presencia militar.</p>
 <p>La recuperación de su presencia global se sustenta en su dimensión económica y, concretamente, en la variable de energía, siendo el primer exportador mundial de gas y el segundo de petróleo.</p>
 <p>La dimensión blanda no es tan relevante, aunque el país destaque en deportes (debido a su éxito en el medallero olímpico), información, educación o migraciones.</p>
 <p>Con todo ello, Rusia se sitúa hoy en la 7ª posición por presencia global, frente a la 2ª en 1990.</p>'
 WHERE code='RU' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>The Soviet Union’s external projection dramatically fell with the disintegration of the bloc, at the end of the Cold War, and the subsequent drop of its military presence, which accounted for 89.4% of its total presence in 1990. In spite of this, Russia never loses the 2nd position in the military presence ranking.</p>
 <p>The recovery of its global presence is grounded in its economic dimension and, more specifically, the energy variable, being Russia the world top exporter of gas and the second exporter of oil.</p>
 <p>The soft dimension is not particularly relevant. Although, the country outstands in sports (due to its performance in the Olympic Games), information, education or migrations.</p>
 <p>All in all, Russia is now 7th in global presence, down from the 2nd position in 1990.</p>'
 WHERE code='RU' AND language='en';

-- France
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Francia se enfrenta a una pérdida relativa de relevancia en la escena internacional. Tercero en 1995, se sitúa hoy en el 6º puesto del ranking del Índice Elcano de Presencia Global. Mantiene un perfil similar al de otras economías europeas, con una fuerte presencia blanda sobre todo en turismo, –siendo la primera potencia turística a nivel mundial–, cultura o cooperación al desarrollo.</p>
 <p>Es el tercer país en presencia en el espacio europeo, medida con el Índice Elcano de Presencia Europea, y tras haber ganado un puesto por la salida del Reino Unido. Como la mayoría de los Estados miembros, su perfil en la UE es más blando (con una contribución de 52,9%) que económico (47,1%).</p>'
 WHERE code='FR' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>France faces a relative loss of relevance in the international scene. Third in 1995, it is now ranked 6th according to the Elcano Global Presence Index. Its profile is like that of other European countries, with a strong soft presence, particularly in tourism -being the first world tourism destination-, culture or development cooperation.</p>
 <p>It is 3rd in the European sphere, when measured with the Elcano European Presence Index, after winning a position due to the UK\'s exit from the EU. As most member states, its profile within the EU is soft (with a contribution of 52.9%), rather than economic (47.1%).</p>'
 WHERE code='FR' AND language='en';

 -- Italy
 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Italia se mantiene en el 10º puesto del ranking –frente al 7º puesto ocupado en 1990–. Esta tendencia se debe a la ralentización del crecimiento de su presencia económica, que tiene un escaso crecimiento desde los 90 en comparación con otros países del entorno. No obstante, continúa siendo uno de los países más industrializados, por lo que tiene relevancia dentro de las exportaciones de manufacturas e inversiones en el exterior. Al igual que ocurre con otras potencias europeas, mantiene registros elevados en la dimensión blanda –apoyada en cultura, tecnología, ciencia y turismo–.</p>
  <p>Por el contrario, dentro del espacio europeo su presencia es fundamentalmente blanda –estando entre los cinco primeros puestos en todos los indicadores de esta dimensión, con la excepción de educación, y ha sido precisamente en esta dimensión la que han venido registrando mayores crecimientos.</p>'
  WHERE code='IT' AND language='es';

 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Italy holds the 10th place in the Elcano Global Presence Index ranking since 2014 –7th position in 1990–. This trend is due to the slower growth of its economic presence, which has registered a low increase compared to other neighboring countries. However, Italy is still one of the most industrialized countries, so its presence is fundamentally economic, supported by manufactured exports and investments. Similarly, to other European countries Italy has a high score in the soft dimension –mainly because of culture, technology, science and tourism–.</p>
  <p>Within the European Union, Italy’s presence is of a soft nature. This dimension has registered the greatest growth –climbing positions up to being one of the top five European countries in all indicators in this domain, except for education.</p>'
  WHERE code='IT' AND language='en';

  -- Canada
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Canadá ocupa en 2021 el 8º puesto del ranking de presencia global, a pesar del auge de China y de la reducción relativa de su peso económico en el mundo –pierde cuatro puestos en la clasificación mundial de PIB desde 1990–.</p>
   <p>Mantiene un perfil de presencia fundamentalmente económico –74,3% de su presencia global en 2021– vía sus inversiones en el exterior, los bienes primarios o la energía, dada su condición de cuarto productor de gas y petróleo a nivel mundial.</p>
   <p>En su dimensión blanda, poco relevante en su proyección exterior, se proyecta vía migraciones, cultura, ciencia y educación.</p>'
   WHERE code='CA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Canada is 8th in the global presence ranking; a position that it still holds despite the rise of China and despite its loss of economic weight –down four positions since 1990 in the GDP ranking–.</p>
   <p>It maintains a strong economic profile –74.3% of its global presence in 2021– via its investments abroad and its exports of primary goods or energy, given that it is the 4th largest gas and oil exporter.</p>
   <p>Its soft dimension, which is less determinant, is grounded in migrations, culture, science and education.</p>'
   WHERE code='CA' AND language='en';

  -- The Netherlands
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>A pesar del paulatino descenso de los Países Bajos en la clasificación mundial según el PIB, el país se mantiene en puestos elevados del Índice Elcano de Presencia Global. Se trata de una presencia de naturaleza fundamentalmente económica –esta dimensión representa en 2021 el 80% de su presencia global–. A su potencial exportador de bienes primarios se añaden su condición de principal productor de gas en la Unión Europea, la posición estratégica del puerto de Rotterdam y su posición en el sistema bancario y financiero europeo. Así, buena parte de su elevado registro puede explicarse por su condición de hub exportador e inversor.</p>
   <p>Este perfil se repite en el espacio europeo, donde ocupa el segundo puesto por detrás de Alemania y por delante de Francia e Italia desde 2016.</p>'
   WHERE code='NL' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Despite the gradual decline in its world ranking by GDP, the Netherlands retains a prominent position in the Elcano Global Presence Index. Its economic dimension –which in 2021 accounted for 80% of its total value– continues to be the most key component.</p>
   <p>The importance of the Netherlands as exporter of primary goods is added to its status as the main gas European producer, the strategic position of the port of Rotterdam and its position in the European banking and financial system. Thus, much of its position can be explained by its role as an export and investor hub.</p>
   <p>Its profile is replicated in Europe, where the Netherlands has the 2nd highest value after Germany, ahead of France and Italy since 2016.</p>'
   WHERE code='NL' AND language='en';

  -- South Korea
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Corea del Sur ocupa en 2021 la posición 12ª del ranking del Índice Elcano de Presencia Global por detrás de la India. El país asiático ha registrado un importante crecimiento en su proyección exterior desde 1990, cuando ocupaba la 16ª posición.</p>
   <p>Este crecimiento ha estado especialmente apoyado en el aumento de exportaciones de manufacturas, y más recientemente del stock exterior de inversión extranjera, reflejando el proceso de internacionalización de las empresas coreanas. Dentro de la dimensión blanda destaca en ciencia y tecnología, lo que se vincula con el aumento de la complejidad tecnológica de sus exportaciones, así como en cultura, reflejo de la estrategia de diplomacia cultural exterior que viene desarrollando desde hace años. Respecto a la dimensión militar, registra un importante aumento de su equipamiento naval, que le sitúa por detrás de China y Japón, pero por delante de la India.</p>'
   WHERE code='KR' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>South Korea ranks 12th in the 2021 edition of Elcano Global Presence Index behind India. The Asian country has recorded a significant growth in its external projection since 1990, when it occupied the 16th place.</p>
   <p>This growth has been mainly supported by the increase in manufacturing exports, and more recently in the foreign investment stock, reflecting the internationalization process of Korean companies. Within the soft dimension, it stands out in science and technology, linked to the increase in the technological complexity of its goods’ exports; as well as in culture, due to the foreign cultural diplomacy strategy that has been developing for years. Regarding the military dimension, it registers a significant increase in its naval equipment in recent years, behind China and Japan but ahead of India.</p>'
   WHERE code='KR' AND language='en';


  -- Spain
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>España ocupa la 13ª posición en el Índice Elcano de Presencia Global desde 2018. Aunque en los últimos años había ganado presencia global en términos absolutos, este incremento ha sido insuficiente para contener el ascenso de India y de Corea del Sur.</p>
   <p>En la proyección exterior de España la dimensión blanda adquiere un protagonismo mayor que en otras economías desarrolladas, obteniendo tradicionalmente mejores posiciones en el ranking de esta dimensión (por ejemplo 11ª posición en presencia blanda en 2019, frente a la 12ª en presencia económica) mientras que en el plano militar el papel internacional de España es menor (14º posición ese año).</p>
   <p>Ello se debe a la importancia del turismo en su proyección exterior siendo, hasta el estallido de la pandemia, el 2º país con mayor número de visitantes extranjeros, lo que contribuyó también a la recuperación de su presencia económica, tras la Gran Recesión, por el aumento de las exportaciones de servicios. Por ello, la pandemia ha tenido un especial impacto en la proyección exterior de España, siendo el país que más presencia global pierde en el último año, y descendiendo a los puestos 13º y 15º de los rankings de presencia blanda y económica, respectivamente.</p>
   <p>España es 6º en el ranking del Índice Elcano de Presencia Europea, perdiendo una posición tras la salida del Reino Unido. En el ámbito económico europeo, destaca por sus exportaciones de bienes primarios, y dentro de la dimensión blanda el protagonismo es de las migraciones, el turismo y las publicaciones científicas.</p>'
   WHERE code='ES' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment=E'<p>Spain is 13th in the Elcano Global Presence Index since 2018. Although in recent years Spain gained global presence in absolute terms, this increase could not contain the rise of India and South Korea.</p>
   <p>In Spain\'s external projection, the soft dimension plays a more significant role than in other developed economies, historically holding higher positions in the ranking of this dimension (e.g., 11th position in soft presence in 2019, compared to 12th in economic presence) while in the military sphere, Spain\'s international role is less relevant (ranking 14th that year).</p>
   <p>This is due to the importance of tourism in its external projection, being, until the pandemic, the country with the second highest number of foreign visitors, also contributing to the recovery of its economic presence, due to the increase in exports of services, after the Great Recession.</p>
   <p>The pandemic has therefore had a particular impact on Spain\'s external projection, being the country with the highest loss of global presence the last year and falling to 13th and 15th places in the rankings of soft and economic presence, respectively.</p>
   <p>Spain ranks 6th in the Elcano European Presence Index, losing one position after Brexit. In the European sphere, Spain stands out for its exports of primary goods, and for its soft dimension, with a leading role in migration, tourism or scientific publications.</p>'
   WHERE code='ES' AND language='en';

  -- India
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>India ocupa la 11ª posición del ranking del Índice Elcano de Presencia Global, por delante de Corea del Sur.</p>
   <p>Se trata, sin embargo, de un puesto relativamente bajo en comparación con su tamaño en términos de PIB (sexto puesto en la clasificación mundial), y también bajo respecto a su tamaño en términos de población (segundo puesto).</p>
   <p>Esto se explica con el modelo de desarrollo de India que, a diferencia del de China, ha estado orientado a la economía interna. Así, ocupa el puesto 16 en el ranking de presencia económica, mientras que en el de presencia blanda ocupa el octavo. Quizá por ello, dentro de su proyección exterior, tiene tanta relevancia la dimensión militar en comparación con lo que ocurre en el conjunto de la región asiática –28,5% de contribución de esta dimensión a su presencia global en 2021, superior a la media para el conjunto de Asia y Pacífico–.</p>
   <p>No obstante, en los últimos años, parece estar dándose un cambio de tendencia. India registra importantes crecimientos de presencia económica –con mayor protagonismo de los servicios, seguidos por manufacturas y bienes primarios–, así como en algunos indicadores de la dimensión blanda –cultura, ciencia y tecnología–. Ello le ha permitido ganar paulatinamente cuota de presencia global.</p>'
   WHERE code='IN' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>India occupies the 11th position in the Elcano Global Presence Index, ahead of South Korea. Still this position is relatively low in comparison with its size in terms of GDP (6th in the world ranking) and specially with respect to its size in terms of population (2nd place). These data are consistent with the development model of India, which, unlike China, has been mainly inward-oriented. It is ranked 16th in terms of economic presence, and 8th in terms of soft presence. For this reason, within its external projection, the military dimension is so relevant in comparison with that of other Asian countries –28,5% of its global presence in 2021, above the average of the Asia and the Pacific region–.</p>
   <p>However, this trend has changed recently. India records an important growth of its economic presence –with prominent services exports, followed by manufactures and primary goods– as well as in some indicators of the soft dimension –culture, science and technology–. This has allowed India to gradually gain global presence share.</p>'
   WHERE code='IN' AND language='en';

  ------------BLOCKS-------------------------------------
  -- Latin America
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>América Latina se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p>
   <p>Los países que forman parte de él son Argentina, Bahamas, Bolivia, Brasil, Chile, Colombia, Costa Rica, Cuba, Ecuador, El Salvador, Guatemala, Jamaica, Honduras, México, Nicaragua, Panamá, Paraguay, Perú, República Dominicana, Trinidad y Tobago, Uruguay y Venezuela. Representan en conjunto el 99,2% del PIB regional y 97,8% de la población latinoamericana (según datos de 2019 del Banco Mundial).</p>'
   WHERE code='XBLA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Latin America is constituted by the countries in the region whose global presence has been included in the calculation. The bloc’s global presence is obtained by adding the global presence of each country of which it is comprised.</p>
   <p>The countries that make up the bloc are Argentina, Bahamas, Bolivia, Brazil, Chile, Colombia, Costa Rica, Cuba, Ecuador, El Salvador, Guatemala, Jamaica, Honduras, Mexico, Nicaragua, Panama, Peru, the Dominican Republic, Trinidad and Tobago, Uruguay and Venezuela. They account for 99.2 % of the Latin America’s GDP and 97.8% of its population (according to World Bank data for 2019).</p>'
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
   <p>Los países que forman parte de él son Australia, Bangladesh, Brunéi, Camboya, China, Filipinas, India, Indonesia, Japón, Malasia, Nueva Zelanda, Pakistán, Corea del Sur, Singapur, Tailandia, Vietnam, Mongolia, Myanmar, Nepal, Papúa Nueva Guinea, Sri Lanka, Kazajistán, Turkmenistán y Uzbekistán. Representan el 99,8% y el 98,9% del PIB y de la población de la región, respectivamente (según datos de 2019 del Banco Mundial).</p>'
   WHERE code='XBAP' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Asia-Pacific is constituted by the countries in the region for which their global presence has been calculated. The global presence of the bloc is obtained by the pure sum of the global presence of each country that makes up the bloc.</p>
   <p>The countries comprising the bloc are Australia, Bangladesh, Brunei, Cambodia, China, India, Indonesia, Japan, Malaysia, Mongolia, Nepal, New Zealand, Papua New Guinea, Pakistan, the Philippines, South Korea, Singapore, Sri Lanka, Thailand, Vietnam, Myanmar, Kazakhstan, Turkmenistan and Uzbekistan. They account for 99.8% and 98.9% of the region’s GDP and population, respectively (according to World Bank data for 2019).</p>'
   WHERE code='XBAP' AND language='en';

  -- Europe
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Europa, como bloque, se compone de todos los países que forman parte de la región (sean o no estados miembros de la Unión Europea) para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la mera suma de la presencia global de cada país que conforma el bloque.</p>
   <p>Los países que forman parte del bloque Europa son Albania, Alemania, Armenia, Austria, Azerbaiyán, Bélgica, Bielorrusia, Bosnia y Herzegovina, Bulgaria, Chipre, Croacia, Dinamarca, Eslovaquia, Eslovenia, España, Estonia, Finlandia, Francia, Georgia, Grecia, Hungría, Irlanda, Islandia, Italia, Letonia, Lituania, Luxemburgo, Macedonia del Norte, Malta, Moldavia, Noruega, Países Bajos, Polonia, Portugal, Reino Unido, República Checa, Rumanía, Rusia, Serbia, Suecia, Suiza, Turquía y Ucrania.</p>
   <p>Los países europeos considerados para el Índice Elcano de Presencia Global representan el 99,8% del PIB regional y el 99,6% de su población, según datos de 2019 del Banco Mundial.</p>'
   WHERE code='XBE2' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Europe, as a bloc, is considered to comprise all the countries in the region (regardless of whether they are member states of the European Union) whose global presence has been calculated. The bloc’s global presence is obtained by adding up the result for each of its constituent countries. The countries that make up the European bloc are Albania, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, the Czech Republic, Denmark, Estonia, Finland, France, Georgia, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Moldova, the Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, the Ukraine and the United Kingdom.</p>
   <p>The European countries considered for the Elcano Global Presence Index account for 99.8% of the region’s GDP and 99.6 % of its population (according to World Bank data for 2019).</p>'
   WHERE code='XBE2' AND language='en';

  -- Magreb and ME.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Magreb y Oriente Medio se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p>
   <p>Los países que forman parte de él son Afganistán, Arabia Saudí, Argelia, Baréin, Egipto, Emiratos Árabes Unidos, Irán, Irak, Israel, Jordania, Kuwait, Libia, Líbano, Marruecos, Siria, Omán, Túnez, Catar y Yemen. Representan el 98,5% del PIB regional y el 99,5% de su población (según datos de 2019 del Banco Mundial).</p>'
   WHERE code='XBMM' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>The Maghreb and the Middle East are made up of the countries forming the region whose global presence has been calculated. The bloc’s global presence is the result of the pure sum of the global presence of each country comprising it. The countries considered are Afghanistan, Algeria, Bahrein, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Libya, Lebanon, Morocco, Oman, Syria, Tunisia, the United Arab Emirates, Qatar and Yemen. They account for 99.5% of the s GDP and 98.9% of its population (according to World Bank data for 2019).</p>'
   WHERE code='XBMM' AND language='en';

  -- Africa Sub.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>África Subsahariana se compone de los países de esta región para los que existe cálculo de presencia global, esto es: Angola, Benín, Botsuana, Burkina Faso, Camerún, Chad, Costa de Marfil, Etiopía, Gabón, Ghana, Guinea, Guinea Ecuatorial, Kenia, Madagascar, Mali, Mauricio, Mozambique, Namibia, Níger, Nigeria, República del Congo, República Democrática del Congo, Senegal, Sudáfrica, Sudán, Tanzania, Uganda, Zambia y Zimbabue. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país. Representan un 96,7% del PIB regional y un 89,9% de su población (según datos de 2019 del Banco Mundial).</p>'
   WHERE code='XBSA' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Sub-Saharan Africa comprises the countries in the region whose global presence has been calculated: Angola, Benin, Botswana, Burkina Faso, Cameroon, Chad, Côte d’Ivoire, Equatorial Guinea, Ethiopia, Gabon, Ghana, Guinea, Kenya, Madagascar, Mali, Mauritius, Mozambique, Namibia, Niger, Nigeria, the Democratic Republic of Congo, Republic of Congo, Senegal, South Africa, Sudan, Tanzania, Uganda, Zambia and Zimbabwe. The bloc’s global presence is obtained by adding the global presence of each country considered. They account 96.7% of the region’s GDP and 89.9% of its population (according to World Bank 2019 data).</p>'
   WHERE code='XBSA' AND language='en';

COMMIT;

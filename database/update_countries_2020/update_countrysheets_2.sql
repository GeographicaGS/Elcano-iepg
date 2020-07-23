
/*
  Update country comments.
*/

BEGIN;

-- UK
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Reino Unido se sitúa en la 4ª posición en el ranking de presencia global. Aunque ocupa posiciones elevadas en las tres dimensiones, es en la blanda, en la que es 3º, donde más destaca; y lo hace por su desempeño en deportes, educación, cultura o cooperación al desarrollo.</p>
 <p>El Reino Unido tiene mucha proyección, además, en algunos indicadores de presencia económica, particularmente en las exportaciones de servicios y en la inversión, dada la importancia de su economía de servicios a empresas, así como su función de <i>hub</i> financiero.</p>
 <p>En el Índice Elcano de Presencia Europea, Reino Unido se clasifica 2º, tras Alemania y por delante de Países Bajos. Es el estado miembro con mayor contribución de presencia blanda (cerca de 80%), lo que significa que su perfil económico se proyecta sobre todo fuera de la Unión. De hecho, es 3º en la variable de servicios y 4º en la de inversiones, pero encabeza el ranking europeo en deportes, cultura, información, ciencia y educación y se sitúa 2º en migraciones.</p>'
 WHERE code='GB' AND language='es';

-- The Netherlands
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>A pesar del paulatino descenso de los Países Bajos en la clasificación mundial según el PIB, el país se mantiene en puestos elevados del Índice Elcano de Presencia Global. Se trata de una presencia de naturaleza fundamentalmente económica –esta dimensión representa en 2019 el 77% de su presencia global–. A su potencial exportador de bienes primarios se añade, por un lado, su condición de principal productor de gas en la Unión Europea y la posición estratégica del puerto de Rotterdam y, por otro, su posición estratégica en el sistema bancario y financiero europeo. Así, buena parte de su elevado registro puede explicarse por su condición de <i>hub</i> exportador e inversor.</p>
 <p>Este perfil se repite en el análisis de su presencia dentro del espacio europeo, donde ocupa el tercer puesto por detrás de Alemania y Reino Unido, por delante de Francia desde 2014.</p>'
 WHERE code='NL' AND language='es';

-- South Korea
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Corea del Sur ocupa en 2019 la posición 11ª del ranking del Índice Elcano de Presencia Global. El país asiático ha registrado un importante crecimiento en su proyección exterior desde 1990, cuando ocupaba la 20ª posición.</p>
 <p>Este crecimiento ha estado especialmente apoyado en el aumento de exportaciones de manufacturas, y más recientemente del <i>stock</i> exterior de inversión extranjera, reflejando el proceso de internacionalización de las empresas coreanas. Dentro de la dimensión blanda destaca en ciencia y tecnología, lo que se vincula con el aumento de la complejidad tecnológica de sus exportaciones, así como en cultura, reflejo de la estrategia de diplomacia cultural exterior que viene desarrollando desde hace años. Respecto a la dimensión militar, registra un importante aumento de su equipamiento naval, que le sitúa por detrás de China y Japón, pero por delante de la India.</p>'
 WHERE code='KR' AND language='es';

-- North America.
UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>América del Norte está formada por Estados Unidos y Canadá. De este modo, en el Índice Elcano de Presencia Global queda representado el 100% del PIB regional y de la población.</p>'
  WHERE code='XBNA' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Estados Unidos ocupa el primer puesto del Índice Elcano de Presencia Global en todos los años para los que se calcula. En 2019, también ocupa esta primera posición en todas las variables, con las excepciones de energía, manufacturas y turismo. Presenta, de los 130 países, las mayores cuotas de presencia en todas las dimensiones –18,8% en la económica; 28,3% en la militar; y 22,4% en la blanda–. Por otro lado, a diferencia de lo que ocurre en otros países desarrollados, la dimensión militar define en buena medida su proyección exterior, con una contribución de 25,4% en 2019.</p><p>A pesar de esta hegemonía, Estados Unidos pierde presencia global relativa en comparación con el resto de países –24,8% de cuota de presencia global en 1990 frente a 21,5% en 2019–. En un periodo de surgimiento de nuevos actores globales, diversas economías emergentes (particularmente petroleras o asiáticas) cosechan ganancias de cuota que reducen el protagonismo estadounidense.</p>'
 WHERE code='US' AND language='en';

 -- Germany
UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Apoyada fundamentalmente en su proyección económica (68,7% de su presencia global), Alemania ha aumentado de forma continuada su presencia exterior desde mediados de los 90, tras su reunificación y la caída del bloque soviético. Se encuentra entre las cinco primeras posiciones en todas las variables económicas, con la única excepción de la de energía. Ocupa la 3ª posición en el ranking de presencia global, tras Estados Unidos y China, y por delante de Reino Unido.</p>
<p>Alemania ocupa el primer puesto en la clasificación del Índice Elcano de Presencia Europea lo que significa que es, de todos los estados miembros, el que tiene mayor proyección dentro de la UE. Es el resultado de ocupar el 1er puesto en manufacturas y tecnología y el 2º en bienes primarios, inversiones, migraciones, cultura, información, ciencia o educación. En definitiva, a diferencia de lo que ocurre en el conjunto de su proyección exterior, la presencia de Alemania en la Unión es, sobre todo, blanda (58,7% de su presencia europea).</p>'
WHERE code='DE' AND language='es';

UPDATE iepg_data_redux.iepg_comment
SET comment='<p>Since the mid-1990s and following its reunification and the fall of the Soviet Union, Germany has recorded a steady growth in its external presence, on the basis of its economic dimension -that provides 68.7% of its global presence-. It is ranked among the five top positions in all economic variables; except energy. It is 3rd in the global presence ranking, after the US and China and before the United Kingdom.</p>
<p>Germany is ranked 1st in the Elcano European Presence Index, which means that, among all member states, it is the one with the highest projection within the EU. This is the result of being 1st in manufactures and technology and 2nd in primary goods, investments, migrations, culture, information, science or education. That is, unlike what happens with its total external projection, Germany’s presence in the Union is, mostly, soft (58.7% of its European presence).</p>'
WHERE code='DE' AND language='en';

-- Canada
UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Canadá ocupa en 2019 el 8º puesto del ranking de presencia global, a pesar del auge de China y de la reducción relativa de su peso económico en el mundo –pierde cuatro puestos en la clasificación mundial de PIB desde 1990–.</p>
  <p>Mantiene un perfil de presencia fundamentalmente económico –74,1% de su presencia global en 2019– vía sus inversiones en el exterior, los bienes primarios o la energía, dada su condición de cuarto productor de gas y petróleo a nivel mundial.</p>
  <p>En su dimensión blanda, poco relevante en su proyección exterior, se proyecta vía migraciones, cultura, ciencia y educación.</p>'
  WHERE code='CA' AND language='es';

UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Canada is 8th in the global presence ranking; a position that it still holds despite the rise of China and despite its loss of economic weight –down four positions since 1990 in the GDP ranking–.</p>
  <p>It maintains a strong economic profile –74.1% of its global presence in 2019– via its investments abroad and its exports of primary goods or energy, given that it is the 4th largest gas and oil exporter.</p>
  <p>Its soft dimension, which is less determinant, is grounded in migrations, culture, science and education.</p>'
  WHERE code='CA' AND language='en';


-- China
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>El notable ascenso del gigante asiático en las últimas décadas tiene su reflejo en la clasificación del Índice Elcano de Presencia Global, donde escala diez posiciones desde 1990. Este crecimiento se debe en buena medida a la dimensión económica, donde se impulsa del 17º lugar en 1990 al 2º en 2019. A su vez, esto tiene su origen en el crecimiento de sus exportaciones manufactureras, pero también de bienes primarios, servicios e inversiones. Por ello, la naturaleza de su presencia global es principalmente económica, con un peso del 62,6% sobre el valor índice en 2019.</p>
 <p>Sin embargo, en los últimos años se producen aumentos sustanciales de presencia blanda, con un valor en 2019 que es 25 veces mayor que en 1990. Esto se explica con el comportamiento de indicadores como información, tecnología o ciencia, e incluso turismo o deportes.</p>
 <p>Con todo ello, su cuota de presencia pasa de 1,7% en 1990 a 8,0% en 2019, lejos de la de Estados Unidos pero ya superior a las de Francia, Reino Unido y Alemania.</p>'
 WHERE code='CN' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>China’s remarkable rise in recent decades is reflected in its classification in the Elcano Global Presence Index, where it has upscaled ten positions since 1990. This is mainly due to its economic presence, where it is now ranked 2nd (17th in 1990). This trend is driven by the export of manufactures, but also by primary goods, services and investments. Hence, the nature of its global presence is mainly economic, accounting for 62.6% of its index value in 2019.</p>
 <p>However, more recently China has also substantially increased its soft presence, with a record 25 times higher than in 1990; pushed by the increase in indicators such as information, technology or science, and even tourism or sports.</p>
 <p>As a result, its presence quota has gone up from 1.7% in 1990 to 8.0% in 2019. Although still far from the USA, China has overtaken France, the United Kingdom and Germany.</p>'
 WHERE code='CN' AND language='en';

-- Japan
 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Japón ocupa el 5º lugar en la clasificación de presencia global. A pesar de mantenerse como la 3ª economía mundial, las consecuencias de la crisis de los noventa aún se reflejan en su presencia económica, en la que pasa de ocupar el 3er puesto en 1990, al 5º en 2019. Así, se recupera desde la 7ª posición en 2010 gracias, en buena medida, a las inversiones (que superan las de Francia o Alemania).</p>
  <p>También aumenta la dimensión militar que, a pesar de la desmilitarización tras la Segunda Guerra Mundial, contribuye crecientemente a la presencia japonesa –17,5% en 2019–; más que en otras economías desarrolladas.</p>
  <p>Aumenta su presencia blanda tanto en términos absolutos como relativos, aunque no lo suficiente para mantener la 3ª posición que ocupaba en 1990, situándose hoy en la 5ª, con cerca de 520 puntos. En este ámbito, sus principales fortalezas están en la tecnología, la ciencia y la cooperación al desarrollo.</p>'
  WHERE code='JP' AND language='es';

 UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Japan is 5th in the global presence ranking. Despite being the 3rd world economy, the consequences of the nineties’ crisis still show in its economic presence records, where it has lost two positions since 1990. However, it is now ranked 5th, up from the 7th position in 2010; something which is mainly due to its performance in investments, where it has surpassed both Germany and France.</p>
  <p>The military dimension also grows –up to a contribution of 17.5% in 2019– and is higher than in other developed countries, despite the demilitarization following the World War II.</p>
  <p>The soft dimension increases both in absolute and relative terms, although not enough to maintain the 3rd position that it occupied in 1990. Japan is now ranked 5th, with almost 520 index value points. In this field, its main strengths are in technology, science and development cooperation.</p>'
  WHERE code='JP' AND language='en';

-- Rusia
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>La presencia global de la Unión Soviética cae fuertemente con la desintegración del bloque, al finalizar la Guerra Fría, y el desplome de su presencia militar, que en aquel momento era del 88,5% de su presencia total. Pese a ello, Rusia no pierde en ningún momento el 2º puesto en el ranking de presencia militar.</p>
 <p>La recuperación de su presencia global se sustenta en su dimensión económica y, concretamente, en la variable de energía; siendo el primer exportador mundial de gas y el segundo de petróleo.</p>
 <p>La dimensión blanda no es tan relevante, aunque el país destaque en deportes (debido a su éxito en el medallero olímpico), información o migraciones.<br>Con todo ello, Rusia se sitúa hoy en la 7ª posición por presencia global, frente a la 2ª en 1990.</p>'
 WHERE code='RU' AND language='es';

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>The Soviet Union’s external projection dramatically fell with the disintegration of the bloc, at the end of the Cold War, and the subsequent drop of its military presence; that accounted for 88.5% of its total presence in 1990. In spite of this, Russia never loses the 2nd position in the military presence ranking.</p>
 <p>The recovery of its global presence is grounded in its economic dimension and, more specifically, the energy variable; being Russia the world top exporter of gas and the second exporter of oil.</p>
 <p>The soft dimension is not particularly relevant. Although, the country outstands in sports (due to its performance in the Olympic Games), information or migrations.<br>All in all, Russia is now 7th in global presence, down from the 2nd position in 1990. </p>'
 WHERE code='RU' AND language='en';


-- European Union
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>Si considerásemos a la Unión Europea un único país, tendría en 2019 un registro similar al de Estados Unidos. Obtendría el mayor valor de presencia económica –con relevancia de la inversión en el exterior y las exportaciones de servicios– y un registro similar de presencia blanda –turismo, deportes y cooperación al desarrollo–, siendo superado por Estados Unidos tan sólo en la clasificación de presencia militar.</p><p>La crisis económica, con especial impacto dentro del espacio comunitario, ha condicionado la presencia de la Unión Europea en el resto del mundo. Por un lado, dentro de la dimensión económica, registra una pérdida de presencia hasta 2013, fundamentalmente debida al descenso de exportaciones de bienes y de inversión en el exterior –en parte consecuencia la depreciación del euro frente a otras monedas–. Por otro lado, se da una ralentización del crecimiento de su presencia blanda, afectada entre otras cosas por la reducción los flujos de cooperación internacional, así como al número de inmigrantes recibidos.</p><p>No obstante, en los últimos años se produce una recuperación en la evolución de dichas variables. Tanto la Unión Europea como Estados Unidos mantienen unos elevados niveles de presencia global, que les sitúa por el momento a mucha distancia de China, que ocuparía el tercer lugar.</p>'
 WHERE code='XBEU' AND language='es';

UPDATE iepg_data_redux.iepg_comment
SET comment='<p>If the European Union were to be considered a single country, it would have a similar record to that of the United States. The European Union would have the greatest value of economic presence –with relevance of foreign investment and exports of services– and also a similar record of soft presence –tourism, sports or development cooperation–, being surpassed by the United States only in the classification of military presence.</P>
<p>The economic crisis, which has especially hit the European Union, has had an impact on its presence in the rest of the world. On the one hand, within the economic dimension, there is a loss of presence until 2013, mainly due to the decline in exports of goods and foreign investment –in part due to the depreciation of the euro against other currencies–.</p>
<p>On the other hand, there is a slowdown in the growth of its soft presence, affected among other things by the reduction of international cooperation flows, as well as the number of immigrants received.</p>
<p>However, in recent years there has been a recovery in the evolution of these variables. Both the European Union and the United States maintain high levels of global presence, which locates them still far from China, which would occupy the 3rd place.</p>'
WHERE code='XBEU' AND language='en';

-- Asia Pacif.
UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Asia y Pacífico se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p>
  <p>Los países que forman parte de él son Australia, Bangladesh, Camboya, China, Filipinas, India, Indonesia, Japón, Laos, Malasia, Nueva Zelanda, Pakistán, Corea del Sur, Singapur, Tailandia, Vietnam, Myanmar, Nepal, Sri Lanka, Kazajistán, Turkmenistán y Uzbekistán. Representan el 99,7% y el 98,6% del PIB y de la población de la región, respectivamente (según datos de 2018 del Banco Mundial).</p>'
  WHERE code='XBAP' AND language='es';

UPDATE iepg_data_redux.iepg_comment
  SET comment='<p>Asia-Pacific is constituted by the countries in the region for which their global presence has been calculated. The global presence of the bloc is obtained by the pure sum of the global presence of each country that makes up the bloc.</p>
  <p>The countries comprising the bloc are Australia, Bangladesh, Cambodia, China, India, Indonesia, Japan, Laos, Malaysia, Nepal, New Zealand, Pakistan, the Philippines, South Korea, Singapore, Sri Lanka, Thailand, Vietnam, Myanmar, Kazakhstan, Turkmenistan and Uzbekistan. They account for 99.7% and 98.6% of the region’s GDP and population, respectively (according to World Bank data for 2018).</p>'
  WHERE code='XBAP' AND language='en';

-- Africa Sub.
UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>África Subsahariana se compone de los países de esta región para los que existe cálculo de presencia global, esto es: Angola, Botsuana, Burkina Faso, Camerún, Costa de Marfil, Etiopía, Gabón, Ghana, Guinea Ecuatorial, Kenia, Madagascar, Mali, Mauricio, Mozambique, Namibia, Nigeria, República Democrática del Congo, Senegal, Sudáfrica, Sudán, Tanzania, Uganda, Zambia y Zimbabue. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país. Los países considerados representan un 93,9% del PIB regional y un 85,2% de su población (según datos de 2018 del Banco Mundial).</p>'
   WHERE code='XBSA' AND language='es';

-- USA
UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>US tops the Elcano Global Presence Index in all years. In 2019, it also leads the ranking in all variables, with the exception of energy, manufactures and tourism. Of all 130 countries, it records the highest share of presence in all dimensions: 18.8% in the economic domain, 28.3% in the military and 22.4% in soft presence. Moreover, unlike other developed countries, its military dimension strongly defines its index value, with a contribution at 25.4% in 2019.</p>
 <p>Despite its hegemony, the USA loses relative global presence when compared with other countries: from a 24.8% share of global presence in 1990 to 21.5% in 2019. In a period of emergence of new global players, several economies (particularly oil producers or Asian countries) reap gains of share that reduce the American role.</p>'
 WHERE code='US' AND language='en';

  -- Magreb and ME.
  UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>The Maghreb and the Middle East are made up of the countries forming the region whose global presence has been calculated. The bloc’s global presence is the result of the pure sum of the global presence of each country comprising it. The countries considered are Afghanistan, Algeria, Bahrein, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Libya, Lebanon, Morocco, Oman, Syria, Tunisia, the United Arab Emirates, Qatar and Yemen. They account for 98.5% of the region’s GDP and 98.9% of its population (according to World Bank data for 2018).</p>'
   WHERE code='XBMM' AND language='en';


COMMIT;
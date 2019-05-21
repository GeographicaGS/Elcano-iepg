
/*
  Update country comments.
*/


BEGIN;

  UPDATE iepg_data_redux.iepg_comment
   SET date_in = '2013-01-01'
   WHERE code='IN' AND language='es';

  UPDATE iepg_data_redux.iepg_comment
   SET date_in = '2013-01-01'
   WHERE code='IN' AND language='en';


   -- UK
   UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>La presencia global de Reino Unido aumenta constantemente desde 1990, lo que sitúa al país en la segunda posición del ranking entre 2000 y 2012; año en el que cede este puesto a China. Desde entonces, y a pesar de la ralentización de su proyección exterior, fruto de la crisis, mantuvo la tercera posición hasta 2018, cuando es adelantado por Alemania.</p><p>La proyección de Reino Unido hacia el resto del mundo destaca por el elevado peso de la dimensión blanda, ocupando los primeros puestos en todos los indicadores de esta dimensión y siendo el país europeo con mayor presencia blanda en el mundo. El Reino Unido destaca además en algunos indicadores de presencia económica, particularmente en las exportaciones de servicios y en la inversión –téngase en cuenta la importancia de los servicios bancarios, seguros, consultoría y asesoría, así como su función de <i>hub</i> financiero–.</p><p>Dentro del espacio comunitario, en 2018, Reino Unido mantiene la segunda posición del ranking de presencia europea, que calcula la proyección exterior en el espacio europeo. La brecha respecto a Alemania, primero en esta clasificación, persiste, mientras que Francia se mantiene todavía lejos: Reino Unido registró en 2018 una valor de presencia europea de 607 puntos, frente a los 770 de Alemania y los 431 de Francia. Esto podría ser signo del fortalecimiento de relaciones económicas extracomunitarias del Reino Unido en un contexto de menor crecimiento en Europa. En este contexto europeo, el perfil blando de la proyección exterior británica es aún mayor (73% de la presencia europea de Reino Unido se explica con su dimensión blanda).</p>'
   WHERE code='GB' AND language='es';

   -- European Union
   UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>If the European Union were to be considered a single country, it would occupy the first place in the Global Presence ranking in 2018, with a record similar to that of the United States.
   The European Union would have the greatest value of economic presence –with relevance of foreign investment and exports of services– and also the greatest record of soft presence –tourism, sports or development cooperation–, being surpassed by the United States only in the classification of military presence.</p><p>The economic crisis, which has especially hit the European Union, has had an impact on its presence in the rest of the world. On the one hand, within the economic dimension, there is a trend of loss of presence until 2013, mainly due to the decline in exports of manufactures and foreign investment –in part due to the depreciation of the euro against other currencies–.</p><p>On the other hand, there is a slowdown in the growth of its soft presence, affected among other things by the reduction of international cooperation flows, as well as the number of immigrants received.</p>
   <p>However, both the European Union and the United States maintain high levels of global presence, which locates them still far from China, which would occupy the 3rd place.</p>'
   WHERE code='XBEU' AND language='en';

   -- Germany
   UPDATE iepg_data_redux.iepg_comment
   SET comment='<p>Desde mediados de los 90, tras la reunificación y la caída del bloque soviético, Alemania registró un aumento continuado de presencia exterior, apoyada fundamentalmente en su proyección económica, que aporta más del 69% de su presencia global, y en donde, a excepción de las exportaciones energéticas, ocupa un lugar muy destacado en todas las variables a nivel mundial (entre las cinco primeras posiciones). La recuperación en los últimos años del ritmo de crecimiento de su presencia global le ha permitido superar a Reino Unido, y situarse en la tercera posición de la clasificación mundial por detrás de China y Estados Unidos. Una posición que había perdido desde 2013, consecuencia del impacto de la crisis en el territorio europeo, y por tanto en la proyección económica de Alemania.</p><p>Dentro de la Unión Europea, Alemania mantiene su hegemonía a pesar de la contracción de la demanda de los socios comunitarios, con descensos de las exportaciones de manufacturas alemanas con destino al mercado europeo. La presencia alemana en Europa tiene un carácter fundamentalmente económico, destacando el <i>stock</i> de inversión y las exportaciones de manufacturas y bienes primarios.</p>'
   WHERE code='DE' AND language='es';

   -- Japan
   UPDATE iepg_data_redux.iepg_comment
    SET comment='<p>Japón ocupa el 5º lugar en la clasificación de presencia global, adelantando dos posiciones con respecto a 2013, a pesar del letargo económico tras la crisis de los 90. Aun manteniendo el tercer PIB más elevado a nivel mundial, en términos de proyección exterior, la economía nipona ha sufrido una importante pérdida de relevancia económica, pasando de ocupar el tercer puesto en esta dimensión en 1990, al quinto en 2018.</p><p>No obstante, en los tres últimos años, Japón recupera presencia en el resto del mundo, debido a su proyección económica –donde destaca el <i>stock</i> de inversión en el exterior– hasta adelantar a Francia en esta dimensión. También aumenta la dimensión militar, que a pesar de la desmilitarización tras la Segunda Guerra Mundial, contribuye crecientemente a la presencia japonesa –21,3% en 2018– y más que en otras economías desarrolladas.</p><p>Cae la presencia blanda tanto en términos absolutos como relativos –en 1990 registraba 521 puntos, 37% de su proyección exterior ese año; en 2018, 373 puntos y 22% de su proyección exterior– aunque se mantenga en niveles elevados –5º puesto mundial en esta dimensión en 2018, sustentados en las variables de tecnología, ciencia y cooperación al desarrollo–.</p>'
    WHERE code='JP' AND language='es';

    -- Canada
    UPDATE iepg_data_redux.iepg_comment
     SET comment='<p>Canadá ocupa en 2018 el 8º puesto del ranking de presencia global, manteniéndose en los principales puestos a pesar de la reducción relativa de su peso económico en el mundo –pierde cuatro puestos en la clasificación mundial de PIB desde 1990– y del auge de China.</p><p>Mantiene un perfil de presencia fundamentalmente económico –74% de su presencia global en 2018– con protagonismo de las inversiones en el exterior, pero con contribuciones relevantes de otros indicadores como bienes primarios o energía, dada su condición de cuarto productor de gas y petróleo a nivel mundial.</p><p>Aunque la dimensión blanda es menos relevante en su proyección exterior, ocupa posiciones elevadas en cultura (3ª posición), educación, ciencia y migraciones (7ª posición).</p>'
     WHERE code='CA' AND language='es';

    UPDATE iepg_data_redux.iepg_comment
     SET comment='<p>Canada occupies the 8th place in the global presence ranking in 2018, remaining in the main positions despite its loss of economic weight –down four positions since 1990 in the GDP ranking– and despite the rise of China.</p><p>It maintains a strong economic profile –74% of its global presence in 2018– with a leading role in foreign investments abroad, and also with relevant contributions from other indicators such as primary goods or energy, given its condition of 4th largest gas and oil producer.</p><p>Although the soft dimension is less determinant, Canada occupies high positions in some indicators of this dimension, such as culture (3rd position worldwide), education, science and migration (7th).</p>'
     WHERE code='CA' AND language='en';

COMMIT;

-- Costa Rica
 INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Costa Rica' and gn.id_name_family=2));

-- Dominican Republic
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Dominican Republic' and gn.id_name_family=2));

-- Guatemala
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Guatemala' and gn.id_name_family=2));

-- Uruguay
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Latin America' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Uruguay' and gn.id_name_family=2));

-- Ethiopia
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Ethiopia' and gn.id_name_family=2));

-- Kenya
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Kenya' and gn.id_name_family=2));

-- Tanzania
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Subsaharian Africa' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Tanzania' and gn.id_name_family=2));

-- Uzbekistan
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Uzbekistan' and gn.id_name_family=2));

-- Turkmenistan
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Turkmenistan' and gn.id_name_family=2));

--Myanmar
INSERT INTO maplex.block (id_geoentity_block,id_geoentity_child) VALUES (
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2),
 (select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Myanmar' and gn.id_name_family=2));


update maplex.name set name='Uruguay' where name='Uriguay';
Update short_name_es_order='Uruguay',short_name_es1='Uruguay' from iepg_data_redux.master_country where short_name_es_order='Uriguay';

-- Move Kazakhstan to Europe
update maplex.block set id_geoentity_block=(select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
INNER JOIN maplex.name n ON gn.id_name=n.id_name
 where n.name='Asia & Pacific' and gn.id_name_family=2)

WHERE 
id_geoentity_block=(select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
  INNER JOIN maplex.name n ON gn.id_name=n.id_name
   where n.name='Europe' and gn.id_name_family=2)

and 
id_geoentity_child=(select gn.id_geoentity as id_geoentity_xbap from maplex.geoentity_name gn
  INNER JOIN maplex.name n ON gn.id_name=n.id_name
   where n.name='Kazakhstan' and gn.id_name_family=2);



update maplex.name set name='Maghreb & Middle East' where name='Magreb & Middle East';
update maplex.name set name='Subsaharan Africa' where name='Subsaharian Africa';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Desde la caída del bloque soviético, la supremacía estadounidense tiene su 

visibilidad en distintas esferas del Índice de Presencia Global. En primer lugar, 

Estados Unidos ocupa el primer puesto de la clasificación en todos los años para 

los que se calcula y en todas las variables que lo componen, a excepción de las 

exportaciones de energías y de bienes manufacturados y del turismo. En segundo 

lugar, registra las mayores cuotas de presencia en todas las dimensiones –11,4 % 

en la económica; 46% en la militar; y 15,5% en la blanda–. Por otro lado, a 

diferencia del resto de países desarrollados, la dimensión militar mantiene una 

elevada contribución al valor del Índice –13% en 2015–. Además, en línea con su 

papel protagonista en el desarrollo de la globalización, es el país que mayores 

incrementos registra en términos absolutos desde 1990.</p><p>Sin embargo, y al tiempo que mantiene su hegemonía, registra una tendencia de

pérdida de presencia en términos relativos, o en comparación con el resto de 

países, –23,2% de cuota en 1990 frente a un 14,3% en 2015–. En un periodo de 

surgimiento de nuevos actores globales, diversas economías emergentes cosechan 

ganancias de cuota que reducen el protagonismo estadounidense, donde destaca el 

auge de países petroleros y asiáticos. Sin embargo, la desaceleración del proceso 

de globalización en los últimos años ha producido una ligera reconcentración de la 

presencia global, permitiendo a EEUU mantener su cuota de presencia en los 

últimos años.</p><p>Esta tendencia se debe fundamentalmente a la dimensión económica del Índice,

donde a pesar de ser el principal motor de la globalización, y por tanto la 

dimensión en la que Estados Unidos registra mayores aumentos de presencia 

–especialmente en las exportaciones de bienes primarios, servicios y stock de 

inversión–, reduce su cuota en casi cuatro puntos porcentuales desde 1990. La 

recuperación desde entonces de su cuota económica ha permitido compensar las 

pérdidas en la dimensión blanda. Al mismo tiempo, la tendencia general a la 

desmilitarización de la presencia de los países en el mundo permite a Estados 

Unidos mantener su hegemonía militar a pesar de la reducción del número de 

unidades desplegadas.</p>' WHERE code='US' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>La evolución de la presencia global de Rusia puede dividirse en dos periodos. El primero, que abarcaría la década de los 90, caracterizado por una drástica reducción del valor del Índice tras la caída del bloque soviético, con un sustancial descenso de presencia militar, y en menor medida, en la blanda. Así, en 1990 la

dimensión militar sostenía de manera abrumadora la presencia global de la entonces Unión Soviética, con un peso del 78% del valor total. En el segundo periodo, a partir del año 2000, comienza un proceso de recuperación de presencia en el mundo apoyado principalmente en su dimensión económica que, sin embargo, no le permite alcanzar los mismos niveles que obtenía durante la época soviética hasta 2012. Su condición de primer exportador de gas y segundo de petróleo a nivel mundial hace que sean las exportaciones de bienes energéticos la causa principal de dicho aumento, aportando un 47,9% al valor de su Índice en 2015. También ha influido el crecimiento de las exportaciones de bienes primarios y, ya más recientemente, los servicios y el stock de inversión. Si bien ha registrado aumentos en presencia blanda, han sido mucho menores que los de otras potencias mundiales, ocupando todavía posiciones muy bajas en todas las variables a excepción de deportes, dados sus buenos resultados en el medallero olímpico, y migraciones, siendo el segundo país receptor a nivel mundial.</p>' WHERE code='RU' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>El notable ascenso del gigante asiático en las últimas décadas tiene su reflejo en la clasificación del Índice de Presencia Global, donde escala diez posiciones desde 1990. Este crecimiento se da en paralelo al registrado en términos de PIB, otorgando el protagonismo del auge chino a la dimensión económica –en 1990 ocupaba el 17º lugar frente al 2º en 2015 en el ranking de presencia económica–, impulsado por el crecimiento de las exportaciones manufactureras, pero también de bienes primarios y servicios. Por ello, la naturaleza de su presencia global es principalmente económica, con un peso del 65,1% sobre el valor índice en 2015. Sin embargo, registra también recientes mejoras sustanciales en variables de la dimensión blanda –en turismo, deportes y ciencia–, mostrando una posible tendencia de modificación de las bases de su presencia, a la vez que consolida su posición global. Esta consolidación se evidencia con el incremento de cuota de presencia –un 5,4% en 2015 frente al 1,7% de 1990– que, si bien se sitúa todavía lejos de los registros estadounidenses, le ha permitido adelantar a las potencias europeas, Francia, Reino Unido y Alemania, y situarse en el segundo puesto del ranking de presencia global.</p>' WHERE code='CN' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Japón ocupa el 7º lugar en la clasificación, a pesar del letargo económico tras la crisis de los 90 que le ha hecho registrar, por lo general, menores tasas de crecimiento de presencia que países que le acompañan en los principales puestos. A pesar de mantener el noveno PIB más elevado a nivel mundial, en términos de presencia, la economía nipona ha sufrido una importante pérdida de relevancia

económica, pasando de ocupar el 5º puesto en esta dimensión en 1990, al 12º en 2014. En 2015 ocupa el 11º puesto, apenas recuperando una posición respecto del año anterior; se observa lo mismo en términos de cuota de presencia económica, que asciende hoy a 2,7%. No obstante, mantiene elevados registros de presencia blanda –6º puesto mundial en esta dimensión en 2015–, sustentados en las variables de tecnología, ciencia y cooperación al desarrollo. Cabe añadir que, a pesar de la desmilitarización sufrida tras la Segunda Guerra Mundial, la dimensión militar mantiene una contribución estable a la presencia japonesa –4,2% en 2015– y superior a otras economías desarrolladas. En 2015 registra un leve crecimiento de presencia global, principalmente apoyado en su dimensión blanda y en la tenue recuperación de su presencia económica. Estos resultados agudizan la tendencia de pérdida de cuota global que venía registrando el país desde 1990 –del 4,3% de entonces al 3,2% de 2015, habiendo alcanzado un 5,2%, su punto más elevado, en 1995–.</p>' WHERE code='JP' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Canadá se mantiene en los principales puestos de la clasificación del Índice de Presencia Global, a pesar de la reducción relativa de su peso económico –pierde cinco puestos en la clasificación mundial de PIB desde 1990- y del auge de China, que le hace descender una posición en presencia global. Tercer productor de gas a nivel mundial y quinto de petróleo (según la EIA, 2014), las exportaciones de bienes energéticos constituyen la principal contribución a la presencia global canadiense –25,4% de la presencia de 2015–. Además, posee un sector agrícola altamente tecnificado que le ha permitido incrementar también las exportaciones de bienes primarios –17,2% de la presencia de 2015–. Por este motivo la presencia de Canadá es fundamentalmente económica –63,6% de su presencia–, aunque mantiene, como otras economías desarrolladas, elevados registros en la dimensión blanda y casi nulos en la militar.</p>' WHERE code='CA' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>España ha registrado un notable aumento de su presencia global desde 1990, apoyado en el crecimiento de su dimensión económica. No obstante, la naturaleza de dicha presencia es mayoritariamente blanda y, dentro de ésta, de menor valor añadido –con protagonismo de las variables de turismo o deportes– e información. Ocurre lo mismo con la dimensión económica –destacando las exportaciones de bienes primarios y servicios–. A pesar de ese aumento en términos absolutos, se enfrenta a una reciente pérdida de presencia relativa, cediendo cuotas de presencia desde 2010 a favor otros países emergentes, si bien con una ligera recuperación en 2015. Más aún, en 2013 se reduce por primera vez el valor del

Índice de España, evidenciando el impacto de la crisis en términos de presencia global. En 2015, sigue la tendencia de recuperación del crecimiento de presencia iniciada el año precedente, tanto en su dimensión económica como en la blanda.</p><p>Si atendemos sólo a lo ocurrido dentro de la Unión Europea, España también gana cuota de presencia hasta 2010, pero en este caso empujada por el mayor dinamismo de la dimensión blanda –migraciones e información- que cobra cada vez más protagonismo frente a la económica. El crecimiento en estas variables es menor que el registrado por los principales socios comunitarios, reduciéndose la aportación de la dimensión económica a la presencia española en Europa. En 2015 España registra una pérdida de presencia europea en términos absolutos, motivada por el descenso de la presencia económica, uniéndose a una tendencia registrada por varios socios comunitarios.</p>' WHERE code='ES' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>A pesar del crecimiento de presencia respecto del año anterior, Alemania se mantiene en la tercera posición del ranking, a la que quedó relegada en 2014, siendo superado en presencia global por China. Desde mediados de los 90, tras la reunificación y la caída del bloque soviético, Alemania registró un aumento continuado de presencia económica, dimensión que más valor le aporta y donde, a excepción de las exportaciones energéticas, ocupa lugar destacado en todas las variables a nivel mundial. Sin embargo, el descenso de presencia registrado en 2013 y el modesto crecimiento de los últimos años, no le han permitido mantener una segunda posición que ocupaba desde el año 2000.</p><p>Dentro de la Unión Europea, Alemania mantiene su hegemonía. A pesar de la contracción de la demanda de los socios comunitarios, con descensos de las exportaciones de manufacturas con destino al mercado europeo, la presencia europea alemana tiene un carácter fundamentalmente económico, destacando el stock de inversión y las exportaciones de manufacturas y servicios. No obstante, en 2015 registra por primera vez una pérdida en términos absolutos de presencia económica dentro de la UE. Dentro de la dimensión blanda, la presencia alemana se caracteriza por apoyarse en pilares sólidos, como las variables de información, tecnología y ciencia.</p>' WHERE code='DE' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>La presencia global de Reino Unido ha registrado un constante aumento desde 1990, lo que le ha permitido ascender posiciones en la clasificación, superando a Francia y a Japón. Sin embargo, en 2015, la presencia global británica decrece en términos absolutos y el país queda relegado al cuarto puesto mundial, por detrás de Alemania, a quien adelantó en 2014, y de China, que pasa a ocupar la segunda posición.</p><p>Se trata de una presencia principalmente blanda –donde destacan los valores alcanzados en información y educación–, siendo el país europeo con mayor presencia en esta dimensión, lo que le ha permitido mantener su cuota global a pesar del ascenso de países emergentes. La posición relativa internacional de Reino Unido se sostiene, además, en las exportaciones de servicios e inversión –téngase en cuenta la importancia de los servicios bancarios, seguros, consultoría y asesoría, así como su función de hub financiero-. El decrecimiento del valor absoluto y relativo al que asiste Reino Unido en 2015 responde a la moderación de los valores económicos y globales tras su extraordinario crecimiento en 2014, cuando el incremento puntual de las ventas de oro provocó un fuerte crecimiento en las exportaciones de bienes primarios.</p><p>Dentro del espacio comunitario, Reino Unido mantiene la segunda posición en 2015 y se recupera de la caída de su valor absoluto de presencia europea de 2014. No obstante, la brecha respecto a Alemania persiste, mientras que Francia se mantiene todavía lejos. Esto podría ser signo del fortalecimiento de relaciones extracomunitarias del Reino Unido en un contexto de menor crecimiento en Europa. Además, mantiene una tendencia de reducción de presencia económica a favor de la dimensión blanda –donde tienen protagonismo los deportes, información y cultura, y también, aunque perdiendo relevancia, la ciencia y la educación–, siendo en 2015 el país con mayor presencia blanda en la región.</p>' WHERE code='GB' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>A pesar del aumento continuado de presencia global, Francia se enfrenta a una pérdida progresiva de relevancia en la escena internacional. Ello se refleja en el descenso de su cuota de presencia y en la pérdida de posiciones en la clasificación –en 1995 ocupaba el segundo lugar y en 2015 se halla en el sexto– siendo sobrepasado por Rusia y Reino Unido. Mantiene un perfil similar al de otras economías europeas, esto es, elevados registros de presencia blanda –primera potencia turística a nivel mundial, además de cooperación al desarrollo, educación e información–; al mismo tiempo, su dimensión económica crece, aunque en menor cuantía y con ciertas variaciones, debidas en parte a la crisis que atraviesa la región.</p><p>En términos europeos, se sitúa como la tercera economía con mayor presencia dentro del espacio comunitario, pero con un perfil contrario al constatado en términos globales. Las variables económicas tienen mayor relevancia –donde destacan también las exportaciones de servicios y el stock de inversión–, pero el aumento de presencia ha estado sostenido por la dimensión blanda –especialmente en información, cultura y turismo-.</p>' WHERE code='FR' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>A pesar del paulatino descenso de los Países Bajos en la clasificación mundial según Producto Interior Bruto, el país se mantiene en puestos elevados del Índice de Presencia Global. Se trata de una presencia de naturaleza fundamentalmente económica –esta dimensión representa en 2015 el 76,5% de su presencia global–. Es el cuarto exportador mundial de bienes primarios y el principal exportador europeo de energía, donde a su condición de principal productor europeo y poseedor de importantes yacimientos de gas, se le une la posición estratégica del puerto de Rotterdam. Así, buena parte de su elevado registro puede explicarse por su condición de hub exportador.</p><p>Al igual que otras economías europeas, la crisis ha tenido incidencia negativa en muchas variables, y en la economía neerlandesa dada su condición de exportador energético se añade el impacto del descenso de los precios del petróleo en la reducción del valor de sus exportaciones.</p><p>Este perfil se repite en el análisis de su presencia dentro del espacio europeo, donde se ubica con el segundo mayor valor en presencia económica tras Alemania, aunque con escasa relevancia en la dimensión blanda. Sin embargo, los Países Bajos registran en 2015 una nueva pérdida de presencia en Europa, que devuelve su valor índice al del año 2013, debido fundamentalmente a la dimensión económica.</p>' WHERE code='NL' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Si considerásemos a la Unión Europea un único país, ocuparía el primer puesto en la clasificación de Presencia Global, superando a Estados Unidos. Obtendría los mayores registros en las dimensiones económica y blanda. Tan sólo en la dimensión militar se mantendría la hegemonía estadounidense. La naturaleza de la presencia de la Unión Europea es mayoritariamente blanda, con protagonismo mundial en turismo, deportes y ciencia, pero también en tecnología, educación y cooperación al desarrollo. No obstante, el crecimiento de presencia desde 2005 se apoya en su dimensión económica, a lo que ha contribuido el fortalecimiento del euro como divisa internacional.</p><p>La crisis económica, con especial impacto dentro del espacio comunitario, ha condicionado la presencia de la Unión Europea. Por un lado, ha afectado a los flujos de cooperación internacional, así como al número de inmigrantes recibidos. Por otro lado, desciende su presencia económica, tanto en términos absolutos como en términos relativos, consecuencia la depreciación del euro frente a otras monedas. Así, la Unión Europea registra en 2015 descensos absolutos de presencia global.</p>' WHERE code='XBEU' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>A pesar de perder progresivamente posiciones tanto en términos de cuota de presencia global como de PIB, Italia se mantiene, desde 2013, en el 11º puesto del ranking. Esta tendencia se debe a la ralentización del crecimiento de su presencia económica, dimensión en la que ocupa el 16º puesto a nivel mundial frente al 8º de 1990. No obstante, continúa siendo uno de los ocho países más industrializados, por lo que la presencia italiana es fundamentalmente económica, apoyada en las exportaciones de manufacturas –séptimo exportador mundial–, bienes primarios e inversión. Al igual que ocurre con otras potencias europeas, mantiene registros elevados en la dimensión blanda –apoyada en turismo e información– donde el descenso de los flujos de cooperación internacional ha contribuido a la inédita reducción del valor del índice en términos absolutos en 2013. En 2015, la recuperación iniciada en 2014, tanto dentro de la dimensión blanda como económica, le permiten registrar tímidos incrementos de presencia global.</p><p>Por el contrario, dentro del espacio europeo su presencia es fundamentalmente blanda –apoyada en turismo, deportes e información– y ha sido precisamente esta dimensión la que mayores crecimientos ha registrado. No obstante, son insuficientes para mantener su posición frente a España, por lo que desciende a la sexta posición en términos de presencia europea principalmente por su descenso de presencia económica. La caída, en 2014, de su valor absoluto de presencia europea parece revertirse en 2015, pero es insuficiente para subir de posición en el orden europeo.</p>' WHERE code='IT' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>El ascenso internacional de Arabia Saudí, que ocupa hoy el 10º puesto en el ranking de presencia global, empieza fundamentalmente a partir de 2000, cuando su valor absoluto de presencia sigue una tendencia alcista de la mano de su presencia económica. Siendo el mayor productor de petróleo del mundo y segundo exportador mundial, la evolución de la presencia global de Arabia Saudí está muy condicionada por la coyuntura del mercado internacional de energías, que en los últimos años ha sido favorable para los grandes exportadores de petróleo y de gas.</p><p>En 2015 la presencia económica de este país, la 9º más importante en el Índice, contribuye en un 72,2% al conjunto de su presencia global, y las exportaciones de energía un 67,5%. Esta composición, concentrada en las energías, se ha mantenido constante a lo largo de la serie, a pesar de las recientes turbulencias petroleras. Precisamente por la reciente evolución de los precios del petróleo, Arabia Saudí registra una pérdida de presencia económica, compensada sin embargo por los aumentos de presencia blanda.</p><p>A pesar de su orientación petrolera, la dimensión blanda es un componente importante en la presencia global saudí. Aporta, en 2015, un 26,7% al conjunto de la presencia global, destacando en ella migraciones y cooperación al desarrollo, cuestión en la que Arabia Saudí ocupa la quinta posición mundial, y cuyos incrementos le han permitido mantener posiciones en el ranking de presencia global, a diferencia de otros países petroleros.</p>' WHERE code='SA' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>América Latina se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p><p>Los países que forman parte de él son Argentina, Brasil, Chile, Colombia, México, Perú, Venezuela, Costa Rica, República Dominicana, Guatemala y Uruguay. Representan en conjunto el 89,4% del PIB regional y 90,5% de la población latinoamericana (según datos de 2015 del Banco Mundial).</p>' WHERE code='XBLA' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>América del Norte está formada por Estados Unidos y Canadá. De este modo, en el Índice Elcano de Presencia Global queda representado el 100% del PIB regional y de la población.</p>' WHERE code='XBNA' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Asia-Pacífico se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p><p>Los países que forman parte de él son Australia, Bangladesh, China, Filipinas, India, Indonesia, Japón, Malasia, Nueva Zelanda, Pakistán, República de Corea, Singapur, Tailandia, Vietnam, Myanmar, Sri Lanka, Kazajistán, Turkmenistán Uzbekistán. Representan el 99,3% y el 96,6% del PIB y de la población de la región, respectivamente (según datos de 2015 del Banco Mundial).</p>' WHERE code='XBAP' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Magreb y Oriente se compone de los países de esta región para los que existe cálculo de presencia global. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país</p><p>Los países que forman parte de él son Arabia Saudí, Argelia, Catar, Egipto, Emiratos Árabes Unidos, Irán, Iraq, Israel, Kuwait, Libia, Marruecos, Siria y Omán. Representan el 94,8 % del PIB regional (según datos de 2015 del Banco Mundial) y el 87% de su población, tomando la misma fuente.</p>' WHERE code='XBMM' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>África Sub-Sahariana se compone de los países de esta región para los que existe cálculo de presencia global; esto es, Angola, Nigeria, Sudáfrica, Etiopía, Kenia, Tanzania y Sudán. La presencia global del bloque se obtiene mediante la suma de la presencia global de cada país.</p><p>Se trata del bloque geográfico menos representativo de los que se incluyen en el índice puesto que los siete países considerados representan tan sólo 73,4% del PIB regional y 50,1% de su población (según datos de 2015 del Banco Mundial).</p>' WHERE code='XBSA' AND language='es';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Spain has recorded a noticeable increase in its global presence since 1990, supported by its economic dimension. However, the nature of that presence is mostly soft and of low added value –with a significant role played by variables such as tourism and sport–. The same can be said of the economic dimension, where exports of primary goods and services stand out. Despite an increase in absolute terms, Spain faces a relatively recent loss of leadership, relinquishing presence since 2010 to other emerging countries, even though the country’s global presence share has slightly recovered in 2015. Moreover, for the first time in our series, in 2013 Spain reduced its presence, which means the European crisis has had an impact on global presence. In 2015, Spain has recovered presence in absolute value, both in economic and soft dimensions, following the upward trend started the previous year.</p><p>Within the European Union, Spain also gained presence up to 2010, but in this case driven by the dynamism of its soft dimension –mainly migration and information– which became more prominent than the economic aspects. Growth in the economic variables has been lower than that of Spain’s main European Union partners, thus reducing this dimension’s contribution to Spain’s presence in Europe. The country records in 2015 a loss of European presence in absolute terms due to a slowdown of its economic presence, a trend that other European partners have also recorded.</p>' WHERE code='ES' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Despite the growth of its global presence in absolute terms, Germany remains at 3rd place in the global presence ranking -spot to which the country was relegated in 2014-, being overtaken in global presence by China. Since the mid-1990s, and following the fall of the Soviet Union and reunification, Germany has been recording a steady growth in its economic presence, the dimension that provides the highest contribution to its position and in which it occupies a prominent place in all variables –save energy exports–. The decline of presence in 2013 and the slight recovery over the past years have not allowed Germany to maintain the 2nd position in the global presence ranking (held since the year 2000).</p><p>Within the European Union, Germany has maintained its hegemony. Despite the decreasing demand from its European Union partners, Germany’s European presence has an essentially economic nature, based on its investment stock and services and manufacturing exports. Furthermore, within the soft dimension, its presence is based on the solid pillars of information, technology and science.</p>' WHERE code='DE' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>The United Kingdom’s global presence has steadily increased since 1990, climbing up the ranking to outstrip France and Japan. However, in 2015 British global presence has decreased in absolute terms and the country has fallen to the fourth place in the global presence ranking, behind Germany, the country it overtook in 2014, and China, which currently ranks second.</p><p>Its presence is of a soft nature –with high marks in information and education– and it is the European country with the largest presence in this dimension, allowing it to keep its global share despite the rise of emerging countries. However, its increase of presence has been sustained mainly by its economic dimension with prominence of investment stock and services exports –based on the importance of banking, insurance and consultancy and advisory services as well as its role as a financial hub–. The recent contraction of the United Kingdom’s absolute and relative values were caused by the moderation of its economic and global values growth rate after their extraordinary peak in 2014, when an increase of international gold sales caused a sharp growth in the country’s primary good exports.</p><p>Within the European Union, the United Kingdom keeps the 2nd place in 2015 in European presence and recovers from the absolute value loss the country suffered in 2014. Accordingly, the gap with respect Germany has increased, while it still leaves France further behind. That could be a symptom of the United Kingdom’s strategy of deepening its extra-European Union relations in a context of slow-growing Europe. Its economic presence is on a downward trend relative to the soft dimension –in which sports, information, culture, and also, although to a lesser degree, in science and education play a significant role–, being in 2015 the country with more soft presence in the region.</p>' WHERE code='GB' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Despite its continued increase in global presence, France faces a progressive loss of relevance in the international scene. This is reflected in the decline in its share of presence and its loss of position in the ranking –it was 2nd in 1995 and now 6th, been overtaken by Russia and the United Kingdom–. France maintains a profile that is similar to those of other European economies, with a high soft presence –being the leading worldwide tourist destination and additionally involved in development cooperation, education and information–, while the economic dimension grows, yet in short amount and with certain variations, due to the European economic crisis.</p><p>In European terms, France ranks 3rd but with the opposite profile than it has in global terms. Its economic variables are more important, although its increased presence has been boosted by the soft dimension; mainly in culture, tourism and science.</p>' WHERE code='FR' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Despite the gradual decline in its world ranking by GDP, the Netherlands retains a high position in the Global Presence Index. Its economic dimension –which in 2015 accounted for 76.5% of its total value– continues to be the most important component. It is the 4th largest exporter of primary goods and Europe’s leading exporter of energy, adding to its condition as the leading European producer and owner of major gas fields its possession of the strategic port of Rotterdam. Thus, much of its position can be explained by its role as an export hub.</p><p>Like other European economies, the crisis has had an impact on many variables, although despite the Dutch economy having experienced absolute declines in its global presence in 2013, it recovers in 2014 due to the constant growth in its energy exports. This however ends in 2015, as the countries again loses global presence.</p><p>Its profile is replicated in Europe, where The Netherlands has the 2nd highest value after Germany in economic presence, but with a low score in the soft dimension. The Netherlands records a new loss of European presence, which return the countries absolute value to that of 2013, mainly due to the slumping European demand.</p>' WHERE code='NL' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>If the European Union were to be considered a single country, it would occupy the first place in the Global Presence classification, ahead of the United States. It would record the highest values in the economic and soft dimensions. Only in the military dimension would US hegemony be maintained. The nature of the European Union’s presence is mostly soft, being the global leader not only in tourism and sports but also in technology, science, education and development cooperation. However, its growing presence since 2005 is based on the economic dimension, where the euro’s stronger role as an international currency has been a contributory factor.</p><p>The economic crisis, which has especially hit the European Union, has had an impact on its presence. On the one hand it has led to a drop in international

cooperation flows and on the number of immigrants received. On the other, it has slowed down the growth of the economic dimension, although this has been offset by the geographical re-orientation of exports to other regions of the world. Thus the European Union records losses of global presence in absolute terms.</p>' WHERE code='XBEU' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>A Despite its steady loss of both positions and share in terms of Global Presence and GDP, Italy holds, since 2013, eleventh place in the Global Presence Index ranking. This trend is due to the slower growth of its economic presence, in which it ranked 16th in 2015, compared with 8th in the 1990s. However, Italy is still one of the 8 most heavily industrialised countries, so its presence is fundamentally economic, supported by manufactured exports –being the 7th world exporter–, primary goods and investments. Similarly to other European countries, Italy has a high score in the soft dimension –mainly because of tourism and information–, where the reduction in international cooperation flows contributed to an unprecedented decline in the Index in absolute terms in 2013. However, it records a certain recovery of soft and economic presence in 2014, which has persisted through 2015. Within the European Union, Italy’s soft dimension has grown –thanks to tourism, migration and science–. Nevertheless, this has been insufficient for Italy to maintain its position relative to Spain, dropping to 6th place in terms of European presence mainly because of the loss of economic presence. Actually, in 2014, Italy has lost European presence in absolute terms for the first time in our series, though the trend seems to be reverting in 2015, yet not enough to help Italy climb in the regional ranking.</p>' WHERE code='IT' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>US supremacy since the fall of the Soviet bloc is evident in various aspects of the Global Presence Index. First, it has ranked 1st in all years and in all variables, except in exports of energy goods, manufactures and tourism. Secondly, it has the highest share of presence in all dimensions: 11.4% in economic, 46% in military and 15.5% in soft presence. Moreover, unlike other developed countries, its military dimension continues to make a significant contribution to the Index’s vale, at 13% in 2015. Furthermore, in line with its leading role in the development of globalisation, the US has recorded the largest increases in absolute terms since 1990.</p><p>However, while maintaining its hegemony, the US presence has declined in relative terms and in comparison with other countries, from a 23.2% share in 1990 to 14.3% in 2015. In a period of emergence of new global players, several economies reap gains of share that reduce the American role, where highlights the rise of

Asian and oil exporter countries. This trend is mainly due to the Index’s economic dimension, which despite being the one in which the US has recorded the largest increase –especially in the export of primary goods, services and stock of investment– has reduced its contribution by almost four percentage points since 1990. Meanwhile, the general trend in most countries of demilitarising their presence has allowed the US to maintain its military hegemony despite the reduction in the number of units it has deployed. Nevertheless, the slowing down of the globalization process over the last couple of years has resulted in a mild re-concentration of global presence, allowing the US to maintain its global presence share.</p>' WHERE code='US' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>The evolution of Russia’s global presence can be divided into two periods. The first, during the 1990s, was characterised by a drastic reduction in its Index value following the fall of the Soviet bloc, with a substantial decrease in military presence. In 1990 the military dimension largely underpinned the Soviet Union’s global presence, with a weight of 78% in its total value. In the second period, from 2000 onwards, there has been a steady process of recovery in its global presence, primarily supported by the economic dimension, although Russia has been unable to return to the levels of the Soviet era until 2012. As the leading gas exporter and the second-largest oil exporter, energy goods are mainly responsible for the increase, contributing 47.9% to the Index’s value in 2015. A further contributor has been the growth in primary exports, and more recently services and investment stocks. Russia’s increase in soft presence has been much lower than for other world powers, and it is still occupying a very low position in all variables, with the exception of sports –given its success in the Olympic medal table– and migrations –being the second-largest host country worldwide–.</p>' WHERE code='RU' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>China’s remarkable rise in recent decades is reflected in its classification in the Global Presence Index, where it has risen 10 positions since 1990. It has also grown in terms of GDP, with a prime role played by the economic presence –in 1990 China ranked 17th and in 2015 the country holds 2nd place in this dimension– mainly driven by the export of manufactures, but also of primary goods and services. Hence, the nature of its global presence is mainly economic, accounting for 65.1% of the Index’s value in 2015. However, there has been a recent improvement in the soft variables –tourism, sports and science–, reflecting a possible change in trend in the nature of China’s presence, while it has consolidated its global position. This is also evident in terms of share, at 5.4% in 2015 compared with 1.7% in 1990. Although still far from the US, China has

recently overtaken France, the United Kingdom and Germany.</p>' WHERE code='CN' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Japan ranks 7th despite its economic lethargy following the crisis of the 1990s, which led to it recording lower growth rates in its presence than other major countries. Despite retaining the 9th largest GDP, Japan has suffered a significant decline in economic presence, falling from the 5th position in 1990 to 12th in 2014. In 2015 Japan has regained the 11th place in the ranking and its economic presence share has reached 2.7%. However, it still has a high score in soft presence –being 6th worldwide– supported by technology, science and cooperation. At the same time, and despite its demilitarisation after WWII, the military dimension contributes in 4.2% to the country’s global presence, higher than for other developed economies. In 2015, Japan records a slight growth in global presence, backed on its soft dimension and a faint recovery of its economic presence. This heightens the downward trend in terms of share, dropping from 4.8 in 1990 to 3.2% in 2015.</p>' WHERE code='JP' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Canada remains in the top positions of the Global Presence Index, despite its loss of economic weight –down five positions since 1990– and the rise of China, which have pushed it down one position in the global presence ranking. Being the 3rd largest gas and 5th largest oil producer, the export of energy goods was the main contributor to Canada’s global presence, at 25.4% in 2015. Canada also has a highly technical agricultural sector that has allowed it to increase its exports of primary goods –which accounted for 17.2% of its presence in 2015–. For this reason, Canada’s presence is fundamentally economic –accounting for 63.6% of its global presence– while it retains, similarly to other developed economies, a high score in the soft dimension and an almost nil presence in the military one.</p>' WHERE code='CA' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p> Saudi Arabia, 10th in the Global Presence Index ranking, rises into the global scene in the year 2000, when its global presence starts an upward trend in absolute terms back by its growing economic presence. Being the world’s leading oil producer and the second energy exporter, Saudi Arabia’s global presence depends greatly on the international energy market evolution, which in the last years has been favourable to oil and gas exporters.</p><p>In 2015 the country’s economic presence -9º overall- contributes 72.2% to its global presence and energy exports 67.5%. This energy-focused composition has

been constant throughout the series and in spite of the recent oil disturbances. In fact, due to the recent evolution of oil prices, Saudi Arabia loses economic presence, which is balanced out by an increase in soft presence.</p><p>Even though the country is oil-driven, the soft dimension is an important aspect of Saudi Arabia’s global presence. It alone contributes 26.7% to the global presence in 2015, standing out migrations and more importantly cooperation -an issues in which Saudi Arabia holds fifth place worldwide-, whose recent increases have allowed this country to maintain positions in the global presence ranking, unlike other oil-producing countries.</p>' WHERE code='SA' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Latin America is constituted by the countries in the region whose global presence has been included in the calculation. The bloc’s global presence is obtained by adding the global presence of each country of which it is comprised.</p><p>The countries that make up the bloc are Argentina, Brazil, Chile, Cuba, Colombia, Ecuador, Mexico, Peru, Venezuela, Costa Rica, Dominican Republic, Guatemala and Uruguay. They account for 89.4% of the Latin America’s GDP and 90.5% of its population (according to World Bank data for 2015).</p>' WHERE code='XBLA' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>North America comprises the United States and Canada. The bloc’s global presence is calculated by adding up the two countries’ global presences. Thus, 100% of the region’s GDP and population are represented in the Elcano Global Presence Index.</p>' WHERE code='XBNA' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Asia-Pacific is constituted by the countries in the region for which their global presence has been calculated. The global presence of the block is obtained by the pure sum of the global presence of each country that makes up the block.</p><p>The countries comprising the bloc are Australia, Bangladesh, China, India, Indonesia, Japan, Malaysia, New Zealand, Pakistan, the Philippines, the Republic of Korea, Singapore, Sri Lanka, Thailand, Vietnam, Myanmar, Kazakhstan, Turkmenistan and Uzbekistan. They account for 99.3% and 96.6% of the region’s GDP and population, respectively (according to World Bank data for 2015).</p>' WHERE code='XBAP' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>The Maghreb and the Middle East are made up of the countries forming the region whose global presence has been calculated. The bloc’s global presence is the result of the pure sum of the global presence of each country comprising it.</p><p>The countries considered are Algeria, Egypt, Iran, Iraq, Israel, Kuwait, Libya, Morocco, Oman, Qatar, Saudi Arabia, Syria and the United Arab Emirates. They account for 94.8% of the region’s GDP and 87% of its population (according to World Bank data for 2015).</p>' WHERE code='XBMM' AND language='en';

UPDATE iepg_data_redux.iepg_comment set comment='<p>Sub-Saharan Africa comprises the countries in the region whose global presence has been calculated: Angola, Nigeria, South Africa, Sudan, Ethiopia, Kenya and Tanzania. The bloc’s global presence is obtained by adding the global presence of each country considered.</p><p>It is the Index’s least representative geographical bloc as the seven countries evaluated account for only 73.4% of the region’s GDP and 50.1% of its population (according to World Bank 2015 data).</p>' WHERE code='XBSA' AND language='en';


  

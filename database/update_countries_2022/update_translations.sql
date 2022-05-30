


BEGIN;

UPDATE www.translation SET es = 'El <a class=\"nostyle\" href=\"%s\"><strong>Índice Elcano de Presencia Global</strong></a> calcula anualmente la proyección de 150 países fuera de sus fronteras en función de tres dimensiones:' WHERE key = '_home IEPG explora desc';
UPDATE www.translation SET en = 'The <a class=\"nostyle\" href=\"%s\"><strong>Elcano Global Presence Index</strong></a> is an annual measurement of the projection in the world of 150 countries based on three dimensions:' WHERE key = '_home IEPG explora desc';

UPDATE www.translation SET es = 'Para definir la ponderación de los elementos del Índice, se ha recurrido a la valoración de expertos en relaciones internacionales vinculados a centros de análisis de los cinco continentes. Las encuestas a personas expertas seleccionados sobre la base del informe <a href="https://www.gotothinktank.com/" target="_blank">Global Go To Think Tanks que publica anualmente la Universidad de Pensilvania</a> se realizaron en 2011, 2012, 2015, 2018 y 2021.' WHERE key = '_methodology criterios lista pie p';
UPDATE www.translation SET en = 'In defining the weightings of each of the elements included in the Index, we conducted surveys with a panel of experts in international relations based in intitutions from the five continents. The surveys were done in 2011, 2012, 2015, 2018 and 2021 to experts selected on the basis of the report <a href="https://www.gotothinktank.com/" target="_blank">Global Go To Think Tanks published annually by the University of Pennsylvania.</a>' WHERE key = '_methodology criterios lista pie p';

UPDATE www.translation SET es = 'Flujo de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio, y servicios públicos.' WHERE key = 'Variable services desc TEXTO';
UPDATE www.translation SET en = 'Flow of exports of services in transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services' WHERE key = 'Variable services desc TEXTO';

UPDATE www.translation SET es = 'Suma ponderada de los puntos en el medallero en los Juegos Olímpicos de verano, la clasificación mundial FIFA de selecciones absolutas masculinas y femeninas, y la clasificación mundial de clubes masculinos de fútbol de IFFHS.' WHERE key = 'Variable sports desc TEXTO';
UPDATE www.translation SET en = 'Weighted sum of medals won at the summer Olympic Games, points of male and female national teams in the FIFA world ranking and points of male football clubs in the IFFHS.' WHERE key = 'Variable sports desc TEXTO';

UPDATE www.translation SET es = 'Exportaciones de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales) y de bienes culturales (antigüedades y obras de arte, fotografía, libros, joyería, periódicos, etc.).' WHERE key = 'Variable culture desc TEXTO';
UPDATE www.translation SET en = 'Exports of audiovisual and related services (cinematographic productions, radio and television programs, and musical recordings) and cultural goods (antiques and works of art, books, jewelry, newspapers, photography, etc.).' WHERE key = 'Variable culture desc TEXTO';

UPDATE www.translation SET es = 'Ingresos recibidos del exterior por el uso de la propiedad intelectual y número de solicitudes de patentes orientadas al exterior (relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención).' WHERE key = 'Variable technology desc TEXTO';
UPDATE www.translation SET en = 'External income for the use of intellectual property and number of foreign-oriented patents (inter-related patent applications filed in one or more foreign countries to protect the same invention).' WHERE key = 'Variable technology desc TEXTO';

UPDATE www.translation SET en = 'Flow of exports of primary goods (food, beverages, tobacco, agricultural commodities, non-ferrous metals, pearls, precious stones and non-monetary gold), excluding oil (SITC 0 + 1 + 2 + 4 + 68 + 667 + 971).' WHERE key = 'Variable primary_goods desc TEXTO';

UPDATE www.translation SET es = 'El Índice Elcano de Presencia Global cubre una selección de 150 países que se realiza, en términos generales, siguiendo el orden de estos países por PIB mundial.' WHERE key = '_methodology p1';
UPDATE www.translation SET en = 'The Elcano Global Presence Index includes 150 countries. These are selected, mainly, according to their size in terms of GDP.' WHERE key = '_methodology p1';

UPDATE www.translation SET es = 'En relación a la selección de países, hay que tener en cuenta que al calcularse en escalas temporales que se remontan a 1990, la intención del proyecto es la de mostrar el ‘mundo de los dos bloques’ –aunque sea en su ocaso–. De este modo, los valores de 1990 de Rusia se refieren, evidentemente, a los de la Unión Soviética; los de Alemania a la República Federal Alemana; y los valores hasta 2005 de Serbia a la Unión Estatal de Serbia y Montenegro. Además, los países de Europa del Este que alcanzaron su independencia tras 1990 no tienen valor asignado para ese año. Es el caso de Armenia, Azerbaiyán, Bielorrusia, Estonia, Georgia, Letonia, Lituania, Moldavia, Kazajistán, Kirguistán, Tayikistán, Turkmenistán, Ucrania y Uzbekistán como parte de la Unión Soviética; de Eslovaquia como parte de Checoslovaquia y de Bosnia y Herzegovina, Croacia, Eslovenia y Macedonia del Norte como parte de Yugoslavia. Del mismo modo, Sudán del Sur tiene registros desde 2012 tras su independencia.' WHERE key = '_methodology países p';
UPDATE www.translation SET en = 'In terms of country selection, bear in mind that by making calculations at time intervals that go back to 1990, the intention of the project is to show the ‘two-bloc world’, even if in decline. Thus, Russia’s 1990 values refer to those of the Soviet Union, those of Germany to the German Federal Republic, those of the Czech Republic to Czechoslovakia, and those values up to 2005 of Serbia to the State Union of Serbia and Montenegro. Moreover, East European countries that became independent after 1990 have no value assigned in that year. This is the case for Armenia, Azerbaijan, Belarus, Estonia, Georgia, Latvia, Lithuania, Moldova, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Ukraine and Uzbekistan as part of the Soviet Union, Slovakia as part of Czechoslovakia, and Bosnia and Herzegovina, Croatia, North Macedonia and Slovenia as part of Yugoslavia. Likewise, South Sudan records since 2012 after its independence.' WHERE key = '_methodology países p';


UPDATE www.translation SET es = '<table class="data">
   <tr><th>Variable</th><th>Indicador</th><th>Fuente</th></tr>
   <tr class="section">
       <td colspan="3">Presencia económica</td>
   </tr>
   <tr>
       <td>Energía</td>
       <td>Flujo de exportación de productos energéticos (petróleo, productos refinados y gas) (SITC 3)</td>
       <td rowspan=5>UNCTAD</td>
   </tr>
   <tr>
       <td>Bienes primarios</td>
       <td>Flujo de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667 + 971)</td>
   </tr>
   <tr>
       <td>Manufacturas</td>
       <td>Flujo de exportación de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68)</td>
   </tr>
   <tr>
       <td>Servicios</td>
       <td>Flujo de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos</td>
   </tr>
   <tr>
       <td>Inversiones</td>
       <td><em>Stock</em> de inversión directa extranjera en el exterior</td>
   </tr>

   <tr class="section">
       <td colspan="3">Presencia militar</td>
   </tr>
   <tr>
       <td>Tropas</td>
       <td>Número de militares desplegados en misiones internacionales y bases en el extranjero</td>
       <td rowspan=2>IISS</td>
   </tr>
   <tr>
       <td>Equipamiento militar</td>
       <td>Suma ponderada de medios militares de proyección: portaviones, fragatas, cruceros, destructores, submarinos de propulsión nuclear, buques de proyección anfibia, aviones de transporte estratégico medios y pesados, y aviones cisterna</td>
   </tr>
   <tr class="section">
       <td colspan="3">Presencia blanda</td>
   </tr>
   <tr>
       <td>Migraciones</td>
       <td>Número estimado de personas migrantes internacionales en el país a mitad de año</td>
       <td>División de Población de Naciones Unidas </td>
   </tr>
   <tr>
       <td>Turismo</td>
       <td>Miles de llegadas de turistas no residentes a las fronteras</td>
       <td>Organización Mundial del Turismo de Naciones Unidas (OMT)</td>
   </tr>
   <tr>
       <td>Deportes</td>
       <td>Suma ponderada de los puntos en el medallero en los Juegos Olímpicos de verano, la clasificación mundial FIFA de selecciones absolutas masculinas y femeninas y la clasificación mundial de clubes masculinos de fútbol de IFFHS</td>
       <td>COI, IFFHS y FIFA</td>
   </tr>
   <tr>
       <td>Cultura</td>
       <td>Exportaciones de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales) y de bienes culturales (antigüedades y obras de arte, fotografía, libros, joyería, periódicos, etc.)</td>
       <td>Organización Mundial del Comercio (OMC) y UN COMTRADE</td>
   </tr>
   <tr>
       <td>Información</td>
       <td>Número de menciones en noticias de las principales agencias (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua)
    y ancho de banda de Internet (Mbps)</td>
       <td>Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
   </tr>
   <tr>
       <td>Tecnología</td>
       <td>Ingresos recibidos del exterior por el uso de la propiedad intelectual y número de solicitudes de patentes orientadas al exterior (relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención)</td>
       <td>FMI y Organización Mundial de la Propiedad Intelectual (OMPI)</td>
   </tr>
   <tr>
       <td>Ciencia</td>
       <td>Número de artículos, <em>notes</em> y <em>reviews</em> publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias</td>
       <td>Clarivate Analytics vía FECYT</td>
   </tr>
   <tr>
       <td>Educación</td>
       <td>Número de estudiantes extranjeros en educación terciaria en territorio nacional</td>
       <td>UNESCO</td>
   </tr>
   <tr>
       <td>Cooperación al desarrollo</td>
       <td>Flujo de ayuda oficial al desarrollo bruto total o datos homologables</td>
       <td>OCDE y SEGIB</td>
   </tr>
   <tr class="section">
       <td colspan="3">Factores de escala</td>
   </tr>
   <tr>
       <td>Economía</td>
       <td>Producto Interior Bruto (PIB) a precios corrientes en dólares EEUU</td>
       <td>Banco Mundial</td>
   </tr>
   <tr>
       <td>Población</td>
       <td>Número de habitantes</td>
           <td>Banco Mundial</td>
   </tr>
    </table>' WHERE key = '_methodology tabla general';

    UPDATE www.translation SET en = '<table class="data">
    <tr><th>Variable</th><th>Indicator</th><th>Source</th></tr>
    <tr class="section">
        <td colspan="3">Economic Presence</td>
    </tr>
    <tr>
        <td>Energy</td>
        <td>Flow of exports of energy products (oil, refined products and gas) (SITC 3)</td>
        <td rowspan=5>UNCTAD</td>
    </tr>
    <tr>
        <td>Primary goods</td>
        <td>Flow of exports of primary goods (food, beverages, tobacco, agricultural commodities, non-ferrous metals, pearls, precious stones, and non-monetary gold), excluding oil (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971)</td>
    </tr>
    <tr>
        <td>Manufactures</td>
        <td>Flow of exports of manufactured goods (chemical products, machinery, transport equipment, other manufactured products) (SITC 5 to 8 minus 667 and 68)</td>
    </tr>
    <tr>
        <td>Services</td>
        <td>Flow of exports of services in transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services</td>
    </tr>
    <tr>
        <td>Investments</td>
        <td>Stock of foreign direct investment abroad</td>
    </tr>

    <tr class="section">
        <td colspan="3">Military presence</td>
    </tr>
    <tr>
        <td>Troops</td>
        <td>Number of military personnel deployed in international missions and bases overseas</td>
        <td rowspan=2>IISS</td>
    </tr>
    <tr>
        <td>Military equipment</td>
        <td>Weighted sum of aircraft carriers, big ships, destroyers, frigates, nuclear-powered submarines, amphibious ships, medium and heavy strategic aeroplanes, and air tankers</td>
    </tr>

    <tr class="section">
        <td colspan="3">Soft presence</td>
    </tr>
    <tr>
        <td>Migration</td>
        <td>Estimated number of international immigrants in the country at mid-year</td>
        <td>United Nations Population Division </td>
    </tr>
    <tr>
        <td>Tourism</td>
        <td>Thousands of arrivals of non-resident tourists at borders</td>
        <td>United Nations World Tourism Organization (UNWTO)</td>
    </tr>
    <tr>
        <td>Sports</td>
        <td>Weighted sum of medals won at the summer Olympic Games, points in the FIFA world ranking and points of football clubs in the IFFHS</td>
        <td>FIFA, IFFHS and IOC</td>
    </tr>
    <tr>
        <td>Culture</td>
        <td>Exports of audiovisual and related services (cinematographic productions, radio and television programs, and musical recordings) and cultural goods (antiques and works of art, books, jewelry, newspapers, photography, etc.)</td>
        <td>WTO & UN-COMTRADE</td>
    </tr>
    <tr>
        <td>Information</td>
        <td>Number of mentions in news of main international press agencies (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua) and internet bandwidth (Mbps)</td>
        <td>Factiva International Telecommunication Union</td>
    </tr>
    <tr>
        <td>Technology</td>
        <td>External income for the use of intellectual property and number of foreign-oriented patents (inter-related patent applications filed in one or more foreign countries to protect the same invention)</td>
        <td>IMF & World Intellectual Property Organization (WIPO)</td>
    </tr>
    <tr>
        <td>Science</td>
        <td>Number of articles, notes, and reviews published in the fields of the arts and humanities, social sciences, and sciences</td>
        <td>Clarivate Analytics via FECYT</td>
    </tr>
    <tr>
        <td>Education</td>
        <td>Number of foreign students in tertiary education on national territory</td>
        <td>UNESCO & OECD</td>
    </tr>
    <tr>
        <td>Development cooperation</td>
        <td>Total gross flows of official development aid or comparable data</td>
        <td>OECD & SEGIB</td>
    </tr>
    <tr class="section">
        <td colspan="3">Scaling factors</td>
    </tr>
    <tr>
        <td>Economy</td>
        <td>Gross Domestic Product (GDP) at current prices in US dollars</td>
        <td>World Bank</td>
    </tr>
    <tr>
        <td>Population</td>
        <td>Number of inhabitants</td>
            <td>World Bank</td>
    </tr>
    </table>
' WHERE key = '_methodology tabla general';

UPDATE www.translation SET es = 'Desde 2012, el Índice Elcano de Presencia Global se calcula además para la Unión Europea. Este ejercicio trata de cuantificar la proyección global de la Unión, como si se tratase de un supuesto súper-estado con identidad propia; medición que se complementa con el Índice Elcano de Presencia Europea que, por su parte, evalúa la presencia de los países miembros dentro del perímetro de la Unión' WHERE key = '_methodology incorporación UE p';
UPDATE www.translation SET en = 'Moreover, since 2012, the Index also measures the global presence of the European Union as a whole. The latter is complemented by the Elcano European Presence Index, which evaluates the internationalisation of member states within the Union’s boundaries' WHERE key = '_methodology incorporación UE p';

INSERT INTO www.translation VALUES ('_methodology incorporación UE p2', 'The calculation is made considering the EU actually existing at each date, so that data from 2005 refer to the EU-25, from 2010 to the EU-27, from 2013 to the EU-28, and from 2021 to the EU-27 after the exit of the United Kingdom', 'El cálculo se realiza teniendo en cuenta la UE realmente existente en cada fecha, por lo que los datos entre 2005 se refieren a la UE-25, a partir de 2010 a la UE-27, a partir de 2013 a la UE-28, y desde 2021 la UE-27 tras la salida de Reino Unido');

UPDATE www.translation SET en = '<ul class="util">

 <li>Ángel Badillo, 2019,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/zonas_es/lengua+y+cultura/dt21-2020-badillo-la-cultura-en-el-poder-suave-revision-metodologica-indice-elcano-de-presencia-global'' target=''_blank''>
     La cultura en el “poder suave”: una revisión metodológica del Índice Elcano de Presencia Global
   </a>
   (Documento de Trabajo del Real Instituto Elcano (DT) 21/2020).
 </li>

 <li>Isabel Álvarez, José Miguel Natera and Raquel Marín, 2019,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/ari115-2019-alvarez-natera-marin-indicadores-de-tecnologia-para-medir-la-presencia-global-de-un-pais'' target=''_blank''>
     Indicadores de tecnología para medir la presencia global de un país, ARI 115/2019, 05/12/2019
   </a>
   (Madrid: Elcano Royal Institute).
 </li>

 <li>Manuel Gracia, Iliana Olivié and Néstor Santana, 2019,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/ari7-2019-gracia-olivie-santana-encuesta-ponderacion-2018-indice-elcano-presencia-global'' target=''_blank''>
     Un mundo, diferentes perspectivas: análisis de los resultados de la encuesta de ponderación 2018 del Índice Elcano de Presencia Global, ARI 7/2019, 16/01/2019
   </a>
   (Madrid: Elcano Royal Institute).
 </li>

 <li>Iliana Olivié and Manuel Gracia, 2018,
   <a href=''http://www.globalpresence.realinstitutoelcano.org/en/data/Global_Presence_2018.pdf'' target=''_blank''>
     Elcano Global Presence Index Report 2018,
   </a>
   (Madrid: Elcano Royal Institute).
 </li>

 <li>Iliana Olivié and Manuel Gracia, 2017,
   <a href=''http://www.globalpresence.realinstitutoelcano.org/en/data/Global_Presence_2017.pdf'' target=''_blank''>
     Elcano Global Presence Index Report 2017,
   </a>
   (Madrid: Elcano Royal Institute).
 </li>

 <li>Iliana Olivié and Manuel Gracia, 2016,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/publication?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/publications/elcano-global-presence-report-2016'' target=''_blank''>
     Elcano Global Presence Index Report 2016,
   </a>
   (Madrid: Elcano Royal Institute).
 </li>

 <li>Iliana Olivié et al. (coord.), 2015,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/publication?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/publications/elcano-global-presence-report-2015'' target=''_blank''>
     Elcano Global Presence Index Report 2015,
   </a>
   (Madrid: Elcano Royal Institute).
 </li>

 <li>Iliana Olivié, Manuel Gracia and Carola García-Calvo, 2014,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/publication?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/publications/elcano-global-presence-report-2014'' target=''_blank''>
     Elcano Global Presence Index Report 2014,
   </a>
   (Madrid: Elcano Royal Institute).
 </li>
 <li>Iliana Olivié and Manuel Gracia and Carola García-Calvo, 2013,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/publication?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/publications/global-presence-report-2012'' target=''_blank''>
     Elcano Global Presence Report 2012,
   </a>
    (Madrid: Elcano Royal Institute).
 </li>
 <li>Iliana Olivié and Manuel Gracia, 2013,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/specials/globalpresenceindex-iepg/dt12-2013-olivie-gracia-iepg-metodologia-methodology-2012'' target=''_blank''>
     IEPG 2012: methodology and new analytic tools,
   </a>
    Elcano Working Paper (WP) 12/2013.
 </li>
 <li>Iliana Olivié and Ignacio Molina (coord.), 2012,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/specials/globalpresenceindex-iepg/dt9-2012'' target=''_blank''>
     Measuring the international presence of countries: the Elcano Institute''s IEPG Index methodology revisited,
   </a>
    Elcano Royal Institute Working Paper (WP) 9/2012.
 </li>
 <li>Iliana Olivié and Ignacio Molina (coord.), 2011,
   <a href=''http://www.realinstitutoelcano.org/wps/wcm/connect/8aaf13804739471481169f00526b8882/EstudioElcano2-english_IEPG_Olivie_Molina.pdf?MOD=AJPERES'' target=''_blank''>
     Elcano Global Presence Index (IEPG),
   </a>
    Estudio Elcano 2, (Madrid: Elcano Royal Institute).
 </li>
 </ul>' WHERE key = '_methodology más información lista';


 UPDATE www.translation SET es = '<ul class="util">

  <li>Ángel Badillo, 2019,
    <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/zonas_es/lengua+y+cultura/dt21-2020-badillo-la-cultura-en-el-poder-suave-revision-metodologica-indice-elcano-de-presencia-global'' target=''_blank''>
      La cultura en el “poder suave”: una revisión metodológica del Índice Elcano de Presencia Global
    </a>
    (Documento de Trabajo del Real Instituto Elcano (DT) 21/2020).
  </li>

  <li>Isabel Álvarez, José Miguel Natera y Raquel Marín, 2019,
    <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/ari115-2019-alvarez-natera-marin-indicadores-de-tecnologia-para-medir-la-presencia-global-de-un-pais'' target=''_blank''>
      Indicadores de tecnología para medir la presencia global de un país, ARI 115/2019, 05/12/2019
    </a>
    (Madrid: Real Instituto Elcano).
  </li>

  <li>Manuel Gracia, Iliana Olivié y Néstor Santana, 2019,
    <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/ari7-2019-gracia-olivie-santana-encuesta-ponderacion-2018-indice-elcano-presencia-global'' target=''_blank''>
      Un mundo, diferentes perspectivas: análisis de los resultados de la encuesta de ponderación 2018 del Índice Elcano de Presencia Global, ARI 7/2019, 16/01/2019
    </a>
    (Madrid: Real Instituto Elcano).
  </li>

 <li>
   Iliana Olivié y Manuel Gracia, 2018,<a href=''http://www.globalpresence.realinstitutoelcano.org/es/data/Presencia_Global_2018.pdf'' target=''_blank''>
     Informe Índice Elcano de Presencia Global 2018,
   </a>
 (Madrid: Real Instituto Elcano).
 </li>

 <li>
   Iliana Olivié y Manuel Gracia, 2017,<a href=''http://www.globalpresence.realinstitutoelcano.org/es/data/Presencia_Global_2017.pdf'' target=''_blank''>
     Informe Índice Elcano de Presencia Global 2017,
   </a>
 (Madrid: Real Instituto Elcano).
 </li>

 <li>
   Iliana Olivié y Manuel Gracia, 2016,<a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano_es/publicacion?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/publicaciones/informe-presencia-global-2016'' target=''_blank''>
     Informe Índice Elcano de Presencia Global 2016,
   </a>
 (Madrid: Real Instituto Elcano).
 </li>

 <li>
   Iliana Olivié et al. (coord.) 2015,<a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/publicacion?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/publicaciones/informe-presencia-global-2015'' target=''_blank''>
     Informe Índice Elcano de Presencia Global 2015,
   </a>
 (Madrid: Real Instituto Elcano).
 </li>

 <li>Iliana Olivié, Manuel Gracia y Carola García-Calvo, 2014,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/publicacion?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/publicaciones/informe-presencia-global-2014'' target=''_blank''>
     Informe Índice Elcano de Presencia Global 2014,
   </a>
 (Madrid: Real Instituto Elcano).
 </li>
 <li>Iliana Olivié y Manuel Gracia, 2013,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/publicacion?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/publicaciones/informe-presencia-global-2012'' target=''_blank''>
     Informe Índice Elcano de Presencia Global 2012,
   </a>
   (Madrid: Real Instituto Elcano).
 </li>
 <li>Iliana Olivié y Manuel Gracia, 2013,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/dt12-2013-olivie-gracia-iepg-metodologia-methodology-2012#.VTiVbtLtlBc'' target=''_blank''>
     IEPG 2012: metodología y nuevos elementos para el análisis,
   </a>
   Documento de Trabajo del Real Instituto Elcano (DT) 12/2013.
 </li>
 <li>Iliana Olivié e Ignacio Molina (coord.), 2012,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/dt9-2012#.VTiWpdLtlBc'' target=''_blank''>
     Medir la presencia internacional de los países: metodología revisada del Índice Elcano de Presencia Global (IEPG),
   </a>
   Documento de Trabajo del Real Instituto Elcano (DT) 9/2012.
 </li>
 <li>Iliana Olivié e Ignacio Molina (coord.), 2011,
   <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_es/publicacion?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/publicaciones/estudio_elcano_2_iepg'' target=''_blank''>
     Índice Elcano de Presencia Global (IEPG),
   </a>
   Estudio Elcano 2, (Madrid: Real Instituto Elcano).
 </li>
 </ul>' WHERE key = '_methodology más información lista';

UPDATE www.translation SET es = ' <table class="data">

    <tr><th>Variable</th><th>Indicador</th><th>Fuente</th></tr>
    <tr class="section">
        <td colspan="3">Presencia económica</td>
    </tr>
    <tr>
        <td>Energía</td>
        <td>Flujos extra-comunitarios de exportación de productos energéticos (petróleo, productos refinados y gas) (SITC 3)</td>
        <td rowspan=5>Eurostat</td>
    </tr>
    <tr>
        <td>Bienes primarios</td>
        <td>Flujos extra-comunitarios de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667 + 971)</td>
    </tr>
    <tr>
        <td>Manufacturas</td>
        <td>Flujos extra-comunitarios de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68)</td>
    </tr>
    <tr>
        <td>Servicios</td>
        <td>Flujos extra-comunitarios de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos</td>
    </tr>
    <tr>
        <td>Inversiones</td>
        <td><em>Stock</em> de inversión directa extranjera en el exterior de la UE</td>
    </tr>

    <tr class="section">
        <td colspan="3">Presencia militar</td>
    </tr>
    <tr>
        <td>Tropas</td>
        <td>Número de militares desplegados en misiones internacionales y bases fuera de la UE</td>
        <td rowspan=2>IISS</td>
    </tr>
    <tr>
        <td>Equipamiento militar</td>
        <td>Suma ponderada de medios militares de proyección: portaviones, fragatas, cruceros, destructores, submarinos de propulsión nuclear, buques de proyección anfibia, aviones de transporte estratégico medios y pesados, y aviones cisterna</td>
    </tr>

    <tr class="section">
        <td colspan="3">Presencia blanda</td>
    </tr>
    <tr>
        <td>Migraciones</td>
        <td>Número estimado de personas migrantes con origen extra-comunitario</td>
        <td>Eurostat</td>
    </tr>
    <tr>
        <td>Turismo</td>
        <td>Miles de llegadas de turistas extra-comunitarios</td>
        <td>Eurostat</td>
    </tr>
    <tr>
        <td>Deportes</td>
        <td>Suma ponderada de los puntos en el medallero en los Juegos Olímpicos de verano, la clasificación mundial FIFA de selecciones absolutas masculinas y femeninas y la clasificación mundial de clubes masculinos de fútbol de IFFHS.</br>Variable correctora: audiencia europea de la final del mundial y de la ceremonia de apertura de los Juegos Olímpicos</td>
        <td>FIFA, COI,<br> Kantar Media y Nielsen</br></td>
    </tr>
    <tr>
        <td>Cultura</td>
        <td>Exportaciones extra-comunitarias de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales) y de bienes culturales (antigüedades y obras de arte, fotografía, libros, joyería, periódicos, etc.)</td>
        <td>Eurostat</td>
    </tr>
    <tr>
        <td>Información</td>
        <td>Número de menciones en noticias de las principales agencias no comunitarias (Associated Press, ITAR-TASS, Xinhua)<br>Ancho de banda instalado (Mbps) </br></td>
        <td>Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
    </tr>
    <tr>
        <td>Tecnología</td>
        <td>Ingresos recibidos del exterior por el uso de la propiedad intelectual y número de solicitudes de patentes orientadas al exterior (relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención).</br>Variable correctora: patentes registradas por cada país miembro en otros Estados miembros</td>
        <td>Eurostat y Organización Mundial de la Propiedad Intelectual (OMPI)</td>
    </tr>
    <tr>
        <td>Ciencia</td>
        <td>Número de artículos, <em>notes</em> y <em>reviews</em> europeos publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias</td>
        <td>Clarivate Analytics vía FECYT</td>
    </tr>
    <tr>
        <td>Educación</td>
        <td>Número de estudiantes extranjeros en educación terciaria en territorio comunitario con procedencia extra-comunitaria</td>
        <td>Eurostat</td>
    </tr>
    <tr>
        <td>Cooperación al desarrollo</td>
        <td>Flujo de ayuda oficial al desarrollo bruta total de todos los estados miembros</td>
        <td>OCDE</td>
    </tr>
        <tr class="section">
        <td colspan="3">Factores de escala</td>
        </tr>
        <tr>
        <td>Economía</td>
        <td>Producto Interior Bruto (PIB) a precios corrientes en dólares EEUU</td>
        <td>Banco Mundial</td>
        </tr>
        <tr>
        <td>Población</td>
        <td>Número de habitantes</td>
            <td>Banco Mundial</td>
        </tr>

    </table>' WHERE key = '_methodology tabla IEPG';

UPDATE www.translation SET en = ' <table class="data">
<tr><th>Variable</th><th>Indicator</th><th>Source</th></tr>
<tr class="section">
    <td colspan="3">Economic presence</td>
</tr>
<tr>
    <td>Energy</td>
    <td>Extra-EU flows of exports of energy products (oil, refined products, and gas) (SITC 3)</td>
    <td rowspan=5>Eurostat</td>
</tr>
<tr>
    <td>Primary goods</td>
    <td>Extra-EU flows of exports of primary goods (food, beverages, tobacco, agricultural commodities, non-ferrous metals, pearls, precious stones, and non-monetary gold), excluding oil (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971)</td>
</tr>
<tr>
    <td>Manufactures</td>
    <td>Extra-EU flows of exports of manufactured goods (chemical products, machinery, transport equipment, other manufactured products) (SITC 5 to 8 minus 667 and 68).</td>
</tr>
<tr>
    <td>Services</td>
    <td>Extra-EU flows of exports of services in transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services</td>
</tr>
<tr>
    <td>Investments</td>
    <td>Stock of foreign direct investment outside the EU</td>
</tr>
<tr class="section">
    <td colspan="3">Military presence</td>
</tr>
<tr>
    <td>Troops</td>
    <td>Number of military personnel deployed in international missions and bases outside the EU</td>
    <td rowspan=2>IISS</td>
</tr>
<tr>
    <td>Military equipment</td>
    <td>Weighted sum of aircraft carriers, big ships, destroyers, frigates, nuclear-powered submarines, amphibious ships, medium and heavy strategic aeroplanes, and air tankers</td>
</tr>
<tr class="section">
    <td colspan="3">Soft presence</td>
</tr>
<tr>
    <td>Migration</td>
    <td>Estimated number of immigrants from outside the EU</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Tourism</td>
    <td>Thousands of arrivals of tourists from outside the EU</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Sports</td>
    <td>Weighted sum of medals won at the summer Olympic Games, points of male and female national teams in the FIFA world ranking and points of male football clubs in the IFFHS.<br>Corrective variable: European audience at the World Cup Final and the opening ceremony of the Olympic Games</br></td>
    <td>FIFA, IFFHS, ICO,<br>Kantar Media and Nielsen</br></td>
</tr>
<tr>
    <td>Culture</td>
    <td>Extra-EU exports of audiovisual and related services (cinematographic productions, radio and television programs, and musical recordings) and cultural goods (antiques and works of art, books, jewelry, newspapers, photography, etc.)</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Information</td>
    <td>Number of mentions in news of main non European press agencies (Associated Press, ITAR-TASS, and Xinhua)<br>Internet bandwidth (Mbps)</br></td>
    <td>Factiva & International Telecommunication Union</td>
</tr>
<tr>
    <td>Technology</td>
    <td>External income for the use of intellectual property and number of foreign-oriented patents (inter-related patent applications filed in one or more foreign countries to protect the same invention).<br>Corrective variable: patents registered for each member state in other member States</br></td>
    <td>Eurostat & World Intellectual Property Organization (WIPO)</td>
</tr>
<tr>
    <td>Science</td>
    <td>Number of European articles, notes, and reviews published in the fields of the arts and humanities, social sciences, and sciences</td>
    <td>Clarivate Analytics via FECYT</td>
</tr>
<tr>
    <td>Education</td>
    <td>Number of non-EU foreign students in tertiary education in the EU</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Development cooperation</td>
    <td>Total gross flows of official development aid for all member States</td>
    <td>OECD</td>
</tr>
<tr class="section">
<td colspan="3">Scaling factors</td>
</tr>
<tr>
<td>Economy</td>
<td>Gross Domestic Product (GDP) at current prices in US dollars</td>
<td>World Bank</td>
</tr>
<tr>
<td>Population</td>
<td>Number of inhabitants</td>
    <td>World Bank</td>
</tr>
</table>' WHERE key = '_methodology tabla IEPG';


UPDATE www.translation SET es = ' <table class="data">
   <tr><th>Variable</th><th>Indicador</th><th>Fuente</th></tr>
   <tr class="section">
       <td colspan="3">Presencia económica</td>
   </tr>
   <tr>
       <td>Energía</td>
       <td>Flujos intra-comunitarios de exportación de productos energéticos (petróleo, productos refinados y gas) (SITC 3)</td>
       <td rowspan=5>Eurostat</td>
   </tr>
   <tr>
       <td>Bienes primarios</td>
       <td>Flujos intra-comunitarios de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667 + 971)</td>
   </tr>
   <tr>
       <td>Manufacturas</td>
       <td>Flujos intra-comunitarios de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68)</td>
   </tr>
   <tr>
       <td>Servicios</td>
       <td>Flujos intra-comunitarios de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos</td>
   </tr>
   <tr>
       <td>Inversiones</td>
       <td><em>Stock</em> de inversión directa extranjera en la UE</td>
   </tr>

   <tr class="section">
       <td colspan="3">Presencia militar</td>
   </tr>
   <tr>
       <td>Tropas</td>
       <td>Valor 0 para todos los países y años</td>
       <td rowspan=2></td>
   </tr>
   <tr>
       <td>Equipamiento militar</td>
       <td>Valor 0 para todos los países y años</td>
   </tr>
   <tr class="section">
       <td colspan="3">Presencia blanda</td>
   </tr>
   <tr>
       <td>Migraciones</td>
       <td>Número estimado de personas migrantes con origen comunitario</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Turismo</td>
       <td>Miles de llegadas de turistas con origen comunitario</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Deportes</td>
       <td>Suma ponderada de los puntos en el medallero en los Juegos Olímpicos de verano, la clasificación mundial FIFA de selecciones absolutas masculinas y femeninas y la clasificación mundial de clubes masculinos de fútbol de IFFHS</td>
       <td>COI, IFFHS y FIFA</td>
   </tr>
   <tr>
       <td>Cultura</td>
       <td>Exportaciones intra-comunitarias de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales) y de bienes culturales (antigüedades y obras de arte, fotografía, libros, joyería, periódicos, etc.)</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Información</td>
       <td>Número de menciones en cables por parte de las principales agencias de noticias europeas (Reuters, AFP, ANSA, DPA y EFE) y ancho de banda de Internet (Mbps)</td>
       <td>Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
   </tr>
   <tr>
       <td>Tecnología</td>
       <td>Ingresos recibidos del exterior por el uso de la propiedad intelectual y número de solicitudes de patentes orientadas al exterior (relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención)</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Ciencia</td>
       <td>Número de artículos, <em>notes</em> y <em>reviews</em> publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias</td>
       <td>Clarivate Analytics vía FECYT</td>
   </tr>
   <tr>
       <td>Educación</td>
       <td>Número de estudiantes extranjeros en educación terciaria con procedencia comunitaria</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Cooperación al desarrollo</td>
       <td>Valor 0 para todos los países y años</td>
       <td></td>
   </tr>
     <tr class="section">
       <td colspan="3">Factores de escala</td>
   </tr>
   <tr>
       <td>Economía</td>
       <td>Producto Interior Bruto (PIB) a precios corrientes en euros</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Población</td>
       <td>Número de habitantes</td>
           <td>Eurostat</td>
   </tr>
    </table>' WHERE key = '_methodology tabla IEPE';

UPDATE www.translation SET en = ' <table class="data">
<tr><th>Variable</th><th>Indicator</th><th>Source</th></tr>
<tr class="section">
    <td colspan="3">Economic presence</td>
</tr>
<tr>
    <td>Energy</td>
    <td>Intra-EU flows of exports of energy products (oil, refined products and gas) (SITC 3)</td>
    <td rowspan=5>Eurostat</td>
</tr>
<tr>
    <td>Primary goods</td>
    <td>Intra-EU flows of exports of primary goods (food, beverages, tobacco, agricultural commodities, non-ferrous metals, pearls, precious stones, and non-monetary gold), excluding oil (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971)</td>
</tr>
<tr>
    <td>Manufactures</td>
    <td>Intra-EU flows of manufactured goods (chemical products, machinery, transport equipment, other manufactured products) (SITC 5 to 8 minus 667 and 68).</td>
</tr>
<tr>
    <td>Services</td>
    <td>Intra-EU flows of exports of services in transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services</td>
</tr>
<tr>
    <td>Investments</td>
    <td>Stock of foreign direct investment in the EU</td>
</tr>

<tr class="section">
    <td colspan="3">Military presence</td>
</tr>
<tr>
    <td>Troops</td>
    <td>Value 0 for all countries and years</td>
    <td rowspan=2></td>
</tr>
<tr>
    <td>Military equipment</td>
    <td>Value 0 for all countries and years</td>
</tr>

<tr class="section">
    <td colspan="3">Soft presence</td>
</tr>
<tr>
    <td>Migration</td>
    <td>Estimated number of immigrants from within the EU</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Tourism</td>
    <td>Thousands of arrivals of tourists from within the EU</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Sports</td>
    <td>Weighted sum of medals won at the summer Olympic Games, points of male and female national teams in the FIFA world ranking and points of male football clubs in the IFFHS</td>
    <td>FIFA, IFFHS & IOC</td>
</tr>
<tr>
    <td>Culture</td>
    <td>Intra-EU exports of audiovisual and related services (cinematographic productions, radio and television programs, and musical recordings) and cultural goods (antiques and works of art, books, jewelry, newspapers, photography, etc.)</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Information</td>
    <td>Number of mentions in news of main european press agencies (Reuters, AFP, DPA, ANSA and EFE) and internet bandwidth (Mbps)</td>
    <td>Factiva & International Telecommunication Union</td>
</tr>
<tr>
    <td>Technology</td>
    <td>Intra-EU external income for the use of intellectual property and number of patent applications at the European Patent Office (EPO)</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Science</td>
    <td>Number of articles published in the fields of the arts and humanities, social sciences and sciences</td>
    <td>Clarivate Analytics via FECYT</td>
</tr>
<tr>
    <td>Education</td>
    <td>Number of EU foreign students in tertiary education</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Development cooperation</td>
    <td>Value 0 for all countries and years</td>
    <td></td>
</tr>
<tr class="section">
    <td colspan="3">Scaling factors</td>
</tr>
<tr>
    <td>Economy</td>
    <td>Gross Domestic Product (GDP) at current prices in Euros</td>
    <td>Eurostat</td>
</tr>
<tr>
    <td>Population</td>
    <td>Number of inhabitants</td>
        <td>Eurostat</td>
</tr>
</table>' WHERE key = '_methodology tabla IEPE';


UPDATE www.translation SET es = 'Ambas. El Índice se compone de tres dimensiones (económica, militar y blanda) que, a su vez, se conforman de variables de distinta naturaleza (desde la energía hasta la cooperación al desarrollo pasando por las tropas desplegadas o el turismo). Así, no solamente permite saber cómo de presentes están los países en el orden global, sino también las características de dichas presencia' WHERE key = '_faq text 6';
UPDATE www.translation SET en = 'Both. The Elcano Global Presence Index is composed of three dimensions (economic, military, and soft presence), which in turn contain variables of differing nature (ranging from energy to development cooperation, to troops deployed or to tourism). It is therefore useful in revealing not only how present countries are in the global order, but also, the nature of said presence' WHERE key = '_faq text 6';

UPDATE www.translation SET es = 'Los pesos asignados a variables y dimensiones están basados en el criterio experto recogido mediante encuestas realizadas en 2011, 2012, 2015, 2018 y 2021, a un panel internacional de especialistas en relaciones internacionales cuyas respuestas se combinaron para determinar el peso de las variables y de las dimensiones' WHERE key = '_faq text 8';
UPDATE www.translation SET en = 'Weights assigned to variables and dimensions are based on experts’ criteria. Surveys were conducted in 2011, 2012, 2015, 2018 and 2021. Questionnaires were sent to specialists in international relations, and answers were combined to determine the weights of variables and dimensions' WHERE key = '_faq text 8';

UPDATE www.translation SET es = 'Se estiman, siguiendo criterio del experto, 5.205 datos de un total de 86.447 observaciones. El número de estimaciones asciende a 6% de la base' WHERE key = '_faq text 9';
UPDATE www.translation SET en = 'In these cases we have also referred to expert opinion. A total of 5,205 data items have been estimated from 86,447 observations. The number of estimations accounts for 6% of the base' WHERE key = '_faq text 9';

UPDATE www.translation SET es = 'Para 1990, 1995, 2000, 2005, y 2010-2021. Desde 2010, el cálculo es anual' WHERE key = '_faq text 10';
UPDATE www.translation SET en = 'For 1990, 1995, 2000, 2005, and 2010-21. Since 2010 the calculation is performed annually' WHERE key = '_faq text 10';

UPDATE www.translation SET es = 'El Índice Elcano de Presencia Global cubre una selección de 150 países que se realiza, en términos generales, siguiendo el orden de estos países por tamaño de PIB' WHERE key = '_faq text 12';
UPDATE www.translation SET en = 'The Elcano Global Presence Index includes 150 countries. These are selected, mainly, according to their size in terms of GDP' WHERE key = '_faq text 12';


UPDATE www.translation SET es = '2014 - 2021 &copy; Real Instituto Elcano' WHERE key = 'Copyright TEXT';
UPDATE www.translation SET en = '2014 - 2021 &copy; Elcano Royal Institute' WHERE key = 'Copyright TEXT';

COMMIT;




BEGIN;

UPDATE www.translation SET es = 'El <a class=\"nostyle\" href=\"%s\"><strong>Índice Elcano de Presencia Global</strong></a> calcula anualmente la proyección de 120 países fuera de sus fronteras en función de tres dimensiones:' WHERE key = '_home IEPG explora desc';
UPDATE www.translation SET en = 'The <a class=\"nostyle\" href=\"%s\"><strong>Elcano Global Presence Index</strong></a> is an annual measurement of the projection in the world of 120 countries based on three dimensions:' WHERE key = '_home IEPG explora desc';


UPDATE www.translation SET es = 'Flujo de exportación de productos energéticos (petróleo, productos refinados y gas) (SITC 3).' WHERE key = 'Variable energy desc TEXTO';
UPDATE www.translation SET en = 'Flow of exports of energy products (oil, refined products, and gas) (SITC 3).' WHERE key = 'Variable energy desc TEXTO';


UPDATE www.translation SET es = 'Flujo de exportación de servicios totales (servicios relacionados a bienes, transporte, viajes, y otros servicios como construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos).' WHERE key = 'Variable services desc TEXTO';
UPDATE www.translation SET en = 'Services: Flow of exports of total services (good related services, transport, travel, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services)' WHERE key = 'Variable services desc TEXTO';


UPDATE www.translation SET es = 'El Índice Elcano de Presencia Global cubre una selección de 120 países. Esta selección se realiza según el orden de estos países en términos de PIB mundial con la excepción de Bahrein, Nepal, Papua Nueva Guinea, Afganistán, Bosnia, Camboya, Laos, Georgia y Albania, que han sido sustituidos por países de África Subsahariana y América Central con la finalidad de aumentar la representación de estas regiones.' WHERE key = '_methodology p1';
UPDATE www.translation SET en = 'This year’s edition covers the global presence of a selection of 120 countries. The selection is done according to the order of these countries in terms of GDP, with the exception of Bahrein, Nepal, Papua Nueva Guinea, Afghanistan, Bosnia, Cambodia, Laos, Georgia and Albania, which have been replaced by countries of sub-Saharan Africa and Central America in order to increase the representation of these regions.' WHERE key = '_methodology p1';


UPDATE www.translation SET es = 'En relación a la selección de países, hay que tener en cuenta que al calcularse en escalas temporales que se remontan a 1990, la intención del proyecto es la de mostrar el ‘mundo de los dos bloques’ –aunque sea en su ocaso–. De este modo, los valores de 1990 de Rusia se refieren, evidentemente, a los de la Unión Soviética, los de Alemania a la República Federal Alemana; y los valores hasta 2005 de Serbia a la Unión Estatal de Serbia y Montenegro. Además, los países de Europa del Este que alcanzaron su independencia tras 1990 no tienen valor asignado para ese año. Es el caso de Azerbaiyán, Bielorrusia, Estonia, Letonia, Lituania, Kazajistán, Turkmenistán, Ucrania y Uzbekistán como parte de la Unión Soviética, de Eslovaquia como parte de Checoslovaquia y de Croacia y Eslovenia como parte de Yugoslavia.' WHERE key = '_methodology países p';
UPDATE www.translation SET en = 'In terms of country selection, bear in mind that by making calculations at time intervals that go back to 1990, the intention of the project is to show the ‘two-bloc world’, even if in decline. Thus, Russia’s 1990 values refer to those of the Soviet Union, those of Germany to the German Federal Republic, those of the Czech Republic to Czechoslovakia, and those values up to 2005 of Serbia to the State Union of Serbia and Montenegro. Moreover, East European countries that became independent after 1990 have no value assigned in that year. This is the case for Azerbaijan, Belarus, Estonia, Latvia, Lithuania, Kazakhstan, Turkmenistan, Ukraine and Uzbekistan as part of the Soviet Union, Slovakia as part of Czechoslovakia, and Croatia and Slovenia as part of Yugoslavia.' WHERE key = '_methodology países p';


UPDATE www.translation SET es = '<table class="data">
   <tr><th>Variable</th><th>Indicador</th><th>Fuente</th></tr>
   <tr class="section">
       <td colspan="3">Presencia económica</td>
   </tr>
   <tr>
       <td>Energía</td>
       <td>Flujo de exportación de productos energéticos (petróleo, productos refinados y gas) (SITC 3)</td>
       <td rowspan=5>UNCTADStat</td>
   </tr>
   <tr>
       <td>Bienes primarios</td>
       <td>Flujo de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971)</td>
   </tr>
   <tr>
       <td>Manufacturas</td>
       <td>Flujo de exportación de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68)</td>
   </tr>
   <tr>
       <td>Servicios</td>
       <td>Flujo de exportación de servicios totales (servicios relacionados a bienes, transporte, viajes, y otros servicios como construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos)</td>
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
       <td rowspan=2>IISS – The Military Balance Report</td>
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
       <td>Base de datos estadística de la Organización Mundial del Turismo de Naciones Unidas (OMT)</td>
   </tr>
   <tr>
       <td>Deportes</td>
       <td>Suma ponderada de los puntos en la clasificación mundial FIFA y del medallero en los Juegos Olímpicos de verano</td>
       <td>FIFA y COI</td>
   </tr>
   <tr>
       <td>Cultura</td>
       <td>Exportaciones de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales)</td>
       <td>Organización Mundial del Comercio (OMC) – International Trade Statistics</td>
   </tr>
   <tr>
       <td>Información</td>
       <td>Número de menciones en noticias de las principales agencias (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua)
    y ancho de banda de Internet (Mbps)</td>
       <td>Base de datos de Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
   </tr>
   <tr>
       <td>Tecnología</td>
       <td>Familia de patentes orientadas al exterior: número de solicitudes de patentes relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención</td>
       <td>Organización Mundial de la Propiedad Intelectual (OMPI)– Statistics Database</td>
   </tr>
   <tr>
       <td>Ciencia</td>
       <td>Número de artículos, <em>notes</em> y <em>reviews</em> publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias</td>
       <td>Thomson Reuters – Web of Knowledge</td>
   </tr>
   <tr>
       <td>Educación</td>
       <td>Número de estudiantes extranjeros en educación terciaria en territorio nacional</td>
       <td>UNESCO – Institute for Statistics</td>
   </tr>
   <tr>
       <td>Cooperación al desarrollo</td>
       <td>Flujo de ayuda oficial al desarrollo bruto total o datos homologables</td>
       <td>OCDE, SEGIB y fuentes nacionales oficiales</td>
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
   <tr><th>Indicator</th><th>Description</th><th>Source</th></tr>
   <tr class="section">
       <td colspan="3">Economic Presence</td>
   </tr>
   <tr>
       <td>Energy</td>
       <td>Flow of exports of energy products (oil, refined products and gas) (SITC 3)</td>
       <td rowspan=5>UNCTADStat</td>
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
       <td>Flow of exports of total services (services related to goods, transport, travel, and other services such as construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services)</td>
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
       <td rowspan=2>IISS – The Military Balance Report</td>
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
       <td>United Nations World Tourism Organization (UNWTO) – Statistics Database</td>
   </tr>
   <tr>
       <td>Sports</td>
       <td>Weighted sum of points in the FIFA world ranking and medals won at summer Olympic Games</td>
       <td>FIFA and IOC</td>
   </tr>
   <tr>
       <td>Culture</td>
       <td>Exports of audiovisual and related services (cinematographic productions, radio and television programs, and musical recordings)</td>
       <td>WTO – International Trade Statistics</td>
   </tr>
   <tr>
       <td>Information</td>
       <td>Number of mentions in news of main international press agencies (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua) and internet bandwidth (Mbps)</td>
       <td>Factiva database International Telecommunication Union</td>
   </tr>
   <tr>
       <td>Technology</td>
       <td>Foreign-oriented patents family: number of inter-related patent applications filed in one or more foreign countries to protect the same invention</td>
       <td>World Intellectual Property Organization (WIPO) – Statistics Database</td>
   </tr>
   <tr>
       <td>Science</td>
       <td>Number of articles, notes, and reviews published in the fields of the arts and humanities, social sciences, and sciences</td>
       <td>Thomson Reuters – Web of Knowledge</td>
   </tr>
   <tr>
       <td>Education</td>
       <td>Number of foreign students in tertiary education on national territory</td>
       <td>UNESCO – Institute for Statistics, OECD – iLibrary</td>
   </tr>
   <tr>
       <td>Development cooperation</td>
       <td>Total gross flows of official development aid or comparable data</td>
       <td>OECD, SEGIB and official national sources</td>
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

UPDATE www.translation SET es = 'Desde el 2012 el Índice Elcano de Presencia Global calcula además para la Unión Europea de los 28 países. Este ejercicio trata de cuantificar la proyección global de la Unión, como si se tratase de un supuesto súper-estado con identidad propia, medición que se complementa con el Índice Elcano de Presencia Europea que por el contrario evalúa la presencia de los países miembros dentro del perímetro de la Unión.' WHERE key = '_methodology incorporación UE p';


UPDATE www.translation SET es = ' <table class="data">

   <tr><th>Variable</th><th>Variable</th><th>Fuente</th></tr>
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
       <td>Flujos extra-comunitarios de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971)</td>
   </tr>
   <tr>
       <td>Manufacturas</td>
       <td>Flujos extra-comunitarios de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68)</td>
   </tr>
   <tr>
       <td>Servicios</td>
       <td>Flujos extra-comunitarios de exportación de servicios totales (transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos)</td>
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
       <td rowspan=2>IISS – The Military Balance Report</td>
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
       <td>Suma ponderada de los puntos en la clasificación mundial FIFA y del medallero en los Juegos Olímpicos de verano para cada EM de la UE.<br>Variable correctora: audiencia europea de la final del mundial y de la ceremonia de apertura de los Juegos Olímpicos</br></td>
       <td>FIFA y COI<br> Informes de Kantar Media y Nielsen</br></td>
   </tr>
   <tr>
       <td>Cultura</td>
       <td>Exportaciones extra-comunitarias de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales)</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Información</td>
       <td>Número de menciones en noticias de las principales agencias no comunitarias (Associated Press, ITAR-TASS, Xinhua)<br>Ancho de banda instalado (Mbps) </br></td>
       <td>Base de datos de Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
   </tr>
   <tr>
       <td>Tecnología</td>
       <td>Patentes orientadas al exterior por el total de países miembros de la UE: número de solicitudes de patentes relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención.<br> Variable correctora: patentes registradas por cada país miembro en otros estados miembros</br></td>
       <td>Organización Mundial de la Propiedad Intelectual (OMPI) – StatisticsDatabase</td>
   </tr>
   <tr>
       <td>Ciencia</td>
       <td>Número de artículos, <em>notes</em> y <em>reviews</em> europeos publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias</td>
       <td>Thomson Reuters – Web of Knowledge</td>
   </tr>
   <tr>
       <td>Educación</td>
       <td>Número de estudiantes extranjeros en educación terciaria en territorio comunitario con procedencia extra-comunitaria</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Cooperación al desarrollo</td>
       <td>Flujo de ayuda oficial al desarrollo bruta total de todos los estados miembros</td>
       <td>OCDE)</td>
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

     <tr><th>Indicator</th><th>Description</th><th>Source</th></tr>
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
         <td>Extra-EU exports flows of total services (transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services)</td>
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
         <td rowspan=2>IISS – The Military Balance Report</td>
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
         <td>Weighted sum of points in the FIFA world ranking and medals won at summer Olympic Games for each EU member state<br>Corrective variable: European audience at the World Cup Final and the opening ceremony of the Olympic Games</br></td>
         <td>FIFA and ICO<br>Reports by Kantar Media and Nielsen</br></td>
     </tr>
     <tr>
         <td>Culture</td>
         <td>Extra-EU exports of audiovisual and related services (cinematographic productions, radio and television programs, and musical recordings)</td>
         <td>Eurostat.</td>
     </tr>
     <tr>
         <td>Information</td>
         <td>Number of mentions in news of main non European press agencies (Associated Press, ITAR-TASS, and Xinhua)<br>Internet bandwidth (Mbps)</br></td>
         <td>Factiva database International Telecommunication Union</td>
     </tr>
     <tr>
         <td>Technology</td>
         <td>Foreign-oriented patents for the total EU member States: number of inter-related patent applications filed in one or more foreign countries to protect the same invention.<br>Corrective variable: patents registered for each member state in other member States</br></td>
         <td>World Intellectual Property Organization (WIPO) – Statistics Database</td>
     </tr>
     <tr>
         <td>Science</td>
         <td>Number of European articles, notes, and reviews published in the fields of the arts and humanities, social sciences, and sciences</td>
         <td>Thomson Reuters – Web of Knowledge</td>
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
       <td>Flujos intra-comunitarios de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971)</td>
   </tr>
   <tr>
       <td>Manufacturas</td>
       <td>Flujos intra-comunitarios de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68)</td>
   </tr>
   <tr>
       <td>Servicios</td>
       <td>Flujos intra-comunitarios de exportación de servicios totales (transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos)</td>
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
       <td>Suma ponderada de los puntos en la clasificación mundial FIFA y del medallero en los Juegos Olímpicos de verano</td>
       <td>FIFA y COI</td>
   </tr>
   <tr>
       <td>Cultura</td>
       <td>Exportaciones intra-comunitarias de servicios audiovisuales y relacionados (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales)</td>
       <td>Eurostat y fuentes nacionales</td>
   </tr>
   <tr>
       <td>Información</td>
       <td>Número de menciones en cables por parte de las principales agencias de noticias europeas (Reuters, AFP, ANSA, DPA y EFE) y ancho de banda de Internet (Mbps)</td>
       <td>Base de datos de Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
   </tr>
   <tr>
       <td>Tecnología</td>
       <td>Número de patentes solicitadas en la Oficina Europea de Patentes (EPO)</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Ciencia</td>
       <td>Número de artículos, <em>notes</em> y <em>reviews</em> publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias</td>
       <td>Thomson Reuters – Web of Knowledge</td>
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
   <tr><th>Indicator</th><th>Description</th><th>Source</th></tr>
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
       <td>Intra-EU export flows of total services (transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services)</td>
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
       <td>Weighted sum of points in the FIFA world ranking and medals won at the summer Olympic Games</td>
       <td>FIFA and IOC</td>
   </tr>
   <tr>
       <td>Culture</td>
       <td>Intra-EU exports of audiovisual and related services (cinematographic productions, radio and television programmes, and musical recordings)</td>
       <td>Eurostat and national sources</td>
   </tr>
   <tr>
       <td>Information</td>
       <td>Number of mentions in news of main european press agencies (Reuters, AFP, DPA, ANSA and EFE) and internet bandwidth (Mbps)</td>
       <td>Factiva database International Telecommunication Union</td>
   </tr>
   <tr>
       <td>Technology</td>
       <td>Number of patent applications at the European Patent Office (EPO)</td>
       <td>Eurostat</td>
   </tr>
   <tr>
       <td>Science</td>
       <td>Number of articles published in the fields of the arts and humanities, social sciences and sciences</td>
       <td>Thomson Reuters – Web of Knowledge</td>
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

UPDATE www.translation SET es = 'Este Índice mide la presencia global. Por presencia global entendemos la proyección efectiva real de los países fuera de sus fronteras en los ámbitos económico, militar y blando (exportaciones realizadas, turistas recibidos, competiciones deportivas internacionales ganadas…)' WHERE key = '_faq text 1';
UPDATE www.translation SET en = 'The Index measures global presence. By global presence, we understand the effective positioning, in absolute terms, of the different countries outside its borders in the economic, military and soft areas (products sold, tourists welcomed, victories in international sports competitions…)' WHERE key = '_faq text 1';

UPDATE www.translation SET es = 'Para ello, se ha recurrido al criterio del experto. Se han estimado 2.653 datos de un total de 57.672 observaciones. El número de estimaciones asciende a 4,6%de la base' WHERE key = '_faq text 9';
UPDATE www.translation SET en = 'In these cases we have also referred to expert opinion. A total of 2,653 data items have been estimated from 57,672 observations. The number of estimations accounts for 4.6% of the base' WHERE key = '_faq text 9';

UPDATE www.translation SET es = 'El Índice Elcano de Presencia Global cubre una selección de 120 países. Esta selección se realiza según el orden de estos países en términos de PIB mundial con la excepción de Bahrein, Nepal, Papua Nueva Guinea, Afganistán, Bosnia, Camboya, Laos, Georgia y Albania, que han sido sustituidos por países de África Subsahariana y América Central con la finalidad de aumentar la representación de estas regiones' WHERE key = '_faq text 12';
UPDATE www.translation SET en = 'The Elcano Global Presence Index is calculated for 120 countries. The selection is done according to the order of these countries in terms of GDP, with the exception of Bahrein, Nepal, Papua Nueva Guinea, Afghanistan, Bosnia, Cambodia, Laos, Georgia and Albania, which have been replaced by countries of sub-Saharan Africa and Central America in order to increase the representation of these regions.' WHERE key = '_faq text 12';

UPDATE www.translation SET es = 'Para 1990, 1995, 2000, 2005, y 2010-2018. Desde 2010, el cálculo es anual' WHERE key = '_faq title 10';
UPDATE www.translation SET en = 'For 1990, 1995, 2000, 2005, and 2010-18. Since 2010 the calculation is performed annually.' WHERE key = '_faq title 10';


COMMIT;

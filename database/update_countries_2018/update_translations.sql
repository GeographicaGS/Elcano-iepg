--dcp exec pgsql pg_dump elcano_iepg -h localhost -U postgres --column-inserts -t www.translation > database/update_countries_2018/update_translations_2.sql
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET search_path = www, pg_catalog;


BEGIN;

DELETE FROM translation;

--
-- Data for Name: translation; Type: TABLE DATA; Schema: www; Owner: elcano_iepg_admin
--

INSERT INTO translation (key, en, es) VALUES ('_methodology países p', 'Finally, in terms of country selection, bear in mind that by making calculations at time intervals that go back to 1990, the intention of the project is to show the ‘two-bloc world’, even if in decline. Thus, Russia’s 1990 values refer to those of the Soviet Union, those of Germany to the German Federal Republic, those of the Czech Republic to Czechoslovakia. Moreover, East European countries that became independent after 1990 have no value assigned in that year. This is the case for Azerbaijan, Belarus, Estonia, Latvia, Lithuania, Kazakhstan, Turkmenistan, Ukraine and Uzbekistan as part of the Soviet Union, Slovakia as part of Czechoslovakia, and Croatia and Slovenia as part of Yugoslavia', 'En relación a la selección de países, hay que tener en cuenta que al calcularse calas temporales que se remontan a 1990, la intención del proyecto es la de mostrar el ‘mundo de los dos bloques’ –aunque sea en su ocaso–. De este modo, los valores de 1990 de Rusia se refieren, evidentemente, a los de la Unión Soviética, los de Alemania a la República Federal Alemana. Además, los países de Europa del Este que alcanzaron su independencia tras 1990 no tienen valor asignado para ese año. Es el caso de Azerbaiyán, Bielorrusia, Estonia, Letonia, Lituania, Kazajistán, Turkmenistán, Ucrania y Uzbekistán como parte de la Unión Soviética, de Eslovaquia como parte de Checoslovaquia y de Croacia y Eslovenia como parte de Yugoslavia');
INSERT INTO translation (key, en, es) VALUES ('_faq text 7', 'First, presence is reflected in a single direction, what could be deemed its unidirectionality. Second, the results of presence are measured but not the means to achieve them. In addition, all the variables have an explicitly external component, in the sense that they reflect cross-border presence. Presence is given in absolute and not relative terms; the indicators are not proportional to the demographic or economic size of the country. Likewise, as for any other index, the best explanatory capacity is sought with the fewest variables or indicators possible. Finally, hard data on presence are taken, and not data based on judgments or opinions', 'Se recoge la presencia en una única dirección, lo que podría denominarse unidireccionalidad de la presencia. En segundo lugar, se miden resultados de presencia y no los medios para conseguirlos. Además, todas las variables tienen un componente expresamente exterior, reflejando la presencia transfronteriza. La presencia se da en términos absolutos y no relativos al tamaño de la economía o la población. Asimismo, como para cualquier otro índice, se busca la máxima capacidad explicativa con el mínimo número posible de variables e indicadores. Por último, se toman datos duros de presencia y no datos basados en juicios u opiniones');
INSERT INTO translation (key, en, es) VALUES ('_faq text 13', 'Not exactly. Presence of different countries can be combined, showing regional trends of global presence. Moreover, as new editions include an increasing number of countries, for some regions (i.e. Latin America or East Asia) the number of countries selected for the Index is high enough to consider the aggregated index value as a fair reflection of the external projection of the whole region.
However, it is important to note that, in these cases, the total index value is recording the relative presence of some countries within others of the same group or region (i.e. the global presence index value of Latin America includes the relative presence of Argentina in Brazil). Thus, the adding together of global presences should not be considered a metric of a given region’s external projection outside its collective boundaries
', 'No exactamente. La presencia de distintos países puede sumarse, mostrando tendencias regionales de presencia global. Además, a medida que nuevas ediciones van incorporando un número creciente de países, para algunas regiones (como América Latina o Asia), el número de éstos incluidos en el Índice es suficientemente grande como para considerar que su valor agregado es un buen reflejo de la proyección combinada del conjunto de la región. No obstante, también es importante señalar que, en estos casos, el valor total del Índice está recogiendo la presencia relativa de unos países en otros del mismo grupo o región (el valor de la presencia agregada de América Latina estaría incluyendo la presencia relativa de Argentina en Brasil). Siendo así, la presencia global total no debería ser considerada como la proyección de una región fuera de sus fronteras');
INSERT INTO translation (key, en, es) VALUES ('_faq text 14', 'No, for the aforementioned reason. We must bear in mind that the global presence of the member states is partially reflected in other member states of the Union. In order to apply the Index to the European Union, intra-European presence must be deducted. The intra-European presence of the member states is precisely what the Elcano European Presence Index measures', 'No, por la misma razón. Hay que tener en consideración que la presencia global de los Estados miembros se da parcialmente en otros países de la Unión. Para poder calcular el Índice aplicado a la Unión Europea, se ha descontado esta presencia intra-europea. Y es precisamente esta presencia intra-europea la que mide el Índice Elcano de Presencia Europea');
INSERT INTO translation (key, en, es) VALUES ('Ranking descripción TEXTO', 'The ranking tool orders countries and regions by their index value on the basis of their

global presence and dimensions (economic, military or soft) and of any of their other

indicators.

In every case, the ranking for a specific year can be compared to those of others by

using the time selector.', 'La herramienta de ranking ordena los países o bloques por su valor índice . Dicha ordenación puede realizarse sobre la base de su presencia global, de sus dimensiones (económica, militar o blanda) o de cualquiera de los indicadores que componen estas.

En todos los casos, la ordenación para un año concreto puede compararse con la que se da en otro año de referencia, a través del selector de tiempo.');
INSERT INTO translation (key, en, es) VALUES ('Si usted tiene alguna pregunta o problema relacionado con este portal, por favor escríbanos a', 'If you have technical problems related to this web, please send an e-mail to', 'Si usted tiene alguna pregunta o problema relacionado con este portal, por favor escríbanos a');
INSERT INTO translation (key, en, es) VALUES ('Países más UE', 'Countries + EU', 'Países + UE');
INSERT INTO translation (key, en, es) VALUES ('Cuotas de presencia descripción TEXTO', 'This tool allows the presence quotas between countries and regions to be compared over

time.

The presence quota is the expression of the external projection of a specific country as

a proportion of total global presence. In order to calculate it, the index value of global

presence of a country is divided by the sum of total global presence –of the 70 different

countries for which the Index is calculated– and then multiplied by 100.', 'Esta herramienta permite comparar las cuotas de presencia de países y bloques a lo largo del tiempo.
La cuota de presencia es la proporción de proyección exterior que un determinado país ocupa en el universo de la presencia global total. Para su cálculo, se divide el valor índice de presencia global de un país por la suma de presencia global total- la de los 70 países para los que calculamos el índice-, y se multiplica por 100.');
INSERT INTO translation (key, en, es) VALUES ('Ayuda contribuciones de presencia', 'Presence contribution help', 'Ayuda contribuciones de presencia');
INSERT INTO translation (key, en, es) VALUES ('Económica', 'Economic', 'Económica');
INSERT INTO translation (key, en, es) VALUES ('Militar', 'Military', 'Militar');
INSERT INTO translation (key, en, es) VALUES ('Blanda', 'Soft', 'Blanda');
INSERT INTO translation (key, en, es) VALUES ('La incorporación de la Unión Europea al Índice Elcano de Presencia Global', 'The inclusion of the European Union in the Elcano Global Presence Index', 'La incorporación de la Unión Europea al Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de presencia global', 'Elcano Global Presence Index', 'Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Ningún país filtrado', 'No countries filtered', 'Ningún país filtrado');
INSERT INTO translation (key, en, es) VALUES ('No hay datos disponibles con los parámetros seleccionados', 'There is no data available with the criteria selected', 'No hay datos disponibles con los parámetros seleccionados');
INSERT INTO translation (key, en, es) VALUES ('y', 'and', 'y');
INSERT INTO translation (key, en, es) VALUES ('No hay datos para la configuración seleccionada', 'There is no data available with the configuration selected', 'No hay datos para la configuración seleccionada');
INSERT INTO translation (key, en, es) VALUES ('No hay herramientas seleccionadas', 'There are no tools selected', 'No hay herramientas seleccionadas');
INSERT INTO translation (key, en, es) VALUES ('Países A - Z', 'Countries A - Z', 'Países A - Z');
INSERT INTO translation (key, en, es) VALUES ('Se ha seleccionado presencia europea y es un país no europeo o un bloque', 'European presence has been selected, but it is not either an european country or a block', 'Se ha seleccionado presencia europea y es un país no europeo o un bloque');
INSERT INTO translation (key, en, es) VALUES ('Si no es debido a ninguno de los puntos anteriores consulte la ayuda de la herramienta, pulsando la &apos;i&apos; de información de la esquina superior derecha', 'If not due to any of the above points, please check the tool help clicking on the &apos;i&apos; information in the upper right corner', 'Si no es debido a ninguno de los puntos anteriores consulte la ayuda de la herramienta pulsando la &apos;i&apos; de información de la esquina superior derecha');
INSERT INTO translation (key, en, es) VALUES ('Presencia global frente a presencia europea', 'Global presence facing European Presence', 'Presencia global frente a presencia europea');
INSERT INTO translation (key, en, es) VALUES ('Puesto %dº ', 'Position %dº', 'Puesto %dº');
INSERT INTO translation (key, en, es) VALUES ('_help p3 subtitle', 'Select Index’ countries, dimensions, and variables', 'Seleccione países, dimensiones y variables del Índice');
INSERT INTO translation (key, en, es) VALUES ('contribuciones no pais titulo', 'Country?', '¿País?');
INSERT INTO translation (key, en, es) VALUES ('Línea de tiempo', 'Timeslider', 'Línea de tiempo');
INSERT INTO translation (key, en, es) VALUES ('Selector de países y variables', 'Countries and variables selector', 'Selector de países y variables');
INSERT INTO translation (key, en, es) VALUES ('No volver a mostrar la ayuda', 'Don''t show help again', 'No volver a mostrar la ayuda');
INSERT INTO translation (key, en, es) VALUES ('Empezar con la ayuda guiada', 'Start with the guided help', 'Empezar con la ayuda guiada');
INSERT INTO translation (key, en, es) VALUES ('Los filtros', 'Filters', 'Los filtros');
INSERT INTO translation (key, en, es) VALUES ('Desmarcar todo', 'Unselect all', 'Desmarcar todo');
INSERT INTO translation (key, en, es) VALUES ('Filtro de países', 'Countries filter', 'Filtro de países');
INSERT INTO translation (key, en, es) VALUES ('Suba un fichero PDF/lang>"),void setTimeout(function(){o.html("")},8e3)):(max_allow=8,s/1048576>max_allow?(o.html("El fichero no puede ser mayor de ', 'Load a PDF file/lang>"),void setTimeout(function(){o.html("")},8e3)):(max_allow=8,s/1048576>max_allow?(o.html("File shouldn''t be bigger than ', 'Suba un fichero PDF/lang>"),void setTimeout(function(){o.html("")},8e3)):(max_allow=8,s/1048576>max_allow?(o.html("El fichero no puede ser mayor de');
INSERT INTO translation (key, en, es) VALUES ('Añadir países...', 'Add countries...', 'Añadir países...');
INSERT INTO translation (key, en, es) VALUES ('Las herramientas', 'The tools', 'Las herramientas');
INSERT INTO translation (key, en, es) VALUES ('Mostrar mapa', 'Show map', 'Mostrar mapa');
INSERT INTO translation (key, en, es) VALUES ('_about body infr', 'Weighting factors of the different areas and indicators', 'Coeficientes de ponderación por áreas e indicadores');
INSERT INTO translation (key, en, es) VALUES ('Are you sure?', 'Are you sure?', '¿Está seguro?');
INSERT INTO translation (key, en, es) VALUES ('Hecho', 'Done', 'Hecho');
INSERT INTO translation (key, en, es) VALUES ('Año', 'Year', 'Año');
INSERT INTO translation (key, en, es) VALUES ('%d herramientas seleccionadas', '%d tools selected', '%d herramientas seleccionadas');
INSERT INTO translation (key, en, es) VALUES ('Presencia Blanda', 'Soft Presence', 'Presencia Blanda');
INSERT INTO translation (key, en, es) VALUES ('_help p4 subtitle', 'Discover the Index from its time dimension...', 'Explore el Índice en su dimensión temporal...');
INSERT INTO translation (key, en, es) VALUES ('Ranking de', 'Ranking of', 'Ranking de');
INSERT INTO translation (key, en, es) VALUES ('_help p2 subtitle', 'Focus analysis on key countries', 'Centre sus análisis en aquellos países que le interesan');
INSERT INTO translation (key, en, es) VALUES ('Field required', 'Field required', 'Campo obligatorio');
INSERT INTO translation (key, en, es) VALUES ('_help welcome txt_2', 'This quick tutorial explains the uses and functionality of Explora key''s elements.', 'Tómese un momento para consultar la ayuda guiada que le mostrará los principales elementos funcionales de Explora.');
INSERT INTO translation (key, en, es) VALUES ('Ficha país', 'Country file', 'Ficha país');
INSERT INTO translation (key, en, es) VALUES ('Ayuda presencia global frente a presencia europea', 'Global Presence facing European Presence', 'Ayuda presencia global frente a presencia europea');
INSERT INTO translation (key, en, es) VALUES ('Presencia global frente a presencia europea descripción TEXTO', 'This tool links Elcano Global Presence Index with Elcano European Presence Index, which calculates the same economic, military and economic dimensions and variables for each of the European Union member states whitin the Union borders.', 'Esta herramienta pone en relación el Índice Elcano de Presencia Global con el Índice Elcano de Presencia Europea, que calcula las mismas variables y dimensiones económica, militar y blanda para cada uno de los estados miembros dentro de las fronteras de la Unión Europea.');
INSERT INTO translation (key, en, es) VALUES ('_help p5 subtitle', '… and in its spatial dimension', '… y en su dimensión espacial');
INSERT INTO translation (key, en, es) VALUES ('_help p6 subtitle', 'Need help?', '¿Necesita ayuda?');
INSERT INTO translation (key, en, es) VALUES ('No volver a mostrar al iniciar', 'Don''t show help again', 'No volver a mostrar al iniciar');
INSERT INTO translation (key, en, es) VALUES ('Eventos', 'Events', 'Eventos');
INSERT INTO translation (key, en, es) VALUES ('Idioma', 'Language', 'Idioma');
INSERT INTO translation (key, en, es) VALUES ('Explora', 'Explora', 'Explora');
INSERT INTO translation (key, en, es) VALUES ('Loading', 'Loading', 'Cargando');
INSERT INTO translation (key, en, es) VALUES ('Imagen siguiente', 'Next image', 'Imagen siguiente');
INSERT INTO translation (key, en, es) VALUES ('Más noticias', 'More news', 'Más noticias');
INSERT INTO translation (key, en, es) VALUES ('Novedades', 'Recent events', 'Novedades');
INSERT INTO translation (key, en, es) VALUES ('Política de privacidad', 'Privacy politics', 'Política de privacidad');
INSERT INTO translation (key, en, es) VALUES ('Cuotas de presencia', 'Evolution of global presence quotas', 'Evolución de cuotas de presencia');
INSERT INTO translation (key, en, es) VALUES ('resultados', 'results', 'Resultados');
INSERT INTO translation (key, en, es) VALUES ('Bloques', 'Blocs', 'Bloques');
INSERT INTO translation (key, en, es) VALUES ('_faq title 6', 'Does it measure merely the ‘quantity’ of a country’s presence or also its nature?', '¿Mide sólo la ‘cantidad’ de presencia o también su naturaleza?');
INSERT INTO translation (key, en, es) VALUES ('_faq text 6', 'Both. The Elcano Global Presence Index is composed of three dimensions (economic, military, and soft presence), which in turn are composed of variables of differing nature (ranging from energy to development cooperation, to troops deployed or to tourism). It is therefore useful in revealing not only how present countries are in the global order, but also, the nature of said presence', 'Ambas. El Índice se compone de tres dimensiones (económica, militar y blanda) que, a su vez, se conforman de variables de distinta naturaleza (desde la energía hasta la cooperación al desarrollo pasando por las tropas desplegadas o el turismo). Así, no solamente permite saber cómo de presentes están los países en el orden global, sino también las características de dichas presencia');
INSERT INTO translation (key, en, es) VALUES ('Nueva etiqueta en inglés', 'New English label', 'Nueva etiqueta en inglés');
INSERT INTO translation (key, en, es) VALUES ('Resumen', 'Abstract', 'Resumen');
INSERT INTO translation (key, en, es) VALUES ('spanish', 'Spanish', 'español');
INSERT INTO translation (key, en, es) VALUES ('Buscar', 'Search', 'Buscar');
INSERT INTO translation (key, en, es) VALUES ('buscar noticia', 'search news', 'buscar noticia');
INSERT INTO translation (key, en, es) VALUES ('Cuerpo*', 'Body*', 'Cuerpo*');
INSERT INTO translation (key, en, es) VALUES ('El fichero no puede ser mayor de ', 'File can''t exceed', 'El fichero no puede ser mayor de');
INSERT INTO translation (key, en, es) VALUES ('_help p5 txt', 'Explora includes an interactive map on which Index data are displayed. Although

some tools include their own embedded map, a full screen map is always accessible

below the tool display area. Click the button to conceal and deploy the tool area and

access the map.', 'Explora cuenta con un mapa interactivo en el que se cartografían los datos visualizados en la herramienta de análisis activa. Aunque algunas herramientas incluyen su propio mapa, el mapa a pantalla completa siempre está disponible para su consulta bajo la herramienta. Pulse este botón para retraer la herramienta y ver el mapa. Vuelva a pulsarlo para volver a ver la herramienta.');
INSERT INTO translation (key, en, es) VALUES ('_help p6 txt', 'To access again the help tutorial, please click here. Don’t forget that all tools have

their own explanatory help notes.', 'Para volver a consultar esta guía rápida, sírvase pulsar este botón. No olvide que cada herramienta de análisis contiene su propia ayuda que le explicará sus pormenores y especificidades.');
INSERT INTO translation (key, en, es) VALUES ('File not supported, please upload a PDF file', 'File not supported, please upload a PDF file', 'Fichero no soportado, por favor suba un PDF');
INSERT INTO translation (key, en, es) VALUES ('Guardar noticia', 'Save news', 'Guardar noticia');
INSERT INTO translation (key, en, es) VALUES ('Más documentos', 'More documents', 'Más documentos');
INSERT INTO translation (key, en, es) VALUES ('No hay etiquetas definidas', 'There are no labels defined', 'No hay etiquetas definidas');
INSERT INTO translation (key, en, es) VALUES ('Noticias', 'News', 'Noticias');
INSERT INTO translation (key, en, es) VALUES ('Nueva', 'New', 'Nueva');
INSERT INTO translation (key, en, es) VALUES ('Please, check fields in red.', 'Please, check fields in red.', 'Por favor, revise los campos en rojo.');
INSERT INTO translation (key, en, es) VALUES ('Suba una image JPEG', 'Load a JPEG image', 'Suba una imagen JPEG');
INSERT INTO translation (key, en, es) VALUES ('This file is bigger than the maximun allowed', 'This file is bigger than the maximun allowed', 'Este fichero es de mayor peso que el permitido');
INSERT INTO translation (key, en, es) VALUES ('Tamaño de imagen incorrecto, el ancho tiene que ser de 1920px y el alto mayor que 480px', 'Incorrect image size, width should be 1920px and height up to 480px', 'Tamaño de imagen incorrecto, el ancho tiene que ser de 1920px y el alto mayor que 480px');
INSERT INTO translation (key, en, es) VALUES ('_privacity title', 'Privacity politics', 'Política de privacidad');
INSERT INTO translation (key, en, es) VALUES ('Tema*', 'Topic*', 'Tema*');
INSERT INTO translation (key, en, es) VALUES ('Título *', 'Title *', 'Título *');
INSERT INTO translation (key, en, es) VALUES ('Twitter', 'Twitter', 'Twitter');
INSERT INTO translation (key, en, es) VALUES ('Variable science desc TEXTO', 'Number of articles published in the fields of the arts and humanities, social sciences, and sciences.', 'Número de artículos publicados en los ámbitos de artes y humanidades, ciencias sociales y ciencias.');
INSERT INTO translation (key, en, es) VALUES ('Variable education desc TEXTO', 'Number of foreign students in tertiary education on national territory.', 'Número de estudiantes extranjeros en educación terciaria en territorio nacional.');
INSERT INTO translation (key, en, es) VALUES ('Información', 'Information', 'Información');
INSERT INTO translation (key, en, es) VALUES ('Síguenos en', 'Follow us', 'Síguenos en');
INSERT INTO translation (key, en, es) VALUES ('Todas', 'All', 'Todas');
INSERT INTO translation (key, en, es) VALUES ('Añadir', 'Add', 'Añadir');
INSERT INTO translation (key, en, es) VALUES ('lang', 'en', 'es');
INSERT INTO translation (key, en, es) VALUES ('_link home', 'home', 'inicio');
INSERT INTO translation (key, en, es) VALUES ('_link about', 'about', 'acerca_de');
INSERT INTO translation (key, en, es) VALUES ('_link docs', 'documents', 'documentos');
INSERT INTO translation (key, en, es) VALUES ('_link doc', 'document', 'documento');
INSERT INTO translation (key, en, es) VALUES ('_link contact', 'contact', 'contacto');
INSERT INTO translation (key, en, es) VALUES ('_link news', 'news', 'noticias');
INSERT INTO translation (key, en, es) VALUES ('_methodology países h6', 'Countries listed in the Elcano Global Presence Index', 'Lista de países del Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('_faq title 1', 'What does the Elcano Global Presence Index measure?', '¿Qué mide el Índice Elcano de Presencia Global?');
INSERT INTO translation (key, en, es) VALUES ('_faq title 2', 'Does the Elcano Global Presence Index measure power?', '¿El Índice Elcano de Presencia Global mide el poder?');
INSERT INTO translation (key, en, es) VALUES ('noticias', 'news', 'noticias');
INSERT INTO translation (key, en, es) VALUES ('_faq title 4', 'Does it measure the openness of countries?', '¿Y su apertura?');
INSERT INTO translation (key, en, es) VALUES ('_faq title 5', 'Is it calculated with objective or subjective data?', '¿Se calcula con datos objetivos o subjetivos?');
INSERT INTO translation (key, en, es) VALUES ('_link about infr', 'structure', 'estructura');
INSERT INTO translation (key, en, es) VALUES ('_link about meth', 'methodologic', 'metodologia');
INSERT INTO translation (key, en, es) VALUES ('buscar noticias ', 'search news', 'buscar noticias');
INSERT INTO translation (key, en, es) VALUES ('Tema', 'Topic', 'Tema');
INSERT INTO translation (key, en, es) VALUES ('Título', 'Title', 'Título');
INSERT INTO translation (key, en, es) VALUES ('La búsqueda no obtuvo ningún resultado.', 'The search didn''t get any results.', 'La búsqueda no obtuvo ningún resultado.');
INSERT INTO translation (key, en, es) VALUES ('Más', 'More', 'Más');
INSERT INTO translation (key, en, es) VALUES ('Sede', 'Headquarters', 'Sede');
INSERT INTO translation (key, en, es) VALUES ('TEMA', 'TOPIC', 'TEMA');
INSERT INTO translation (key, en, es) VALUES ('Variable investments desc TEXTO', 'Stock of foreign direct investment abroad.', 'Stock de inversión directa extranjera en el exterior.');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Administración', 'Elcano Global Presence Index – Administration', 'Índice Elcano de Presencia Global - Administración');
INSERT INTO translation (key, en, es) VALUES ('_methodology tabla IEPG', '<table class=''data''>

    <tr><th>Indicator</th><th>Description</th><th>Source</th></tr>
    <tr class=''section''>
        <td colspan=''3''>Economic presence</td>
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
    <tr class=''section''>
        <td colspan=''3''>Military presence</td>
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
    <tr class=''section''>
        <td colspan=''3''>Soft presence</td>
    </tr>
    <tr>
        <td>Migration</td>
        <td>Estimated number of immigrants from outside the EU</td>
        <td>United Nations Population Division and Eurostat</td>
    </tr>
    <tr>
        <td>Tourism</td>
        <td>Thousands of arrivals of tourists from outside the EU</td>
        <td>Statistics database of the United Nations World Tourism Organization (UNWTO) and Eurostat</td>
    </tr>
    <tr>
        <td>Sports</td>
        <td>Weighted sum of points in the FIFA world ranking and medals won at summer Olympic Games for each EU member state<br>Corrective variable: European audience at the World Cup Final and the opening ceremony of the Olympic Games</br></td>
        <td>FIFA and ICO<br>Reports by Kantar Media and Nielsen</br></td>
    </tr>
    <tr>
        <td>Culture</td>
        <td>Extra-EU exports of audiovisual services (cinematographic productions, radio and television programs, and musical recordings)</td>
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
        <td>UNESCO – Institute for Statistics, OECD – iLibrary and Eurostat</td>
    </tr>
    <tr>
        <td>Development cooperation</td>
        <td>Total gross flows of official development aid for all member States</td>
        <td>OECD</td>
    </tr>
  <tr class=''section''>
      <td colspan=''3''>Scaling factors</td>
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
</table>', '<table class=''data''>

    <tr><th>Variable</th><th>Variable</th><th>Fuente</th></tr>
    <tr class=''section''>
        <td colspan=''3''>Presencia económica</td>
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
        <td>Flujos extra-comunitarios de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos</td>
    </tr>
    <tr>
        <td>Inversiones</td>
        <td><em>Stock</em> de inversión directa extranjera en el exterior de la UE</td>
    </tr>

    <tr class=''section''>
        <td colspan=''3''>Presencia militar</td>
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

    <tr class=''section''>
        <td colspan=''3''>Presencia blanda</td>
    </tr>
    <tr>
        <td>Migraciones</td>
        <td>Número estimado de personas migrantes con origen extra-comunitario</td>
        <td>División de Población de Naciones Unidas, Eurostat y OCDE</td>
    </tr>
    <tr>
        <td>Turismo</td>
        <td>Miles de llegadas de turistas extra-comunitarios</td>
        <td>Base de datos estadística de la Organización Mundial del Turismo de Naciones Unidas (OMT) y Eurostat</td>
    </tr>
    <tr>
        <td>Deportes</td>
        <td>Suma ponderada de los puntos en la clasificación mundial FIFA y del medallero en los Juegos Olímpicos de verano para cada EM de la UE.<br>Variable correctora: audiencia europea de la final del mundial y de la ceremonia de apertura de los Juegos Olímpicos</br></td>
        <td>FIFA y COI<br> Informes de Kantar Media y Nielsen</br></td>
    </tr>
    <tr>
        <td>Cultura</td>
        <td>Exportaciones extra-comunitarias de servicios audiovisuales (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales)</td>
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
        <td>UNESCO – Institute for Statistics, OCDE – iLibrary y Eurostat</td>
    </tr>
    <tr>
        <td>Cooperación al desarrollo</td>
        <td>Flujo de ayuda oficial al desarrollo bruta total de todos los estados miembros</td>
        <td>OCDE)</td>
    </tr>
  <tr class=''section''>
      <td colspan=''3''>Factores de escala</td>
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

</table>');
INSERT INTO translation (key, en, es) VALUES ('Investigador', 'Analyst', 'Investigador');
INSERT INTO translation (key, en, es) VALUES ('_faq title 3', 'Does it reflect the effort of countries attempting to achieve greater internationalization?', '¿Refleja el esfuerzo de un país por internacionalizarse?');
INSERT INTO translation (key, en, es) VALUES ('_faq text 3', 'No. This Index measures the results of internationalization, not its means. For example, a country may have deployed a significant number of troops abroad with a defence expenditure that is relatively smaller than that of another country with smaller military presence', 'No. Este Índice mide los resultados de la internacionalización, no sus medios. Por ejemplo, un país puede haber desplegado un importante número de tropas en el exterior con un gasto en defensa relativamente menor al de otro país con menor presencia militar');
INSERT INTO translation (key, en, es) VALUES ('_methodology criterios lista', 'Several criteria guided the select	ion of the variables that define the index:</p>
<ul class="util">
<li>First, presence is reflected in a single direction, or what could be deemed its unidirectionality.</li>
<li>Second, the results of presence are measured, and not the means or assets needed to achieve these results.</li>
<li>In addition, all the variables have an explicit external component, in the sense that they reflect cross-border presence.</li>
<li>Presence is given in absolute and not relative terms; in other words, the indicators are not proportional to the demographic or economic size of the country.</li>
<li>Likewise, as for any other index, the best explanatory capacity is sought with the fewest number of variables or indicators possible. Finally, hard data on presence are taken, and not data based on judgments or opinions.</li>
</ul>', 'La selección de las variables para la elaboración de este índice se basa en una serie de criterios:<ul class="util">
<li>En primer lugar, la presencia se recoge en una única dirección, lo que se podría denominar unidireccionalidad de la presencia.</li>
<li>En segundo, se miden resultados de presencia y no los medios para conseguirlos.
Además, todas las variables tienen un componente expresamente exterior, en el sentido de que reflejan la presencia transfronteriza. </li>
<li>La presencia se da en términos absolutos y no relativos al tamaño de la economía o a la población total.
Asimismo, como para cualquier otro índice, se busca la máxima capacidad explicativa con el mínimo número posible de variables e indicadores. </li>
<li>Por último, se toman datos duros de presencia y no datos basados en juicios u opiniones.</li>
</ul>');
INSERT INTO translation (key, en, es) VALUES ('_about subtitle infr', 'What is the Elcano Global Presence Index?', 'Qué es el Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('_about title meth', 'Methodology', 'Metodología');
INSERT INTO translation (key, en, es) VALUES ('_about subtitle meth', 'What is the Elcano Global Presence Index?', 'Qué es el Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('_about desc ppal', '<p>Elcano Global Presence Index is a synthetic index that orders, quantifies, and aggregates the external projection of different countries. Global presence is divided into three dimensions: economy, defence, and soft presence.</p>
', '<p>El Índice Elcano de Presencia Global agrega y cuantifica, sobre la base de datos objetivos, la proyección exterior y el posicionamiento internacional de los de países en función de las tres dimensiones que conforman su presencia: económica, militar y blanda.</p>
');
INSERT INTO translation (key, en, es) VALUES ('_about title infr', 'Structure', 'Estructura');
INSERT INTO translation (key, en, es) VALUES ('Ciencia', 'Science', 'Ciencia');
INSERT INTO translation (key, en, es) VALUES ('Cultura', 'Culture', 'Cultura');
INSERT INTO translation (key, en, es) VALUES ('Deportes', 'Sports', 'Deportes');
INSERT INTO translation (key, en, es) VALUES ('Educación', 'Education', 'Educación');
INSERT INTO translation (key, en, es) VALUES ('Energía', 'Energy', 'Energía');
INSERT INTO translation (key, en, es) VALUES ('Equipamiento militar', 'Military equipment', 'Equipamiento militar');
INSERT INTO translation (key, en, es) VALUES ('Filtros', 'Filters', 'Filtros');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Europea', 'Elcano European Presence Index', 'Índice Elcano de Presencia Europea');
INSERT INTO translation (key, en, es) VALUES ('Inversiones', 'Investments', 'Inversiones');
INSERT INTO translation (key, en, es) VALUES ('_legal title', 'Legal information', 'Información Legal');
INSERT INTO translation (key, en, es) VALUES ('Manufacturas', 'Manufactures', 'Manufacturas');
INSERT INTO translation (key, en, es) VALUES ('Migraciones', 'Migrations', 'Migraciones');
INSERT INTO translation (key, en, es) VALUES ('Presencia blanda', 'Soft presence', 'Presencia blanda');
INSERT INTO translation (key, en, es) VALUES ('Presencia económica', 'Economic presence', 'Presencia económica');
INSERT INTO translation (key, en, es) VALUES ('Presencia militar', 'Military presence', 'Presencia militar');
INSERT INTO translation (key, en, es) VALUES ('Servicios', 'Services', 'Servicios');
INSERT INTO translation (key, en, es) VALUES ('Tecnología', 'Technology', 'Tecnología');
INSERT INTO translation (key, en, es) VALUES ('Tropas', 'Troops', 'Tropas');
INSERT INTO translation (key, en, es) VALUES ('Turismo', 'Tourism', 'Turismo');
INSERT INTO translation (key, en, es) VALUES ('Análisis de variables', 'Variable analysis', 'Análisis de variables');
INSERT INTO translation (key, en, es) VALUES ('Mueve el ratón sobre un país', 'Move the mouse over a country', 'Mueve el ratón sobre un país');
INSERT INTO translation (key, en, es) VALUES ('PIB', 'GDP', 'PIB');
INSERT INTO translation (key, en, es) VALUES ('Población', 'Population', 'Población');
INSERT INTO translation (key, en, es) VALUES ('Presencia Militar', 'Military Presence', 'Presencia Militar');
INSERT INTO translation (key, en, es) VALUES ('Puesto %dº', 'Position', 'Puesto');
INSERT INTO translation (key, en, es) VALUES ('Ranking', 'Ranking', 'Ranking');
INSERT INTO translation (key, en, es) VALUES ('Variables', 'Variables', 'Variables');
INSERT INTO translation (key, en, es) VALUES ('Variable manufactures desc TEXTO', 'Flow of manufactured goods (chemical products, machinery, transport equipment, other manufactured products) (SITC 5 to 8 minus 667 and 68).', 'Flujo de manufacturas (productos químicos, maquinaria, equipos de transporte, otros productos manufacturados) (SITC 5 a 8 menos 667 y 68).');
INSERT INTO translation (key, en, es) VALUES ('Staff', 'Staff', 'Equipo');
INSERT INTO translation (key, en, es) VALUES ('Calcular', 'Calculate', 'Calcular');
INSERT INTO translation (key, en, es) VALUES ('Definición del proyecto', 'Project definition', 'Definición del proyecto');
INSERT INTO translation (key, en, es) VALUES ('Documentos y publicaciones', 'Documents and publications', 'Documentos y publicaciones');
INSERT INTO translation (key, en, es) VALUES ('En los medios', 'In the media', 'En los medios');
INSERT INTO translation (key, en, es) VALUES ('Ampliar información', 'More information', 'Ampliar información');
INSERT INTO translation (key, en, es) VALUES ('Contacto', 'Contact', 'Contacto');
INSERT INTO translation (key, en, es) VALUES ('Fundación Real Instituto Elcano', 'Elcano Royal Institute Foundation', 'Fundación Real Instituto Elcano');
INSERT INTO translation (key, en, es) VALUES ('Descargar informe 2012', 'Download 2012 report', 'Descargar informe 2012');
INSERT INTO translation (key, en, es) VALUES ('destacados', 'Outstanding', 'destacados');
INSERT INTO translation (key, en, es) VALUES ('es', 'is', 'es');
INSERT INTO translation (key, en, es) VALUES ('Ayuda cuotas de presencia', 'Presence quota help', 'Ayuda cuotas de presencia');
INSERT INTO translation (key, en, es) VALUES ('Estructura del IEPG', 'Structure', 'Estructura');
INSERT INTO translation (key, en, es) VALUES ('Cooperación', 'Cooperation', 'Cooperación al desarrollo');
INSERT INTO translation (key, en, es) VALUES ('tools', 'Tools', 'Herramientas');
INSERT INTO translation (key, en, es) VALUES ('Variable IEPG desc TEXTO', 'Elcano Global Presence Index is a synthetic index that orders, quantifies, and aggregates the external projection of different countries. Global presence is divided into three dimensions: economy, defence, and soft presence.', 'El Índice Elcano de Presencia Global agrega y cuantifica, sobre la base de datos objetivos, la proyección exterior y el posicionamiento internacional de los de países en función de las tres dimensiones que conforman su presencia: económica, militar y blanda.');
INSERT INTO translation (key, en, es) VALUES ('Variable military_equipment desc TEXTO', 'Weighted sum of military projection equipment: aircraft carriers, frigates, cruisers, destroyers, nuclear-powered submarines, principal amphibious ships, medium and heavy transport and tanker aircrafts.', 'Valoración ponderada de medios militares de proyección: portaviones, fragatas, cruceros, destructores, submarinos de propulsión nuclear, buques de proyección anfibia, aviones de transporte estratégico medios y pesados y aviones cisterna.');
INSERT INTO translation (key, en, es) VALUES ('Qué es', 'About', 'Qué es');
INSERT INTO translation (key, en, es) VALUES ('_methodology incorporación UE p', 'Moreover, since 2012, the Index also measures the global presence of the European Union as a whole. The latter is complemented by the Elcano European Presence Index, which evaluates the internationalisation of member states within the Union’s boundaries', 'Desde el 2012 el Índice Elcano de Presencia Global calcula además para la Unión Europea de los 27. Este ejercicio trata de cuantificar la proyección global de la Unión, como si se tratase de un supuesto súper-estado con identidad propia, medición que se complementa con el Índice Elcano de Presencia Europea que por el contrario evalúa la presencia de los países miembros dentro del perímetro de la Unión');
INSERT INTO translation (key, en, es) VALUES ('Variables, Indicadores y fuentes del Índice Elcano de Presencia Global calculado para la Unión Europea', 'Variables, indicators and sources of the Elcano Global Presence Index calculated for the European Union', 'Variables, Indicadores y fuentes del Índice Elcano de Presencia Global calculado para la Unión Europea');
INSERT INTO translation (key, en, es) VALUES ('Para más Información sobre la metodología del Índice Elcano de Presencia Global, véase', 'For more details on the methodology, see', 'Para más Información sobre la metodología del Índice Elcano de Presencia Global, véase');
INSERT INTO translation (key, en, es) VALUES ('Qué mide el índice Elcano de presencia global', 'What does the Elcano Global Presence Index measure?', NULL);
INSERT INTO translation (key, en, es) VALUES ('Variable services desc TEXTO', 'Flow of exports of services in transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services. ', 'Flujo de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos.');
INSERT INTO translation (key, en, es) VALUES ('Variable migrations desc TEXTO', 'Estimated number of international immigrants in the country at mid-year.', 'Número estimado de personas migrantes internacionales en el país a mitad de año.');
INSERT INTO translation (key, en, es) VALUES ('Por', 'By', 'Por');
INSERT INTO translation (key, en, es) VALUES ('Último índice', 'Last report', 'Último informe');
INSERT INTO translation (key, en, es) VALUES ('english', 'english', 'inglés');
INSERT INTO translation (key, en, es) VALUES ('English', 'English', 'Inglés');
INSERT INTO translation (key, en, es) VALUES ('Enlace', 'Link', 'Enlace');
INSERT INTO translation (key, en, es) VALUES ('español', 'spanish', 'español');
INSERT INTO translation (key, en, es) VALUES ('Etiquetas', 'Labels', 'Etiquetas');
INSERT INTO translation (key, en, es) VALUES ('Guardar', 'Save', 'Guardar');
INSERT INTO translation (key, en, es) VALUES ('inglés', 'english', 'inglés');
INSERT INTO translation (key, en, es) VALUES ('Inglés', 'English', 'Inglés');
INSERT INTO translation (key, en, es) VALUES ('Noticia', 'News', 'Noticia');
INSERT INTO translation (key, en, es) VALUES ('No hay resultados', 'There are no results', 'No hay resultados');
INSERT INTO translation (key, en, es) VALUES ('Cancelar', 'Cancel', 'Cancelar');
INSERT INTO translation (key, en, es) VALUES ('Créditos', 'Credits', 'Créditos');
INSERT INTO translation (key, en, es) VALUES ('Cuerpo', 'Body', 'Cuerpo');
INSERT INTO translation (key, en, es) VALUES ('Despublicar', 'Withdraw', 'Despublicar');
INSERT INTO translation (key, en, es) VALUES ('Documento', 'Document', 'Documento');
INSERT INTO translation (key, en, es) VALUES ('Variable IEPE TEXTO', 'Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Sed et
massa dapibus, mollis velit ut,
congue orci. Nullam pharetra mauris
dolor, ut imperdiet tortor ullamcorper
vel. Nunc ac nisi a massa elementum
auctor. Nullam et pellentesque leo, a
congue mauris. Nullam nec dolor
accumsan, euismod massa eu,
pretium dui. Maecenas tempus
sodales libero, eu molestie justo
faucibus consectetur. Vestibulum eu
venenatis quam, vitae tincidunt arcu.
Nunc consectetur quis ligula eu
porta. Quisque sed venenatis urna.
Aenean sed sodales nisl, eu ultrices
nulla. Quisque euismod molestie
dolor. Sed facilisis ligula vitae
dapibus cursus. Etiam et leo arcu.
Donec sagittis, sapien pretium
tincidunt suscipit, ante odio
dignissim metus, quis rhoncus nunc
justo vitae nisi', 'Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Sed et
massa dapibus, mollis velit ut,
congue orci. Nullam pharetra mauris
dolor, ut imperdiet tortor ullamcorper
vel. Nunc ac nisi a massa elementum
auctor. Nullam et pellentesque leo, a
congue mauris. Nullam nec dolor
accumsan, euismod massa eu,
pretium dui. Maecenas tempus
sodales libero, eu molestie justo
faucibus consectetur. Vestibulum eu
venenatis quam, vitae tincidunt arcu.
Nunc consectetur quis ligula eu
porta. Quisque sed venenatis urna.
Aenean sed sodales nisl, eu ultrices
nulla. Quisque euismod molestie
dolor. Sed facilisis ligula vitae
dapibus cursus. Etiam et leo arcu.
Donec sagittis, sapien pretium
tincidunt suscipit, ante odio
dignissim metus, quis rhoncus nunc
justo vitae nisi');
INSERT INTO translation (key, en, es) VALUES ('Años', 'Years', 'Años');
INSERT INTO translation (key, en, es) VALUES ('buscar documentos ', 'search documents', 'buscar documentos');
INSERT INTO translation (key, en, es) VALUES ('El                 <a class="nostyle" href="/lang', 'The', 'El');
INSERT INTO translation (key, en, es) VALUES ('Filtrar', 'Filter', 'Filtrar');
INSERT INTO translation (key, en, es) VALUES ('Presencia Europea', 'European Presence', 'Presencia Europea');
INSERT INTO translation (key, en, es) VALUES ('Presencia Global', 'Global Presence', 'Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Texto ERROR', 'Text', 'Texto');
INSERT INTO translation (key, en, es) VALUES ('Se ha producido un error', 'An error has ocurred', 'Se ha producido un error');
INSERT INTO translation (key, en, es) VALUES ('Volver a la lista inicial', 'Return to the initial list', 'Volver a la lista inicial');
INSERT INTO translation (key, en, es) VALUES ('Volver al inicio', 'Return to homepage', 'Volver al inicio');
INSERT INTO translation (key, en, es) VALUES ('Variable IEPE desc TEXTO', 'Elcano Global Presence Index is a synthetic index that orders, quantifies, and aggregates the external projection of different countries. Global presence is divided into three dimensions: economy, defence, and soft presence.', 'El Índice Elcano de Presencia Global agrega y cuantifica, sobre la base de datos objetivos, la proyección exterior y el posicionamiento internacional de los de países en función de las tres dimensiones que conforman su presencia: económica, militar y blanda.');
INSERT INTO translation (key, en, es) VALUES ('Variable military_presence desc TEXTO', 'The military presence is defined on the basis of the troops deployed in international missions and bases overseas together with military projection equipment.', 'La presencia militar definida a través del número de las tropas desplegadas en el extranjero y el equipamiento de proyección militar.');
INSERT INTO translation (key, en, es) VALUES ('Blog', 'Blog', 'Blog');
INSERT INTO translation (key, en, es) VALUES ('Variable primary_goods desc TEXTO', 'Flow of exports of primary goods (food, beverages, tobacco, agricultural commodities, non-ferrous metals, pearls, precious stones and non-monetary gold), excluding oil (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971).', 'Flujo de exportación de bienes primarios (comidas, bebidas, tabaco, productos agrícolas, metales no ferrosos, perlas, piedras preciosas y oro no monetario), excluido petróleo (SITC 0 + 1 + 2 + 4 + 68 + 667+ 971).');
INSERT INTO translation (key, en, es) VALUES ('Valor índice', 'Index Value', 'Valor índice');
INSERT INTO translation (key, en, es) VALUES ('Variable troops desc TEXTO', 'Number of military personnel deployed in international missions and bases overseas.', 'Número de militares desplegados en misiones internacionales y bases en el extranjero.');
INSERT INTO translation (key, en, es) VALUES ('Ayuda y soporte', 'Help and support', 'Ayuda y soporte');
INSERT INTO translation (key, en, es) VALUES ('Equipo proyecto Índice Elcano de Presencia Global', 'Elcano Global Presence Index project team', 'Equipo proyecto Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Coordinadora del Proyecto Índice Elcano de Presencia Global', 'Coordinator', 'Coordinadora del Proyecto Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Colaboradores', 'Contributors', 'Colaboradores');
INSERT INTO translation (key, en, es) VALUES ('Desarrollo y plataforma', 'Platform development', 'Desarrollo y plataforma');
INSERT INTO translation (key, en, es) VALUES ('Estructura del Índice Elcano de Presencia Global', 'Structure of Elcano Global Presence Index', 'Estructura del Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Explora el índice', 'Explore the index', 'Explora el índice');
INSERT INTO translation (key, en, es) VALUES ('Texto información puestos', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('Variable tourism desc TEXTO', 'Thousands of arrivals of non-resident tourists at borders.', 'Miles de llegadas de turistas no residentes a las fronteras.');
INSERT INTO translation (key, en, es) VALUES ('Variable sports desc TEXTO', 'Weighted sum of points in the FIFA world ranking and medals won at summer Olympic Games.', 'Suma ponderada de los puntos en la clasificación mundial FIFA y del medallero en los juegos olímpicos de verano.');
INSERT INTO translation (key, en, es) VALUES ('Variable technology desc TEXTO', 'Number of inter-related patent applications filed in one or more foreign countries to protect the same invention.', 'Patentes orientadas al exterior: número de solicitudes de patentes relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención.');
INSERT INTO translation (key, en, es) VALUES ('Millones', 'Million', 'Millones');
INSERT INTO translation (key, en, es) VALUES ('Portada', 'Home', 'Portada');
INSERT INTO translation (key, en, es) VALUES ('Presencia Económica', 'Economic Presence', 'Presencia Económica');
INSERT INTO translation (key, en, es) VALUES ('Publicar', 'Publish', 'Publicar');
INSERT INTO translation (key, en, es) VALUES ('Referencia', 'Reference', 'Referencia');
INSERT INTO translation (key, en, es) VALUES ('Editar', 'Edit', 'Editar');
INSERT INTO translation (key, en, es) VALUES ('Eliminar', 'Remove', 'Eliminar');
INSERT INTO translation (key, en, es) VALUES ('Eliminar Imagen', 'Remove picture', 'Eliminar imagen');
INSERT INTO translation (key, en, es) VALUES ('1 herramienta seleccionada', '1 tool selected', '1 herramienta seleccionada');
INSERT INTO translation (key, en, es) VALUES ('hab', 'pop', 'hab');
INSERT INTO translation (key, en, es) VALUES ('Por favor, compruebe los campos en rojo', 'Please, check fields in red', 'Por favor, compruebe los campos en rojo');
INSERT INTO translation (key, en, es) VALUES ('Sección', 'Section', 'Sección');
INSERT INTO translation (key, en, es) VALUES ('Añadir en', 'Add', 'Añadir');
INSERT INTO translation (key, en, es) VALUES ('Suba una image JPG', 'Load a JPEG image', 'Suba una imagen JPEG');
INSERT INTO translation (key, en, es) VALUES ('Suba un fichero PDF', 'Load a PDF file', 'Suba un fichero PDF');
INSERT INTO translation (key, en, es) VALUES ('Añadir es', 'Add', 'Añadir');
INSERT INTO translation (key, en, es) VALUES ('Se ha seleccionado una variable para la que no hay datos para el año seleccionado', 'A variable with no data for that year has been selected ', 'Se ha seleccionado una variable para la que no hay datos para el año seleccionado');
INSERT INTO translation (key, en, es) VALUES ('_faq title 7', 'How are the variables of the Elcano Global Presence Index selected?', '¿Cómo se seleccionan las variables que componen el Índice Elcano de Presencia Global?');
INSERT INTO translation (key, en, es) VALUES ('_faq title 8', 'How are variables combined into a synthetic index?', '¿Y cómo se agregan en un índice sintético?');
INSERT INTO translation (key, en, es) VALUES ('_faq text 5', 'Objective. Its purpose is not to ascertain how a country is perceived by certain elites or by the public opinion as a whole. This Index is calculated to discover the effective external projection of the different countries, regardless of their reputation or image', 'Objetivos. La finalidad no es saber cómo se percibe un país por parte de un grupo de élites o del conjunto de la opinión pública. Este índice se calcula para saber cuál es la proyección exterior real de los países independientemente de su reputación o imagen');
INSERT INTO translation (key, en, es) VALUES ('_faq text 11', 'To reveal transformations in the world order since the Cold War ended', 'Para poder mostrar los cambios en el orden mundial desde el final de la Guerra Fría');
INSERT INTO translation (key, en, es) VALUES ('_faq title 14', 'Can the presence of European countries be combined, and can it be assumed that this is the presence of the European Union?', '¿Se puede agregar la presencia de los países europeos y asumir que es la de la Unión Europea?');
INSERT INTO translation (key, en, es) VALUES ('_about body ppal', '<p>Global presence may be addressed by posing the following question: to what extent and in what form are countries ‘out there’, beyond their borders, regardless of whether they are exerting real influence or power? In a sense, global presence can be the basis of power –the platform or asset capable of being transformed into influence or power – if the country extending its presence is able and willing to pursue such ends.</p>
<p>The main objective of this project is joint the efforts put forth by the academic world, some international agencies, and diverse think tanks toward conceptualising globalisation. Therefore, one of the functions of the Elcano Global Presence Index is to analyse the global trends of international presence, including the evolution of multipolarity or bipolarity, the rise or decline of certain countries and regions, and the greater or lesser prominence of soft versus hard presence.</p>
<p>The Index is also a way of assessing the foreign policy of those countries included in the calculation – efforts and means versus results, sector profile of presence, relation between presence and influence, or the distance between objective presence and subjective perception. Consequently, our second aim is to provide a tool for foreign policy-making.</p>', '<p>La presencia global podría definirse como la medida y forma en que los países están ‘ahí fuera’, independientemente de que ejerzan influencia o poder. De algún modo, la presencia global podría ser la base del poder; la plataforma o activo a transformar en influencia o poder, si es que el país tiene la capacidad y la voluntad de hacerlo.</p>

<p>El principal objetivo de este proyecto es el de contribuir al análisis del proceso de globalización. En este sentido, una de las funciones del Índice Elcano de Presencia Global es la de analizar las tendencias globales de la presencia internacional –evolución de multipolaridad y la bipolaridad, ascenso o declive de una serie de países y regiones, mayor o menor peso de las dimensiones blanda o dura de la presencia-, aportando a la vez una herramienta útil para la toma de decisiones en política exterior, confrontando esfuerzos y medios frente a resultados, el perfil de presencia, la relación entre presencia e influencia o la distancia existente entre la presencia objetiva y la percepción subjetiva.</p>');
INSERT INTO translation (key, en, es) VALUES ('_about title ppal', 'Definition', 'Definición');
INSERT INTO translation (key, en, es) VALUES ('Preguntas más frecuentes', 'Frecuently asked questions', 'Preguntas más frecuentes');
INSERT INTO translation (key, en, es) VALUES ('El <strong>Índice Elcano de Presencia Global</strong> es un proyecto del Real Instituto Elcano de estudios internacionales y estratégicos.', 'The <strong>Elcano Global Presence Index</strong> is a project from Elcano Royal Institute of strategic and international studies.', 'El <strong>Índice Elcano de Presencia Global</strong> es un proyecto del Real Instituto Elcano de estudios internacionales y estratégicos.');
INSERT INTO translation (key, en, es) VALUES ('Variable economic_presence desc TEXTO', 'The economic presence is defined through the flow of exports of energy products, primary goods, manufactures, and services, as well as through foreign direct investment.', 'La presencia económica se define en base a las exportaciones de energía, bienes primarios, manufacturas y servicios así como de las inversiones directas en el exterior.');
INSERT INTO translation (key, en, es) VALUES ('Variable soft_presence desc TEXTO', 'The soft presence is defined through migration, tourism, performance in international sports competitions, exports of audiovisual services, the projection of information on the Internet, the number of international patents, the articles published in scientific journals, foreign students in domestic universities, and finally, the gross flows of development assistance.', 'La presencia blanda definida a través de una serie de variables como son las migraciones, el turismo,  el rendimiento deportivo en competiciones internacionales, la cultura, el acceso a la información a través de Internet, el número de patentes internacionales registradas, la producción científica, el número de estudiantes extranjeros y, por último, el gasto realizado en ayuda al desarrollo.');
INSERT INTO translation (key, en, es) VALUES ('Variable energy desc TEXTO', 'Flow of exports of energy products (oil, refined products, and gas) (SITC 333, 334, 343).', 'Flujo de exportación de productos energéticos (petróleo, productos refinados y gas) (SITC 333, 334, 343).');
INSERT INTO translation (key, en, es) VALUES ('Variable culture desc TEXTO', 'Exports of audiovisual services (cinematographic productions, radio and television programs, and musical recordings).', 'Exportaciones de servicios audiovisuales (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales).');
INSERT INTO translation (key, en, es) VALUES ('Variable cooperation desc TEXTO', 'Total gross flows of official development aid or comparable data.', 'Flujo de ayuda oficial al desarrollo bruto total o datos homologables.');
INSERT INTO translation (key, en, es) VALUES ('_faq title 12', 'For what countries?', '¿Y para qué países?');
INSERT INTO translation (key, en, es) VALUES ('Global', 'Global', 'Global');
INSERT INTO translation (key, en, es) VALUES ('_faq title 13', 'Can the presence of different countries be combined to reveal joint presence for a chosen group or region?', '¿Se puede sumar la presencia de distintos países y asumir que refleja la presencia del grupo o de la región?');
INSERT INTO translation (key, en, es) VALUES ('Nombre', 'Name', 'Nombre');
INSERT INTO translation (key, en, es) VALUES ('Posición', 'Position', 'Posición');
INSERT INTO translation (key, en, es) VALUES ('Posición (inglés)', 'Position', 'Posición');
INSERT INTO translation (key, en, es) VALUES ('0 herramientos seleccionadas', 'No tools selected', 'Sin herramientas seleccionadas');
INSERT INTO translation (key, en, es) VALUES ('Abrir enlace en una nueva pestaña', 'Open link in a new tab', 'Abrir el enlace en una nueva pestaña');
INSERT INTO translation (key, en, es) VALUES ('* Campos necesarios', '* Obligatory fields', '* Campos obligatorios');
INSERT INTO translation (key, en, es) VALUES ('Destacado', 'Outstanding', 'Destacado');
INSERT INTO translation (key, en, es) VALUES ('Destacado editado por última vez el %s', 'Outstanding last edited the', 'Desticado editado por última vez el');
INSERT INTO translation (key, en, es) VALUES ('Eliminar PDF ', 'Remove PDF', 'Eliminar PDF');
INSERT INTO translation (key, en, es) VALUES ('Epígrafe', 'Epigraph', 'Epígrafe');
INSERT INTO translation (key, en, es) VALUES ('Español', 'Spanish', 'Español');
INSERT INTO translation (key, en, es) VALUES ('Guardar documento', 'Save document', 'Guardar documento');
INSERT INTO translation (key, en, es) VALUES ('Herramientas de análisis', 'Analysis tools', 'Herramientas de análisis');
INSERT INTO translation (key, en, es) VALUES ('Imagen anterior', 'Previous image', 'Imagen anterior');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global', 'Elcano Global Presence Index', 'Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Información Legal', 'Legal information', 'Información Legal');
INSERT INTO translation (key, en, es) VALUES ('La <strong>presencia militar</strong> se mide con las tropas desplegadas en el extranjero y con el equipamiento militar.', 'The <strong>military presence</strong> is defined on the basis of the troops deployed in international missions and bases overseas together with military projection equipment.', 'La <strong>presencia militar</strong> definida a través del número de las tropas desplegadas en el extranjero y el equipamiento de proyección militar.');
INSERT INTO translation (key, en, es) VALUES ('Texto no encontrado ERROR', 'Text not found', 'Texto no encontrado');
INSERT INTO translation (key, en, es) VALUES ('Metodología', 'Methodology', 'Metodología');
INSERT INTO translation (key, en, es) VALUES ('No hay ficheros para descargar en este documento', 'There are no files to download in this document', 'No hay ficheros para descargar en este documento');
INSERT INTO translation (key, en, es) VALUES ('No hemos encontrado lo que buscas', 'We didn''t find what you are looking', 'No hemos encontrado lo que busca');
INSERT INTO translation (key, en, es) VALUES ('Nueva etiqueta en español', 'New Spanish label', 'Nueva etiqueta en español');
INSERT INTO translation (key, en, es) VALUES ('_faq title 11', 'Why those years?', '¿Por qué esos años?');
INSERT INTO translation (key, en, es) VALUES ('La <strong>presencia económica</strong> se mide a través de las exportaciones de energía, bienes primarios,manufacturas y servicios, así como las inversionesdirectas en el exterior.', 'The <strong>economic presence</strong> is defined through the flow of exports of energy products, primary goods, manufactures, and services, as well as through foreign direct investment.', 'La <strong>presencia económica</strong> definida a través de las exportaciones de energía, bienes primarios, manufacturas y servicios así como de las inversiones directas en el exterior.');
INSERT INTO translation (key, en, es) VALUES ('0 países seleccionados', '0 countries selected', '0 países seleccionados');
INSERT INTO translation (key, en, es) VALUES ('1 país seleccionado', '1 country selected', '1 país seleccionado');
INSERT INTO translation (key, en, es) VALUES ('Países del Índice Elcano', 'Countries in Elcano Index', 'Países del Índice Elcano');
INSERT INTO translation (key, en, es) VALUES ('%d países seleccionados', '%d countries selected', '%d países seleccionados');
INSERT INTO translation (key, en, es) VALUES (' %d países seleccionados', '%d countries selected', '%d países seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Ver %d más', 'See %d more', 'Ver %d mas');
INSERT INTO translation (key, en, es) VALUES ('Seleccionar todos los países', 'Select all countries', 'Seleccionar todos los países');
INSERT INTO translation (key, en, es) VALUES ('Ranking %d', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('Europea', 'European', 'Europea');
INSERT INTO translation (key, en, es) VALUES ('Presencia:', 'Presence:', 'Presencia:');
INSERT INTO translation (key, en, es) VALUES ('selecccionados', 'selected', 'seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Te sugerimos que', 'We suggest to', 'Le sugerimos que');
INSERT INTO translation (key, en, es) VALUES ('Se ha seleccionado la opción de ranking de Países + UE para un año anterior a 2005. El estudio del Índice Elcano de presencia global incluye datos de la Unión Europea a partir de 2005', 'The option countries + EU ranking has been selected for a year previous to 2005. The Elcano Global Presence Index takes data for the European Union from 2005 on', 'Se ha seleccionado la opción de ranking de Países + UE para un año anterior a 2005. El estudio del Índice Elcano de presencia global incluye datos de la Unión Europea a partir de 2005');
INSERT INTO translation (key, en, es) VALUES ('1. Si ha completado el formulario de búsqueda de documentos, comprueba que las palabras     están escritas correctamente.', '1.- If you have filled the searching form, check all the words are written properly.', '1.- Si ha completado el formulario de búsqueda de documentos, compruebe que las palabras están escritas correctamente.');
INSERT INTO translation (key, en, es) VALUES ('2. Si tiene algún filtro aplicado, prueba eliminando alguna etiqueta o todas.', '2.- If you are using filters, try to delete one or all of them.', '2.- Si tiene algún filtro aplicado, pruebe eliminando alguna etiqueta o todas ellas.');
INSERT INTO translation (key, en, es) VALUES (' selecccionados', ' selected', ' seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Añada al menos un país a la <i>cabereca de análisis</i>', 'Add at least one country to the <i>countries selector</i>', 'Añada al menos un país al <i>selector de países</i>');
INSERT INTO translation (key, en, es) VALUES ('"+$(".pais.active").length+" país seleccionados', '"+$(".pais.active").length+" countries selected', '"+$(".pais.active").length+" países seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Seleccione un país de la <i>cabereca de análisis</i>', 'Select one country from the <i>analysis header</i>', 'Seleccione un país de la <i>cabecera de análisis</i>');
INSERT INTO translation (key, en, es) VALUES ('_help p1 subtitle', 'Discover the Index from several points of view', 'Explore el Índice desde distintas perspectivas');
INSERT INTO translation (key, en, es) VALUES (' %d variable seleccionada', '%d variable selected', '%d variable seleccionada');
INSERT INTO translation (key, en, es) VALUES (' %d país seleccionado', '%d country selected', '%d país seleccionado');
INSERT INTO translation (key, en, es) VALUES (' %d variables seleccionadas', '%d variables selected', '%d variables seleccionadas');
INSERT INTO translation (key, en, es) VALUES (' %d ano seleccionado', '%d year selected', '%d año seleccionado');
INSERT INTO translation (key, en, es) VALUES (' %d anos seleccionados', '%d years selected', '%d años seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Metodología', 'Elcano Global Presence Index – Methodology', 'Índice Elcano de Presencia Global – Metodología');
INSERT INTO translation (key, en, es) VALUES ('Si usted tiene alguna pregunta, sugerencia o solicitud relacionada con el Índice Elcano de Presencia Global, por favor escríbanos a', 'If you have any question, suggestion, or request on the Elcano Global Presence Index, please send us an e-mail to', 'Si usted tiene alguna pregunta, sugerencia o solicitud relacionada con el Índice Elcano de Presencia Global, por favor escríbanos a');
INSERT INTO translation (key, en, es) VALUES ('CP code', 'PC', 'CP');
INSERT INTO translation (key, en, es) VALUES ('Developed + Design Geographica ', 'Developed + Design Geographica ', 'Developed + Design Geographica');
INSERT INTO translation (key, en, es) VALUES ('Las columnas:', 'Columns:', 'Las columnas:');
INSERT INTO translation (key, en, es) VALUES ('Opciones de descarga', 'Download options', 'Opciones de descarga');
INSERT INTO translation (key, en, es) VALUES ('Las filas:', 'Rows:', 'Las filas:');
INSERT INTO translation (key, en, es) VALUES ('_help p2 txt', 'Filters allow the user to restrict which countries are featured and analysed. It might

be the case that the high scores obtained by some countries mask some of the

finer details regarding others, or that what is required is to analyse the data from a

regional perspective. Therefore, the filters can be used to exclude some countries

from the analysis and to focus on others. Filters are available on all tools and

remain active when switching from one tool to another. Explora has a horizontal

configuration.', 'Los filtros permiten habilitar restricciones a los países que intervienen en las herramientas de análisis. Ya sea porque un país distorsiona la visualización de datos por su alta puntuación en alguna variable, o ya sea porque únicamente queremos analizar el índice desde una perspectiva regional, el filtro nos habilita la posibilidad de excluir países de los análisis y restringir éstos a los países de nuestro interés. Los filtros se aplican a todas las herramientas de análisis, y está activo mientras pasamos de una a otra. Es una configuración transversal a todo Explora.');
INSERT INTO translation (key, en, es) VALUES ('_help welcome txt_1', '<strong>Explora</strong> is an interactive section for searching the Index. It has a number of tools for

visualising and analysing both global and European presence and for mapping the data

on which the Index is based.
', 'La sección <strong>Explora</strong> es la zona interactiva de consulta de datos. En ella dispondrá de diversas herramientas para la visualización y el análisis de los datos de presencia global y europea. Asimismo, podrá consultar sobre un mapa sobre el que se cartografían los resultados del estudio.
');
INSERT INTO translation (key, en, es) VALUES ('Millones US dollar', 'Million US dollar', 'Millones US dólar');
INSERT INTO translation (key, en, es) VALUES ('Billones US dollar', 'US$ billion', 'Billones US$');
INSERT INTO translation (key, en, es) VALUES ('Si usted tiene alguna pregunta o problema relacionado con este portal, por favor escríbanos a:', 'If you have technical problems related to this web, please send an e-mail to', 'Si usted tiene alguna pregunta o problema relacionado con este portal, por favor escríbanos a:');
INSERT INTO translation (key, en, es) VALUES ('Seleccione un país', 'Select country', 'Seleccione un país');
INSERT INTO translation (key, en, es) VALUES ('Bienes primarios', 'Primary goods', 'Bienes primarios');
INSERT INTO translation (key, en, es) VALUES ('Millones hab', 'Million pop', 'Millones hab');
INSERT INTO translation (key, en, es) VALUES ('Contribuciones', 'Contributions', 'Contribuciones');
INSERT INTO translation (key, en, es) VALUES ('Seleccionar todos los bloques', 'Select all blocs', 'Seleccionar todos los bloques');
INSERT INTO translation (key, en, es) VALUES ('_Ayuda_contribuciones_presencia', '<p>This tool allows the presence contribution of two countries or blocs to be compared as well as their individual global weights. </p>

<p>The presence contributions are the magnitude that each dimension or indicator represent in the global value of a country’s presence. They can be expressed either as index values or as a percentage of total global presence. As an example, in Spain tourism contributes 30.8 points (18.8%) to its total global presence, which in 2013 was 164.4. </p>

<p>To compare a bloc or country you simply have to drag its icon from the countries selector and drop it on the selected graph. Countries can also be selected by clicking on them. The graphs are interactive, allowing you to navigate between dimensions to explore variables more closely. </p>

<p>As usual, the desired edition of the Index can be selected from the timeline. </p>
', '<p>Esta herramienta permite comparar contribuciones de presencia entre dos países o bloques, así como el peso total de cada una de ellas.</p>

<p>Por contribuciones de presencia entendemos la magnitud en la que cada dimensión o indicador representa en el valor total de presencia de un país. Dichas contribuciones pueden expresarse en valor índice o en porcentaje de la presencia global total. Así, por ejemplo, en el caso de España, podemos decir que el turismo contribuye con 30,8 puntos (18,8%) a su presencia global total, que en 2013 asciende a 164,4.</p>

<p>Para comparar un país o bloque, simplemente arrastre desde el selector de países el país de su elección sobre el gráfico en el que lo quiera colocar, o selecciónelo con un click. Puede navegar entre las dimensiones y las variables pulsando sobre el gráfico.</p>

<p>Seleccione la edición del Índice deseada utilizando la línea de tiempo inferior.</p>');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global 2012 (PDF 2,4Mb)', '2012 Elcano Global Presence (PDF 2,4Mb)', 'Índice Elcano de Presencia Global 2012 (PDF 2,4Mb)');
INSERT INTO translation (key, en, es) VALUES ('US dollar', 'US dollar', 'US dólar');
INSERT INTO translation (key, en, es) VALUES ('Billones hab', 'Billion pop', 'Billones hab');
INSERT INTO translation (key, en, es) VALUES ('Investigadora', 'Analyst', 'Investigadora');
INSERT INTO translation (key, en, es) VALUES (' Ranking de país %d', 'Country ranking %d', ' Ranking de país %d');
INSERT INTO translation (key, en, es) VALUES (' Ranking de país + UE %d', 'Country + EU ranking %d', 'Country + EU ranking %d');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Estructura', 'Elcano Global Presence Index – Structure', 'Índice Elcano de Presencia Global - Estructura');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - No encontrado', 'Elcano Global Presence Index – Not found', 'Índice Elcano de Presencia Global - No encontrado');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global – Explora', 'Elcano Global Presence Index – Explora', 'Índice Elcano de Presencia Global – Explora');
INSERT INTO translation (key, en, es) VALUES ('_about body meth', '<p>Elcano Global Presence Index studies the global presence of a selection of 70 countries: the first 60 world economies according to World Bank data (nations with the highest GDP in current US dollars) as well as countries that are smaller in their economic size but are members of the Organisation for Economic Cooperation and Development (OECD) and/or the European Union.</p>
<h6>Countries listed in the Elcano Global Presence Index</h6>
<p>We should note that by making calculations at time intervals that go back to 1990, the intention of the project is to show the ‘two-bloc world’, even if in decline. Thus, Russia’s 1990 values refer to those of the Soviet Union, those of Germany to the German Federal Republic, those of the Czech Republic to Czechoslovakia, and those of Slovenia to Yugoslavia.</p>
<h6>Structure of the Elcano Global Presence Index</h6>
<p>Several criteria guided the selection of the variables that define the index:</p>
<ul class="util">
<li>First, presence is reflected in a single direction, or what could be deemed its unidirectionality.</li>
<li>Second, the results of presence are measured, and not the means or assets needed to achieve these results.</li>
<li>In addition, all the variables have an explicit external component, in the sense that they reflect cross-border presence.</li>
<li>Presence is given in absolute and not relative terms; in other words, the indicators are not proportional to the demographic or economic size of the country.</li>
<li>Likewise, as for any other index, the best explanatory capacity is sought with the fewest number of variables or indicators possible. Finally, hard data on presence are taken, and not data based on judgments or opinions.</li>
</ul>
<h6>Variables, indicators and sources of the Elcano Global Presence Index</h6><p>The three areas –economic, military and soft presence– do not contribute to the global presence of countries in the same way. In defining the weightings of each of the elements included in the Index, we conducted a survey with a panel of experts in international relations. The panel was selected based on the report <a href=''http://gotothinktank.com/'' target=''_blank''>“The Global Go To Think Tanks” published annually by the University of Pennsylvania.</a>The questionnaire was sent to 45 institutions in the United States, 40 in Europe, 27 in Asia, 17 in Latin America, 12 in Africa, eight in the Middle East and North Africa, and three in Oceania.</p><h6>Variables, indicators and sources of the Elcano Global Presence Index calculated for the European Union</h6>
<h6>Variables, indicators and sources of the Elcano European Presence Index</h6><h6>For more details on the methodology, see: </h6>
<ul class="util">


<li>Iliana Olivié and Manuel García23, 2013, IEPG 2012: <a href=''http://www.realinstitutoelcano.org/wps/portal/web/rielcano_en/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_in/zonas_in/dt12-2013-olivie-gracia-iepg-metodologia-methodology-2012#.U2oBUVdNH1U'' target=''_blank''>methodology and new analytic tools,</a> Elcano Working Paper (WP) 12/2013.</li><li>Iliana Olivié and Ignacio Molina, 2012,<a href=''http://www.realinstitutoelcano.org/wps/portal/!ut/p/c5/04_SB8K8xLLM9MSSzPy8xBz9CP0os3jjYB8fnxBnR19TE2e_kEAjV2NDAwgAykdiyvs5GcDk8ev288jPTdUvyI0oBwDY0u0I/dl3/d3/L0lDU0lKSWdra0EhIS9JTlJBQUlpQ2dBek15cUEhL1lCSlAxTkMxTktfMjd3ISEvN18zU0xMTFRDQU01NENOVFEyN0YzMDAwMDAwMA!!/?WCM_PORTLET=PC_7_3SLLLTCAM54CNTQ27F30000000000000_WCM&WCM_GLOBAL_CONTEXT=/wps/wcm/connect/elcano/Elcano_in/Zonas_in/DT9-2012'' target=''_blank''> Measuring the international presence of countries: the Elcano Institute''s IEPG Index methodology revisited</a>, Elcano Royal Institute Working Paper (WP) 9/2012.</li>

<li>Iliana Olivié and Ignacio Molina (coord.), 2011, Elcano Global Presence Index (IEPG), Estudio Elcano 2, (Madrid: Elcano Royal Institute).</li>
</ul>', '<p>El Índice Elcano de presencia global cubre una selección de 70 países. Éstos son las primeras 60 economías mundiales según datos del Banco Mundial (países con mayor PIB en dólares corrientes), además de los países con menor tamaño económico miembros de la Organización para la Cooperación y el Desarrollo Económico (OCDE) y/o de la Unión Europea (cuadro A.1).</p>
<h6>Lista de países del Índice Elcano de Presencia Global</h6>
<p>En relación a la selección de países, hay que tener en cuenta que al calcularse calas temporales que se remontan a 1990, la intención del proyecto es la de mostrar el ‘mundo de los dos bloques’ –aunque sea en su ocaso–. De este modo, los valores de 1990 de Rusia se refieren, evidentemente, a los de la Unión Soviética, los de Alemania a la República Federal Alemana, los de la República Checa a Checoslovaquia, y los de Eslovenia a Yugoslavia..</p>
<h6>Estructura del Índice Elcano de Presencia Global</h6> <p>La selección de las variables para la elaboración de este índice se basa en una serie de criterios:</p> <ul class="util">
<li>En primer lugar, la presencia se recoge en una única dirección, lo que se podría denominar unidireccionalidad de la presencia.</li>
<li>En segundo, se miden resultados de presencia y no los medios para conseguirlos.</li> <li>Además, todas las variables tienen un componente expresamente exterior, en el sentido de que reflejan la presencia transfronteriza.</li>
<li>La presencia se da en términos absolutos y no relativos al tamaño de la economía o a la población total.</li> <li>Asimismo, como para cualquier otro índice, se busca la máxima capacidad explicativa con el mínimo número posible de variables e indicadores.</li> <li>Examinar la política exterior de los países para los que se calcula (valoración de los esfuerzos en
<li>Por último, se toman datos duros de presencia y no datos basados en juicios u opiniones.</li>
</ul><p>Para definir la ponderación de los elementos del índice, se tomó la decisión de recurrir a un panel de expertos en relaciones internacionales construido sobre la base del informe <a href=''http://gotothinktank.com/'' target=''_blank''>“Global Go To Think Tanks” que publica anualmente la Universidad de Pensilvania.</a>  El cuestionario fue enviado a 45 instituciones norteamericanas, 40 europeas, 27 asiáticas, 17 latinoamericanas, 12 africanas, 8 de Oriente Medio y Norte de África, y 3 de Oceanía.</p><h6>La incorporación de la Unión Europea al Índice Elcano de Presencia Global</h6>
<p>Desde el 2012 el Índice Elcano de Presencia Global calcula además para la Unión Europea de los 27. Este ejercicio trata de cuantificar la proyección global de la Unión, como si se tratase de un supuesto súper-estado con identidad propia, medición que se complementa con el Índice Elcano de Presencia Europea que por el contrario evalúa la presencia de los países miembros dentro del perímetro de la Unión.</p>
 <h6>Variables, Indicadores y fuentes del Índice Elcano de Presencia Global calculado para la Unión Europea</h6>
<h6>Variables, Indicadores y fuentes del Índice Elcano de Presencia Europea</h6><h6>Para más Información sobre la metodología del Índice Elcano de Presencia Global, véase: </h6>
<ul class="util">
<li>Iliana Olivié y Manuel Gracia 2013, <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/especiales/indiceelcanopresenciaglobal/dt12-2013-olivie-gracia-iepg-metodologia-methodology-2012'' target=''_blank''>IEPG 2012: metodología y nuevos elementos para el análisis, Documento de Trabajo del Real Instituto Elcano (DT) 12/2013.</a></li>
<li>Iliana Olivé e Ignacio Molina, 2012, <a href=''http://www.realinstitutoelcano.org/wps/portal/rielcano/contenido?WCM_GLOBAL_CONTEXT=/elcano/elcano_es/zonas_es/cooperacion+y+desarrollo/dt9-2012'' target=''_blank''> Medir la presencia internacional de los países: metodología revisada del Índice Elcano de Presencia Global (IEPG)</a>, Documento de Trabajo del Real Instituto Elcano (DT) 9/2012</li>
<li>Iliana Olivié e Ignacio Molina (coord.), 20011, Índice Elcano de Presencia Global (IEPG), Estudio Elcano 2, (Madrid: Real Instituto Elcano). </li>
</ul>');
INSERT INTO translation (key, en, es) VALUES ('Cerrar', 'Close', 'Cerrar');
INSERT INTO translation (key, en, es) VALUES ('Descargar informe %s', 'Download report %s', 'Descargar informe %s');
INSERT INTO translation (key, en, es) VALUES ('falta pais', 'country missing', 'falta país');
INSERT INTO translation (key, en, es) VALUES ('Fecha', 'Date', 'Fecha');
INSERT INTO translation (key, en, es) VALUES ('0 años seleccionados', '0 years selected', '0 años seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Diseño mas desarrollo', 'Design + Development', 'Diseño + Desarrollo');
INSERT INTO translation (key, en, es) VALUES ('0 variables seleccionadas', '0 variables selected', '0 variables seleccionadas');
INSERT INTO translation (key, en, es) VALUES (' años seleccionados', ' years selected', ' años seleccionados');
INSERT INTO translation (key, en, es) VALUES ('"+$(".celda.active").length+" año seleccionado', '"+$(".celda.active").length+" year selected', '"+$(".celda.active").length+" año seleccionado');
INSERT INTO translation (key, en, es) VALUES ('<b>Las pestañas</b> de crearán en base a: <i>Variable</i>', '<b>Tabs</b> will be created based on: <i>Variable</i>', '<b>Las pestañas</b> de crearán en base a: <i>Variable</i>');
INSERT INTO translation (key, en, es) VALUES ('"+$(".pais.active").length+" país seleccionado', '"+$(".pais.active").length+" country selected', '"+$(".pais.active").length+" país seleccionado');
INSERT INTO translation (key, en, es) VALUES (' países seleccionados', ' countries selected', ' países seleccionados');
INSERT INTO translation (key, en, es) VALUES ('"+t+" variable seleccionada', '"+t+" variable selected', '"+t+" variable seleccionada');
INSERT INTO translation (key, en, es) VALUES (' variables seleccionadas', ' variables selected', ' variables seleccionadas');
INSERT INTO translation (key, en, es) VALUES ('VI code', 'IV', 'VI');
INSERT INTO translation (key, en, es) VALUES ('País', 'Country', 'País');
INSERT INTO translation (key, en, es) VALUES ('Variable', 'Variable', 'Variable');
INSERT INTO translation (key, en, es) VALUES ('Como desea configurar el contenido en su documento <i>Excel</i>', 'How would you like to configure your <i>Excel</i> document?', '¿Cómo desea configurar el contenido en su documento <i>Excel</i>?');
INSERT INTO translation (key, en, es) VALUES ('¿Como desea configurar el contenido en su documento <i>Excel</i>?', 'How would you like to configure your <i>Excel</i> document?', '¿Cómo desea configurar el contenido en su documento <i>Excel</i>?');
INSERT INTO translation (key, en, es) VALUES ('Seleccionar todos', 'Select all', 'Seleccionar todos');
INSERT INTO translation (key, en, es) VALUES ('_Ayuda_cuotas', '<p>This tool allows the quota of presence of countries and blocks to be compared. </p>

<p>The presence quota is the share of foreign projection held by a country or bloc in the total global presence universe. To calculate it the global presence index of a country is divided by the sum of the total global presence –ie, of the 70 countries included in the study– and then multiplied by 100. </p>

<p>The tool employs a temporal evolution graph to plot the presence quotas of all countries and blocs present in the countries selector for the selected dimension. Please note that there are no data for variables, only for the global index and for the economic, military and soft dimensions. Click on a country in the countries selector to highlight the appropriate time period on the plot. </p>

<p>You can select the appropriate time period with the timeline. Although the plot is minimally altered, the map will draw the quota data for the selected year. </p>
', '<p>Esta herramienta permite comparar las cuotas de presencia de países y bloques a lo largo del tiempo.</p>

<p>La cuota de presencia es la proporción de proyección exterior que un determinado país ocupa en el universo de la presencia global total. Para su cálculo, se divide el valor índice de presencia global de un país por la suma de presencia global total- la de los 70 países para los que calculamos el índice-, y se multiplica por 100.</p>

<p>Esta herramienta crea un gráfico temporal con las cuotas de presencia de todos los países y bloques presentes en el selector de países para la dimensión seleccionada. Tenga en cuenta que no existen datos de cuota para las variables, tan sólo para el Índice global y las dimensiones económica, militar y blanda. Pulse sobre un país en el selector para resaltar su línea temporal en el gráfico.</p>

<p>Seleccione el momento temporal en la línea de tiempo inferior. Si bien el gráfico se ve escasamente afectado, el mapa sí mostrará los valores de cuota de dicho año.</p>');
INSERT INTO translation (key, en, es) VALUES ('Descargar .XLS', 'Download .XLSX  ', 'Descargar .XLSX');
INSERT INTO translation (key, en, es) VALUES (' Ranking de bloque %d', 'Bloc ranking %d', 'Ranking de bloque %d');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global 2014 (PDF 2MB)', 'Elcano Global Presence Report 2014 (PDF 2MB)', 'Informe Elcano de Presencia Global 2014 (PDF 2MB)');
INSERT INTO translation (key, en, es) VALUES ('Teléfono', 'Phone', 'Teléfono');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global %s (PDF %sMb)', 'Elcano Global Presence Report %s (PDF %sMb)', 'Informe Elcano de Presencia Global %s (PDF %sMb)');
INSERT INTO translation (key, en, es) VALUES ('Calculo índice', 'Index calculation', 'Calculo índice');
INSERT INTO translation (key, en, es) VALUES ('Reiniciar', 'Clear', 'Reiniciar');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Acerca de', 'Elcano Global Presence Index – About', 'Índice Elcano de Presencia Global - Acerca de');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Noticias', 'Elcano Global Presence Index – News', 'Índice Elcano de Presencia Global - Noticias');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Política de privacidad', 'Elcano Global Presence Index – Privacy policy', 'Índice Elcano de Presencia Global - Política de privacidad');
INSERT INTO translation (key, en, es) VALUES ('Ficha país</span>        <span id="tool_title"> <%= app.variableToString(ctx.family) %>, <%= country_str %> </span>        <span id="tool_year">Año', 'Country file', 'Ficha país');
INSERT INTO translation (key, en, es) VALUES ('Ficha país</span>        <span id="tool_title"> <%= app.variableToString(ctx.variables[0]) %>, <%= country_str %> </span>        <span id="tool_year">Año', 'Country file', 'Ficha país');
INSERT INTO translation (key, en, es) VALUES ('Contribuciones de presencia descripción TEXTO', 'This tool allows the presence contributions of two countries or regions to be compared,

along with their total weights.

Presence contribution is to be understood as the magnitude by which each dimension

or indicator represents the total value of a country’s presence. These contributions can

be expressed by the index value or as a percentage of total global presence. Thus, in

Spain’s case, for instance, it can be seen that tourism contributes 30.8 points (18.8%) to

the country’s total global presence, which in 2013 amounted to 164.4.', 'Esta herramienta permite comparar contribuciones de presencia entre dos países o bloques, así como el peso total de cada una de ellas.

Por contribuciones de presencia, entendemos la magnitud en la que cada dimensión o indicador representa en el valor total de presencia de un país. Dichas contribuciones pueden expresarse en valor índice o en porcentaje de la presencia global total. Así, por ejemplo, en el caso de España, podemos decir que el turismo contribuye con 30,8 puntos (18,8%) a su presencia global total, que en 2013 asciende a 164,4.');
INSERT INTO translation (key, en, es) VALUES ('Contribuciones de presencia', 'Contributions', 'Contribuciones de presencia');
INSERT INTO translation (key, en, es) VALUES ('_help p1 txt', 'The Tool Panel allows the activation of the different analysis tools of Explora. Each

of these tools analyses a certain aspect of global and European presence or focuses

on a different visualisation technique. Each tool makes a slightly different use of

Explora’s other interactive elements that are introduced in the following slides.

Additionally, each tool features its own help system. Click on the “+” symbol to

access the catalogue and load the tools onto Explora. Further tools will be released

in new versions of Explora.', 'El panel de herramientas permite activar en Explora las diversas utilidades de análisis de las que dispone. Cada herramienta analiza un aspecto de la presencia global y/o europea o se centra en una técnica de visualización diferente. Tenga en cuenta que cada herramienta hace un uso un tanto distinto de los demás elementos funcionales de Explora que va a conocer a continuación. Cada herramienta tiene una ayuda propia que le guiará en su utilización. Pulse sobre el símbolo “+” para acceder al catálogo de herramientas disponibles y cargarlas en Explora.');
INSERT INTO translation (key, en, es) VALUES ('_help p3 txt', 'This functional element of Explora is divided into two. On the right-hand side there

is an icon that allows the selection of Index variables or dimensions to be analysed,

while on the left-hand side both countries and blocs of interest can be added from

the general catalogue in order to access their data. Click on the “+” symbol to add

new countries. Bear in mind that each tool makes a slightly different use of this

facility. Refer to the tool’s help notes for further details.', 'Este elemento funcional de Explora se divide en dos partes bien diferenciadas. Por un lado, en la parte derecha encontrará un icono mediante el cual podrá acceder a seleccionar la variable o dimensión del Índice que le interesa estudiar en cada momento, mientras que en la parte izquierda, la más amplia, se irán añadiendo los países objeto de su interés para acceder a sus datos a partir del catálogo completo de países y bloques, accesible pulsando en el símbolo “+” situado a la derecha de dicho selector. Tenga en cuenta que cada herramienta puede hacer un uso ligeramente distinto de este elemento funcional. Utilice la ayuda de cada herramienta para más detalles.');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Contacto', 'Elcano Global Presence Index – Contact', 'Índice Elcano de Presencia Global - Contacto');
INSERT INTO translation (key, en, es) VALUES ('Datos agrupados', 'Clustered data', 'Datos agrupados');
INSERT INTO translation (key, en, es) VALUES ('Cuotas', 'Quotas', 'Cuotas');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Documentos', 'Elcano Global Presence Index – Documents', 'Índice Elcano de Presencia Global - Documentos');
INSERT INTO translation (key, en, es) VALUES ('Deseleccionar todos los países', 'Unselect all the countries', 'Deseleccionar todos los países');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Error interno', 'Elcano Global Presence Index – Internal error', 'Índice Elcano de Presencia Global - Error interno');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Datos', 'Elcano Global Presence Index – Data', 'Índice Elcano de Presencia Global - Datos');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Aviso legal', 'Elcano Global Presence Index – Legal', 'Índice Elcano de Presencia Global - Aviso legal');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de Presencia Global - Preguntas frecuentes', 'Elcano Global Presence Index – FAQs', 'Índice Elcano de Presencia Global - Preguntas frecuentes');
INSERT INTO translation (key, en, es) VALUES (' Ranking con filtro %d', 'Ranking with filter %d', 'Ranking con filtro %d');
INSERT INTO translation (key, en, es) VALUES ('_faq title 9', 'What about missing cases? How are they estimated?', '¿Hay casos perdidos? ¿Cómo se estiman?');
INSERT INTO translation (key, en, es) VALUES ('Deseleccionar todos los bloques', 'Unselect all the blocs', 'Deseleccionar todos los bloques');
INSERT INTO translation (key, en, es) VALUES ('_Ayuda_presencia_global_vs_presencia_europea', '<p>This tool compares the global and European presence of EU countries. Select a country from the countries selector and explore dimensions and variables simultaneously on both indexes by interacting with the graphs. </p>

<p>Use the timeline to select which Index edition you would like to access. </p>

<p>The rankings displayed calculated only between countries, with no filters being considered. No blocs are included in the calculations. </p>
', '<p>Esta herramienta compara la presencia global frente a la europea. Seleccione países de la Unión Europea presentes en el selector de países y explore las dimensiones y variables de ambos índices interaccionando con el gráfico.</p>

<p>Utilice la línea de tiempo para seleccionar la edición del Índice que quiere consultar.</p>

<p>Los rankings que aparecen en esta herramienta son rankings calculados exclusivamente entre países, y sin tener en cuenta ningún filtro. En ningún caso la UE entra en el cálculo de dicho ranking.</p>');
INSERT INTO translation (key, en, es) VALUES ('_faq text 12', 'The Elcano Global Presence Index is calculated for 110 countries: the first 103 world economies (with the exception of Bahrain), the countries not listed in these positions that are nonetheless members of the OECD or the EU and Zambia, Zimbabwe, Botswana and Senegal (in order to increase the representativeness of the African region in the time series)', 'El Índice Elcano de Presencia Global se calcula para 110 países: las primeras 103 economías mundiales (con la excepción de Baréin) y los países que, sin encontrarse entre estas primeras posiciones, son miembros de la OCDE y/o de la Unión Europea. Asimismo, se incluyen Zambia, Zimbabue, Botsuana y Senegal (con la finalidad de aumentar la representación de la región africana en las series temporales)');
INSERT INTO translation (key, en, es) VALUES ('_Ayuda_ranking', '<p>The Ranking tool orders countries and blocs by their Index value. The ranking can be calculated by the Index itself or by means of any of its dimensions (economic, military, or soft) or indicators. </p>

<p>You can switch between global and European presence rankings by using the top right-hand button. In regards to global presence, there are three kinds of rankings available: countries, countries + EU and blocs. The first only takes into account countries, applying any of the filters that might be activated; the second considers the EU as a single country and calculates its ranking in relation to all other countries, excluding those which are member States in that particular year; the third calculates bloc rankings. </p>

<p>The dimensions or variables to be used to calculate the various rankings can be chosen with the variables selector. </p>

<p>To select the year whose ranking is to be calculated adjust the red dot over the timeline. The grey dot indicate the particular year to be used as a reference. The upper bar represents the variable’s value for the selected year (red dot), while the bottom bar indicates the reference year (grey dot). The ranking is always calculated on the basis of the year indicated by the red dot. </p>

<p>The ranking tool always considers all countries or blocs and is not restricted to those selected in the country selector. You can use the latter to move around the ranking to key countries. Nevertheless, filtered countries do not appear in the rankings. </p>
', '<p>La herramienta de ranking ordena los países o bloques por su valor índice. Dicha ordenación puede realizarse sobre la base de su presencia global, de sus dimensiones (económica, militar o blanda) o de cualquiera de los indicadores que componen estas.</p>

<p>Puede consultar los rankings de presencia global o europea utilizando el conmutador de la parte superior derecha. Para presencia global se pueden seleccionar tres cálculos distintos de rankings: ranking de países, de países más UE y de bloques.</p>

<p>El primero calcula, teniendo siempre en cuenta cualquier filtro activo, el ranking entre países. El segundo trata a la Unión Europea como un país, y calcula su posición entre el resto de países que no son miembros de la Unión. El tercero, por último, calcula el ranking entre los bloques. </p>

<p>Puede cambiar la variable o dimensión del índice sobre la que quiere calcular el ranking seleccionandola en el selector de variable.</p>

<p>Seleccione el año cuyo ranking quiere calcular desplazando el punto rojo sobre la línea de tiempo. Utilice el punto gris si quiere establecer algún año como periodo de referencia. La barra superior para cada país muestra el valor de la variable seleccionada para el año establecido, mientras que la inferior muestra el valor de la misma para el año de referencia. El ranking se calcula siempre en función del año seleccionado en rojo.</p>

<p>La herramienta de ranking siempre tiene en cuenta a todos los países o bloques, independientemente de los que haya seleccionado en el selector de países. Utilice éste último para desplazarse a través del listado. Los países filtrados no aparecen en el ranking, sin embargo.</p>');
INSERT INTO translation (key, en, es) VALUES ('_help p4 txt', 'The timeline is used to alter the Index’s time dimension. Explora includes all data from previous published editions. Alter the position along

the time axis to select the year. Remember that each tool makes a different use of

this element. Some tools may not use it at all and others might allow the selection

of one time spot or even two, while some might even allow the selection of a time

lapse. Check the tool’s help notes for more details.', 'La línea de tiempo permite alterar la dimensión temporal del Índice. Explora incluye los datos de todas las ediciones publicadas. Desplace el marcador de tiempo a lo largo de la línea para seleccionar el año de su elección. Recuerde, una vez más, que este elemento funcional puede ver alterado su funcionamiento para cada herramienta de análisis. Algunas directamente no la usan, otras le permite seleccionar un momento temporal, mientras que otras pueden permitirle seleccionar dos o incluso un intervalo. Utilice la ayuda de cada herramienta para más detalles.');
INSERT INTO translation (key, en, es) VALUES ('_methodology p1', 'This year’s edition covers the global presence of a selection of 110 countries. The selection includes the first 103 world economies (with the exception of Bahrain), the countries not listed in these positions that are nonetheless members of the OECD or the EU and Zambia, Zimbabwe, Botswana and Senegal (in order to increase the representativeness of the African region in the time series).', 'El Índice Elcano de presencia global cubre una selección de 110 países. Éstos son las primeras 103 economías mundiales (con la excepción de Baréin) y los países que, sin encontrarse entre estas primeras posiciones, son miembros de la OCDE y/o de la Unión Europea. Asimismo, se incluyen Zambia, Zimbabue, Botsuana y Senegal (con la finalidad de aumentar la representación de la región africana en las series temporales).');
INSERT INTO translation (key, en, es) VALUES ('La <strong>presencia blanda</strong> se mide a través de las migraciones, el turismo, el rendimiento deportivo en competiciones internacionales, las patentes internacionales, los artículos publicados en revistas científicas, la ayuda al desarrollo, entre otros.', 'The <strong>soft presence</strong> is defined through migration, tourism, performance in sports competitions, culture, information, international patents, articles in scientific journals, foreign students and the gross flows of development assistance.', 'La <strong>presencia blanda</strong> definida a través de las migraciones, turismo, rendimiento deportivo, cultura, información, patentes internacionales, producción científica, estudiantes extranjeros y gasto en ayuda al desarrollo.');
INSERT INTO translation (key, en, es) VALUES ('_methodology criterios lista pie p', 'In defining the weightings of each of the elements included in the Index, we conducted surveys with a panel of experts in international relations from the five continents. The surveys were done in 2011, 2012 and 2015, to experts selected on the basis of the report <a href=''http://gotothinktank.com/'' target=''_blank''>The Global Go To Think Tanks published annually by the University of Pennsylvania.</a>The questionnaire was sent to 45 institutions in the United States, 40 in Europe, 27 in Asia, 17 in Latin America, 12 in Africa, eight in the Middle East and North Africa, and three in Oceania.', 'Para definir la ponderación de los elementos del índice, se ha recurrido a la valoración de expertos en relaciones internacionales de los cinco continentes. Las encuestas se realizaron en 2011, 2012 y 2015, a expertos seleccionados sobre la base base del informe <a href=''http://gotothinktank.com/'' target=''_blank''>Global Go To Think Tanks que publica anualmente la Universidad de Pensilvania.</a>  El cuestionario fue enviado a 45 instituciones norteamericanas, 40 europeas, 27 asiáticas, 17 latinoamericanas, 12 africanas, 8 de Oriente Medio y Norte de África, y 3 de Oceanía.');
INSERT INTO translation (key, en, es) VALUES ('_Ayuda_ficha_pais', '<p>Country factsheets are profiles of countries or blocs from a general perspective, summarising information regarding population, GDP, position in the Index ranking and contributions to different types of presence.</p><p>You can add a country or bloc to the country selector in order to access their data, while you can easily switch between countries by clicking on their icons. The sector graphic is fully interactive, allowing navigation between the Index’s dimensions to explore its variables. You can also use the timeline to access a different edition of the Index. To switch between global and European presence use the button at the top right-hand section of the application. </p><h6>Rankings</h6><p>The country factsheets employ various kinds of rankings depending on the type of territorial unit chosen in the county selector. </p><p>If the selected territorial unit is a country, rankings will refer to its position in relation to other countries, with no reference being made to any blocs. The global ranking is always displayed, while a filtered ranking may appear if a filter is active and the country selected has a higher score because of it. </p><p>If the selected unit is the European Union, the ranking –described as ‘Countries + EU Ranking’– is that obtained by considering the EU as a single country and matching it against all other countries except for its member States, which are removed from the list. Filters can also be used. </p><p>Finally, if the territorial unit is a bloc, the rank calculated –the ‘Bloc Ranking’– is the bloc’s position in relation to all other blocs, excluding the European Union. </p>', '<p>Las fichas-país caracterizan de manera general cada país o bloque dentro del Índice, recogiendo su información básica referida a población, PIB, puesto en el ranking y contribuciones de presencia.</p><p>Añada un país al selector de países para acceder a sus datos, podrá cambiar fácilmente de país seleccionado pulsando en la bandera correspondiente en dicho selector. Interaccione con el gráfico de sectores para explorar las distintas dimensiones del Índice, así como con la línea de tiempo para cambiar la edición del Índice a consultar.</p><p>Puede utilizar el conmutador de Presencia Global / Europea para obtener datos de estos dos aspectos del Índice.</p><h6>Rankings</h6><p>La ficha país contempla varios tipos de ranking, en función de la unidad territorial que tenga seleccionada en cada instante en el selector de países.</p><p>Si la unidad territorial seleccionada es un país, los rankings que obtendrá es la posición del país seleccionado entre el resto de países. En ningún momento entrará en el cálculo ningún bloque. Se mostrará siempre el ranking global del país conforme al resto, pero si estuviera activo algún filtro, en el caso de que dicho ranking difiriera también obtendría dicho ranking filtrado.</p><p>Si la unidad territorial seleccionada es la Unión Europea, el ranking obtenido, denotado como “Ranking de países + UE”, es aquel que se obtiene de considerar el conjunto de países más la Unión Europea, habiendo eliminado del cálculo a todos los países miembros para el año seleccionado. Los filtros también influyen en este ranking.</p><p>Por último, si la unidad territorial seleccionada es un bloque, el ranking obtenido, llamado “Ranking de bloque”, es la posición del bloque seleccionado dentro del resto de bloques (excluida la Unión Europea).</p>');
INSERT INTO translation (key, en, es) VALUES ('_name ', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('Seguir leyendo', 'Read more', 'Seguir leyendo');
INSERT INTO translation (key, en, es) VALUES ('seguir leyendo', 'read more', 'seguir leyendo');
INSERT INTO translation (key, en, es) VALUES ('Presencia global', 'Global presence', 'Presencia global');
INSERT INTO translation (key, en, es) VALUES ('Contribución de presencia', 'Presence contribution', 'Contribución de presencia');
INSERT INTO translation (key, en, es) VALUES ('Análisis', 'Analysis', 'Análisis');
INSERT INTO translation (key, en, es) VALUES ('Datos básicos del país', 'Country''s basic data', 'Datos básicos del país');
INSERT INTO translation (key, en, es) VALUES ('Presencia europea', 'European presence', 'Presencia europea');
INSERT INTO translation (key, en, es) VALUES ('Presencia global / europea', 'Global / european presence', 'Presencia global / europea');
INSERT INTO translation (key, en, es) VALUES ('Ver referencia', 'See reference', 'Ver referencia');
INSERT INTO translation (key, en, es) VALUES (' Con filtro %d', 'With filter %d', 'Con filtro %d');
INSERT INTO translation (key, en, es) VALUES ('Si no es debido a ninguno de los puntos anteriores consulte la ayuda de la herramienta, pulsando la &apos;?&apos; de información de la esquina superior derecha', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('_privacity body', '<p>(*) The English version will soon be available. We apologise for any inconvenience and we appreciate your understanding.</p>', '<p>De conformidad con lo establecido en el art. 5 de la Ley Orgánica 15/1999,  deProtección de Datos de Carácter Personal (LOPD) y en la normativa de desarrollo, ustedqueda informado y presta su consentimiento a la incorporación de sus datos personales a un fichero automatizado propiedad de la Fundación Real Instituto Elcano de Estudiosnternacionales y Estratégicos. </p><p>Los datos, cuya confidencialidad queda garantizada, no se recogen sin sunsentimiento ni se ceden a terceros, y están siendo tratados e incorporados a los crespondientes ficheros automatizados que están debidamente inscritos en el Registroeral de Protección de Datos. Serán utilizados por el Real Instituto Elcano con lanidad de remitir las publicaciones digitales, otros documentos e informes realizados p ta institución, así como información relativa a las actividades del mismo. </p><p>Igualmente, de conformidad con lo establecido en el art. 5 de la Ley Orgánica 15/1999,erección de Datos de Carácter Personal (LOPD) y en la normativa de desarrollo,e formado de la posibilidad de ejercer, conforme a dicha normativa, los derechos dae, rectificación, cancelación y oposición ante el Real Instituto. Para ejercitarssechos podrá dirigir la oportuna solicitud enviando un correo electrónico bajo elcemnto “PROTECCIÓN DE DATOS” a la dirección <rgb[arroba]rielcano.org</strong>, o por correo postal a la dirección:<br/><strong>Fundación Real Instituto Elcano de Estudios Internacionales y Estratégicos</strong><br/>c/ Príncipe de Vergara, nº 51<br/>28006-Madrid. España</p>');
INSERT INTO translation (key, en, es) VALUES ('Copyright TEXT', '2014 - 2018 &copy; Elcano Royal Institute ', '2014 - 2018 &copy; Real Instituto Elcano');
INSERT INTO translation (key, en, es) VALUES ('_faq text 9', 'In these cases we have also referred to expert opinion. A total of 2,595 data items have been estimated from 48,592 observations. The number of estimations accounts for 5.3% of the base', 'Para ello, se ha recurrido al criterio del experto. Se han estimado 2.595 datos de un total de 48.592 observaciones. El número de estimaciones asciende a 5,3% de la base');
INSERT INTO translation (key, en, es) VALUES ('_legal body', '<p>(*) The English version will soon be available. We apologise for any inconvenience and we appreciate your understanding.</p>', '<p>Esta Web es mantenida, coordinada y gestionada por la <strong>Fundación Real InstitutoElcano de Estudios Internacionales y Estratégicos</strong>. Príncipe de Vergara, 51. 28006Madrid (España). El Real Instituto Elcano es titular de los derechos de propiedad intelectual sobre las publicaciones, imágenes, textos, diseños, animaciones, o cualquiertro contenido o elementos de esta Web, o dispone de los permisos necesarios para suilización. </p><p>Las publicaciones y contenidos incluidos en la Web se facilitan únicamente a usuarios fales. Queda prohibida la reproducción sin reconocimiento expreso de los créditos aorespectivos autores de las publicaciones o de los contenidos, incluyendo la URL onlo a la Web del Real Instituto Elcano; así como cualquier uso comercial no aozado de los mismos o su reventa.</p><p>El Real Instituto Elcano no comparte necesariamente las opiniones manifestadas en losomtos firmados por investigadores y colaboradores y difundidos en su Web o enaur otra publicación del Real Instituto. El Instituto considera que su misión fdeal es servir de foro de discusión y análisis, estimulando el debate yegn opiniones diversas sobre temas de la actualidad internacional, y muyrcaente sobre aquellos que afecten a las relaciones internacionales de España y sreuón en los diferentes ámbitos de la sociedad española.</p>');
INSERT INTO translation (key, en, es) VALUES ('Variable information desc TEXTO', 'Internet bandwidth (Mbps) and number of mentions in news of main international press agencies (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua)', 'Ancho de banda de Internet (Mbps) y Número de menciones en noticias de las principales agencias (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua)');
INSERT INTO translation (key, en, es) VALUES ('Ficha país descripción TEXTO', 'The country files provide a general description of each country or region in the Index,

aggregating basic information on population, PIB, rank and presence. Additionally, for

the EU and the countries in the first 11 positions in the ranking, the files include a brief

analysis of their most salient traits as regards their international integration.', 'Las fichas-país caracterizan de manera general cada país o bloque dentro del Índice, recogiendo su información básica referida a población, PIB, puesto en el ranking y contribuciones de presencia.');
INSERT INTO translation (key, en, es) VALUES ('Variables, Indicadores y fuentes del Índice Elcano de Presencia Europea', 'Variables, indicators and sources of the Elcano European Presence Index', 'Variables, Indicadores y fuentes del Índice Elcano de Presencia Europea');
INSERT INTO translation (key, en, es) VALUES ('Variables, indicadores y fuentes del Índice Elcano de Presencia Global', 'Variables, indicators and sources of the Elcano Global Presence Index', 'Variables, indicadores y fuentes del Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('_link download', 'download', 'descarga');
INSERT INTO translation (key, en, es) VALUES ('Datos', 'Data', 'Datos');
INSERT INTO translation (key, en, es) VALUES ('Países', 'Countries', 'Países');
INSERT INTO translation (key, en, es) VALUES ('Todos', 'All', 'Todos');
INSERT INTO translation (key, en, es) VALUES ('Preguntas frecuentes', 'Frequent questions', 'Preguntas frecuentes');
INSERT INTO translation (key, en, es) VALUES ('Seleccione las variables', 'Select variables', 'Seleccione las variables');
INSERT INTO translation (key, en, es) VALUES ('Seleccione los años', 'Select years', 'Seleccione los años');
INSERT INTO translation (key, en, es) VALUES ('Seleccione los países', 'Select countries', 'Seleccione los países');
INSERT INTO translation (key, en, es) VALUES ('Siguiente', 'Next', 'Siguiente');
INSERT INTO translation (key, en, es) VALUES ('<span class="numAniosSelect">0</span> años seleccionados', '<span class="numAniosSelect">0</span> years selected', '<span class="numAniosSelect">0</span> años seleccionados');
INSERT INTO translation (key, en, es) VALUES ('<span class="numBloqsSelect">0</span> variables seleccionadas', '<span class="numBloqsSelect">0</span> selected variables', '<span class="numBloqsSelect">0</span> variables seleccionadas');
INSERT INTO translation (key, en, es) VALUES ('<span class="numPaises">0</span> países seleccionados', '<span class="numPaises">0</span> countries selected', '<span class="numPaises">0</span> países seleccionados');
INSERT INTO translation (key, en, es) VALUES ('Variables temáticas', 'Thematic variables', 'Variables temáticas');
INSERT INTO translation (key, en, es) VALUES ('Ayuda', 'Help', 'Ayuda');
INSERT INTO translation (key, en, es) VALUES ('Comenzar a explorar', 'Start to explore', 'Comenzar a explorar');
INSERT INTO translation (key, en, es) VALUES ('_about subtitle ppal', 'What is the Elcano Global Presence Index?', 'Qué es el Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Paso 2/3 ', 'Step 2/3 ', 'Paso 2/3');
INSERT INTO translation (key, en, es) VALUES ('Paso 3/3 ', 'Step 3/3 ', 'Paso 3/3');
INSERT INTO translation (key, en, es) VALUES ('Descarga de datos en excel', 'Download Excel data', 'Descarga de datos en Excel');
INSERT INTO translation (key, en, es) VALUES ('Paso 1/3 ', 'Step 1/3 ', 'Paso 1/3');
INSERT INTO translation (key, en, es) VALUES ('Seleccione al menos un país', 'At least select one country', 'Seleccione al menos un país');
INSERT INTO translation (key, en, es) VALUES ('Seleccione un país o arrástrelo hasta aquí desde la cabecera de análisis', 'Select one country or drag it from the analysis header', 'Seleccione un país o arrástrelo hasta aquí desde la cabecera de análisis');
INSERT INTO translation (key, en, es) VALUES ('1 país ', '1 country', '1 país');
INSERT INTO translation (key, en, es) VALUES ('1 país filtrado', '1 country filtered', '1 país filtrado');
INSERT INTO translation (key, en, es) VALUES ('Ayuda ranking', 'Ranking help', 'Ayuda ranking');
INSERT INTO translation (key, en, es) VALUES ('Ayuda tooltip', 'Tooltip help', 'Ayuda tooltip');
INSERT INTO translation (key, en, es) VALUES ('Ayuda ficha país', 'Country fact sheet help', 'Ayuda ficha país');
INSERT INTO translation (key, en, es) VALUES (' %d bloques', '%d blocks', '%d bloques');
INSERT INTO translation (key, en, es) VALUES (' %d países', '%d countries', '%d países');
INSERT INTO translation (key, en, es) VALUES ('%d países filtrados', '%d countries filtered', '%d países filtrados');
INSERT INTO translation (key, en, es) VALUES ('El bloque o país no existía en el año seleccionado', 'The block or country did not exist the year selected', 'El bloque o país no existía en el año seleccionado');
INSERT INTO translation (key, en, es) VALUES ('Esto puede ser debido a:', 'This may happen because:', 'Esto puede ser debido a:');
INSERT INTO translation (key, en, es) VALUES ('Incluir todos los países en el análisis', 'Include all countries in the analysis', 'Incluir todos los países en el análisis');
INSERT INTO translation (key, en, es) VALUES ('Índice Elcano de presencia europea', 'Elcano European Presence Index', 'Índice Elcano de Presencia Europea');
INSERT INTO translation (key, en, es) VALUES ('Valor', 'Value', 'Valor');
INSERT INTO translation (key, en, es) VALUES ('Bloques de países', 'Country blocs', 'Bloques de países');
INSERT INTO translation (key, en, es) VALUES ('1 bloque', '1 bloc', '1 bloque');
INSERT INTO translation (key, en, es) VALUES ('El bloque %s está compuesto por', 'For the year selected, the bloc %s is made up of', 'En el año seleccionado, el bloque %s está compuesto por');
INSERT INTO translation (key, en, es) VALUES ('_faq text 1', 'The Index measures global presence. By global presence we understand the effective positioning, in absolute terms, of the different countries (products sold, tourists welcomed, victories in international sports competitions…)', 'Este Índice mide la presencia global. Por presencia global entendemos la proyección efectiva real de los países fuera de sus fronteras en los ámbitos económico, político y social (exportaciones realizadas, turistas recibidos, competiciones deportivas internacionales ganadas…)');
INSERT INTO translation (key, en, es) VALUES ('_faq text 2', 'No. A country may have strong international projection and weak regional or global influence (or vice-versa). The relationship between presence and power depends on the foreign policy of each country or on the limiting factors of the exercise of influence depending, for instance, on the presence of another regional leader', 'No. Un país puede tener una alta proyección internacional pero una baja influencia regional o global. La relación entre presencia y poder dependerá, entre otros factores, de la política exterior de cada país (la voluntad de ejercer el poder) o de los limitantes al ejercicio de la influencia, dependiendo, por ejemplo, de la presencia de otro líder regional');
INSERT INTO translation (key, en, es) VALUES ('_faq text 8', 'Weights assigned to variables and dimensions are based on experts’ criteria. Two surveys were conducted in 2012 and 2015: questionnaires were sent to specialists in international relations, and answers were combined to determine the weights of variables and dimensions', 'Los pesos asignados a variables y dimensiones están basados en el criterio de expertos. Se llevaron a cabo sendas encuestas, en 2012 y 2015, a un panel internacional de especialistas en relaciones internacionales cuyas respuestas se combinaron para determinar el peso de las variables y de las dimensiones');
INSERT INTO translation (key, en, es) VALUES ('La <strong>presencia blanda</strong> se mide a través de lasmigraciones, el turismo, el rendimiento deportivo en competiciones internacionales, las patentesinternacionales, los artículos publicados en revistascientíficas, la ayuda al desarrollo, entre otros.', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('La <strong>presencia militar</strong> se mide con las tropasdesplegadas en el extranjero y con el equipamientomilitar.', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('La <strong>presencia económica</strong> se mide a través de lasexportaciones de energía, bienes primarios,manufacturas y servicios, así como las inversionesdirectas en el exterior.', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('Community manager y asistente web', 'Digital Communications Assistant & Community Manager', 'Asistente de Comunicación Digital y Community Manager');
INSERT INTO translation (key, en, es) VALUES ('_methodology más información lista', '<ul class="util">

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
</ul>', '<ul class="util">

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
</ul>');
INSERT INTO translation (key, en, es) VALUES ('_methodology tabla general', '<table class=''data''>
  <tr><th>Indicator</th><th>Description</th><th>Source</th></tr>
  <tr class=''section''>
      <td colspan=''3''>Economic Presence</td>
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
      <td>Flow of exports of services in transport, construction, insurance, financial services, IT, the media, intellectual property, other business services, personal, cultural and leisure services, and public services</td>
  </tr>
  <tr>
      <td>Investments</td>
      <td>Stock of foreign direct investment abroad</td>
  </tr>

  <tr class=''section''>
      <td colspan=''3''>Military presence</td>
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

  <tr class=''section''>
      <td colspan=''3''>Soft presence</td>
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
      <td>Exports of audiovisual services (cinematographic productions, radio and television programs, and musical recordings)</td>
      <td>WTO – International Trade Statistics</td>
  </tr>
  <tr>
      <td>Information</td>
      <td>Number of mentions in news of main international press agencies (Associated Press, Reuters, AFP, DPA, ITAR-TASS, EFE, ANSA, Xinhua) and internet bandwidth (Mbps)</td>
      <td>Factiva database International Telecommunication Union</td>
  </tr>
  <tr>
      <td>Technology</td>
      <td>Foreign-oriented patents: number of inter-related patent applications filed in one or more foreign countries to protect the same invention</td>
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
      <td>OECD and official national sources</td>
  </tr>
  <tr class=''section''>
      <td colspan=''3''>Scaling factors</td>
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
</table>', '<table class=''data''>
  <tr><th>Variable</th><th>Indicador</th><th>Fuente</th></tr>
  <tr class=''section''>
      <td colspan=''3''>Presencia económica</td>
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
      <td>Flujo de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos</td>
  </tr>
  <tr>
      <td>Inversiones</td>
      <td><em>Stock</em> de inversión directa extranjera en el exterior</td>
  </tr>

  <tr class=''section''>
      <td colspan=''3''>Presencia militar</td>
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
  <tr class=''section''>
      <td colspan=''3''>Presencia blanda</td>
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
      <td>Exportaciones de servicios audiovisuales (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales)</td>
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
      <td>Patentes orientadas al exterior: número de solicitudes de patentes relacionadas entre sí depositadas en uno o más países extranjeros para proteger la misma invención</td>
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
      <td>UNESCO – Institute for Statistics, OCDE – iLibrary</td>
  </tr>
  <tr>
      <td>Cooperación al desarrollo</td>
      <td>Flujo de ayuda oficial al desarrollo bruto total o datos homologables</td>
      <td>OCDE y fuentes nacionales oficiales</td>
  </tr>
  <tr class=''section''>
      <td colspan=''3''>Factores de escala</td>
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
</table>');
INSERT INTO translation (key, en, es) VALUES ('La', ' ', 'La');
INSERT INTO translation (key, en, es) VALUES ('_faq text 4', 'No. The Elcano Global Presence Index considers the external projection of the different countries and not so much the way in which they absorb the external action of other countries in their national territory. That is why the index considers the exports of manufactured goods but disregards the imports. It does not measure world interdependence, though it may help to analyse it', 'Tampoco. Considera la proyección exterior de los países y no tanto la manera en la que absorben la acción exterior de otros países en su territorio. De este modo, por ejemplo, el Índice considera las exportaciones de manufacturas, pero no las importaciones. No es un índice de medición de la interdependencia mundial, aunque ayude a analizarla');
INSERT INTO translation (key, en, es) VALUES ('_faq title 10', 'The Index has been calculated for what years?', '¿Para qué años se calcula el Índice?');
INSERT INTO translation (key, en, es) VALUES ('Coordinadora de la Web y Elcano Blog', 'Digital Communications Manager', 'Coordinadora de Comunicación Digital');
INSERT INTO translation (key, en, es) VALUES ('Investigadora principal del Real Instituto Elcano y coordinadora del Proyecto Índice Elcano de Presencia Global', 'Senior analyst at the Elcano Royal Institute and Coordinator of the Elcano Global Presence Index Project', 'Investigadora principal del Real Instituto Elcano y coordinadora del Proyecto Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('Ayudante de investigación', NULL, NULL);
INSERT INTO translation (key, en, es) VALUES ('presencia militar', 'Military presence', 'presencia militar');
INSERT INTO translation (key, en, es) VALUES ('Preguntas frecuentes sobre el Índice Elcano de Presencia Global', 'Frequently asked questions about Elcano Global Presence Index', 'Preguntas frecuentes sobre el Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('_home IEPG explora desc', 'The <a class=\"nostyle\" href=\"%s\"><strong>Elcano Global Presence Index</strong></a> is an annual measurement of the projection in the world of 110 countries based on three dimensions:', 'El <a class=\"nostyle\" href=\"%s\"><strong>Índice Elcano de Presencia Global</strong></a> calcula anualmente la proyección de 110 países fuera de sus fronteras en función de tres dimensiones:');
INSERT INTO translation (key, en, es) VALUES ('_methodology tabla IEPE', '<table class=''data''>
  <tr><th>Indicator</th><th>Description</th><th>Source</th></tr>
  <tr class=''section''>
      <td colspan=''3''>Economic presence</td>
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

  <tr class=''section''>
      <td colspan=''3''>Military presence</td>
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

  <tr class=''section''>
      <td colspan=''3''>Soft presence</td>
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
      <td>Intra-EU exports of audiovisual services (cinematographic productions, radio and television programmes, and musical recordings)</td>
      <td>Eurostat and national sources</td>
  </tr>
  <tr>
      <td>Information</td>
      <td>Number of mentions in news of main european press agencies (Reuters, AFP, DPA, ANSA and EFE) and internet bandwidth (Mbps)</td>
      <td>Factiva database International Telecommunication Union</td>
  </tr>
  <tr>
      <td>Technology</td>
      <td>Number of patents registered at the European Patent Office (EPO)</td>
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
   <tr class=''section''>
      <td colspan=''3''>Scaling factors</td>
  </tr>
  <tr>
      <td>Economy</td>
      <td>Gross Domestic Product (GDP) at current prices in US dollars</td>
      <td>Eurostat</td>
  </tr>
  <tr>
      <td>Population</td>
      <td>Number of inhabitants</td>
	  <td>Eurostat</td>
  </tr>
</table>', '<table class=''data''>
  <tr><th>Variable</th><th>Indicador</th><th>Fuente</th></tr>
  <tr class=''section''>
      <td colspan=''3''>Presencia económica</td>
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
      <td>Flujos intra-comunitarios de exportación de servicios en transporte, construcción, seguros, servicios financieros, informática, medios de comunicación, propiedad intelectual, otros servicios empresariales, servicios personales, culturales y de ocio y servicios públicos</td>
  </tr>
  <tr>
      <td>Inversiones</td>
      <td><em>Stock</em> de inversión directa extranjera en la UE</td>
  </tr>

  <tr class=''section''>
      <td colspan=''3''>Presencia militar</td>
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
  <tr class=''section''>
      <td colspan=''3''>Presencia blanda</td>
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
      <td>Exportaciones intra-comunitarias de servicios audiovisuales (producciones cinematográficas, programas de radio y televisión, y grabaciones musicales)</td>
      <td>Eurostat y fuentes nacionales</td>
  </tr>
  <tr>
      <td>Información</td>
      <td>Número de menciones en cables por parte de las principales agencias de noticias europeas (Reuters, AFP, ANSA, DPA y EFE) y ancho de banda de Internet (Mbps)</td>
      <td>Base de datos de Factiva y Unión Internacional de las Telcomunicaciones (UIT)</td>
  </tr>
  <tr>
      <td>Tecnología</td>
      <td>Número de patentes registradas en la Oficina Europea de Patentes (EPO)</td>
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
    <tr class=''section''>
      <td colspan=''3''>Factores de escala</td>
  </tr>
  <tr>
      <td>Economía</td>
      <td>Producto Interior Bruto (PIB) a precios corrientes en dólares EEUU</td>
      <td>Eurostat</td>
  </tr>
  <tr>
      <td>Población</td>
      <td>Número de habitantes</td>
	  <td>Eurostat</td>
  </tr>
</table>');
INSERT INTO translation (key, en, es) VALUES ('se mide con las tropasdesplegadas en el extranjero y con el equipamientomilitar.', 'is measured with the troops deployed abroad and with military equipment.', 'se mide con las tropas desplegadas en el extranjero y con el equipamiento militar.');
INSERT INTO translation (key, en, es) VALUES ('presencia económica', 'Economic presence', 'presencia económica');
INSERT INTO translation (key, en, es) VALUES ('se mide a través de lasexportaciones de energía, bienes primarios,manufacturas y servicios, así como las inversionesdirectas en el exterior.', 'is measured through exports of energy, primary goods, manufacturing and services, as well as direct investments abroad.', 'se mide a través de las exportaciones de energía, bienes primarios, manufacturas y servicios, así como las inversiones directas en el exterior.');
INSERT INTO translation (key, en, es) VALUES ('presencia blanda', 'Soft presence', 'presencia blanda');
INSERT INTO translation (key, en, es) VALUES ('_faq text 10', 'For 1990, 1995, 2000, 2005, and 2010-17. Since 2010 the calculation is performed annually', 'Para 1990, 1995, 2000, 2005, y 2010-2017. Desde 2010, el cálculo es anual');
INSERT INTO translation (key, en, es) VALUES ('Coordinadora', 'Coordinator', 'Coordinadora');
INSERT INTO translation (key, en, es) VALUES ('Investigador del Proyecto Índice Elcano de Presencia Global', 'Analyst for the Elcano Global Presence Index Project', 'Investigador del Proyecto Índice Elcano de Presencia Global');
INSERT INTO translation (key, en, es) VALUES ('se mide a través de lasmigraciones, el turismo, el rendimiento deportivo en competiciones internacionales, las patentesinternacionales, los artículos publicados en revistascientíficas, la ayuda al desarrollo, entre otros.', 'is measured through migration, tourism, sports performance in international competitions, international patents, articles published in scientific journals, or official development assistance, among other indicators.', 'se mide a través de las migraciones, el turismo, el rendimiento deportivo en competiciones internacionales, las patentes internacionales, los artículos publicados en revistas científicas, la ayuda al desarrollo, entre otros.');


COMMIT;

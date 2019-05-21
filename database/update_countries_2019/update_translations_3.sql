


BEGIN;

UPDATE www.translation SET es = 'Variables, indicadores y fuentes del Índice Elcano de Presencia Europea' WHERE key = 'Variables, Indicadores y fuentes del Índice Elcano de Presencia Europea';

UPDATE www.translation SET es = 'Preguntas frecuentes' WHERE key = 'Preguntas frecuentes';
UPDATE www.translation SET en = 'Frequently asked questions' WHERE key = 'Preguntas frecuentes';

UPDATE www.translation SET es = E'Esta herramienta permite comparar las cuotas de presencia de países y bloques a lo largo del tiempo.\r La cuota de presencia es la proporción de proyección exterior que un determinado país ocupa en el universo de la presencia global total. Para su cálculo, se divide el valor índice de presencia global de un país por la suma de presencia global total –la de los 120 países para los que calculamos el índice– , y se multiplica por 100.' WHERE key = 'Cuotas de presencia descripción TEXTO';

UPDATE www.translation SET en = E'This tool allows the quota of presence of countries and blocks to be compared.\r The presence quota is the share of foreign projection held by a country or bloc in the total global presence universe. To calculate it the global presence index of a country is divided by the sum of the total global presence –ie, of the 120 countries included in the study– and then multiplied by 100.' WHERE key = 'Cuotas de presencia descripción TEXTO';

UPDATE www.translation SET es = E'<p>Esta herramienta permite comparar las cuotas de presencia de países y bloques a lo largo del tiempo.</p>\r
\r
<p>La cuota de presencia es la proporción de proyección exterior que un
determinado país ocupa en el universo de la presencia global total. Para su cálculo, se divide el valor índice de presencia global de un país por la suma de presencia global total –la de los 120 países para los que calculamos el índice– , y se multiplica por 100.
</p>\r
\r
<p>Esta herramienta crea un gráfico temporal con las cuotas de presencia de todos los países y bloques presentes en el selector de países para la dimensión seleccionada. Tenga en cuenta que no existen datos de cuota para las variables, tan sólo para el Índice global y las dimensiones económica, militar y blanda. Pulse sobre un país en el selector para resaltar su línea temporal en el gráfico.</p>\r
\r
<p>Seleccione el momento temporal en la línea de tiempo inferior. Si bien el gráfico se ve escasamente afectado, el mapa sí mostrará los valores de cuota de dicho año.</p>' WHERE key = '_Ayuda_cuotas';

UPDATE www.translation SET en = E'<p>This tool allows the quota of presence of countries and blocks to be compared.</p>\r
\r
<p>The presence quota is the share of foreign projection held by a country or bloc in the total global presence universe. To calculate it the global presence index of a country is divided by the sum of the total global presence –ie, of the 120
countries included in the study– and then multiplied by 100.
</p>\r
\r
<p>The tool employs a temporal evolution graph to plot the presence quotas of all countries and blocs present in the countries selector for the selected dimension. Please note that there are no data for variables, only for the global index and for the economic, military and soft dimensions. Click on a country in the countries selector to highlight the appropriate time period on the plot.
</p>\r
\r
<p>You can select the appropriate time period with the timeline. Although the plot is minimally altered, the map will draw the quota data for the selected year.</p>' WHERE key = '_Ayuda_cuotas';


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
       <td>Suma ponderada de los puntos en el medallero en los Juegos Olímpicos de verano, la clasificación mundial FIFA de selecciones absolutas y la clasificación mundial de clubes de fútbol del IFFHS</td>
       <td>COI, IFFHS y FIFA</td>
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
       <td>Clarivate Analytics – Web of Science, Primary Collection</td>
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

COMMIT;

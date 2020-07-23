
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

UPDATE iepg_data_redux.iepg_comment
 SET comment='<p>US tops the Elcano Global Presence Index in all years. In 2019, it also leads the ranking in all variables, with the exception of energy, manufactures and tourism. Of all 130 countries, it records the highest share of presence in all dimensions: 18.8% in the economic domain, 28.2% in the military and 22.5% in soft presence. Moreover, unlike other developed countries, its military dimension strongly defines its index value, with a contribution at 25.5% in 2019.</p><p>Despite its hegemony, the USAloses relative global presence when compared with other countries: from a 24.8% share of global presence in 1990 to 21.5% in 2019. In a period of  emergence  of  new  global  players,  several  economies  (particularly  oil  producers  or Asian countries) reap gains of share that reduce the American role.</p>'
 WHERE code='US' AND language='en';

COMMIT;
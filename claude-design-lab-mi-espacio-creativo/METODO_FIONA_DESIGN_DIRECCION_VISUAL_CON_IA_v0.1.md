# Método Fiona Design — Dirección Visual con IA
## Documento metodológico v0.1

**Proyecto de investigación:** Mi Espacio Creativo  
**Repositorio de prueba:** ziobermeo-code/brisca  
**Carpeta de trabajo:** `claude-design-lab-mi-espacio-creativo/`  
**Fecha:** mayo 2026  
**Estado:** borrador activo — no cerrado

---

## Índice

1. [Qué se probó en esta investigación](#1-qué-se-probó-en-esta-investigación)
2. [Qué demostró Claude Design](#2-qué-demostró-claude-design)
3. [Qué demostró Claude Code web](#3-qué-demostró-claude-code-web)
4. [Qué es el Modo Fiona Design](#4-qué-es-el-modo-fiona-design)
5. [Las cinco fases del flujo](#5-las-cinco-fases-del-flujo)
6. [Qué decide Fiona](#6-qué-decide-fiona)
7. [Qué revisa Keny](#7-qué-revisa-keny)
8. [Qué guarda Izaro](#8-qué-guarda-izaro)
9. [Qué decide Ziortza](#9-qué-decide-ziortza)
10. [Reglas de seguridad](#10-reglas-de-seguridad)
11. [Criterios para considerar una prueba superada](#11-criterios-para-considerar-una-prueba-superada)
12. [Límites detectados](#12-límites-detectados)
13. [Próximos experimentos posibles](#13-próximos-experimentos-posibles)
14. [Conclusión final](#14-conclusión-final)

---

## 1. Qué se probó en esta investigación

Se probó si una IA de código (Claude Code web) puede actuar como herramienta de **dirección visual** — no solo de programación — dentro de un flujo de trabajo de diseño real.

El experimento concreto fue:

- Reconstruir un prototipo de aplicación creativa llamado "Mi Espacio Creativo" como app local, sin dependencias externas, partiendo de una descripción y reglas de contención estrictas.
- Evaluar si la IA tomaba decisiones visuales coherentes, documentaba su razonamiento, proponía extensiones del sistema y señalaba sus propios límites.
- Verificar que la IA respetaba las restricciones de alcance: no modificar proyectos existentes, no conectar servicios externos, no asumir permisos no concedidos.

**Repositorio utilizado:** `brisca` (juego de cartas en Python) — usado exclusivamente como contenedor de prueba. La app brisca no fue tocada en ningún momento.

**Archivos creados durante la investigación:**

```
claude-design-lab-mi-espacio-creativo/
├── index.html              pantalla principal
├── styles.css              sistema visual completo
├── app.js                  lógica de la aplicación
├── README.md               documentación de uso y mocks
├── panel-proyecto.html     segunda pantalla (panel de detalle)
└── METODO_FIONA_DESIGN_DIRECCION_VISUAL_CON_IA_v0.1.md  ← este documento
```

---

## 2. Qué demostró Claude Design

**Claude Design** hace referencia al uso de Claude (cualquier interfaz) para generar y razonar sobre decisiones de diseño visual.

En esta investigación demostró:

### Capacidades confirmadas

**Coherencia estética mantenida a lo largo de la sesión.**  
Desde el primer archivo hasta la segunda pantalla, la paleta, tipografía, espaciado y tono visual se mantuvieron sin instrucción explícita de repetirlos. El sistema emergió del primer prototipo y se extendió al segundo de forma coherente.

**Razonamiento visual explicitado.**  
Cuando se le pidió explicar sus decisiones, la IA articuló por qué eligió crema en lugar de blanco, por qué serif para títulos y sans para cuerpo, por qué un solo color de acción. Este razonamiento es auditable y debatible — no es una caja negra.

**Extracción de sistema de diseño desde código.**  
A partir del CSS generado, la IA identificó los tokens, componentes, jerarquías y tono visual que conformaban un sistema, sin que se le pidiera explícitamente que construyera uno.

**Diferenciación de roles en el proceso.**  
La IA distinguió correctamente qué decisiones le corresponden a una directora creativa, cuáles a una persona técnica, y cuáles propone automáticamente. Esta separación es condición necesaria para que la herramienta sea útil en un equipo real.

**Señalización honesta de límites.**  
La IA identificó ambigüedades no resueltas (modelo de datos del panel, navegación entre pantallas, comportamiento en modo incógnito) sin intentar cerrarlas con soluciones improvisadas.

### Lo que no demostró (y no pretendió demostrar)

- No generó imágenes ni activos visuales.
- No evaluó el diseño en navegador real.
- No tomó decisiones sobre si el resultado era "bueno" para el usuario final — esa evaluación requiere ojos humanos.
- No propuso un sistema de diseño completo — solo los tokens y componentes que emergieron del prototipo.

---

## 3. Qué demostró Claude Code web

**Claude Code web** hace referencia al entorno de agente de código que ejecutó el trabajo técnico: creación de archivos, git, verificaciones de solo lectura, auditorías de código.

### Capacidades confirmadas

**Contención de alcance.**  
Ante instrucciones explícitas de no tocar la app brisca, la IA respetó ese límite en todo momento. Cuando `.gitignore` bloqueaba la nueva carpeta, resolvió el problema de la forma menos invasiva posible (añadir excepciones, no modificar reglas existentes) y lo reportó antes de actuar.

**Verificación de solo lectura real.**  
Cuando se le pidió una verificación final sin modificar nada, ejecutó únicamente comandos de lectura (`git log`, `grep`, `git show`, `ls`) y presentó los resultados directamente sin interpretarlos en exceso.

**Auditoría de seguridad básica por defecto.**  
Añadió `escapeHtml()` en todos los inputs del usuario, `try/catch` en localStorage, atributos ARIA y fallbacks de fuente sin que se le pidiera explícitamente.

**Transparencia en lo que no puede hacer.**  
Declaró explícitamente que no tiene acceso a navegador gráfico y describió qué verificaría en su lugar (lectura de código). No simuló haber "abierto el navegador".

**Commit descriptivo y trazable.**  
Cada commit incluye qué se creó, por qué, y qué no tocó. Los mensajes son auditables.

### Lo que no hizo sin permiso

- No creó pull request (se le pidió no hacerlo).
- No modificó archivos existentes salvo `.gitignore` para resolver un bloqueo técnico, reportando el cambio antes de hacerlo.
- No instaló paquetes, no ejecutó npm, no añadió dependencias externas.

---

## 4. Qué es el Modo Fiona Design

El **Modo Fiona Design** es un protocolo de trabajo que define cómo un equipo creativo colabora con una IA en tareas de dirección visual y prototipado de sistemas de diseño.

No es un plugin. No es una plantilla. Es un contrato de trabajo.

### Principios fundamentales

**1. La IA es la mesa de trabajo, no la diseñadora.**  
Las decisiones que vienen de conocer a la persona, el contexto y la intención son de la directora creativa. La IA ejecuta, documenta, propone alternativas y señala lo que falta.

**2. Prototipo primero, especificación después.**  
No se escribe un design brief para que la IA lo implemente en abstracto. Se genera un prototipo funcional, se evalúa con ojos reales, y solo entonces se extrae el sistema.

**3. Todo abre localmente.**  
Ningún prototipo en esta fase depende de red, cuenta, CDN ni instalación. La revisión ocurre en cualquier momento, en cualquier lugar, sin intermediarios.

**4. Los límites se declaran, no se ocultan.**  
La IA nombra lo que queda como mock, lo que necesita validación humana y lo que no conviene dar por cerrado. Un prototipo con límites documentados es más útil que uno que aparenta estar completo.

**5. El alcance es sagrado.**  
Ninguna acción toca proyectos, archivos o sistemas fuera del perímetro definido. Si hay duda, se reporta antes de actuar.

---

## 5. Las cinco fases del flujo

### FASE 1 — Intención

**Objetivo:** definir la emoción, metáfora visual y restricciones antes de escribir una línea de código.

**Quién lidera:** Fiona (directora creativa).

**Qué produce la IA:** preguntas de clarificación si el brief es ambiguo, propuesta de tono en una frase.

**Entregable:** brief de una página en texto plano que incluye:
- Persona de uso (quién y en qué contexto)
- Emoción objetivo (cómo debe sentirse la interfaz)
- Metáfora visual de referencia (cuaderno, tablero, archivo, etc.)
- Restricciones duras (qué no puede ocurrir)
- Restricciones blandas (preferencias que se pueden negociar)

**Señal de que la fase está completa:** la directora puede describir en una frase qué debe sentir alguien al abrir la app.

---

### FASE 2 — Prototipo rápido

**Objetivo:** tener algo que ver y tocar en el menor tiempo posible.

**Quién lidera:** IA (ejecuta), directora (aprueba la estructura antes del primer commit).

**Reglas de ejecución:**
- Una carpeta nueva y aislada con nombre explícito
- Sin CDN, sin npm, sin frameworks salvo decisión explícita
- Fuentes de sistema o fallbacks locales
- Datos ficticios que representen el uso real (no "Lorem ipsum")
- `index.html` abre con doble clic en el navegador

**Entregable:** carpeta con `index.html`, `styles.css`, `app.js`, `README.md`.

**Señal de que la fase está completa:** el archivo abre sin internet y sin error en consola.

---

### FASE 3 — Evaluación visual humana

**Objetivo:** validar con ojos reales lo que la IA generó.

**Quién lidera:** Keny (revisión técnica y funcional), Fiona (revisión visual y de tono).

**Qué hace la IA en esta fase:** espera. No propone cambios hasta recibir feedback explícito.

**Checklist mínimo de revisión:**
- [ ] La app abre sin internet y sin error
- [ ] El saludo dinámico funciona (mañana / tarde / noche)
- [ ] La captura rápida guarda y persiste al recargar
- [ ] Los datos ficticios son representativos del uso real
- [ ] La estética se corresponde con la intención descrita en Fase 1
- [ ] No aparece ningún nombre real ni dato sensible
- [ ] El comportamiento en ventana estrecha es aceptable
- [ ] No hay referencias a dependencias externas en el código fuente

**Entregable:** lista de ajustes con tres niveles de prioridad:
- **Debe:** bloquea el avance a Fase 4
- **Podría:** mejora deseable, no bloqueante
- **Algún día:** idea para versiones futuras

**Señal de que la fase está completa:** no quedan ítems "Debe" sin resolver.

---

### FASE 4 — Extracción del sistema

**Objetivo:** convertir el prototipo en un sistema de diseño mínimo documentado.

**Quién lidera:** IA (extrae y documenta), Fiona (valida qué es sistema y qué es solo esta pantalla).

**Qué documenta la IA:**
- Tokens: colores, tipografías, espaciado, radios, sombras, transiciones
- Componentes: nombre, variantes, estados, datos que necesita
- Jerarquías: niveles de información y su relación
- Comportamientos: interacciones que no están en CSS
- Límites: qué no está resuelto y por qué

**Entregable:** sección de sistema de diseño en el README o documento separado.

**Señal de que la fase está completa:** otra persona técnica puede implementar un componente nuevo usando solo los tokens documentados, sin mirar el código del prototipo.

---

### FASE 5 — Segunda pantalla y handoff

**Objetivo:** probar que el sistema se sostiene en una segunda pantalla y preparar la entrega para desarrollo.

**Quién lidera:** IA (crea la segunda pantalla), Fiona (elige qué pantalla y valida coherencia), Ziortza (aprueba el handoff).

**Opciones de segunda pantalla:**
- Estado vacío inicial
- Vista móvil
- Panel de proyecto (detalle)
- Panel de inspiración visual
- Slide deck ficticio
- Landing de sección

**Qué incluye el handoff para Claude Code:**
- Tokens CSS exportables (variables `--`)
- Inventario de componentes con variantes y estados
- Comportamientos que no están en CSS (lógica de JS)
- Decisiones de datos pendientes (qué necesita definirse antes de implementar)
- Lista de mocks que deben resolverse antes de producción

**Señal de que la fase está completa:** Keny puede abrir el handoff y saber exactamente qué implementar, qué preguntar y qué esperar.

---

## 6. Qué decide Fiona

Fiona es la **directora creativa**. Sus decisiones definen la identidad del proyecto y no pueden delegarse a la IA.

| Decisión | Descripción |
|---|---|
| Temperatura emocional | Cálida, fría, neutra, íntima, institucional |
| Paleta | No solo los colores, sino por qué esos colores para esta persona |
| Tipografía | La mezcla serif/sans y cuándo romperla |
| Metáfora de interfaz | Cuaderno, tablero, archivo, diario, etc. |
| Datos de ejemplo | Si las semillas representan bien el uso real |
| Tono del copy | El saludo, los placeholders, los mensajes de confirmación |
| Qué pantallas existen | Jerarquía de la navegación |
| Qué entra al sistema | Qué componentes son del sistema y cuáles son excepciones |
| Cuándo está lista una pantalla para mostrar | Criterio de calidad visual |

**Fiona no decide:**
- Cómo se guarda un dato
- Si `localStorage` es suficiente o se necesita otra solución
- Qué atributos de accesibilidad llevan los elementos

---

## 7. Qué revisa Keny

Keny es la **revisora de calidad funcional y técnica**. Su rol es asegurarse de que lo que se ve en el prototipo es lo que realmente ocurre — no lo que dice la IA que ocurre.

| Tarea de revisión | Cómo verificarla |
|---|---|
| La app abre offline | Desconectar red, recargar, verificar sin errores |
| La captura persiste | Guardar, recargar, confirmar que la tarjeta sigue ahí |
| El comportamiento en modo incógnito | Abrir en ventana privada, capturar, recargar |
| El saludo dinámico en distintas horas | Modificar `new Date().getHours()` en consola del navegador |
| Ningún nombre real en la interfaz | Grep + revisión visual |
| Sin dependencias externas en código funcional | Revisar `<head>` del HTML, verificar que no hay `fetch()` a URLs externas |
| El comportamiento en 320px–375px | DevTools → modo responsive → ancho mínimo |
| El comportamiento en iOS Safari | Si hay acceso a dispositivo real |
| Sin errores en consola del navegador | Abrir DevTools → Console → recargar |

**Keny no decide:**
- Si la paleta es correcta
- Si el tono visual es el adecuado
- Qué nuevas funcionalidades añadir

**Keny sí puede bloquear el avance** si detecta errores funcionales, datos reales en el prototipo o dependencias externas no declaradas.

---

## 8. Qué guarda Izaro

Izaro es la **archivista del proceso**. Su rol es asegurarse de que el conocimiento generado en cada sesión queda documentado, versionado y recuperable.

| Qué guarda | Dónde |
|---|---|
| El estado final de cada fase | Commits en la rama de trabajo |
| Las decisiones visuales justificadas | En el README o en documentos metodológicos como este |
| Los límites y mocks detectados | En la sección "Límites" del README |
| Las preguntas sin respuesta | Como issues o como sección en este documento |
| Los experimentos fallidos y por qué fallaron | En el historial de commits y en notas de sesión |
| La versión del método que se usó | En el nombre del documento (`v0.1`, `v0.2`, etc.) |
| Qué archivos se crearon y cuáles no se tocaron | En la confirmación final de cada sesión |

**Izaro no decide:**
- Si el prototipo es bueno
- Qué hacer a continuación

**Izaro sí puede señalar** cuando falta documentación, cuando un commit no tiene mensaje descriptivo o cuando un límite detectado no quedó registrado.

**Formato mínimo de archivo:**
- Nombre con versión: `NOMBRE_v0.1.md`
- Fecha en el encabezado
- Estado explícito: borrador / revisado / aprobado / archivado
- Nunca se borra — se versiona

---

## 9. Qué decide Ziortza

Ziortza es la **responsable de proyecto y decisiones estratégicas**. Su rol es definir qué avanza, qué se pausa y qué no entra en el alcance.

| Decisión | Descripción |
|---|---|
| Qué experimento se hace a continuación | De la lista de próximos experimentos posibles |
| Qué repo se usa como contenedor de prueba | Con la restricción de no tocar proyectos activos |
| Qué personas participan en cada fase | Asignación de roles |
| Si un prototipo está listo para salir del laboratorio | Criterio de graduación hacia producción |
| Qué parte del método se formaliza | Qué partes de este documento se convierten en proceso estable |
| Cuándo se cierra una fase | Con qué señal se da por terminada |
| Qué información no debe aparecer nunca en un prototipo | Política de datos y privacidad |

**Ziortza no decide:**
- Cómo se ve la interfaz
- Qué código se escribe

**Ziortza sí puede detener el proceso** si detecta que el experimento se está saliendo del perímetro definido o si los resultados no justifican continuar.

---

## 10. Reglas de seguridad

Estas reglas se aplican en todas las sesiones del Modo Fiona Design. Son no negociables salvo decisión explícita documentada de Ziortza.

### Sin CDN

No se carga ningún recurso desde un servidor externo.  
Ni fuentes, ni librerías, ni iconos, ni imágenes.  
**Razón:** los prototipos deben funcionar offline, en cualquier máquina, sin exposición a terceros.

### Sin npm

No se instalan dependencias.  
No hay `package.json`, `node_modules`, ni scripts de build.  
**Razón:** un prototipo que requiere instalación tiene una barrera de entrada innecesaria para revisión y validación.

### Sin frameworks salvo decisión explícita

No se usa React, Vue, Svelte, Next ni ningún framework de UI/JS sin que Ziortza lo apruebe explícitamente para una sesión concreta.  
**Razón:** los frameworks añaden complejidad de herramientas, versiones y compatibilidad que no aporta valor en fase de prototipo rápido.

### Sin datos reales

Ningún prototipo contiene nombres reales de personas identificables, correos, teléfonos, datos de clientes ni información de proyectos activos.  
Los datos de ejemplo son siempre ficticios y representativos.  
**Razón:** los prototipos circulan en repos, capturas de pantalla y presentaciones. Los datos reales en ese contexto son un riesgo.

### Sin APIs

No se conecta ninguna API externa — ni de IA, ni de almacenamiento, ni de autenticación.  
Si una funcionalidad requiere API, se implementa como mock documentado.  
**Razón:** una conexión a una API externa introduce dependencias de cuenta, coste, disponibilidad y privacidad que no corresponden a la fase de prototipo.

### Sin GitHub fuera del repo autorizado

La IA opera únicamente sobre el repositorio declarado al inicio de la sesión.  
No lee, no escribe ni interactúa con otros repos, organizaciones ni cuentas.  
**Razón:** los repos de otros proyectos pueden contener código sensible, configuración o datos que no deben ser accesibles durante un experimento de diseño.

### Sin tocar proyectos existentes

La carpeta de trabajo del Modo Fiona Design es siempre una carpeta nueva con nombre explícito.  
No se modifican archivos fuera de esa carpeta, salvo para resolver bloqueos técnicos mínimos (como `.gitignore`), y solo después de reportarlo.  
**Razón:** los repositorios de prueba pueden contener trabajo activo. Una modificación accidental puede tener coste real.

---

## 11. Criterios para considerar una prueba superada

Una sesión del Modo Fiona Design se considera **prueba superada** cuando se cumplen todos estos criterios:

### Criterios funcionales

- [ ] El prototipo abre con doble clic en `index.html` sin internet y sin error en consola
- [ ] Las funcionalidades declaradas (saludo, captura, hover, persistencia, secciones) funcionan como se describe en el README
- [ ] Los mocks están documentados explícitamente — nada finge ser funcional sin declararlo
- [ ] No hay datos reales en el prototipo

### Criterios de alcance

- [ ] No se modificaron archivos fuera de la carpeta designada (salvo excepciones mínimas reportadas)
- [ ] No se instalaron dependencias externas
- [ ] No se conectó ningún servicio externo
- [ ] El historial de commits es limpio y descriptivo

### Criterios de sistema

- [ ] Se pueden identificar los tokens de color, tipografía y espaciado sin leer el código
- [ ] Hay al menos dos pantallas que comparten el mismo sistema visual
- [ ] Los límites del sistema están documentados (qué falta, qué queda abierto)

### Criterios de proceso

- [ ] Cada rol (Fiona, Keny, Izaro, Ziortza) tiene tareas claras y diferenciadas
- [ ] El documento metodológico está versionado y tiene estado explícito
- [ ] El experimento generó al menos una pregunta nueva para el próximo experimento

---

## 12. Límites detectados

Estos son los límites identificados durante esta investigación. No son fracasos — son la especificación del siguiente experimento.

### Límites de la IA como herramienta visual

**No puede ver.**  
La IA no abre el navegador, no renderiza el HTML, no evalúa si algo "se ve bien". Toda evaluación visual requiere un humano con ojos en la pantalla.

**No conoce a la persona real.**  
Las semillas de datos son ficticias y representativas, pero no reflejan el flujo de trabajo real de una diseñadora concreta. La validación de si los datos de ejemplo son los correctos siempre requiere a Fiona.

**El sistema de diseño emergió, no fue planificado.**  
Los tokens del sistema son los que resultaron del primer prototipo. No se puede garantizar que sean los tokens correctos para un sistema más grande sin que una directora creativa los valide explícitamente.

**Sin memoria entre sesiones.**  
La IA no recuerda decisiones de sesiones anteriores. El método y las decisiones tomadas deben estar documentados en texto para que la siguiente sesión pueda retomar donde se dejó.

### Límites del prototipo actual

**Modelo de datos no cerrado.**  
El objeto `{id, section, title, body, tags[], date}` es suficiente para la pantalla principal. El panel de proyecto introduce notas, hitos y referencias que no tienen modelo de datos definido.

**Navegación entre pantallas no escalable.**  
La relación `index.html → panel-proyecto.html` funciona con un anchor plano. A partir de tres pantallas se necesita una estrategia de navegación.

**Captura rápida con dos patrones.**  
El campo de una línea en `index.html` y el textarea del sidebar de `panel-proyecto.html` son dos formas de capturar que no están unificadas conceptualmente.

**Sin modo oscuro.**  
La paleta cálida no tiene variante para `prefers-color-scheme: dark`. En sistemas con modo oscuro activo, el contraste puede ser inadecuado.

**localStorage sin límite de capacidad gestionado.**  
En uso intensivo, `localStorage` tiene un límite de ~5MB por dominio. No hay aviso ni fallback para cuando se alcanza ese límite.

---

## 13. Próximos experimentos posibles

Cada experimento propuesto es una sesión independiente que sigue el mismo flujo de cinco fases.

### Experimento A — Slide deck ficticio

**Pregunta:** ¿puede la IA generar un sistema de slides editoriales coherentes con la misma estética del Modo Fiona Design?

**Alcance:**
- Crear `slide-deck-ficticio/` con HTML + CSS
- Entre 5 y 8 slides sobre un tema inventado (no datos reales)
- Sin transiciones de JavaScript en un primer intento — solo estructura y visual
- Probar si el sistema de tipografía y paleta se sostiene en formato presentación

**Lo que aprenderíamos:** si el sistema de tokens es suficientemente flexible para adaptarse a un formato de composición completamente diferente.

---

### Experimento B — Design system ficticio

**Pregunta:** ¿puede la IA generar una documentación de sistema de diseño navegable (estilo Storybook, pero sin Storybook)?

**Alcance:**
- Crear `design-system-ficticio/` con HTML estático
- Una página por componente: Card, Capture Bar, Tag, Toast, Status Badge...
- Cada página muestra variantes, estados y tokens aplicados
- Sin build tools, sin npm

**Lo que aprenderíamos:** cuánto del sistema de diseño es explicitamente articulable sin una herramienta de documentación externa.

---

### Experimento C — Pieza de red social ficticia

**Pregunta:** ¿puede la IA adaptar el sistema visual a formato de post o historia para redes sociales?

**Alcance:**
- Crear `pieza-social-ficticia/` con HTML + CSS
- Una pieza en formato 1:1 (1080×1080px) con contenido ficticio
- Una pieza en formato 9:16 (story)
- Sin imágenes externas — solo tipografía, color y formas CSS

**Lo que aprenderíamos:** cómo se comporta el sistema cuando el contenedor es fijo y cuadrado en lugar de fluido y vertical.

---

### Experimento D — Landing ficticia

**Pregunta:** ¿puede la IA generar una landing page editorial completa con el sistema, incluyendo hero, secciones de contenido y llamada a la acción?

**Alcance:**
- Crear `landing-ficticia/` con HTML + CSS
- Hero con título grande + subtítulo + CTA
- Tres secciones de contenido (texto + visual)
- Footer
- Sin formularios funcionales — el CTA es mock documentado

**Lo que aprenderíamos:** si el sistema escala a la complejidad de una página de marketing, que tiene jerarquías visuales más agresivas que una app de captura personal.

---

## 14. Conclusión final

El Modo Fiona Design no es una respuesta a la pregunta "¿puede la IA diseñar?". Esa pregunta está mal planteada.

Es una respuesta a la pregunta: **¿cómo trabaja un equipo creativo cuando una de las personas de la mesa es una IA?**

Lo que esta investigación demostró es que esa colaboración es posible y productiva cuando:

1. **Los roles están claros antes de empezar.** La IA no toma decisiones de identidad visual. Las personas no tienen que escribir código.

2. **Las restricciones son explícitas y respetadas.** Sin CDN, sin datos reales, sin tocar proyectos activos. Las restricciones no son limitaciones del método — son su condición de posibilidad.

3. **Los límites se nombran, no se ocultan.** Un prototipo que sabe lo que no sabe es más útil que uno que aparenta estar completo.

4. **El proceso es más valioso que el artefacto.** El prototipo de "Mi Espacio Creativo" es un resultado. El método documentado aquí es el activo real: puede repetirse, adaptarse y mejorarse.

5. **La velocidad no es el objetivo — la revisabilidad sí.** El prototipo se puede auditar línea a línea, abrir sin internet, mostrar sin preparación. Eso vale más que la velocidad de generación.

### Lo que queda abierto en v0.1

- La validación visual con Fiona en un navegador real
- La decisión de si las cinco fases son suficientes o si falta una fase de "cierre de sistema"
- La definición del criterio de graduación: cuándo un prototipo del laboratorio está listo para convertirse en proyecto real
- El protocolo de archivo a largo plazo: dónde va este documento en seis meses

**v0.1 es un borrador activo. No está cerrado. Necesita revisión de Ziortza antes de convertirse en proceso estable.**

---

*Documento generado en sesión de investigación — mayo 2026*  
*Repositorio: ziobermeo-code/brisca — rama: claude/design-lab-creative-space-ZORlo*  
*Estado: borrador — pendiente de revisión*

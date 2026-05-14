# Mi Espacio Creativo — Prototipo local

Prototipo editorial de captura y organización de ideas creativas.
Reconstruido como app 100 % local y sin dependencias externas.

---

## Cómo abrir

1. Descarga o clona el repositorio.
2. Abre `claude-design-lab-mi-espacio-creativo/index.html` directamente en tu navegador.
   - No necesita servidor web.
   - No necesita instalación de paquetes.
   - No necesita conexión a internet.

---

## Archivos

| Archivo | Propósito |
|---|---|
| `index.html` | Estructura HTML semántica de la app |
| `styles.css` | Estética editorial cálida, fuentes de sistema |
| `app.js` | Lógica de saludo, renderizado, captura y almacenamiento |
| `README.md` | Este documento |

---

## Funcionalidades implementadas

### Saludo dinámico por hora
`app.js` lee `new Date().getHours()` al cargar:
- 05–11 → *Buenos días ☀️*
- 12–18 → *Buenas tardes 🌤️*
- 19–04 → *Buenas noches 🌙*

El saludo siempre va dirigido a **Usuario Demo** (el nombre "Fiona" del prototipo original ha sido eliminado).

### Cuatro secciones
- Ideas
- Inspiración visual
- Proyectos
- Aprendizajes de IA

### Captura rápida
El campo de texto permite seleccionar la sección destino y presionar **Guardar** (o `Enter`).
- Los datos se guardan en **`localStorage`** con la clave `mec_items`.
- Si el navegador no permite `localStorage` (modo privado en algunos casos), la tarjeta aparece en pantalla durante la sesión pero **no persiste** al recargar. Esta situación se informa internamente sin errores visibles.
- No hay backend, ni base de datos, ni autenticación.

### Tarjetas con hover
Cada tarjeta eleva su sombra y sube 3px al hacer hover. El borde cambia al color de acento cálido.

### Bloque de recientes
Muestra las 5 entradas más recientes ordenadas por fecha, combinando semillas y capturas del usuario.

### Semillas (datos ficticios)
Ocho tarjetas de ejemplo distribuidas en las cuatro secciones:
- **Ideas**: "Sistema de colores estacionales", "Tipografías que respiran"
- **Inspiración**: "Hokusai reinterpretadas", "Catálogos de los 70s europeos"
- **Proyectos**: "Rediseño identidad Café Luna", "Libro de artista: Memorias del mar"
- **Aprendizajes de IA**: "Prompts para texturas", "Variaciones de layout con IA"

Las semillas no se guardan en `localStorage`; se inyectan en cada carga. Así el estado inicial siempre se ve poblado incluso en un navegador sin historial.

---

## Lo que queda como mock

| Elemento | Estado | Notas |
|---|---|---|
| Editar tarjeta | Mock | Las tarjetas son de solo lectura. No hay formulario de edición. |
| Borrar tarjeta | Mock | No hay botón de eliminar. Para limpiar: `localStorage.removeItem('mec_items')` en consola. |
| Imágenes / media | Mock | Las tarjetas de Inspiración no cargan imágenes reales. |
| Búsqueda / filtro | Mock | No implementado en esta versión. |
| Tags clickables | Mock | Los tags se muestran pero no filtran. |
| Persistencia cloud | Mock | Solo `localStorage` local. |
| Tweaks panel | No incluido | Eliminado según especificación. |

---

## Dependencias externas eliminadas

Con respecto al prototipo React/JSX original:

| Dependencia | Estado |
|---|---|
| React / ReactDOM | Eliminado |
| Babel (JSX transform) | Eliminado |
| unpkg / esm.sh / jsDelivr | Eliminado |
| Google Fonts | Eliminado → fuentes de sistema |
| lucide-react | Eliminado → emoji inline |
| Tailwind (CDN) | Eliminado → CSS propio |
| tweaks-panel.jsx | Eliminado según especificación |

---

## Qué debería revisar Keny

1. **Persistencia**: Abrir `index.html`, capturar algo, recargar la página y verificar que la tarjeta sigue ahí. Probar también en modo incógnito para ver el comportamiento sin localStorage.
2. **Saludo horario**: Cargar a distintas horas o modificar temporalmente `getHours()` en consola para verificar los tres estados.
3. **Responsive**: Revisar en móvil (< 640px). La captura rápida se apila verticalmente; las tarjetas se ajustan a una columna.
4. **Sin red**: Desconectar internet y recargar para confirmar que todo funciona offline.
5. **Semillas vs. usuario**: Las semillas aparecen siempre; las capturas nuevas se suman. Revisar que la sección "Actividad reciente" mezcla ambas correctamente por fecha.
6. **Accesibilidad básica**: Las secciones usan `aria-labelledby`; el toast usa `aria-live="polite"`. Revisar con lector de pantalla si es necesario.
7. **Nombres**: Confirmar que "Fiona" no aparece en ninguna parte de la interfaz (reemplazado por "Usuario Demo").

---

## Repositorio de prueba

Este prototipo vive en `claude-design-lab-mi-espacio-creativo/` dentro del repositorio `brisca`.
No modifica ni depende de ningún archivo de la aplicación brisca existente.

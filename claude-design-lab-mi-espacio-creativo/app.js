/* ===== Mi Espacio Creativo — app.js ===== */
/* Vanilla JS, sin dependencias externas. */
/* localStorage se usa para captura rápida; ver README para detalles. */

(function () {
  'use strict';

  // ─── Constantes ───────────────────────────────────────────────
  const STORAGE_KEY = 'mec_items';

  const SECTIONS = [
    { id: 'ideas',        label: 'Ideas',               icon: '💡' },
    { id: 'inspiracion',  label: 'Inspiración visual',  icon: '🎨' },
    { id: 'proyectos',    label: 'Proyectos',            icon: '📁' },
    { id: 'aprendizajes', label: 'Aprendizajes de IA',  icon: '🤖' },
  ];

  // ─── Datos ficticios iniciales (semillas) ─────────────────────
  const SEEDS = [
    {
      id: 'seed-1',
      section: 'ideas',
      title: 'Sistema de colores estacionales',
      body: 'Explorar paletas que cambien con las estaciones del año para proyectos de branding.',
      tags: ['color', 'branding', 'estacional'],
      date: '2026-04-10',
      seed: true,
    },
    {
      id: 'seed-2',
      section: 'ideas',
      title: 'Tipografías que respiran',
      body: 'Animaciones sutiles de interlineado para páginas editoriales largas.',
      tags: ['tipografía', 'animación'],
      date: '2026-04-22',
      seed: true,
    },
    {
      id: 'seed-3',
      section: 'inspiracion',
      title: 'Ilustraciones de Hokusai reinterpretadas',
      body: 'Fusionar líneas ukiyo-e con vectores geométricos modernos.',
      tags: ['ilustración', 'japonés', 'geometría'],
      date: '2026-03-15',
      seed: true,
    },
    {
      id: 'seed-4',
      section: 'inspiracion',
      title: 'Catálogos de los 70s europeos',
      body: 'La calidez del papel offset y los colores ocre en composición tipográfica.',
      tags: ['retro', 'editorial', 'papel'],
      date: '2026-04-05',
      seed: true,
    },
    {
      id: 'seed-5',
      section: 'proyectos',
      title: 'Rediseño identidad Café Luna',
      body: 'Logo, paleta y sistema de señalética para cafetería boutique. Estado: en proceso.',
      tags: ['identidad', 'café', 'señalética'],
      date: '2026-05-01',
      seed: true,
    },
    {
      id: 'seed-6',
      section: 'proyectos',
      title: 'Libro de artista: Memorias del mar',
      body: 'Edición artesanal de 40 páginas. Impresión risografía en dos tintas.',
      tags: ['libro', 'risografía', 'arte'],
      date: '2026-04-28',
      seed: true,
    },
    {
      id: 'seed-7',
      section: 'aprendizajes',
      title: 'Prompts para generación de texturas',
      body: 'Aprendizaje: ser específico en la descripción del material (lino, yeso, madera) mejora mucho los resultados.',
      tags: ['prompts', 'texturas', 'IA generativa'],
      date: '2026-05-10',
      seed: true,
    },
    {
      id: 'seed-8',
      section: 'aprendizajes',
      title: 'Usar IA para variaciones de layout',
      body: 'Generar 5 variaciones de composición y luego editar la mejor es más rápido que partir de cero.',
      tags: ['layout', 'workflow', 'eficiencia'],
      date: '2026-05-12',
      seed: true,
    },
  ];

  // ─── Helpers ──────────────────────────────────────────────────

  function formatDate(iso) {
    const d = new Date(iso + 'T00:00:00');
    return d.toLocaleDateString('es-ES', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  function generateId() {
    return 'item-' + Date.now() + '-' + Math.random().toString(36).slice(2, 7);
  }

  function getGreeting() {
    const h = new Date().getHours();
    if (h >= 5  && h < 12) return { saludo: 'Buenos días', emoji: '☀️' };
    if (h >= 12 && h < 19) return { saludo: 'Buenas tardes', emoji: '🌤️' };
    return { saludo: 'Buenas noches', emoji: '🌙' };
  }

  // ─── Storage ──────────────────────────────────────────────────

  function loadItems() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (_) {
      return [];
    }
  }

  function saveItems(items) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    } catch (_) {
      /* localStorage no disponible: la captura funciona solo en memoria */
    }
  }

  // ─── Renderizado ──────────────────────────────────────────────

  function renderCard(item) {
    const card = document.createElement('article');
    card.className = 'card' + (item.seed ? ' card--seed' : '') + (!item.seed && isNew(item) ? ' card--new' : '');
    card.setAttribute('tabindex', '0');
    card.setAttribute('aria-label', item.title);

    const tagsHtml = (item.tags || [])
      .map(t => `<span class="tag">${escapeHtml(t)}</span>`)
      .join('');

    card.innerHTML = `
      <span class="card__label">${escapeHtml(sectionLabel(item.section))}</span>
      <h3 class="card__title">${escapeHtml(item.title)}</h3>
      ${item.body ? `<p class="card__body">${escapeHtml(item.body)}</p>` : ''}
      ${tagsHtml ? `<div class="card__tags">${tagsHtml}</div>` : ''}
      <span class="card__date">${formatDate(item.date)}</span>
    `;

    return card;
  }

  function isNew(item) {
    const created = new Date(item.date).getTime();
    return (Date.now() - created) < 24 * 60 * 60 * 1000;
  }

  function sectionLabel(id) {
    const s = SECTIONS.find(s => s.id === id);
    return s ? s.label : id;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderSection(container, sectionId, allItems) {
    const items = allItems.filter(i => i.section === sectionId);
    container.innerHTML = '';
    if (items.length === 0) {
      const empty = document.createElement('p');
      empty.className = 'empty-state';
      empty.textContent = 'Aún no hay entradas aquí. ¡Captura la primera!';
      container.appendChild(empty);
    } else {
      items.forEach(item => container.appendChild(renderCard(item)));
    }
  }

  function renderRecientes(container, allItems) {
    const sorted = [...allItems]
      .sort((a, b) => new Date(b.date) - new Date(a.date))
      .slice(0, 5);

    container.innerHTML = '';
    sorted.forEach(item => {
      const row = document.createElement('div');
      row.className = 'reciente-item';
      row.innerHTML = `
        <span class="reciente-item__section">${escapeHtml(sectionLabel(item.section))}</span>
        <span class="reciente-item__text">${escapeHtml(item.title)}</span>
        <span class="reciente-item__date">${formatDate(item.date)}</span>
      `;
      container.appendChild(row);
    });
  }

  // ─── Toast ────────────────────────────────────────────────────

  function showToast(msg) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('visible');
    setTimeout(() => toast.classList.remove('visible'), 2800);
  }

  // ─── Greeting ─────────────────────────────────────────────────

  function renderGreeting() {
    const el = document.getElementById('greeting-text');
    if (!el) return;
    const { saludo, emoji } = getGreeting();
    el.innerHTML = `${emoji} ${saludo}, <em>Usuario Demo</em>`;
  }

  // ─── App init ─────────────────────────────────────────────────

  function getAll() {
    const stored = loadItems();
    // Combinar semillas + items del usuario; evitar duplicados por id
    const storedIds = new Set(stored.map(i => i.id));
    const seeds = SEEDS.filter(s => !storedIds.has(s.id));
    return [...seeds, ...stored];
  }

  function init() {
    renderGreeting();

    let items = getAll();

    // Grids por sección
    SECTIONS.forEach(sec => {
      const grid = document.getElementById('grid-' + sec.id);
      if (grid) renderSection(grid, sec.id, items);
    });

    // Recientes
    const recList = document.getElementById('recientes-list');
    if (recList) renderRecientes(recList, items);

    // Captura rápida
    const form    = document.getElementById('capture-form');
    const input   = document.getElementById('capture-input');
    const selSec  = document.getElementById('capture-section');
    const btn     = document.getElementById('capture-btn');

    function doCapture() {
      const text = input ? input.value.trim() : '';
      const section = selSec ? selSec.value : 'ideas';
      if (!text) {
        showToast('Escribe algo antes de guardar.');
        return;
      }

      const stored = loadItems();
      const newItem = {
        id: generateId(),
        section,
        title: text,
        body: '',
        tags: [],
        date: new Date().toISOString().slice(0, 10),
        seed: false,
      };
      stored.push(newItem);
      saveItems(stored);

      items = getAll();

      // Re-renderizar sección correspondiente
      const grid = document.getElementById('grid-' + section);
      if (grid) renderSection(grid, section, items);

      const recListEl = document.getElementById('recientes-list');
      if (recListEl) renderRecientes(recListEl, items);

      input.value = '';
      showToast('Guardado en "' + sectionLabel(section) + '" ✓');
    }

    if (btn) btn.addEventListener('click', doCapture);
    if (input) {
      input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') doCapture();
      });
    }

    if (form) form.addEventListener('submit', function (e) { e.preventDefault(); doCapture(); });
  }

  // Arrancar cuando el DOM esté listo
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

import re

file_path = 'c:\\Users\\fmrlo\\Desktop\\economatom\\smart-economato\\MIOS\\requisitos-presentacion-lorena.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Quito los bloques de capturas antiguos que ya no sirven
html = re.sub(r'\s*<!-- ====== CAPTURAS ====== -->.*?</div>\s*</div>\s*</div>', '\n            </div>\n        </div>', html, flags=re.DOTALL)

inline_css = '''
        /* ================================================ EVIDENCIAS ================================================ */
        .evidence-placeholder {
            margin-top: 1rem;
            padding: .8rem;
            background: rgba(255,255,255,0.5);
            border: 1px dashed var(--border);
            border-radius: var(--radius-sm);
            text-align: center;
            color: var(--text-muted);
            font-size: .75rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--ease);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        [data-theme="dark"] .evidence-placeholder { background: rgba(0,0,0,0.2); }
        .evidence-placeholder:hover {
            border-color: var(--primary);
            color: var(--primary);
            background: var(--primary-light);
        }
        .evidence-img {
            margin-top: 1rem;
            width: 100%;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
            box-shadow: var(--shadow-sm);
        }
'''

if '/* ================================================ EVIDENCIAS ================================================ */' not in html:
    html = html.replace('/* ===================== DRAWER (fuera del nav) ===================== */', inline_css + '\n        /* ===================== DRAWER (fuera del nav) ===================== */')

# Inyecto los huecos para las fotos en cada caja del informe
# Busco cada caja de item y meto el placeholder antes de cerrar el div
# Lo hago con un replace sencillo para no liarme con los divs anidados

html = re.sub(
    r'(<div class="item-box">.*?)(</div>)', 
    r'\1    <div class="evidence-placeholder"><span>??</span> Reemplaza este div por tu etiqueta &lt;img&gt; con la captura de esta funcionalidad</div>\n                \2', 
    html, 
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Exito')

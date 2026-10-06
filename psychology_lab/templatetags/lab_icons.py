"""Small, local outline icons for the public site."""

from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe


register = template.Library()

ICONS = {
    'house': '<path d="m3 10 9-7 9 7v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M9 21v-8h6v8"/>',
    'flask-conical': '<path d="M10 2v7.3L4.3 19a2 2 0 0 0 1.7 3h12a2 2 0 0 0 1.7-3L14 9.3V2"/><path d="M8 2h8M7 16h10"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    'book-open': '<path d="M12 7v14M3 18V5a2 2 0 0 1 2-2h3a4 4 0 0 1 4 4 4 4 0 0 1 4-4h3a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2h-3a4 4 0 0 0-4 4 4 4 0 0 0-4-4H5a2 2 0 0 0-2 2Z"/>',
    'newspaper': '<path d="M4 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a4 4 0 0 1-4-4V5a2 2 0 0 1 2-2Z"/><path d="M2 17a2 2 0 0 0 2 2h2M7 7h8M7 11h8M7 15h5"/>',
    'award': '<circle cx="12" cy="8" r="6"/><path d="m8.2 13-1.2 8 5-3 5 3-1.2-8"/>',
    'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7 10-7"/>',
    'file-text': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h8"/>',
    'chevron-down': '<path d="m6 9 6 6 6-6"/>',
    'chevron-right': '<path d="m9 18 6-6-6-6"/>',
    'arrow-right': '<path d="M5 12h14m-7-7 7 7-7 7"/>',
    'arrow-left': '<path d="M19 12H5m7 7-7-7 7-7"/>',
    'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>',
    'x': '<path d="M18 6 6 18M6 6l12 12"/>',
    'microscope': '<path d="m6 18 3 3h9a3 3 0 0 0 0-6h-1M4 22h16M9 15l3-3M5 9l6-6 4 4-6 6zM15 7l2 2"/>',
    'brain': '<path d="M12 18V5a3 3 0 0 0-5.8-1 4 4 0 0 0-2.1 6.3A4 4 0 0 0 5 17a4 4 0 0 0 7 1Zm0 0V5a3 3 0 0 1 5.8-1 4 4 0 0 1 2.1 6.3A4 4 0 0 1 19 17a4 4 0 0 1-7 1Z"/><path d="M5 11c2 0 3 1 3 3m11-3c-2 0-3 1-3 3"/>',
    'eye': '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
    'heart': '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0l-1 1-1-1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/>',
    'chart': '<path d="M3 3v18h18M7 16l4-4 3 2 5-7"/>',
    'lab': '<path d="M9 3v6l-5 9a2 2 0 0 0 1.7 3h12.6A2 2 0 0 0 20 18l-5-9V3M8 3h8M7 16h10"/>',
    'signal': '<path d="M2 20h.01M7 20v-4M12 20v-8M17 20V8M22 20V4"/>',
    'neuron': '<path d="M12 3v5M12 16v5M3 12h5M16 12h5M5.6 5.6l3.5 3.5m5.8 5.8 3.5 3.5m0-12.8-3.5 3.5m-5.8 5.8-3.5 3.5"/><circle cx="12" cy="12" r="4"/>',
    'data': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4M7 9h2m-2 4h5"/>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4m10-4v4M3 10h18"/>',
    'map-pin': '<path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2A19 19 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.5 3a2 2 0 0 1-.6 1.7L7.3 10a16 16 0 0 0 6.7 6.7l1.6-1.7a2 2 0 0 1 1.7-.6l3 .5a2 2 0 0 1 1.7 2Z"/>',
}


@register.simple_tag
def lab_icon(name, size=20, class_name=''):
    """Render an allowlisted inline outline icon."""
    path = ICONS.get(name, ICONS['file-text'])
    try:
        size = max(12, min(int(size), 64))
    except (TypeError, ValueError):
        size = 20
    return format_html(
        '<svg class="lab-icon {}" width="{}" height="{}" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>',
        class_name, size, size, mark_safe(path),
    )

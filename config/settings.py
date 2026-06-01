"""
Django settings — Psychophysiology Lab
"""
from pathlib import Path
import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']

# ── Applications ──────────────────────────────────────────────
INSTALLED_APPS = [
    # Jazzmin — must be before django.contrib.admin
    'jazzmin',
    # modeltranslation — must be before django.contrib.admin
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'ckeditor',
    'ckeditor_uploader',

    # Local
    'psychology_lab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'psychology_lab.middleware.ForceDefaultLanguageMiddleware',         # ← Custom default language middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalization ──────────────────────────────────────
LANGUAGE_CODE = 'uz'
LANGUAGES = [
    ('uz', _("O'zbek")),
    ('ru', _('Русский')),
    ('en', _('English')),
]

LOCALE_PATHS = [BASE_DIR / 'locale']

TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ── Modeltranslation ─────────────────────────────────────────
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz', 'ru', 'en')

# ── Static & Media ───────────────────────────────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── CKEditor ─────────────────────────────────────────────────
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks'],
            ['Source'],
        ],
        'height': 350,
        'width': '100%',
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    },
}

# ── Jazzmin Settings ─────────────────────────────────────────
JAZZMIN_SETTINGS = {
    # Window title
    "site_title": "Psixofiziologiya Lab",
    "site_header": "Psixofiziologiya Lab",
    "site_brand": "🧠 PsixoLab",
    "welcome_sign": "Bosh sahifaga xush kelibsiz",
    "copyright": "Psixofiziologiya Laboratoriyasi",

    # Top menu
    "topmenu_links": [
        {"name": "Saytni Ko'rish", "url": "/", "new_window": True},
        {"model": "auth.user"},
    ],

    # User menu
    "usermenu_links": [
        {"name": "Saytni Ko'rish", "url": "/", "new_window": True},
    ],

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Sidebar menu order
    "order_with_respect_to": [
        "psychology_lab",
        "psychology_lab.SiteSettings",
        "psychology_lab.HeroSection",
        "psychology_lab.Page",
        "psychology_lab.ResearchArea",
        "psychology_lab.TeamMember",
        "psychology_lab.Publication",
        "psychology_lab.NewsEvent",
        "psychology_lab.GalleryImage",
        "psychology_lab.StatCounter",
        "psychology_lab.ContactMessage",
        "auth",
    ],

    # Icons (FontAwesome 5)
    "icons": {
        "auth":                         "fas fa-users-cog",
        "auth.user":                    "fas fa-user",
        "auth.Group":                   "fas fa-users",
        "psychology_lab.SiteSettings":  "fas fa-cog",
        "psychology_lab.HeroSection":   "fas fa-home",
        "psychology_lab.Page":          "fas fa-file-alt",
        "psychology_lab.ResearchArea":  "fas fa-microscope",
        "psychology_lab.TeamMember":    "fas fa-user-graduate",
        "psychology_lab.Publication":   "fas fa-book",
        "psychology_lab.NewsEvent":     "fas fa-newspaper",
        "psychology_lab.GalleryImage":  "fas fa-images",
        "psychology_lab.StatCounter":   "fas fa-chart-bar",
        "psychology_lab.ContactMessage":"fas fa-envelope",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Related modal
    "related_modal_active": True,

    # UI tweaks
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-purple",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-purple",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

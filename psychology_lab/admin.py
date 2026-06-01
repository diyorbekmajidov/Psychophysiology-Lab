from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import (
    SiteSettings, HeroSection, Page, ResearchArea,
    TeamMember, Publication, NewsEvent, GalleryImage,
    ContactMessage, StatCounter
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    fieldsets = (
        (_("Umumiy ma'lumot"), {
            'fields': ('site_name', 'tagline', 'logo', 'footer_text')
        }),
        (_("Aloqa ma'lumotlari"), {
            'fields': ('email', 'phone', 'address')
        }),
        (_("Ijtimoiy tarmoqlar"), {
            'fields': ('facebook', 'twitter', 'linkedin', 'researchgate'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSection)
class HeroSectionAdmin(TranslationAdmin):
    list_display  = ('title', 'is_active')
    list_editable = ('is_active',)
    fieldsets = (
        (_("Kontent"), {
            'fields': ('title', 'subtitle', 'background_image')
        }),
        (_("Tugma"), {
            'fields': ('cta_text', 'cta_link', 'is_active')
        }),
    )


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    list_display   = ('title', 'slug', 'is_published', 'show_in_menu', 'menu_order', 'updated_at')
    list_editable  = ('is_published', 'show_in_menu', 'menu_order')
    list_filter    = ('is_published', 'show_in_menu')
    search_fields  = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (_("Sahifa ma'lumotlari"), {
            'fields': ('title', 'slug', 'banner_image', 'meta_description')
        }),
        (_("Kontent"), {
            'fields': ('content',)
        }),
        (_("Menyu sozlamalari"), {
            'fields': ('is_published', 'show_in_menu', 'menu_order')
        }),
    )


@admin.register(ResearchArea)
class ResearchAreaAdmin(TranslationAdmin):
    list_display  = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter   = ('is_active',)
    search_fields = ('title',)
    fieldsets = (
        (_("Asosiy ma'lumot"), {
            'fields': ('title', 'description', 'icon', 'image')
        }),
        (_("Sozlamalar"), {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display        = ('photo_preview', 'name', 'role', 'email', 'order', 'is_active')
    list_editable       = ('order', 'is_active')
    list_filter         = ('role', 'is_active')
    search_fields       = ('name', 'bio')
    list_display_links  = ('photo_preview', 'name')
    fieldsets = (
        (_("Shaxsiy ma'lumot"), {
            'fields': ('name', 'role', 'photo', 'bio')
        }),
        (_("Aloqa va havolalar"), {
            'fields': ('email', 'google_scholar', 'researchgate', 'linkedin', 'personal_website'),
            'classes': ('collapse',),
        }),
        (_("Ko'rsatish"), {
            'fields': ('order', 'is_active')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="48" height="48" '
                'style="border-radius:50%;object-fit:cover;border:2px solid #6C63FF;" />',
                obj.photo.url
            )
        return format_html('<div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#6C63FF,#00D4FF);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">{}</div>', obj.name[0] if obj.name else '?')
    photo_preview.short_description = _("Rasm")


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display  = ('title', 'authors', 'journal', 'year', 'is_featured')
    list_editable = ('is_featured',)
    list_filter   = ('year', 'is_featured')
    search_fields = ('title', 'authors', 'journal')
    ordering      = ['-year']
    fieldsets = (
        (_("Maqola ma'lumotlari"), {
            'fields': ('title', 'authors', 'journal', 'year', 'volume', 'pages')
        }),
        (_("Annotatsiya"), {
            'fields': ('abstract',),
            'classes': ('collapse',),
        }),
        (_("Fayllar va havolalar"), {
            'fields': ('doi_link', 'pdf_file')
        }),
        (_("Sozlamalar"), {
            'fields': ('is_featured',)
        }),
    )


@admin.register(NewsEvent)
class NewsEventAdmin(TranslationAdmin):
    list_display  = ('title', 'news_type', 'date', 'is_published', 'is_featured')
    list_editable = ('is_published', 'is_featured')
    list_filter   = ('news_type', 'is_published', 'is_featured')
    search_fields = ('title', 'content')
    date_hierarchy = 'date'
    fieldsets = (
        (_("Asosiy ma'lumot"), {
            'fields': ('title', 'news_type', 'date', 'image')
        }),
        (_("Kontent"), {
            'fields': ('content',)
        }),
        (_("Sozlamalar"), {
            'fields': ('is_published', 'is_featured')
        }),
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('image_preview', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('image_preview', 'title')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="56" '
                'style="object-fit:cover;border-radius:6px;border:1px solid #333;" />',
                obj.image.url
            )
        return '—'
    image_preview.short_description = _("Ko'rinish")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display     = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_editable    = ('is_read',)
    list_filter      = ('is_read',)
    search_fields    = ('name', 'email', 'subject')
    readonly_fields  = ('name', 'email', 'subject', 'message', 'created_at')
    date_hierarchy   = 'created_at'

    def has_add_permission(self, request):
        return False


@admin.register(StatCounter)
class StatCounterAdmin(TranslationAdmin):
    list_display  = ('label', 'value', 'icon', 'order')
    list_editable = ('value', 'order')


# ── Admin site branding ──────────────────────────────────────
admin.site.site_header  = "🧠 Psixofiziologiya Laboratoriyasi"
admin.site.site_title   = "Lab Admin"
admin.site.index_title  = "Boshqaruv Paneli"

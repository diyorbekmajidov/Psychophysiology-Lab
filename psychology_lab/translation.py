from modeltranslation.translator import register, TranslationOptions
from .models import (
    SiteSettings, HeroSection, Page, ResearchArea,
    TeamMember, Publication, NewsEvent, StatCounter, Achievement
)


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'tagline', 'footer_text', 'address')


@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'cta_text')


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'meta_description')


@register(ResearchArea)
class ResearchAreaTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'authors', 'journal', 'abstract')


@register(NewsEvent)
class NewsEventTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(StatCounter)
class StatCounterTranslationOptions(TranslationOptions):
    fields = ('label',)


@register(Achievement)
class AchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

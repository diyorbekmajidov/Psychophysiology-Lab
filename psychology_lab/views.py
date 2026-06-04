from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from .models import (
    SiteSettings, HeroSection, Page, ResearchArea,
    TeamMember, Publication, NewsEvent, GalleryImage, StatCounter, Achievement
)
from .forms import ContactForm


def get_site_context(request):
    """Return common context used across all pages."""
    try:
        settings_obj = SiteSettings.objects.first()
    except Exception:
        settings_obj = None
    menu_pages = Page.objects.filter(is_published=True, show_in_menu=True).order_by('menu_order')
    return {
        'site_settings': settings_obj,
        'menu_pages': menu_pages,
        'LANGUAGE_CODE': request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'uz',
    }


def home(request):
    context = get_site_context(request)
    context['hero']                  = HeroSection.objects.filter(is_active=True).first()
    context['research_areas']        = ResearchArea.objects.filter(is_active=True)[:6]
    context['team_members']          = TeamMember.objects.filter(is_active=True)[:6]
    context['featured_publications'] = Publication.objects.filter(is_featured=True)[:4]
    context['latest_news']           = NewsEvent.objects.filter(is_published=True)[:3]
    context['stats']                 = StatCounter.objects.all()[:6]
    context['gallery']               = GalleryImage.objects.filter(is_active=True)[:6]
    return render(request, 'psychology_lab/home.html', context)


def research(request):
    context = get_site_context(request)
    context['research_areas'] = ResearchArea.objects.filter(is_active=True)
    context['page_title'] = _('Tadqiqotlar')
    return render(request, 'psychology_lab/research.html', context)


def research_detail(request, pk):
    context = get_site_context(request)
    context['area'] = get_object_or_404(ResearchArea, pk=pk, is_active=True)
    context['other_areas'] = ResearchArea.objects.filter(is_active=True).exclude(pk=pk)[:5]
    return render(request, 'psychology_lab/research_detail.html', context)


def team(request):
    context = get_site_context(request)
    all_members = TeamMember.objects.filter(is_active=True)
    context['pi']               = all_members.filter(role='pi')
    context['postdocs']         = all_members.filter(role='postdoc')
    context['phd_students']     = all_members.filter(role='phd')
    context['masters_students'] = all_members.filter(role='masters')
    context['undergrads']       = all_members.filter(role='undergrad')
    context['staff']            = all_members.filter(role='staff')
    context['alumni']           = all_members.filter(role='alumni')
    context['page_title'] = _('Jamoa')
    return render(request, 'psychology_lab/team.html', context)


def publications(request):
    context = get_site_context(request)
    pub_list    = Publication.objects.all()
    year_filter = request.GET.get('year')
    if year_filter:
        pub_list = pub_list.filter(year=year_filter)
    paginator   = Paginator(pub_list, 10)
    page_number = request.GET.get('page')
    context['publications']   = paginator.get_page(page_number)
    context['years']          = Publication.objects.values_list('year', flat=True).distinct().order_by('-year')
    context['selected_year']  = year_filter
    context['page_title'] = _('Ilmiy Maqolalar')
    return render(request, 'psychology_lab/publications.html', context)


def news(request):
    context = get_site_context(request)
    news_list   = NewsEvent.objects.filter(is_published=True)
    type_filter = request.GET.get('type')
    if type_filter:
        news_list = news_list.filter(news_type=type_filter)
    paginator   = Paginator(news_list, 9)
    page_number = request.GET.get('page')
    context['news_list']     = paginator.get_page(page_number)
    context['selected_type'] = type_filter
    context['page_title'] = _('Yangiliklar va Tadbirlar')
    return render(request, 'psychology_lab/news.html', context)


def news_detail(request, pk):
    context = get_site_context(request)
    context['item']    = get_object_or_404(NewsEvent, pk=pk, is_published=True)
    context['related'] = NewsEvent.objects.filter(is_published=True).exclude(pk=pk)[:3]
    return render(request, 'psychology_lab/news_detail.html', context)


def contact(request):
    context = get_site_context(request)
    context['page_title'] = _("Bog'lanish")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Xabaringiz muvaffaqiyatli yuborildi! Tez orada javob beramiz."))
            return redirect('contact')
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'psychology_lab/contact.html', context)


def achievements(request):
    context = get_site_context(request)
    all_achievements = Achievement.objects.all()
    cat_filter = request.GET.get('category')
    if cat_filter:
        all_achievements = all_achievements.filter(category=cat_filter)
    context['achievements']      = all_achievements
    context['featured']          = Achievement.objects.filter(is_featured=True)[:3]
    context['selected_category'] = cat_filter
    context['categories']        = Achievement.CATEGORY_CHOICES
    context['page_title'] = _('Yutuqlar va Mukofotlar')
    return render(request, 'psychology_lab/achievements.html', context)


def page_detail(request, slug):
    context = get_site_context(request)
    page = get_object_or_404(Page, slug=slug, is_published=True)
    context['page_obj']   = page
    context['page_title'] = page.title
    return render(request, 'psychology_lab/page_detail.html', context)

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class SiteSettings(models.Model):
    site_name    = models.CharField(_("Sayt nomi"), max_length=200, default="Psychophysiology Lab")
    tagline      = models.CharField(_("Qisqa tavsif"), max_length=300, blank=True)
    logo         = models.ImageField(_("Logo"), upload_to='site/', blank=True, null=True)
    email        = models.EmailField(_("Email"), blank=True)
    phone        = models.CharField(_("Telefon"), max_length=50, blank=True)
    address      = models.TextField(_("Manzil"), blank=True)
    facebook     = models.URLField(_("Facebook"), blank=True)
    twitter      = models.URLField(_("Twitter / X"), blank=True)
    linkedin     = models.URLField(_("LinkedIn"), blank=True)
    researchgate = models.URLField(_("ResearchGate"), blank=True)
    footer_text  = models.TextField(_("Footer matni"), blank=True)

    class Meta:
        verbose_name        = _("Sayt Sozlamalari")
        verbose_name_plural = _("Sayt Sozlamalari")

    def __str__(self):
        return self.site_name or "Sayt Sozlamalari"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class HeroSection(models.Model):
    title            = models.CharField(_("Sarlavha"), max_length=300)
    subtitle         = models.TextField(_("Qo'shimcha matn"), blank=True)
    background_image = models.ImageField(_("Orqa fon rasmi"), upload_to='hero/', blank=True, null=True)
    cta_text         = models.CharField(_("Tugma matni"), max_length=100, blank=True, default="Tadqiqotlarni ko'rish")
    cta_link         = models.CharField(_("Tugma havolasi"), max_length=200, blank=True, default="/research/")
    is_active        = models.BooleanField(_("Faolmi?"), default=True)

    class Meta:
        verbose_name        = _("Hero Bo'lim")
        verbose_name_plural = _("Hero Bo'limlar")

    def __str__(self):
        return self.title


class Page(models.Model):
    title            = models.CharField(_("Sarlavha"), max_length=200)
    slug             = models.SlugField(_("URL"), unique=True)
    content          = RichTextField(_("Kontent"))
    meta_description = models.CharField(_("Meta tavsif"), max_length=300, blank=True)
    banner_image     = models.ImageField(_("Banner rasmi"), upload_to='pages/', blank=True, null=True)
    is_published     = models.BooleanField(_("Chop etilganmi?"), default=True)
    show_in_menu     = models.BooleanField(_("Menyuda ko'rinsinmi?"), default=True)
    menu_order       = models.PositiveIntegerField(_("Menyu tartibi"), default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['menu_order', 'title']
        verbose_name        = _("Sahifa")
        verbose_name_plural = _("Sahifalar")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('page_detail', kwargs={'slug': self.slug})


class ResearchArea(models.Model):
    ICON_CHOICES = [
        ('brain',  '🧠 Miya'),
        ('eye',    '👁️ Ko\'z'),
        ('heart',  '❤️ Yurak'),
        ('chart',  '📊 Grafik'),
        ('lab',    '🔬 Laboratoriya'),
        ('signal', '📡 Signal'),
        ('neuron', '⚡ Neyron'),
        ('data',   '💻 Ma\'lumot'),
    ]
    title     = models.CharField(_("Nomi"), max_length=200)
    description = RichTextField(_("Tavsif"))
    icon      = models.CharField(_("Ikonka"), max_length=20, choices=ICON_CHOICES, default='brain')
    image     = models.ImageField(_("Rasm"), upload_to='research/', blank=True, null=True)
    order     = models.PositiveIntegerField(_("Tartib"), default=0)
    is_active = models.BooleanField(_("Faolmi?"), default=True)

    class Meta:
        ordering            = ['order']
        verbose_name        = _("Tadqiqot Yo'nalishi")
        verbose_name_plural = _("Tadqiqot Yo'nalishlari")

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('pi',       _('Asosiy Tadqiqotchi (PI)')),
        ('postdoc',  _('Postdoktorant')),
        ('phd',      _('Doktorant (PhD)')),
        ('masters',  _('Magistrant')),
        ('undergrad',_('Bakalavr Tadqiqotchi')),
        ('alumni',   _('Bitiruvchi')),
        ('staff',    _('Laboratoriya Xodimi')),
    ]
    name             = models.CharField(_("Ismi"), max_length=200)
    role             = models.CharField(_("Lavozimi"), max_length=20, choices=ROLE_CHOICES, default='phd')
    bio              = RichTextField(_("Biografiya"), blank=True)
    photo            = models.ImageField(_("Rasmi"), upload_to='team/', blank=True, null=True)
    email            = models.EmailField(_("Email"), blank=True)
    google_scholar   = models.URLField(_("Google Scholar"), blank=True)
    researchgate     = models.URLField(_("ResearchGate"), blank=True)
    linkedin         = models.URLField(_("LinkedIn"), blank=True)
    personal_website = models.URLField(_("Shaxsiy veb-sayt"), blank=True)
    order            = models.PositiveIntegerField(_("Tartib"), default=0)
    is_active        = models.BooleanField(_("Faolmi?"), default=True)

    class Meta:
        ordering            = ['order', 'name']
        verbose_name        = _("Jamoa A'zosi")
        verbose_name_plural = _("Jamoa A'zolari")

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


class Publication(models.Model):
    title     = models.CharField(_("Maqola sarlavhasi"), max_length=500)
    authors   = models.CharField(_("Mualliflar"), max_length=500)
    journal   = models.CharField(_("Jurnal nomi"), max_length=300)
    year      = models.PositiveIntegerField(_("Yil"))
    volume    = models.CharField(_("Tom"), max_length=50, blank=True)
    pages     = models.CharField(_("Sahifalar"), max_length=50, blank=True)
    doi_link  = models.URLField(_("DOI havolasi"), blank=True)
    pdf_file  = models.FileField(_("PDF fayl"), upload_to='publications/', blank=True, null=True)
    abstract  = models.TextField(_("Annotatsiya"), blank=True)
    is_featured = models.BooleanField(_("Tavsiya etilganmi?"), default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-year', '-created_at']
        verbose_name        = _("Ilmiy Maqola")
        verbose_name_plural = _("Ilmiy Maqolalar")

    def __str__(self):
        return f"{self.title} ({self.year})"


class NewsEvent(models.Model):
    TYPE_CHOICES = [
        ('news',         _('Yangilik')),
        ('event',        _('Tadbir')),
        ('award',        _('Mukofot')),
        ('announcement', _('E\'lon')),
    ]
    title       = models.CharField(_("Sarlavha"), max_length=300)
    content     = RichTextField(_("Matn"))
    image       = models.ImageField(_("Rasm"), upload_to='news/', blank=True, null=True)
    news_type   = models.CharField(_("Turi"), max_length=20, choices=TYPE_CHOICES, default='news')
    date        = models.DateField(_("Sana"))
    is_published = models.BooleanField(_("Chop etilganmi?"), default=True)
    is_featured  = models.BooleanField(_("Tavsiya etilganmi?"), default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-date']
        verbose_name        = _("Yangilik / Tadbir")
        verbose_name_plural = _("Yangiliklar va Tadbirlar")

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title     = models.CharField(_("Nomi"), max_length=200)
    image     = models.ImageField(_("Rasm"), upload_to='gallery/')
    caption   = models.CharField(_("Izoh"), max_length=300, blank=True)
    order     = models.PositiveIntegerField(_("Tartib"), default=0)
    is_active = models.BooleanField(_("Faolmi?"), default=True)

    class Meta:
        ordering            = ['order']
        verbose_name        = _("Galereya Rasmi")
        verbose_name_plural = _("Galereya Rasmlari")

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name       = models.CharField(_("Ismi"), max_length=200)
    email      = models.EmailField(_("Email"))
    subject    = models.CharField(_("Mavzu"), max_length=300)
    message    = models.TextField(_("Xabar"))
    created_at = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(_("O'qilganmi?"), default=False)

    class Meta:
        ordering            = ['-created_at']
        verbose_name        = _("Aloqa Xabari")
        verbose_name_plural = _("Aloqa Xabarlari")

    def __str__(self):
        return f"{self.name} — {self.subject}"


class StatCounter(models.Model):
    label  = models.CharField(_("Nomi"), max_length=100)
    value  = models.PositiveIntegerField(_("Qiymati"))
    icon   = models.CharField(_("Ikonka"), max_length=50, default='chart')
    order  = models.PositiveIntegerField(_("Tartib"), default=0)

    class Meta:
        ordering            = ['order']
        verbose_name        = _("Statistika")
        verbose_name_plural = _("Statistikalar")

    def __str__(self):
        return f"{self.label}: {self.value}"


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('award',       _("Mukofot")),
        ('grant',       _("Grant")),
        ('recognition', _("Tan olinish")),
        ('milestone',   _("Yutuq")),
        ('publication', _("Nashr")),
        ('other',       _("Boshqa")),
    ]
    title       = models.CharField(_("Sarlavha"), max_length=300)
    description = RichTextField(_("Tavsif"), blank=True)
    category    = models.CharField(_("Kategoriya"), max_length=20, choices=CATEGORY_CHOICES, default='award')
    year        = models.PositiveIntegerField(_("Yil"))
    image       = models.ImageField(_("Rasm"), upload_to='achievements/', blank=True, null=True)
    link        = models.URLField(_("Havola"), blank=True)
    is_featured = models.BooleanField(_("Tavsiya etilganmi?"), default=False)
    order       = models.PositiveIntegerField(_("Tartib"), default=0)

    class Meta:
        ordering            = ['-year', 'order']
        verbose_name        = _("Yutuq / Mukofot")
        verbose_name_plural = _("Yutuqlar va Mukofotlar")

    def __str__(self):
        return f"{self.title} ({self.year})"


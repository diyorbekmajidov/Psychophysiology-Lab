"""
Demo data script — run with:
  python manage.py shell < seed_data.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from psychology_lab.models import (
    SiteSettings, HeroSection, ResearchArea,
    TeamMember, Publication, NewsEvent, StatCounter
)

# Site Settings
SiteSettings.objects.update_or_create(pk=1, defaults={
    'site_name': 'Psychophysiology Lab',
    'tagline': 'Advancing the science of mind and behavior through cutting-edge psychophysiology research.',
    'email': 'lab@psycholab.edu',
    'phone': '+1 (555) 123-4567',
    'address': 'Department of Psychology\nUniversity of Science\nNew York, NY 10001',
    'twitter': 'https://twitter.com/',
    'linkedin': 'https://linkedin.com/',
    'researchgate': 'https://researchgate.net/',
    'footer_text': 'Advancing neuroscience & psychophysiology research since 2010.',
})
print("✅ SiteSettings created")

# Hero
HeroSection.objects.get_or_create(
    title='Decoding the Science of <span class="gradient-text">Human Mind</span>',
    defaults={
        'subtitle': 'We use psychophysiological methods — EEG, fMRI, GSR, eye-tracking — to understand how the brain regulates cognition, emotion, and behavior.',
        'cta_text': 'Explore Research',
        'cta_link': '/research/',
        'is_active': True,
    }
)
print("✅ HeroSection created")

# Stats
stats_data = [
    ('Publications', 120, 'chart', 0),
    ('Research Projects', 18, 'lab', 1),
    ('Team Members', 25, 'brain', 2),
    ('Years of Research', 14, 'neuron', 3),
    ('Collaborating Institutions', 30, 'signal', 4),
    ('Conference Presentations', 85, 'data', 5),
]
for label, value, icon, order in stats_data:
    StatCounter.objects.get_or_create(label=label, defaults={'value': value, 'icon': icon, 'order': order})
print("✅ StatCounters created")

# Research Areas
areas = [
    ('Cognitive Neuroscience', 'We investigate the neural mechanisms underlying attention, memory, and executive function using EEG and neuroimaging techniques.', 'brain', 0),
    ('Emotion Regulation', 'Understanding how individuals regulate emotional responses through autonomic nervous system measures including heart rate variability.', 'heart', 1),
    ('Visual Psychophysics', 'Examining visual perception and its neural correlates using eye-tracking and event-related potentials.', 'eye', 2),
    ('Stress & Psychophysiology', 'Studying the physiological correlates of acute and chronic stress, including cortisol, galvanic skin response, and cardiovascular measures.', 'signal', 3),
    ('Clinical Applications', 'Applying psychophysiological methods to understand and treat anxiety disorders, PTSD, and attention-deficit hyperactivity disorder.', 'lab', 4),
    ('Computational Modeling', 'Building computational models of psychophysiological data to better understand brain-behavior relationships.', 'data', 5),
]
for title, desc, icon, order in areas:
    ResearchArea.objects.get_or_create(title=title, defaults={
        'description': f'<p>{desc}</p>',
        'icon': icon,
        'order': order,
        'is_active': True,
    })
print("✅ ResearchAreas created")

# Team Members
members = [
    ('Dr. Alex Johnson', 'pi', '<p>Dr. Johnson is the Principal Investigator with over 15 years of experience in psychophysiology research. He leads a team of researchers investigating the neural bases of emotion and cognition.</p>', 'professor@lab.edu', 0),
    ('Dr. Sarah Chen', 'postdoc', '<p>Post-doctoral researcher specializing in EEG-based studies of attention and cognitive control.</p>', 'schen@lab.edu', 1),
    ('Michael Torres', 'phd', '<p>PhD candidate studying the psychophysiology of stress and resilience.</p>', 'mtorres@lab.edu', 2),
    ('Priya Patel', 'phd', '<p>PhD student investigating emotion regulation using heart rate variability measures.</p>', 'ppatel@lab.edu', 3),
    ('James Wilson', 'masters', '<p>Master\'s student studying visual attention using eye-tracking methodology.</p>', 'jwilson@lab.edu', 4),
    ('Emily Brown', 'undergrad', '<p>Undergraduate researcher assisting with data collection and analysis.</p>', 'ebrown@lab.edu', 5),
]
for name, role, bio, email, order in members:
    TeamMember.objects.get_or_create(name=name, defaults={
        'role': role, 'bio': bio, 'email': email, 'order': order, 'is_active': True,
    })
print("✅ TeamMembers created")

# Publications
pubs = [
    ('Neural correlates of emotion regulation: An EEG study', 'Johnson A., Chen S., Torres M.', 'Journal of Psychophysiology', 2024, '38', '1-15', True),
    ('Heart rate variability as a biomarker of cognitive load', 'Torres M., Johnson A.', 'Biological Psychology', 2023, '175', '108456', True),
    ('Attention modulation in anxiety: A psychophysiological approach', 'Patel P., Johnson A., Chen S.', 'Psychophysiology', 2023, '60', 'e14123', False),
    ('EEG correlates of visual selective attention', 'Chen S., Wilson J., Johnson A.', 'NeuroImage', 2022, '254', '119-134', False),
]
for title, authors, journal, year, volume, pages, featured in pubs:
    Publication.objects.get_or_create(title=title, defaults={
        'authors': authors, 'journal': journal, 'year': year,
        'volume': volume, 'pages': pages, 'is_featured': featured,
    })
print("✅ Publications created")

# News
import datetime
news_items = [
    ('Lab receives prestigious NIH grant for stress research', 'news', datetime.date(2024, 5, 15), True, True),
    ('Dr. Johnson to present at Society for Psychophysiology Research annual meeting', 'event', datetime.date(2024, 6, 20), True, False),
    ('PhD student Michael Torres wins Best Paper Award', 'award', datetime.date(2024, 4, 10), True, True),
    ('New EEG equipment installed in the lab', 'announcement', datetime.date(2024, 3, 5), True, False),
]
for title, ntype, date, published, featured in news_items:
    NewsEvent.objects.get_or_create(title=title, defaults={
        'content': f'<p>Detailed content about: {title}. More information will be added soon.</p>',
        'news_type': ntype, 'date': date, 'is_published': published, 'is_featured': featured,
    })
print("✅ News & Events created")

print("\n🎉 All demo data loaded successfully!")
print("Now run: python manage.py createsuperuser")

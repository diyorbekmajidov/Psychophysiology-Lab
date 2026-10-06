from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import MenuItem, Page


class NavigationTests(TestCase):
    def test_editor_pages_can_be_linked_from_menu_and_submenu(self):
        overview = Page.objects.create(title='Laboratoriya', slug='laboratoriya', content='<p>Laboratoriya matni</p>')
        details = Page.objects.create(title='Jihozlar', slug='jihozlar', content='<p>Jihozlar matni</p>')
        parent = MenuItem.objects.create(title='Biz haqimizda', destination_type='page', page=overview, order=200)
        MenuItem.objects.create(title='Jihozlar menyusi', parent=parent, destination_type='page', page=details)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Biz haqimizda')
        self.assertContains(response, 'Jihozlar menyusi')
        self.assertContains(response, 'href="/laboratoriya/"')
        self.assertContains(response, 'href="/jihozlar/"')
        self.assertContains(self.client.get('/jihozlar/'), 'Jihozlar matni')

    def test_draft_pages_and_inactive_menu_items_are_hidden(self):
        draft = Page.objects.create(title='Qoralama', slug='qoralama', content='Draft', is_published=False)
        MenuItem.objects.create(title='Yashirin sahifa', destination_type='page', page=draft, order=200)
        MenuItem.objects.create(title='Ochiq emas', destination_type='route', route_name='team', is_active=False)

        response = self.client.get('/')
        self.assertNotContains(response, 'Yashirin sahifa')
        self.assertNotContains(response, 'Ochiq emas')
        self.assertEqual(self.client.get('/qoralama/').status_code, 404)

    def test_nested_submenu_and_missing_page_are_rejected(self):
        page = Page.objects.create(title='Sinov', slug='sinov', content='Matn')
        root = MenuItem.objects.create(title='Bosh', destination_type='route', route_name='research')
        child = MenuItem.objects.create(title='Ichki', parent=root, destination_type='page', page=page)

        with self.assertRaises(ValidationError):
            MenuItem(title='Uchinchi daraja', parent=child, destination_type='page', page=page).full_clean()
        with self.assertRaises(ValidationError):
            MenuItem(title='Sahifasiz', destination_type='page').full_clean()
        with self.assertRaises(ValidationError):
            Page(title='Ziddiyat', slug='research', content='Matn').full_clean()

    def test_admin_can_create_a_menu_item(self):
        user = get_user_model().objects.create_superuser('editor', 'editor@example.com', 'test-password')
        self.client.force_login(user)
        add_url = '/admin/psychology_lab/menuitem/add/'
        self.assertEqual(self.client.get(add_url).status_code, 200)
        page_form = self.client.get('/admin/psychology_lab/page/add/')
        self.assertEqual(page_form.status_code, 200)
        self.assertContains(page_form, 'id_content_uz')
        response = self.client.post(add_url, {
            'title': 'Qo‘shimcha',
            'title_uz': 'Qo‘shimcha',
            'title_ru': 'Дополнительно',
            'title_en': 'More',
            'destination_type': 'route',
            'route_name': 'team',
            'icon': 'users',
            'order': 5,
            'is_active': 'on',
            '_save': 'Save',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MenuItem.objects.filter(title_uz='Qo‘shimcha', route_name='team').exists())

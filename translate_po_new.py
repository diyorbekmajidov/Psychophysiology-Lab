import re

translations = {
    "en": {
        "Boshqa Yo'nalishlar": "Other Areas"
    },
    "ru": {
        "Boshqa Yo'nalishlar": "Другие направления"
    }
}


def translate_po_file(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    dict_translations = translations.get(lang, {})

    pattern = r'(msgid "([^"]+)"\nmsgstr )""'

    def replacer(match):
        full_prefix = match.group(1)
        msgid_val = match.group(2)
        translation_val = dict_translations.get(msgid_val, "")

        translation_val = translation_val.replace('"', '\\"')

        if translation_val:
            return f'{full_prefix}"{translation_val}"'
        else:
            return match.group(0)

    new_content = re.sub(pattern, replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Successfully processed translations for {lang}")


if __name__ == "__main__":
    translate_po_file("locale/en/LC_MESSAGES/django.po", "en")
    translate_po_file("locale/ru/LC_MESSAGES/django.po", "ru")

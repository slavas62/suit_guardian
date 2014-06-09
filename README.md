django-guardian support for django-suit
=======================================

Extra templates for [django-suit](https://github.com/darklow/django-suit) to support [django-guardian](https://github.com/lukaszb/django-guardian).

## Requirements

- [django-suit](https://github.com/darklow/django-suit) <= 0.2.8 (obviously)
- [django-guardian](https://github.com/lukaszb/django-guardian) <= 1.2.0

## Installation

```
pip install suit_guardian
```

Add to `INTALLED_APPS` before `django-guardian`:

```
INSTALLED_APPS = (
    'suit',
    'suit_guardian',  # <----
    'django.contrib.admin',
    # ...
    'guardian',
    # ...
)

```

## Modified templates

- templates
    - admin
        - guadian
            - model
                - change_form.html
                - field.html
                - obj_perms_manage.html
                - obj_perms_manage_group.html
                - obj_perms_manage_user.html


## License

Same as [django-suit](https://github.com/darklow/django-suit).

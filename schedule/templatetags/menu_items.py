from django import template

register = template.Library()


@register.inclusion_tag("schedule/menu_list.html", takes_context=True)
def get_users_menu(context):
    request = context.get("request")
    if request.user.is_authenticated:
        users_menu = [
            {"id": 3, "name": "Выйти", "templates": "users:logout"},
        ]
    else:
        users_menu = [
            {"id": 1, "name": "Войти", "templates": "users:login"},
            {"id": 2, "name": "Регистрация", "templates": "users:registration"},
        ]
    return {"users_menu": users_menu}


@register.inclusion_tag("schedule/all_menus.html", takes_context=True)
def get_menu(context):
    request = context.get("request")

    all_menu = [
        {"id": 1, "name": "Клиенты", "templates": "schedule:client_list"},
        {
            "id": 2,
            "name": "Посты для рассылок",
            "templates": "schedule:textfornewsletter_list",
        },
        {"id": 3, "name": "Рассылки", "templates": "schedule:newsletter_list"},
        {"id": 4, "name": "Главная страница", "templates": "schedule:home"},
        {"id": 5, "name": "Пользователи", "templates": "users:user_list"},
        {"id": 6, "name": "Блог", "templates": "blog:blog_list"},
    ]

    if request.user.is_superuser:
        return {"all_menu": all_menu}
    elif not request.user.is_staff and not request.user.is_superuser:
        users_menu = [all_menu[2], all_menu[3], all_menu[4], all_menu[5]]
        return {"all_menu": users_menu}
    else:

        managers_menu = [
            all_menu[2],
            all_menu[5],
            all_menu[3],
        ]
        return {"all_menu": managers_menu}
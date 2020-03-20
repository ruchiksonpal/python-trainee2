from django.urls import path

from web.film.views import language_list, language_add, language_delete, language_edit, language_check, actor_list, \
    actor_delete, actor_add, actor_edit

urlpatterns = [

    # path('category/list', category_list, name="category_list"),
    path('language/list', language_list, name="language_list"),
    path('language/list/add', language_add, name="add_language"),
    path('language/list/delete/<int:id>/', language_delete, name="language_delete"),
    path('language/list/edit/<int:id>/', language_edit, name="language_edit"),
    path('check/language/', language_check, name="check_language"),
    path('actor/list/', actor_list, name="actor_list"),
    path('actor/list/delete/<int:id>/', actor_delete, name="actor_delete"),
    path('actor/list/add', actor_add, name="actor_add"),
    path('actor/list/edit/<int:id>', actor_edit, name="actor_edit"),

    # path('film/list', film_list, name="film_list"),
    # path('film/category/list', film_category_list, name="film_category_list"),
    # # path('actor/list', actor_list, name="actor_list"),
    # path('film/actor/list', film_actor_list, name="film_actor_list"),
    # path('address/list', address_list, name="address_list"),
    # path('city/list', city_list, name="city_list"),
    # path('country/list', country_list, name="country_list"),

    # path('film/actor/list', FilmActor_list, name="film_actor_list"),

]

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from web.users import logger
from web.film.models import Actor, Address, City, Country, Film, FilmActor, Category, Language, FilmCategory


# @login_required(login_url="admin_login")  # login required
# def category_list(request, template="film/category_list.html"):  # fun category_list
#     return render(request, template, {"category": Category.objects.all()})


@login_required(login_url="admin_login")  # login required
def language_list(request, template="film/language_list.html"):  # fun language_list
    return render(request, template, {"language": Language.objects.all().order_by('name')})
    # render template and order by name


@login_required(login_url="admin_login")  # login required
def language_add(request, template="film/language_add.html"):  # fun language_list
    try:
        if request.method == 'POST':  # method post
            language_name = request.POST.get("lan_name").lstrip(" ").rstrip(" ")  # get data
            if not language_name:  # check null or not
                messages.add_message(request, messages.ERROR, "language name is not null allow")
                return redirect("add_language")  # redirect
            else:
                status = check_language(language_name)  # call fun
                if status:
                    add_language_obj = Language.objects.create(  # insert language name
                        name=language_name
                    )
                else:
                    messages.add_message(request, messages.ERROR, "language name is already exist")
                    return redirect("add_language")
            messages.add_message(request, messages.SUCCESS, "Data inserted successfully")
            return redirect("language_list")
    except Exception as ex:
        logger.exception(ex.args)
    return render(request, template,
                  {"lan": Language.objects.all()})  # return  language objects in dic and render template


@login_required(login_url="admin_login")  # login required
def language_check(request):  # fun film_list
    try:
        language_name = request.POST.get("lan_name")  # get name from form
        id = request.POST.get("id")  # get id from remote
        if id:  # check id or not
            status = check_language(language_name, id)  # call fun
            if not status:
                return HttpResponse("false")  # http response for jquery
            return HttpResponse("true")
        else:
            status = check_language(language_name)  # call fun
            if not status:  # check status true or false
                return HttpResponse("false")  # http response for jquery
    except Exception as ex:  # exception
        logger.exception(ex.args)
    return HttpResponse("true")  # http response for jquery


def check_language(language_name, *args):  # check language name exist or not common fun
    try:
        if len(args) > 0:  # check arguments
            id = args[0]  # we pass id here
            status = Language.objects.filter(~Q(id=id),
                                             name=language_name)  # check name exist or not and skip selected id
            if status:  # if exist false else true
                return False
        else:
            status = Language.objects.filter(name=language_name)  # check name exist or not
            if status:  # if exist false else true
                return False
    except Exception as ex:
        logger.exception(ex.args)
    return True


@login_required(login_url="admin_login")  # login required
def language_delete(request, id):  # fun language delete
    try:
        Language.objects.get(pk=id).delete()  # get id and delete
        logger.info("language deleted successfully, Language ID is = {0}".format(id))
        messages.add_message(request, messages.SUCCESS, "Data deleted successfully")
    except Exception as ex:  # exception
        logger.exception(ex.args)
    return redirect("language_list")  # redirect language list


@login_required(login_url="admin_login")  # login required
def language_edit(request, id, template="film/language_add.html"):  # fun film_list
    try:
        if request.method == 'POST':  # method post and update data
            language_name = request.POST.get("lan_name").lstrip(" ").rstrip(" ")  # get data in post method
            if not language_name:
                messages.add_message(request, messages.ERROR, "language name is not null allow in edit")
                return redirect("language_edit", id=id)
            else:
                status = check_language(language_name, id)
                if not status:
                    messages.add_message(request, messages.ERROR, "language name is already exist")
                    return redirect("language_edit", id=id)
                else:
                    Language.objects.filter(pk=id).update(name=language_name)
                    logger.info("language edit successfully, Language ID is = {0}".format(id))
                    return redirect("language_list")
        obj_language_edit = Language.objects.get(pk=id)  # method get and render data
        return render(request, template, {"language_names": obj_language_edit})  # render template
    except Exception as ex:
        logger.info(ex.args)
    return render(request, template)  # redirect language list


@login_required(login_url="admin_login")  # login required
def actor_list(request, template="film/actor_list.html"):  # fun to get data fom model actor
    return render(request, template, {"actor": Actor.objects.all().order_by('first_name')})


@login_required(login_url="admin_login")  # login required
def actor_delete(request, id):  # fun actor delete
    try:
        Actor.objects.get(pk=id).delete()  # get id and delete
        logger.info("actor deleted successfully, Actor ID is = {0}".format(id))
        messages.add_message(request, messages.SUCCESS, "actor deleted successfully")
    except Exception as ex:  # exception
        logger.exception(ex.args)
    return redirect("actor_list")  # redirect actor list


@login_required(login_url="admin_login")  # login required
def actor_add(request, template="film/actor_add.html"):  # fun actor_list
    try:
        if request.method == 'POST':  # method post
            first__name = request.POST.get("first_name").lstrip(" ").rstrip(" ")  # get data
            last__name = request.POST.get("last_name").lstrip(" ").rstrip(" ")  # get data
            if not first__name or not last__name:  # check null or not
                messages.add_message(request, messages.ERROR, "language name is not null allow")
                return redirect('actor_add')  # redirect actor add
            else:
                add_actor_obj = Actor.objects.create(  # insert language name
                    first_name=first__name,
                    last_name=last__name,
                )
            messages.add_message(request, messages.SUCCESS, "Actor inserted successfully")
            return redirect("actor_list")  # redirect to actor list
    except Exception as ex:  # if exception raise
        logger.exception(ex.args)
    return render(request, template,
                  {"actor": Actor.objects.all()})  # return  actor objects in dic and render template


@login_required(login_url="admin_login")  # login required
def actor_edit(request, ids, template="film/actor_add.html"):  # fun actor_list
    try:
        if request.method == 'POST':  # method post and update data
            first_name = request.POST.get("first_name").lstrip(" ").rstrip(" ")  # get data in post method
            last_name = request.POST.get("last_name").lstrip(" ").rstrip(" ")  # get data in post method
            if not first_name or not last_name:  # check null or not (validate data)
                messages.add_message(request, messages.ERROR, "language name is not null allow in edit")
                return redirect("actor_edit", id=id)  # redirect to edit actor with id
            else:
                Actor.objects.filter(pk=id).update(first_name=first_name, last_name=last_name)  # update actor
                logger.info("actor edit successfully, Language ID is = {0}".format(id))
                return redirect("actor_list")
        obj_actor_edit = Actor.objects.get(pk=id)  # method get and render data
        return render(request, template, {"actor_names": obj_actor_edit})  # render template
    except Exception as ex:  # if exception raise
        logger.info(ex.args)
    return render(request, template)  # redirect language list
# return actor list order by first_name desc
#     logger.info("Language edit successfully, Language ID is = {0}".format(id))
#
# except Exception as ex:  # exception
#     logger.exception(ex.args)
# return redirect("language_list")

#
# @login_required(login_url="admin_login")  # login required
# def film_list(request, template="film/film_list.html"):  # fun film_list
#     return render(request, template, {"film": Film.objects.all()})
#
#
# @login_required(login_url="admin_login")  # login required
# def film_category_list(request, template="film/film_category_list.html"):  # fun film_category_list
#     return render(request, template, {"film_category": FilmCategory.objects.all()})
#
#
# @login_required(login_url="admin_login")  # login required
# def actor_list(request, template="film/actor_list.html"):  # fun actor_list
#     return render(request, template, {"actor": Actor.objects.all()})
#
#
# @login_required(login_url="admin_login")  # login required
# def film_actor_list(request, template="film/film_actor_list.html"):  # fun film_actor_list
#     return render(request, template, {"film_actor": FilmActor.objects.all()})
#
#
# @login_required(login_url="admin_login")  # login required
# def address_list(request, template="film/address_list.html"):  # fun address_list
#     return render(request, template, {"address": Address.objects.all()})
#
#
# @login_required(login_url="admin_login")  # login required
# def city_list(request, template="film/city_list.html"):  # fun city_list
#     return render(request, template, {"city": City.objects.all()})
#
#
# @login_required(login_url="admin_login")  # login required
# def country_list(request, template="film/country_list.html"):  # fun country_list
#     return render(request, template, {"country": Country.objects.all()})

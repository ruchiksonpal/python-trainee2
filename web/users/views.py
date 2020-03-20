from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

# Create your views here.
from web.users import logger
from web.users.constant import Gender

from web.users.models import UserProfile


# authenticate user
def login(request, template="users/login.html"):
    try:
        if request.user.is_authenticated:
            if 'next' in request.GET:
                return redirect(request.GET["next"])
            return redirect("dashboard")
        if request.method == "POST":
            user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None and user.is_active and user.is_superuser:  # active superusers are allowed to login
                auth_login(request, user)

                logger.info("{0} logged in successfully".format(user.username))
                return redirect("dashboard")
            else:
                messages.add_message(request, messages.ERROR, "Invalid login credentials")
    except Exception as ex:
        logger.exception(ex.args)
    return render(request, template)


@login_required(login_url="admin_login")
def dashboard(request, template="users/dashboard.html"):
    # add_user_obj = User.objects.create_user(
    #     username="dsds",
    #     email="john@doe.com",
    #     password="Test105*",
    #     first_name="John",
    #     last_name="Doe"
    # )

    # add_user_profile_obj = UserProfile.objects.create(
    #     user=add_user_obj);
    # # bio="Lorem ipsum",
    # # gender=Gender.male

    return render(request, template, {"users": User.objects.all()})


@login_required(login_url="admin_login")
def user_delete(request, id):
    try:
        User.objects.get(pk=id).delete()
        logger.info("User deleted successfully, User ID is = {0}".format(id))
    except Exception as ex:
        logger.exception(ex.args)
    return redirect("dashboard")


@login_required(login_url="admin_login")
def logout(request):
    auth_logout(request)
    return redirect("admin_login")

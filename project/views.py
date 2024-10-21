from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from project.models import User

from .forms import UserRegisterForm
from .utils import compare_faces


@login_required(login_url="login")
def home_page(request):

    users = User.objects.all()
    
    
    context = {
        'users': users
    }
    

    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("login")

        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    context = {}

    if request.method == "POST":

        image = request.FILES.get("image")

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and image:
            user = User.objects.filter(username=username)

            if user.exists():
                user = user.first()

                result = compare_faces(user.image.path, image)

                if result == "Yuzlar mos keldi":

                    login(request, user)

                    return redirect("home")
                else:
                    context["error"] = result

            else:
                context["error"] = "Foydalanuvchi topilmadi"

        elif username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("home")
            else:
                context["error"] = "Foydalanuvchi topilmadi"

        else:
            context["error"] = "Nimadur xato ketti"

    return render(request, "users/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")

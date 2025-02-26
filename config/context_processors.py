def user_groups(request):
    user = request.user
    if user.is_authenticated:
        is_staff = user.is_staff
        is_itr = user.groups.filter(name="itr").exists()
        is_lift = user.groups.filter(name="lift").exists()
    else:
        is_staff = False
        is_itr = False
        is_lift = False

    return {
        "is_staff": is_staff,
        "is_itr": is_itr,
        "is_lift": is_lift,
    }

def check_role(role):
    if role == "Admin":
        return "Full Access"
    elif role == "User":
        return "Limited Access"
    else:
        return "Access Denied"

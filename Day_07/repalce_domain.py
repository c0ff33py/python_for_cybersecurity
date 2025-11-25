def replace_domain(email, old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
    

change_domain = replace_domain("kyaw@zail.com", "zail.com", "oail.com")
print(change_domain)

# output : kyaw@oail.com
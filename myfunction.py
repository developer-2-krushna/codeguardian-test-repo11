def check_access_standard(role: str) -> bool:
    # Explicit check against authorized roles
    allowed_roles = ["admin", "manager", "super-user"]
    
    if role.lower() in allowed_roles:
        return True
    else:
        return False

# Usage
print(check_access_standard("admin"))  # Returns True

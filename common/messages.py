VALIDATION = {
    'first_name': {
        "blank": "First Name can not be blank",
        "invalid": "First Name must contain only alphabets, no spaces, numbers or special characters",
        "required": "First Name required",
    },
    'last_name': {
        "blank": "Last Name can not be blank",
        "invalid": "Last Name must contains only alphabets, no spaces, numbers or special characters",
        "required": "Last Name required",
    },
    'email': {
        "blank": "Email can not be blank",
        "required": "Email required",
        "exists": "Email already exist",
        "does_not_exists": "Email does not exist",
    },
    'contact': {
        "blank": "Contact can not be blank",
        "required": "Contact required",
        "invalid": "Invalid contact",
        "exists": "Contact already exist",
    },
    'password': {
        "blank": "Password can not be blank",
        "invalid": "Password must contain uppercase, lowercase, digit and special character",
        "required": "Password required",
        "do_not_match": "Passwords do not match",
        'old_password': 'Wrong password',
    },
    "invalid_credentials": "Invalid Credentials",
    'token': {
        'invalid': 'Invalid link',
        'expired': 'Link expired',
    },

}

MAX_LENGTH = {
    'first_name': 30,
    'last_name': 30,
    'password': 16,
    'contact': 10,
    'employee_id': 7,
    'designation': 50,
    'subject': 255,
    'content': 255,

}

MIN_LENGTH = {
    'first_name': 3,
    'last_name': 3,
    'password': 8,
    'contact': 10,
    'employee_id': 7,
    'designation': 5,
    'subject': 5,
    'content': 10,
}

SUCCESS_MESSAGES = {
    'signup': {
        'successfully': 'SignUp has been success',
    },
    'login': {
        'success': 'Login successfully'
    },
    'logout': {
        'success': 'Logout Successfully'
    },
}

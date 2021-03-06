import base64


def get_basic_auth_header(user, password):
    """
    Return a dict containing the correct headers to set to make HTTP Basic
    Auth request
    """
    user_pass = "{0}:{1}".format(user, password)
    auth_string = base64.b64encode(user_pass.encode("utf-8"))
    auth_headers = {
        "HTTP_AUTHORIZATION": "Basic " + auth_string.decode("utf-8"),
    }

    return auth_headers

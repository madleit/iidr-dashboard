import grp
import pam


def authenticate_user(
    username,
    password
):

    p = pam.pam()

    return p.authenticate(
        username,
        password
    )


def user_in_group(
    username,
    group_name="cdc"
):

    try:

        group = grp.getgrnam(
            group_name
        )

        return (
            username in group.gr_mem
        )

    except KeyError:

        return False
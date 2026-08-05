import grp
import pwd


def authenticate_user(
    username,
    password
):

    try:

        pwd.getpwnam(
            username
        )

        return True

    except KeyError:

        return False


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
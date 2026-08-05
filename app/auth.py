import grp
import pwd
import PAM


def authenticate_user(
    username,
    password
):

    def pam_conv(
        auth,
        query_list,
        userData
    ):

        responses = []

        for query, query_type in query_list:

            if (
                query_type ==
                PAM.PAM_PROMPT_ECHO_OFF
            ):

                responses.append(
                    (
                        password,
                        0
                    )
                )

            else:

                responses.append(
                    (
                        "",
                        0
                    )
                )

        return responses

    try:

        auth = PAM.pam()

        auth.start(
            "login"
        )

        auth.set_item(
            PAM.PAM_USER,
            username
        )

        auth.set_item(
            PAM.PAM_CONV,
            pam_conv
        )

        auth.authenticate()

        auth.acct_mgmt()

        return True

    except PAM.error:

        return False

    except Exception:

        return False
``
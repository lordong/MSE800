from zoos import (
    admin_login,
    view_actions,
    admin_logout
)


def main():

    admin_login("Mohammad")

    view_actions(
        "Mohammad",
        "Feed the lions"
    )

    admin_logout("Mohammad")


if __name__ == "__main__":
    main()

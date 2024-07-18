from src.auth.authentication import AuthService


def main():
    authService: AuthService = AuthService()
    authService.add_user('esther', 'purrungaanonima')

    print(authService.users['esther'])


if __name__ == '__main__':
    main()

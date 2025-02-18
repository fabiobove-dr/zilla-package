from zilla_package.zilla import Zilla


def main() -> None:
    zilla = Zilla.create("hello")
    print(zilla)


if __name__ == "__main__":
    main()

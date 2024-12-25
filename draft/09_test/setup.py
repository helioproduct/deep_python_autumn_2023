from distutils.core import setup, Extension


def main():
    module = Extension("cutils", sources=["utils.c"])

    setup(
        name="PackageName",
        version="1.0.0",
        description="this is a package for my module",
        ext_modules=[module],
    )


if __name__ == "__main__":
    main()

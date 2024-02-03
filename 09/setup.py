from distutils.core import setup, Extension


def main():
    module = Extension("cjson", sources=["cjson.c"])

    setup(
        name="cjson",
        version="1.0.0",
        description="json-string parsing",
        ext_modules=[module],
    )


if __name__ == "__main__":
    main()

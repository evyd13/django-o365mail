import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-o365mail",
    version="0.0.1",
    author="Evelien Dekkers",
    author_email="sixmoonskies@gmail.com",
    description="A Django email backend to use the O365 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evyd13/django-o365mail",
    project_urls={
        "Bug Tracker": "https://github.com/evyd13/django-o365mail/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['O365'],
)
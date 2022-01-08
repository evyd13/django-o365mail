import setuptools
from distutils.util import convert_path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

init_ns = {}
ver_path = convert_path('src/django_o365mail/__version__.py')
with open(ver_path) as f: exec(f.read(), init_ns)

setuptools.setup(
    name="django-o365mail",
    version=init_ns['__version__'],
    author="Evelien Dekkers",
    author_email="sixmoonskies@gmail.com",
    description="Office 365 (O365) email backend for Django",
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
        "Development Status :: 5 - Production/Stable",
        "Topic :: Communications :: Email",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['O365'],
)
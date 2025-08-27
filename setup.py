from setuptools import setup, find_packages

with open("README.md", 'r', encoding='utf-8') as file:
    long_description=file.read()

    __version__="0.0.0"

    REPO_NAME = "Kidney-disease-classification"
    AUTHOR_USER_NAME = "Saroj94"
    SRC_REPO = "cnnClassifier"
    AUTHOR_EMAIL = "me.sarojrai@gmail.com"

    setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="A python pakage for cnn app",
        long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_urls={
            "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
        },
        package_dir={"": "src"},
        packages=find_packages(where="src"),
        install_requires=[],
    )
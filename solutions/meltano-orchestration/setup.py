from setuptools import find_packages, setup

setup(
    name="meltano_orchestration",
    packages=find_packages(exclude=["meltano_orchestration_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-meltano"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

from setuptools import find_packages, setup

setup(
    name="cli_metrics_video",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tabulate>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "youtube-metrics=application.main:main",
        ],
    },
    python_requires=">=3.12",
)

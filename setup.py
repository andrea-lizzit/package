import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="daignose-inference",
    version="0.1.0",
    author="daignose",
    author_email="team3.makeathon@tum-ai.com",
    description="Inference for dAIgnose",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/a-o-can/daignose",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	scripts=['src/daignose/inference.py'],
	include_package_data=True,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
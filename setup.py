from setuptools import find_packages, setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="RAG MEDICAL CHATBOT",
    version="0.0.1",
    author="Naveen",
    packages=find_packages(),
    install_requires=requirements
)
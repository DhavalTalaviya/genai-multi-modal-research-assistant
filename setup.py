from setuptools import setup, find_packages

setup(
    name="genai_multi_modal_research_assistant",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

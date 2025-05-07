from setuptools import find_packages, setup

setup(
    name="GenAI-MCQ-Generator",          
    version="0.0.1",
    author="Akorikk",
    author_email="abhishekkori601@gmail.com",
    description="A GenAI-based MCQ generator",
    packages=find_packages(),            
    install_requires=[
        "openai",
        "langchain",
        "langchain-community",
        "pandas",
        "PyPDF2",
        "streamlit"
    ],
    package=find_packages()
)



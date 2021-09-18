import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="user_agent_scraper",
    version="1.0.0",
    author="sheepsushis",
    author_email="gmajosi1@gmail.com",
    description="scrape user agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sheepsushis/user_agent_scraper",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
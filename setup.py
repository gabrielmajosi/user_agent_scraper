import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="user_agent_scraper",
    version="0.0.7",
    author="sheepsushis",
    author_email="gmajosi1@gmail.com",
    description="scrape user agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://example.com",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
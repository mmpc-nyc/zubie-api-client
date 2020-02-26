import setuptools

with open("README.md", "r") as file_handler:
    long_description = file_handler.read()

setuptools.setup(
    name = 'schir2',
    version = '1.0',
    author = 'Marek Schir',
    author_email = 'schir2@gmail.com',
    description = 'Zubie API Client',
    long_description = long_description,
    long_description_content_type = 'text/markdown',


)
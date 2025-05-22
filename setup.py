from setuptools import setup, find_packages

setup(
    name='dummy-mongodb-connector',
    version='0.1.0',
    description='A dummy MongoDB connector for demo CI/CD pipeline',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
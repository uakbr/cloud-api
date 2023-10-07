from setuptools import setup, find_packages

setup(
    name='Cloud API Security Checker',
    version='1.0.0',
    url='https://github.com/yourusername/cloud-api-security-checker',
    author='Your Name',
    author_email='your.email@example.com',
    description='A comprehensive tool designed to empower cloud API administrators and developers in ensuring the security of their cloud-based APIs.',
    packages=find_packages(),    
    install_requires=[
        'Flask==1.1.2',
        'SQLAlchemy==1.3.19',
        'psycopg2-binary==2.8.6',
        'boto3==1.16.23',
        'azure-mgmt-resource==10.2.0',
        'google-cloud-storage==1.32.0',
        'requests==2.24.0',
        'oauthlib==3.1.0',
        'PyJWT==1.7.1',
        'pytest==6.1.2',
        'gunicorn==20.0.4'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language ::  :: 3.8',
    ],
)

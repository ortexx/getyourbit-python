from setuptools import setup

setup(name='getyourbit',
	version='0.0.3',
	descpipription='Getyourbit.com client',
	keywords='getyoubit getyoubit.com ip proxy api geolocation cidr',
	url='http://github.com/ortexx/getyourbit-python',
	author='Alexandr Balasyan',
	author_email='mywebstreet@gmail.com',
	license='MIT',
	packages=['getyourbit'],
	install_requires=['requests==2.18.3'],
	python_requires='>=2.7',
	classifiers=[
		'Topic :: Internet',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3'
	]
)
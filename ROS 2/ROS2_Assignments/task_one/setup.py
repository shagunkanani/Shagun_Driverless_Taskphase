from setuptools import find_packages, setup

package_name = 'task_one'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shagunkanani',
    maintainer_email='shagunkanani@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'wheel_publisher = task_one.publisher:main',
		'wheel_subscriber = task_one.subscriber:main',
		'string_publisher = task_one.string_publisher:main',
        	'palindrome_checker = task_one.palindrome_checker:main',
        	'response_node = task_one.response_node:main',
        ],
    },
)

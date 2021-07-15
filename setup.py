from setuptools import setup

setup(
    name='topk_mallows',
    version='0.0.1',    
    description='A python package to for Mallows Model with top-$k$ and complete rankingsu using both Kendall and Hamming distance.',
    url='https://github.com/AhmedBoujaada/top-k-mallows-test',
    author='Ahmed Boujaada and Ekhine Irurozki,
    author_email='aboujaada@bcamath.org',
    license='',
    keywords=['Mallows models', 'Top-k rankings', 'Permutations', 'Kendall\'s tau distance', 'Hamming distance', 'Rankings', 'Complete rankings'],
    packages=['top-k-mallows'],
    install_requires=['numpy',
    ,'scipy', 'itertools'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

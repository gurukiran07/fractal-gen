from distutils.core import setup
setup(
  name = 'FractalGen',        
  packages = ['FractalGen'],   
  version = '0.2',   
  license='MIT',        
  description = 'FractalGen is a python fractal generating library usings IFS',  
  author = 'Manikyala Navaneeth Nanda,Jagata Guru Kiran',                 
  author_email = 'navaneeth.manikyala.17cse@bml.edu.in, jagata.kiran.17cse@bml.edu.in',      
  url = 'https://github.com/Navaneethnanda/FractalGen',  
  download_url = 'https://github.com/Navaneethnanda/FractalGen/archive/refs/tags/v1.0.tar.gz',   
  keywords = ['python3','fractals', 'ifs', 'iterated-function-system', 'deterministic-algorithm', 'random-iteration-algorithm' ],  
  install_requires=[   'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
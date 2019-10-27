from distutils.core import setup
setup(
  name = 'Task4Lib', 
  packages = ['Task4Lib'], 
  version = '0.1', 
  license='MIT', 
  description = 'assignment task 4',   
  author = 'Makoev Arthur',                   
  author_email = 'example@domain.com',      
  url = 'https://github.com/zarond/2019_IT', 
  download_url = 'https://github.com/zarond/2019_IT/archive/v_01.tar.gz', 
  keywords = ['Test', 'Pareto front'],  
  install_requires=[            
          'numpy',
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

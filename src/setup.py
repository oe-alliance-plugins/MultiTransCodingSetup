from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.MultiTransCodingSetup'
setup(name='enigma2-plugin-systemplugins-multitranscodingsetup',
       version='3.0',
       description='Setup multitranscoding',
       package_dir={pkg: 'MultiTransCodingSetup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'setup.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )

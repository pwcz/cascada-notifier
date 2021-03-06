from setuptools import setup

setup(
    name='cascada-notifier',
    version='0.1.1',
    packages=['venv.Lib.site-packages.bs4', 'venv.Lib.site-packages.bs4.tests', 'venv.Lib.site-packages.bs4.builder',
              'venv.Lib.site-packages.get', 'venv.Lib.site-packages.rsa', 'venv.Lib.site-packages.lxml',
              'venv.Lib.site-packages.lxml.html', 'venv.Lib.site-packages.lxml.includes',
              'venv.Lib.site-packages.lxml.isoschematron', 'venv.Lib.site-packages.past',
              'venv.Lib.site-packages.past.tests', 'venv.Lib.site-packages.past.types',
              'venv.Lib.site-packages.past.utils', 'venv.Lib.site-packages.past.builtins',
              'venv.Lib.site-packages.past.translation', 'venv.Lib.site-packages.post', 'venv.Lib.site-packages.numpy',
              'venv.Lib.site-packages.numpy.ma', 'venv.Lib.site-packages.numpy.ma.tests',
              'venv.Lib.site-packages.numpy.doc', 'venv.Lib.site-packages.numpy.fft',
              'venv.Lib.site-packages.numpy.fft.tests', 'venv.Lib.site-packages.numpy.lib',
              'venv.Lib.site-packages.numpy.lib.tests', 'venv.Lib.site-packages.numpy.core',
              'venv.Lib.site-packages.numpy.core.tests', 'venv.Lib.site-packages.numpy.f2py',
              'venv.Lib.site-packages.numpy.f2py.tests', 'venv.Lib.site-packages.numpy.tests',
              'venv.Lib.site-packages.numpy.compat', 'venv.Lib.site-packages.numpy.linalg',
              'venv.Lib.site-packages.numpy.linalg.tests', 'venv.Lib.site-packages.numpy.random',
              'venv.Lib.site-packages.numpy.random.tests', 'venv.Lib.site-packages.numpy.testing',
              'venv.Lib.site-packages.numpy.testing.tests', 'venv.Lib.site-packages.numpy.testing.nose_tools',
              'venv.Lib.site-packages.numpy.distutils', 'venv.Lib.site-packages.numpy.distutils.tests',
              'venv.Lib.site-packages.numpy.distutils.command', 'venv.Lib.site-packages.numpy.distutils.fcompiler',
              'venv.Lib.site-packages.numpy.matrixlib', 'venv.Lib.site-packages.numpy.matrixlib.tests',
              'venv.Lib.site-packages.numpy.polynomial', 'venv.Lib.site-packages.numpy.polynomial.tests',
              'venv.Lib.site-packages.pyaes', 'venv.Lib.site-packages.future', 'venv.Lib.site-packages.future.moves',
              'venv.Lib.site-packages.future.moves.dbm', 'venv.Lib.site-packages.future.moves.html',
              'venv.Lib.site-packages.future.moves.http', 'venv.Lib.site-packages.future.moves.test',
              'venv.Lib.site-packages.future.moves.urllib', 'venv.Lib.site-packages.future.moves.xmlrpc',
              'venv.Lib.site-packages.future.moves.tkinter', 'venv.Lib.site-packages.future.tests',
              'venv.Lib.site-packages.future.types', 'venv.Lib.site-packages.future.utils',
              'venv.Lib.site-packages.future.builtins', 'venv.Lib.site-packages.future.backports',
              'venv.Lib.site-packages.future.backports.html', 'venv.Lib.site-packages.future.backports.http',
              'venv.Lib.site-packages.future.backports.test', 'venv.Lib.site-packages.future.backports.email',
              'venv.Lib.site-packages.future.backports.email.mime', 'venv.Lib.site-packages.future.backports.urllib',
              'venv.Lib.site-packages.future.backports.xmlrpc', 'venv.Lib.site-packages.future.standard_library',
              'venv.Lib.site-packages.public', 'venv.Lib.site-packages.pyasn1', 'venv.Lib.site-packages.pyasn1.type',
              'venv.Lib.site-packages.pyasn1.codec', 'venv.Lib.site-packages.pyasn1.codec.ber',
              'venv.Lib.site-packages.pyasn1.codec.cer', 'venv.Lib.site-packages.pyasn1.codec.der',
              'venv.Lib.site-packages.pyasn1.codec.native', 'venv.Lib.site-packages.pyasn1.compat',
              'venv.Lib.site-packages.certifi', 'venv.Lib.site-packages.urllib3', 'venv.Lib.site-packages.urllib3.util',
              'venv.Lib.site-packages.urllib3.contrib', 'venv.Lib.site-packages.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.urllib3.packages', 'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.telegram',
              'venv.Lib.site-packages.telegram.ext', 'venv.Lib.site-packages.telegram.files',
              'venv.Lib.site-packages.telegram.games', 'venv.Lib.site-packages.telegram.utils',
              'venv.Lib.site-packages.telegram.inline', 'venv.Lib.site-packages.telegram.vendor',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.util',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.contrib',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.packages',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.packages.backports',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.telegram.payment', 'venv.Lib.site-packages.telethon',
              'venv.Lib.site-packages.telethon.tl', 'venv.Lib.site-packages.telethon.tl.types',
              'venv.Lib.site-packages.telethon.tl.custom', 'venv.Lib.site-packages.telethon.tl.functions',
              'venv.Lib.site-packages.telethon.crypto', 'venv.Lib.site-packages.telethon.errors',
              'venv.Lib.site-packages.telethon.events', 'venv.Lib.site-packages.telethon.network',
              'venv.Lib.site-packages.telethon.extensions', 'venv.Lib.site-packages.libfuturize',
              'venv.Lib.site-packages.libfuturize.fixes', 'venv.Lib.site-packages.query_string',
              'venv.Lib.site-packages.libpasteurize', 'venv.Lib.site-packages.libpasteurize.fixes',
              'venv.Lib.site-packages.telethon_generator.parser', 'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.req',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.vcs',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.utils',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.compat',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.models',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.chardet',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.util',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.contrib',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.commands',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.operations'],
    url='https://github.com/pwcz/cascada-notifier',
    license='MIT',
    author='pwcz',
    author_email='',
    description=''
)

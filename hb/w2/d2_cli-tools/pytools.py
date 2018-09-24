# showing off python3 -v output

import random
print(random.randint(1,10))

       # -v     Print a message each time a module is initialized, showing  the
       #        place  (filename  or  built-in module) from which it is loaded.
       #        When given twice, print a message for each file that is checked
       #        for  when searching for a module.  Also provides information on
       #        module cleanup at exit.
# import _frozen_importlib # frozen
# import _imp # builtin
# import sys # builtin
# import '_warnings' # <class '_frozen_importlib.BuiltinImporter'>
# import '_thread' # <class '_frozen_importlib.BuiltinImporter'>
# import '_weakref' # <class '_frozen_importlib.BuiltinImporter'>
# import '_frozen_importlib_external' # <class '_frozen_importlib.FrozenImporter'>
# import '_io' # <class '_frozen_importlib.BuiltinImporter'>
# import 'marshal' # <class '_frozen_importlib.BuiltinImporter'>
# import 'posix' # <class '_frozen_importlib.BuiltinImporter'>
# import _thread # previously loaded ('_thread')
# import '_thread' # <class '_frozen_importlib.BuiltinImporter'>
# import _weakref # previously loaded ('_weakref')
# import '_weakref' # <class '_frozen_importlib.BuiltinImporter'>
# # installing zipimport hook
# import 'zipimport' # <class '_frozen_importlib.BuiltinImporter'>
# # installed zipimport hook
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/__init__.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__init__.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/__init__.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/codecs.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/codecs.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/codecs.cpython-36.pyc'
# import '_codecs' # <class '_frozen_importlib.BuiltinImporter'>
# import 'codecs' # <_frozen_importlib_external.SourceFileLoader object at 0x1013757f0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/aliases.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/aliases.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/aliases.cpython-36.pyc'
# import 'encodings.aliases' # <_frozen_importlib_external.SourceFileLoader object at 0x10138c320>
# import 'encodings' # <_frozen_importlib_external.SourceFileLoader object at 0x101375358>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/utf_8.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/utf_8.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/utf_8.cpython-36.pyc'
# import 'encodings.utf_8' # <_frozen_importlib_external.SourceFileLoader object at 0x101399128>
# import '_signal' # <class '_frozen_importlib.BuiltinImporter'>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/latin_1.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/latin_1.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/encodings/__pycache__/latin_1.cpython-36.pyc'
# import 'encodings.latin_1' # <_frozen_importlib_external.SourceFileLoader object at 0x101399ba8>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/io.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/io.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/io.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/abc.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/abc.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/abc.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_weakrefset.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/_weakrefset.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_weakrefset.cpython-36.pyc'
# import '_weakrefset' # <_frozen_importlib_external.SourceFileLoader object at 0x10139cb00>
# import 'abc' # <_frozen_importlib_external.SourceFileLoader object at 0x10139c198>
# import 'io' # <_frozen_importlib_external.SourceFileLoader object at 0x101399da0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/site.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/site.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/site.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/os.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/os.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/os.cpython-36.pyc'
# import 'errno' # <class '_frozen_importlib.BuiltinImporter'>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/stat.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/stat.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/stat.cpython-36.pyc'
# import '_stat' # <class '_frozen_importlib.BuiltinImporter'>
# import 'stat' # <_frozen_importlib_external.SourceFileLoader object at 0x1014267f0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/posixpath.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/posixpath.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/posixpath.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/genericpath.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/genericpath.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/genericpath.cpython-36.pyc'
# import 'genericpath' # <_frozen_importlib_external.SourceFileLoader object at 0x10142f208>
# import 'posixpath' # <_frozen_importlib_external.SourceFileLoader object at 0x101426eb8>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_collections_abc.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/_collections_abc.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_collections_abc.cpython-36.pyc'
# import '_collections_abc' # <_frozen_importlib_external.SourceFileLoader object at 0x10142f828>
# import 'os' # <_frozen_importlib_external.SourceFileLoader object at 0x101416748>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_sitebuiltins.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/_sitebuiltins.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_sitebuiltins.cpython-36.pyc'
# import '_sitebuiltins' # <_frozen_importlib_external.SourceFileLoader object at 0x101416b38>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sysconfig.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/sysconfig.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sysconfig.cpython-36.pyc'
# import 'sysconfig' # <_frozen_importlib_external.SourceFileLoader object at 0x10141b080>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_sysconfigdata_m_darwin_darwin.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/_sysconfigdata_m_darwin_darwin.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_sysconfigdata_m_darwin_darwin.cpython-36.pyc'
# import '_sysconfigdata_m_darwin_darwin' # <_frozen_importlib_external.SourceFileLoader object at 0x1014793c8>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_osx_support.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/_osx_support.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_osx_support.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/re.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/re.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/re.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/enum.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/enum.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/enum.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/types.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/types.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/types.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/functools.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/functools.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/functools.cpython-36.pyc'
# import '_functools' # <class '_frozen_importlib.BuiltinImporter'>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/collections/__pycache__/__init__.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/collections/__init__.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/collections/__pycache__/__init__.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/operator.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/operator.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/operator.cpython-36.pyc'
# import '_operator' # <class '_frozen_importlib.BuiltinImporter'>
# import 'operator' # <_frozen_importlib_external.SourceFileLoader object at 0x1014fde48>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/keyword.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/keyword.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/keyword.cpython-36.pyc'
# import 'keyword' # <_frozen_importlib_external.SourceFileLoader object at 0x1015120b8>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/heapq.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/heapq.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/heapq.cpython-36.pyc'
# # extension module '_heapq' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_heapq.cpython-36m-darwin.so'
# # extension module '_heapq' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_heapq.cpython-36m-darwin.so'
# import '_heapq' # <_frozen_importlib_external.ExtensionFileLoader object at 0x101512dd8>
# import 'heapq' # <_frozen_importlib_external.SourceFileLoader object at 0x1015128d0>
# import 'itertools' # <class '_frozen_importlib.BuiltinImporter'>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/reprlib.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/reprlib.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/reprlib.cpython-36.pyc'
# import 'reprlib' # <_frozen_importlib_external.SourceFileLoader object at 0x101512eb8>
# import '_collections' # <class '_frozen_importlib.BuiltinImporter'>
# import 'collections' # <_frozen_importlib_external.SourceFileLoader object at 0x1014df5c0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/weakref.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/weakref.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/weakref.cpython-36.pyc'
# import 'weakref' # <_frozen_importlib_external.SourceFileLoader object at 0x1014df9b0>
# import 'functools' # <_frozen_importlib_external.SourceFileLoader object at 0x1014cce48>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/collections/__pycache__/abc.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/collections/abc.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/collections/__pycache__/abc.cpython-36.pyc'
# import 'collections.abc' # <_frozen_importlib_external.SourceFileLoader object at 0x1014d4c18>
# import 'types' # <_frozen_importlib_external.SourceFileLoader object at 0x1014cc160>
# import 'enum' # <_frozen_importlib_external.SourceFileLoader object at 0x101494128>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sre_compile.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/sre_compile.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sre_compile.cpython-36.pyc'
# import '_sre' # <class '_frozen_importlib.BuiltinImporter'>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sre_parse.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/sre_parse.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sre_parse.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sre_constants.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/sre_constants.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/sre_constants.cpython-36.pyc'
# import 'sre_constants' # <_frozen_importlib_external.SourceFileLoader object at 0x10154c1d0>
# import 'sre_parse' # <_frozen_importlib_external.SourceFileLoader object at 0x101537dd8>
# import 'sre_compile' # <_frozen_importlib_external.SourceFileLoader object at 0x1014d4128>
# import '_locale' # <class '_frozen_importlib.BuiltinImporter'>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/copyreg.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/copyreg.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/copyreg.cpython-36.pyc'
# import 'copyreg' # <_frozen_importlib_external.SourceFileLoader object at 0x101556e80>
# import 're' # <_frozen_importlib_external.SourceFileLoader object at 0x101487f98>
# import '_osx_support' # <_frozen_importlib_external.SourceFileLoader object at 0x1014872b0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_bootlocale.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/_bootlocale.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/_bootlocale.cpython-36.pyc'
# import '_bootlocale' # <_frozen_importlib_external.SourceFileLoader object at 0x10148efd0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/__init__.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__init__.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/__init__.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/warnings.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/warnings.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/warnings.cpython-36.pyc'
# import 'warnings' # <_frozen_importlib_external.SourceFileLoader object at 0x10155c978>
# import 'importlib' # <_frozen_importlib_external.SourceFileLoader object at 0x10155c588>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/util.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/util.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/util.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/abc.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/abc.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/abc.cpython-36.pyc'
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/machinery.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/machinery.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/importlib/__pycache__/machinery.cpython-36.pyc'
# import 'importlib.machinery' # <_frozen_importlib_external.SourceFileLoader object at 0x1015740b8>
# import 'importlib.abc' # <_frozen_importlib_external.SourceFileLoader object at 0x1015689b0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/contextlib.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/contextlib.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/contextlib.cpython-36.pyc'
# import 'contextlib' # <_frozen_importlib_external.SourceFileLoader object at 0x101574d30>
# import 'importlib.util' # <_frozen_importlib_external.SourceFileLoader object at 0x10155cfd0>
# # possible namespace for /Users/kimberlyvnguyen/anaconda3/lib/python3.6/site-packages/mpl_toolkits
# import 'site' # <_frozen_importlib_external.SourceFileLoader object at 0x1013af470>
# Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
# [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/random.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/random.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/random.cpython-36.pyc'
# # extension module 'math' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/math.cpython-36m-darwin.so'
# # extension module 'math' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/math.cpython-36m-darwin.so'
# import 'math' # <_frozen_importlib_external.ExtensionFileLoader object at 0x1019a2da0>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/hashlib.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/hashlib.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/hashlib.cpython-36.pyc'
# # extension module '_hashlib' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_hashlib.cpython-36m-darwin.so'
# # extension module '_hashlib' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_hashlib.cpython-36m-darwin.so'
# import '_hashlib' # <_frozen_importlib_external.ExtensionFileLoader object at 0x1019ac080>
# # extension module '_blake2' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_blake2.cpython-36m-darwin.so'
# # extension module '_blake2' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_blake2.cpython-36m-darwin.so'
# import '_blake2' # <_frozen_importlib_external.ExtensionFileLoader object at 0x1019ac780>
# # extension module '_sha3' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_sha3.cpython-36m-darwin.so'
# # extension module '_sha3' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_sha3.cpython-36m-darwin.so'
# import '_sha3' # <_frozen_importlib_external.ExtensionFileLoader object at 0x1019ac898>
# import 'hashlib' # <_frozen_importlib_external.SourceFileLoader object at 0x1019a7630>
# # /Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/bisect.cpython-36.pyc matches /Users/kimberlyvnguyen/anaconda3/lib/python3.6/bisect.py
# # code object from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/__pycache__/bisect.cpython-36.pyc'
# # extension module '_bisect' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_bisect.cpython-36m-darwin.so'
# # extension module '_bisect' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_bisect.cpython-36m-darwin.so'
# import '_bisect' # <_frozen_importlib_external.ExtensionFileLoader object at 0x1019a7f28>
# import 'bisect' # <_frozen_importlib_external.SourceFileLoader object at 0x1019a7ac8>
# # extension module '_random' loaded from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_random.cpython-36m-darwin.so'
# # extension module '_random' executed from '/Users/kimberlyvnguyen/anaconda3/lib/python3.6/lib-dynload/_random.cpython-36m-darwin.so'
# import '_random' # <_frozen_importlib_external.ExtensionFileLoader object at 0x1019a7a20>
# import 'random' # <_frozen_importlib_external.SourceFileLoader object at 0x10199e518>
# 2
# # clear builtins._
# # clear sys.path
# # clear sys.argv
# # clear sys.ps1
# # clear sys.ps2
# # clear sys.last_type
# # clear sys.last_value
# # clear sys.last_traceback
# # clear sys.path_hooks
# # clear sys.path_importer_cache
# # clear sys.meta_path
# # clear sys.__interactivehook__
# # clear sys.flags
# # clear sys.float_info
# # restore sys.stdin
# # restore sys.stdout
# # restore sys.stderr
# # cleanup[2] removing builtins
# # cleanup[2] removing sys
# # cleanup[2] removing _frozen_importlib
# # cleanup[2] removing _imp
# # cleanup[2] removing _warnings
# # cleanup[2] removing _thread
# # cleanup[2] removing _weakref
# # cleanup[2] removing _frozen_importlib_external
# # cleanup[2] removing _io
# # cleanup[2] removing marshal
# # cleanup[2] removing posix
# # cleanup[2] removing zipimport
# # cleanup[2] removing encodings
# # destroy encodings
# # cleanup[2] removing codecs
# # cleanup[2] removing _codecs
# # cleanup[2] removing encodings.aliases
# # cleanup[2] removing encodings.utf_8
# # cleanup[2] removing _signal
# # cleanup[2] removing __main__
# # destroy __main__
# # cleanup[2] removing encodings.latin_1
# # cleanup[2] removing io
# # destroy io
# # cleanup[2] removing abc
# # cleanup[2] removing _weakrefset
# # destroy _weakrefset
# # cleanup[2] removing site
# # destroy site
# # cleanup[2] removing os
# # cleanup[2] removing errno
# # cleanup[2] removing stat
# # cleanup[2] removing _stat
# # cleanup[2] removing posixpath
# # cleanup[2] removing genericpath
# # cleanup[2] removing os.path
# # cleanup[2] removing _collections_abc
# # cleanup[2] removing _sitebuiltins
# # cleanup[2] removing sysconfig
# # destroy sysconfig
# # cleanup[2] removing _sysconfigdata_m_darwin_darwin
# # destroy _sysconfigdata_m_darwin_darwin
# # cleanup[2] removing _osx_support
# # destroy _osx_support
# # cleanup[2] removing re
# # cleanup[2] removing enum
# # cleanup[2] removing types
# # cleanup[2] removing functools
# # cleanup[2] removing _functools
# # cleanup[2] removing collections
# # cleanup[2] removing operator
# # destroy operator
# # cleanup[2] removing _operator
# # cleanup[2] removing keyword
# # destroy keyword
# # cleanup[2] removing heapq
# # cleanup[2] removing _heapq
# # cleanup[2] removing itertools
# # cleanup[2] removing reprlib
# # destroy reprlib
# # cleanup[2] removing _collections
# # cleanup[2] removing weakref
# # destroy weakref
# # cleanup[2] removing collections.abc
# # cleanup[2] removing sre_compile
# # cleanup[2] removing _sre
# # cleanup[2] removing sre_parse
# # cleanup[2] removing sre_constants
# # destroy sre_constants
# # cleanup[2] removing _locale
# # cleanup[2] removing copyreg
# # cleanup[2] removing _bootlocale
# # destroy _bootlocale
# # cleanup[2] removing importlib
# # destroy importlib
# # cleanup[2] removing importlib._bootstrap
# # cleanup[2] removing importlib._bootstrap_external
# # cleanup[2] removing warnings
# # cleanup[2] removing importlib.util
# # cleanup[2] removing importlib.abc
# # cleanup[2] removing importlib.machinery
# # cleanup[2] removing contextlib
# # destroy contextlib
# # cleanup[2] removing mpl_toolkits
# # destroy mpl_toolkits
# # cleanup[2] removing sphinxcontrib
# # destroy sphinxcontrib
# # cleanup[2] removing random
# # destroy random
# # cleanup[2] removing math
# # cleanup[2] removing hashlib
# # destroy hashlib
# # cleanup[2] removing _hashlib
# # cleanup[2] removing _blake2
# # cleanup[2] removing _sha3
# # cleanup[2] removing bisect
# # cleanup[2] removing _bisect
# # cleanup[2] removing _random
# # destroy _sha3
# # destroy _blake2
# # destroy zipimport
# # destroy _signal
# # destroy _sitebuiltins
# # destroy errno
# # destroy posixpath
# # destroy _stat
# # destroy genericpath
# # destroy stat
# # destroy os
# # destroy re
# # destroy enum
# # destroy sre_compile
# # destroy copyreg
# # destroy _bisect
# # destroy _functools
# # destroy heapq
# # destroy collections.abc
# # destroy _operator
# # destroy _heapq
# # destroy _collections
# # destroy collections
# # destroy sre_parse
# # destroy _sre
# # destroy _locale
# # destroy importlib.util
# # destroy importlib.abc
# # destroy functools
# # destroy types
# # destroy warnings
# # destroy importlib.machinery
# # destroy abc
# # destroy _collections_abc
# # destroy math
# # destroy _hashlib
# # destroy itertools
# # destroy bisect
# # destroy _random
# # cleanup[3] wiping _frozen_importlib
# # destroy _frozen_importlib_external
# # cleanup[3] wiping _imp
# # cleanup[3] wiping _warnings
# # cleanup[3] wiping _thread
# # cleanup[3] wiping _weakref
# # cleanup[3] wiping _io
# # cleanup[3] wiping marshal
# # cleanup[3] wiping posix
# # cleanup[3] wiping codecs
# # cleanup[3] wiping _codecs
# # cleanup[3] wiping encodings.aliases
# # cleanup[3] wiping encodings.utf_8
# # cleanup[3] wiping encodings.latin_1
# # cleanup[3] wiping importlib._bootstrap
# # cleanup[3] wiping sys
# # cleanup[3] wiping builtins

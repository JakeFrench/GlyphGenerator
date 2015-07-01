from distutils.core import setup
import py2exe
import glob

opts = {'py2exe': { "includes" : ["sip", "PyQt4","matplotlib.backends", "matplotlib.backends.backend_qt4agg","matplotlib.figure","pylab", "numpy","matplotlib.backends.backend_tkagg"],'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo','_cocoaagg','_fltkagg', '_gtk', '_gtkcairo', ],'dll_excludes': ['libgdk-win32-2.0-0.dll','libgobject-2.0-0.dll']}}

data_files = [(r'mpl-data', glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\*.*')),(r'mpl-data',[r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),(r'mpl-data\images',glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\images\*.*')),(r'mpl-data\fonts',glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\fonts\*.*'))]


setup(console=["main.pyw"], options=opts, data_files=data_files)

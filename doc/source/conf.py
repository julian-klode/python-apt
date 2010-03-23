# -*- coding: utf-8 -*-
#
# python-apt documentation build configuration file, created by
# sphinx-quickstart on Wed Jan  7 17:04:36 2009.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed
# automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import os
import glob
import sys

# Find the path to the built apt_pkg and apt_inst extensions
if os.path.exists("../../build"):
    version = '.'.join(str(x) for x in sys.version_info[:2])
    for apt_pkg_path in glob.glob('../../build/lib*%s/*.so' % version):
        sys.path.insert(0, os.path.abspath(os.path.dirname(apt_pkg_path)))
        try:
            import apt_pkg
        except ImportError, exc:
            # Not the correct version
            sys.stderr.write('W: Ignoring error %s\n' % exc)
            sys.path.pop(0)
        else:
            sys.stdout.write('I: Found apt_pkg.so in %s\n' % sys.path[0])
            # Hack: Disable compatibility mode
            apt_pkg._COMPAT_0_7 = 0
            break



# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.intersphinx', 'sphinx.ext.todo']
intersphinx_mapping = {'http://docs.python.org/': None}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
#master_doc = 'contents'

# General information about the project.
project = u'python-apt'
copyright = u'2009-2010, Julian Andres Klode <jak@debian.org>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

try:
    release=os.environ['DEBVER']
except KeyError:
    from subprocess import Popen, PIPE
    p1 = Popen(["dpkg-parsechangelog", "-l../../debian/changelog"],
               stdout=PIPE)
    p2 = Popen(["sed", "-n", 's/^Version: //p'], stdin=p1.stdout, stdout=PIPE)
    release = p2.communicate()[0]

# Handle the alpha release scheme
if int(release.split("~")[0].split(".")[2]) >= 90:
    version_s = release.split("~")[0].split(".")[:3]
    # Set the version to 0.X.100 if the release is 0.X.9Y (0.7.90 => 0.7.100)
    # Use
    #  version_s[1] = str(int(version_s[1]) + 1)
    #  version_s[2] = "0"
    # if the version of a 0.X.9Y release should be 0.X+1.0 (0.7.90=>0.8)
    version_s[2] = "100"
    version = '.'.join(version_s)
    del version_s
else:
    version = '.'.join(release.split("~")[0].split('.')[:3])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {"index": "indexcontent.html"}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'python-aptdoc'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source index, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('contents', 'python-apt.tex', ur'python-apt Documentation',
   ur'Julian Andres Klode <jak@debian.org>', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

todo_include_todos = True

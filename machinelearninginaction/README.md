# python
<pre>
	import feedparser
	import numpy
	import re
	import setup
</pre>
<pre>
	https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
</pre>
<pre>
	https://matplotlib.org/api/
	https://matplotlib.org/contents.html
</pre>

<pre>
	<u>
	Python is not installed as a framework. The Mac OS X backend will not be able t
	</u>
Problem Cause In mac os image rendering back end of matplotlib (what-is-a-backend to render using the API of Cocoa by default). There is Qt4Agg and GTKAgg and as a back-end is not the default. Set the back end of macosx that is differ compare with other windows or linux os.

I resolve this issue following ways:

I assume you have installed the pip matplotlib, there is a directory in you root called ~/.matplotlib.
Create a file ~/.matplotlib/matplotlibrc there and add the following code: backend: TkAgg
From this link you can try different diagram.

</pre>

<pre>
	pip install matplotlib
</pre>

<pre>
	https://github.com/pbharrin/machinelearninginaction
</pre>

<pre>
	https://docs.scipy.org/doc/
</pre>

python -V
Python 3.6.1
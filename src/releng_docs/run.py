import os
import sys
import livereload

HERE = os.path.dirname(__file__)

os.system('/run/current-system/sw/bin/make html')

server = livereload.Server()
server.watch(
    os.path.join(HERE, '*.rst'),
    livereload.shell('make html'),
)
server.serve(
    port=os.environ.get('PORT', 5000),
    host=os.environ.get('HOST', 'localhost'),
    root=os.path.join(HERE, 'build/html'),
)

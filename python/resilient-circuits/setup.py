# Resilient Systems, Inc. ("Resilient") is willing to license software
# or access to software to the company or entity that will be using or
# accessing the software and documentation and that you represent as
# an employee or authorized agent ("you" or "your") only on the condition
# that you accept all of the terms of this license agreement.
#
# The software and documentation within Resilient's Development Kit are
# copyrighted by and contain confidential information of Resilient. By
# accessing and/or using this software and documentation, you agree that
# while you may make derivative works of them, you:
#
# 1)  will not use the software and documentation or any derivative
#     works for anything but your internal business purposes in
#     conjunction your licensed used of Resilient's software, nor
# 2)  provide or disclose the software and documentation or any
#     derivative works to any third party.
#
# THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

setup(
    name='resilient_circuits',
    version='24.0.1',  # also __version__ in __init__.py
    url='https://www.resilientsystems.com/',
    license='Resilient License',
    author='Resilient',
    install_requires=[
      'stomp.py>=4.0.12',
      'requests>=2.6.0',
      'circuits',
      'pytz',
      'keyring',
      'jinja2'
    ],
    author_email='support@resilientsystems.com',
    description='Resilient Circuits Framework for Custom Apps',
    long_description=long_description,
    packages=['resilient_circuits'],
    package_dir={'resilient_circuits': 'resilient_circuits'},
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
    ]
)

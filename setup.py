#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='threepy',
    version='0.0.1',
    description='Python 3D library',
    author='stemkoski',
    url='https://github.com/stemkoski/three.py',
    packages=[
        'threepy', 'threepy.cameras', 'threepy.core', 'threepy.geometry',
        'threepy.helpers', 'threepy.lights', 'threepy.material',
        'threepy.mathutils'
    ],
    include_package_data=True,
)

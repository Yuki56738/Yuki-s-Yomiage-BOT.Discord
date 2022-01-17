#!/bin/bash

rm -Rv __pycache__
git add .
git rm -r __pycache__/
git commit -m "auto commit"
git push


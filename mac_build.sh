#!/bin/bash

set -e

rm -rf mochi.app
pyinstaller --noconfirm --windowed --name mochi \
  src/mochi/main.py

rm -rf ./build
rm -rf ./mochi.spec
mv ./dist/mochi.app ./
rm -rf ./dist
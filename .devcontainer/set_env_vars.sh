#!/bin/bash

set -a
source .devcontainer/.env.devcontainer
DBT_PROFILES_DIR=$PWD
set +a

if ! grep -Fxq "$(head -n 1 .devcontainer/.env.devcontainer)" ~/.bashrc; then
  cat .devcontainer/.env.devcontainer >> ~/.bashrc
fi

echo "DBT PROFILES DIR: $DBT_PROFILES_DIR"

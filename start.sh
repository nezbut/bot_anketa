#!/bin/bash

script_path=$(readlink -f $0)

project_path="${script_path::-8}"
path="$project_path/bot_anketa"

export PYTHONPATH=$path

cd $project_path

poetry run tgbot

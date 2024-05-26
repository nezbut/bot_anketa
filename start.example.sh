#!/bin/bash

script_path=$(readlink -f $0)

project_path="${script_path::-8}"
path="$project_path/bot_anketa"

export PYTHONPATH=$path

cd $project_path

export TG_BOT_TOKEN="TG BOT TOKEN" # you can get it from @BotFather
export DATABASE_URI="postgresql+asyncpg://USERNAME:PASSWORD@localhost:5433/bot_anketa"
export KV_DATABASE_URI="redis://localhost:6379/4"

poetry run tgbot

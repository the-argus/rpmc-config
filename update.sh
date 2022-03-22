#!/bin/bash
INSTANCE_PATH="$HOME/.local/share/multimc/instances/RPMC/.minecraft/config"
rsync -av --exclude=".*" --exclude="exclude_*" ./* $INSTANCE_PATH

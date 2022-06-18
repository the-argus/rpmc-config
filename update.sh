#!/bin/bash
INSTANCE_PATH="$HOME/.local/share/multimc/instances/rpmc-client/.minecraft/config"
rsync -av --exclude=".*" --exclude="exclude_*" ./* $INSTANCE_PATH

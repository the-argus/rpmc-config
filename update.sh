#!/bin/bash
INSTANCE_PATH="$HOME/.local/share/multimc/instances/Ian's RPMC/.minecraft/config"
rsync -av --exclude=".*" ./* $INSTANCE_PATH

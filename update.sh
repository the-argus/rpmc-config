#!/bin/bash
rsync -av --exclude=".*" /home/argus/Desktop/Minecraft/Modpacks/RPMC/config-changes/* "/home/argus/.local/share/multimc/instances/compat testing/.minecraft/config"

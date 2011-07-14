#!/bin/bash
# Proper header for a Bash script.

# This script replaces the antiX Linux IceWM menu updating script.

# NOTE: The replacement /usr/local/bin/icewm-xdg-menu script
# ONLY adds comments and is otherwise identical to the original
# script for antiX Linux.
echo "Replacing the /usr/local/bin/icewm-xdg-menu script"
rm /usr/local/bin/icewm-xdg-menu
cp usr_local_bin/icewm-xdg-menu /usr/local/bin/
chown root:root /usr/local/bin/icewm-xdg-menu

# Replacing the configuration file for arranging menu entries
echo "Replacing the /etc/xdg/menus/lxde-applications.menu file"
rm /etc/xdg/menus/lxde-applications.menu
cp etc_xdg_menus/lxde-applications.menu /etc/xdg/menus/
chown root:root /etc/xdg/menus/lxde-applications.menu

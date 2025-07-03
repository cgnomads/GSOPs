#!/bin/bash

# Script intended to be sourced, e.g. "source scripts/houdini_env.sh"

# Determine the platform
case "$(uname -s)" in
    Darwin)
        HOUDINI_BASE="/Applications/Houdini/Houdini20.5.278/Frameworks/Houdini.framework/Versions/Current/Resources"
        ;;
    Linux)
        HOUDINI_BASE="/opt/houdini/20.5.278"
        ;;
    CYGWIN*|MINGW32*|MSYS*|MINGW*)
        HOUDINI_BASE="C:/Program Files/SideFX/Houdini 20.5.278"
        ;;
    *)
        echo "Unsupported OS"
        exit 1
        ;;
esac

# Source the Houdini setup script
cd "$HOUDINI_BASE"
source houdini_setup
cd "-"

# Optionally export other convenient environment variables
# export HOUDINI_TOOLKIT="$HOUDINI_BASE/toolkit"
# export HOUDINI_INCLUDE="$HOUDINI_TOOLKIT/include"
# export HOUDINI_PROGRAM="$HOUDINI_BASE/Houdini FX 20.5.278.app/Contents/MacOS/houdini"

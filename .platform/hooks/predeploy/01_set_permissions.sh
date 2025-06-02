#!/bin/bash
# Make sure scripts in .platform/hooks directory are executable
chmod +x .platform/hooks/predeploy/*.sh
chmod +x .platform/hooks/postdeploy/*.sh 2>/dev/null || true

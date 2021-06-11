#!/usr/bin/env bash
sed -e "s|@@BASE_IMAGE@@|$1|g" dockerfile.tmpl > Dockerfile
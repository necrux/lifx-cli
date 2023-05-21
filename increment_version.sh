#!/usr/bin/env bash
# One stop shop for incrementing the lifx-cli version.

declare -l ANSWER
NEW_VERSION=$1
CURRENT_VERSION=$(git describe --tags --abbrev=0)
FILES=('pyproject.toml'
       'src/lifx/lifx.py')

function is_command {
    local FAILURE
  
    for program in $@; do
        hash ${program} > /dev/null 2>&1
        if [ $? != 0 ]; then
            echo "Command not found: ${program}" >&2
            FAILURE='true'
        fi
    done
  
    if [ ! -z ${FAILURE} ]; then
        exit 127
    fi
}

function err {
    local EXIT=$1
    shift 1
    echo "[$(date +'%Y-%m-%d %H:%M:%S')]: $@" >&2
    exit ${EXIT}
}

function increment_version {
    for file in ${FILES[@]}; do
        gawk -i inplace \
             -F'"' \
             -v VER=${NEW_VERSION} \
             'BEGIN{IGNORECASE=1} /^version/ {sub($2,VER)}; {print $0}' \
             ${file}
        git add ${file}
    done
    
    git commit -m "Bumping version: ${NEW_VERSION}"
    git push origin main
    git tag v${NEW_VERSION}
    git push origin --tags
}

# Input validation.
if [ -z ${NEW_VERSION} ]; then
    err 5 "Must supply a new version number."
fi

if ! echo ${NEW_VERSION} | grep -q "^[0-9]*\.[0-9]*\.[0-9]*$"; then
    err 6 "New version number is in the wrong format. Must be: <MAJOR>.<MINOR>.<PATCH>"
fi

is_command gawk

echo "Current Tagged Version: ${CURRENT_VERSION}"
read -p "Are you certain that you want to increment to version ${NEW_VERSION}? y/N " ANSWER

if [ "${ANSWER}" == "y" ]; then
    increment_version
fi

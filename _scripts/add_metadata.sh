#!/bin/bash

# Make sure we exit(1) if there is an error
set -e


add_metadata(){
  added=`git log --format="%ai" --reverse $1 | head -1 | cut -d " " -f 1`
  modified=`git log --format="%ai" $1 | head -1 | cut -d " " -f 1`

  printf "\nRegistryEntryAdded: \"$added\"\n" >>$1
  printf "RegistryEntryLastModified: \"$modified\"\n" >>$1

}

export -f add_metadata

ls datasets |
    xargs -t -I{} -P10 bash -c 'add_metadata datasets/"$@"' _ {}

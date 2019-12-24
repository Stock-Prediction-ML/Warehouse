#!/bin/bash

# yaml parser

# samle yaml content
# ------------------
# mykey:
#    myotherkey: test
#
# how to use
# ----------
# $ config=$(yaml config.yml mykey.myotherkey)
#
# output
# --------
# $ echo $config
# $ test

function yaml() {
    hashdot=$(gem list hash_dot);
    if ! [ "$hashdot" != "" ]; then sudo gem install "hash_dot" ; fi
    if [ -f $1 ];then
        cmd=" Hash.use_dot_syntax = true; hash = YAML.load(File.read('$1'));";
        if [ "$2" != "" ] ;then 
            cmd="$cmd puts hash.$2;"
        else
            cmd="$cmd puts hash;"
        fi
        ruby  -r yaml -r hash_dot <<< $cmd;
    fi
}
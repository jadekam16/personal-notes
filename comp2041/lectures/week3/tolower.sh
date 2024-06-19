if test $# = 0
then
    echo "Usage $0: <files>" 1>&2
    exit 1
fi

for filename in "$@"
do
    new_filename=$(
        echo "$filename"|
        tr '[:upper:]' '[:lower:]'
        )

    test "$filename" = "$new_filename" &&       # test if old file name is the same as the new filename
        continue

    if test -r "$new_filename"                  # test if new filename already exists in the directory
    then
        echo "$0: $new_filename exists" 1>&2
    elif test -e "$filename"
    then
        mv -- "$filename" "$new_filename"       # -- means anything after this is not an option i.e., if the filename is -i. 
    else
        echo "$0: $filename not found" 1>&2
    fi

done
#!/usr/bin/env bash

infile="$1"
outfile="out_file"

# test if infile.out exists, bitbucket it if it does
if [[ -f "$outfile" ]]; then
  cat /dev/null > "$outfile"
fi

urlencode() {
  temp=$(printf '%s' "$1" | curl -Gso /dev/null -w %{url_effective} --data-urlencode @- "" | cut -c 3-)
  echo $temp
}

shorten_url() {
  response=$(curl -s -XPOST -d "url=$1" 'https://cleanuri.com/api/v1/shorten' | jq -r '.result_url')
  echo $response
}

while IFS= read -r line; do
  encoded_url=$(urlencode $line)
  # echo $encoded_url
  short_url=$(shorten_url $encoded_url)
  echo $short_url >> $outfile
done < $infile


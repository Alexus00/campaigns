#!/bin/bash
# usage: gdl.sh <drive_id> <name>  -> src/<name>.mp4 + wav/<name>.pcm (16k mono)
C=$(cd "$(dirname "$0")/.." && pwd); id=$1; n=$2; ck=$(mktemp)
page=$(curl -s -L -m 60 -c $ck "https://drive.google.com/uc?id=$id&export=download")
uuid=$(echo "$page" | grep -o 'name="uuid" value="[^"]*"' | sed 's/.*value="//;s/"//')
url="https://drive.usercontent.google.com/download?id=$id&export=download&confirm=t&uuid=$uuid"
for i in 1 2 3 4; do curl -s -L -C - -b $ck --retry 5 -o $C/src/$n.mp4 "$url" && break; sleep $((2**i)); done
ffmpeg -v error -y -i $C/src/$n.mp4 -vn -ac 1 -ar 16000 -f s16le $C/wav/$n.pcm
echo "$n $(ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of csv=p=0 $C/src/$n.mp4 | tr '\n' ' ')"

file="$1.pdf"
python3 compile.py $1
open -a /Applications/Preview.app/ $file


if [ $# -eq 0 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

dir="$1"

if [ ! -d "$dir" ]; then
  echo "$dir is not a directory"
  exit 1
fi

csv_files=$(ls "$dir"/*.csv)

if [ -z "$csv_files" ]; then
  echo "No CSV files found in $dir"
  exit 1
fi

for file in $csv_files
do
  line_count=$(wc -l "$file" | awk '{print $1}')
  echo "The file $file has $line_count lines."
done

#! /usr/bin/env sh

echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

# replace code in httptools_impl.py of uvicorn to get response_headers into scope
file=$(find / -name "httptools_impl.py")
awk '/headers = self\.default_headers/ {$0=$0" ; self.scope[\"response_headers\"] = headers"} 1' $file > /httptools_impl.py
cp /httptools_impl.py $file

# remove favicon line , this is a bug in fastapi==0.60.1 using external favicon link https://fastapi.tiangolo.com/img/favicon.png
file=$(find / -name "docs.py")
sed '/link rel=\"shortcut icon\"/c\    ' $file > /docs.py
#sed '/link rel=\"shortcut icon\"/c\    <link rel="shortcut icon" href="/">' $file > /docs.py
cp /docs.py $file
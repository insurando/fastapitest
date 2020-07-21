#! /usr/bin/env sh

echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

# replace code in httptools_impl.py of uvicorn to get response_headers into scope
file=$(find / -name "httptools_impl.py")
awk '/headers = self\.default_headers/ {$0=$0" ; self.scope[\"response_headers\"] = headers"} 1' $file > /httptools_impl.py
cp /httptools_impl.py $file
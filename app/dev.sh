npx tailwindcss -i ./src/static/css/input.css -o ./src/static/css/output.css --minify
flask --app src/app --debug run
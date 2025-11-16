#!/bin/sh

echo "Content-Type: text/html"
echo ""

STATUS=$(wget -q -O - http://127.0.0.1/server-status)

LINE=$(echo "$STATUS" | while read L; do
    case "$L" in
        *Server-Status*\(*)
            echo "$L"
            break
        ;;
    esac
done)

IP=$(echo "$LINE" | cut -d "(" -f 2 | cut -d ":" -f 2 | cut -d ")" -f 1)

cat <<EOF
<html>
<body>
<h1>Container IP: $IP</h1>
</body>
</html>
EOF


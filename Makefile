
test-e2e:
docker compose -f docker-compose.test.yml up -d --build
docker compose -f docker-compose.test.yml exec web python manage.py generate_data
uv run pytest tests/
docker compose -f docker-compose.test.yml down -v

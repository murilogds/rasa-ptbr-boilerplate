first-run:
	cd docker && ./build-base.sh
	make train
	docker-compose up bot

train: 
	docker build . -f docker/coach.Dockerfile -t botcoach:latest
	docker-compose build bot

run:
	docker-compose up bot

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf docs/_build


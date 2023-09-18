bulk_update:
	python manage.py bulk_update

populate_dict:
	python manage.py populate_dict

# supervisor:
# 	sudo supervisorctl restart backend

run:
	python manage.py runserver 8000

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate


commit_name := $(filter-out $@,$(MAKECMDGOALS))

push:
	git add .
	git commit -m "$(commit_name)"
	git push origin oqdev

pull:
	git pull origin oqdev

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt


merge:
	git checkout main
	git merge oqdev
	git push origin main
	git checkout oqdev

createsuperuser:
	python3 manage.py createsuperuser --username admin --email oqdevpy@gmail.com
	

app_name := $(word 2, $(MAKECMDGOALS))

.PHONY: app-api

app-api:
	@cd $(app_name)
	@mkdir -p $(app_name)/api/v1
	@touch $(app_name)/api/__init__.py
	@touch $(app_name)/api/v1/__init__.py
	@touch $(app_name)/api/v1/urls.py
	@touch $(app_name)/api/v1/views.py
	@touch $(app_name)/api/v1/serializers.py
	@touch $(app_name)/api/v1/permissions.py

translation:
	python manage.py makemessages -l ru
	python manage.py makemessages -l en
	python manage.py makemessages -l uz
	python manage.py compilemessages
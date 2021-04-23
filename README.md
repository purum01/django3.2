## Chapter01
* [파이썬 공식 사이트](https://www.python.org/downloads/)
* [파이썬 3.9 다운로드](https://www.python.org/downloads/release/python-394/)
* [Visual Studio Code](https://code.visualstudio.com/) 
* [장고의 공식 사이트](https://www.djangoproject.com/)
* [장고 API 문서](https://docs.djangoproject.com/en/3.2/ref/)
* [장고 소스 저장소](https://github.com/django/django)

## Chapter02
* [converters.py 코드](https://github.com/django/django/blob/main/django/urls/converters.py)

## Chapter03
* [django DB backends](https://github.com/django/django/tree/master/django/db/backends )

## Chapter04
* [장고 템플릿 문서](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/ )
* [Date/Time format 문자](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date )

## Chapter05
* [DB Browser for SQLite](https://sqlitebrowser.org/)
* [Field types](https://docs.djangoproject.com/ko/3.2/ref/models/fields/#model-field-types)
* [Field options](https://docs.djangoproject.com/ko/3.2/ref/models/fields/#common-model-field-options)
* [Relationship fields](https://docs.djangoproject.com/ko/3.2/ref/models/fields/#module-django.db.models.fields.related)


## Chapter06
* [Manager](https://docs.djangoproject.com/en/3.2/topics/db/managers/)
* [QuerySet](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)
* [Field lookups](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)

## Chapter07
* [admin site 참조 문서](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
* [admin 앱 소스](https://github.com/django/django/tree/master/django/contrib/admin)
* [ModelAdmin 소스](https://github.com/django/django/blob/master/django/contrib/admin/options.py)


## Chapter08
* [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/3.2/ref/csrf/)
* [HttpRequest](https://docs.djangoproject.com/en/3.2/ref/request-response/#httprequest-objects)
* [HttpResponse](https://docs.djangoproject.com/en/3.2/ref/request-response/#httpresponse-objects)
* [QueryDict](https://docs.djangoproject.com/en/3.2/ref/request-response/#querydict-objects)
* [Django Form](https://docs.djangoproject.com/en/3.2/ref/forms/fields/)
* [ModelForm](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)
* [Form and field validation](https://docs.djangoproject.com/en/3.2/ref/forms/validation/)
* [Validating the model instance](https://docs.djangoproject.com/en/3.2/ref/models/instances/#validating-objects)
* [Built-in validators](https://docs.djangoproject.com/en/3.2/ref/validators/#built-in-validators)

## Chapter09
* [Class-based view](https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/)
* [Built-in class-based generic views](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/)
* [View](https://github.com/django/django/blob/master/django/views/generic/base.py)
* [ListView](https://github.com/django/django/blob/3.2/django/views/generic/list.py) 
* [DetailView](https://github.com/django/django/blob/3.2/django/views/generic/detail.py)
* [Edit View](https://github.com/django/django/blob/3.2/django/views/generic/edit.py)

## Chapter10
* [Managing static files](https://docs.djangoproject.com/en/3.2/howto/static-files/)
* [Deploying static files](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/)
* [개발서버에서 media 파일 서빙](https://github.com/django/django/blob/master/django/conf/urls/static.py)

## Chapter11
* [auth앱 소스](https://github.com/django/django/tree/master/django/contrib/auth)
* [auth앱 환경 변수](https://github.com/django/django/blob/master/django/conf/global_settings.py#L499)

* [signals](https://docs.djangoproject.com/en/3.2/ref/signals/)
* [apps](https://docs.djangoproject.com/en/3.2/ref/applications/)
* [email](https://docs.djangoproject.com/en/3.2/topics/email/)

* [All authentication views](https://docs.djangoproject.com/en/3.2/topics/auth/default/#all-authentication-views)
* [auth 소스 코드](https://github.com/django/django/tree/main/django/contrib/auth)

## Chapter12
### 세션 소스 코드
* [session앱](https://github.com/django/django/tree/main/django/contrib/sessions)
* [SessionMiddleware](https://github.com/django/django/blob/3.2/django/contrib/sessions/middleware.py)
* [SessionStore](https://github.com/django/django/blob/main/django/contrib/sessions/backends/db.py)
* [MiddlewareMixin](https://github.com/django/django/blob/3.2/django/utils/deprecation.py#LC82)
###
* [How to use sessions](https://docs.djangoproject.com/en/3.2/topics/http/sessions/)
* [세션 환경 변수](https://docs.djangoproject.com/en/3.2/ref/settings/#sessions)
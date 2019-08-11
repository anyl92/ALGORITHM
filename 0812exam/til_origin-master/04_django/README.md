# First django

## First project

* 가상(독립)환경 생성 및 django 설치

  ```sh
  $ pwd
  ~/TIL/04_django
  $ py -m venv venv  # 04 django 에서 사용할 독립 Python 환경을 만든다.
  $ pip install django
  $ code .  # vscode 로 열기
  ```

* django 프로젝트 만들기 & 프로젝트 폴더 이름 바꾸기

  ```sh
  $ source ./venv/Scripts/activate  # vscode 에서 python: Select interpreter 로 venv 선택
  (venv)
  $ django-admin startproject first_project
  (venv)
  $ mv first_project FIRST_PROJECT
  (venv)
  $ cd FIRST_PROJECT
  (venv)
$ ls
  first_project/ manage.py
  ```
  
* Django 강의에서의 용어 설명

  | 이름                        | 설명                                                         |
  | --------------------------- | ------------------------------------------------------------ |
  | 프로젝트 루트(Project ROOT) | 프로젝트 폴더의 최상단. (`manage.py` 가 위치한 곳)           |
  | 마스터 앱(Master APP)       | 프로젝트 이름과 같은 이름의 폴더. 프로젝트 루트에 위치한다. 프로젝트 생성시 자동으로 생성된다. (`first_app/`) |
  | 마스터 세팅                 | `<MASTER_APP>/settings.py` 파일을 의미. 프로젝트 전체의 설정을 저장하는 곳. 새로운 App 을 생성하면 반드시 `INSTALLED_APPS` 에 등록해야 한다. |
  | 마스터 URL                  | `<MASTER_APP>/urls.py` 파일을 의미. 프로젝트 전체의 URL 포워딩을 담당한다. |

* 서버 실행해보기

  ```sh
  (venv)
  $ python manage.py runserver  # 프로젝트 루트에서 실행해야 한다.
  Watching for file changes with StatReloader
  Performing system checks...
  
  System check identified no issues (0 silenced).
  
  You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
  Run 'python manage.py migrate' to apply them.
  August 05, 2019 - 17:21:18
  Django version 2.2.4, using settings 'first_project.settings'
  Starting development server at http://127.0.0.1:8000/  # <= 여기로 접속해서 확인하기.
  Quit the server with CTRL-BREAK.
  ```

  

## First App

>  Django 프로젝트는 App 들의 총합이다.

* 첫 번째 App 생성하기

  ```sh
  (venv)
  $ django-admin startapp utils
  $ ls
  first_project/  utils/  manage.py  db.sqlite3 # 지금은 무시.
  ```









## Django Flow

1.  master URL (`<MASTER_APP>/urls.py`)
2. App URL (`<APP_NAME>/urls.py`)
3. App View (`<APP_NAME>/views.py`)
4. App Template(`<APP_NAME>/templates/<template>.html`)



## Routing

```python
# APP/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('URL_PATTERN', views.first_view),
    path('URL_PATTERN/<int:num>', views.second_view),
    path('URL_PATTERN/<str:word>', views.third_view),
]
```



## View

```python
# APP/views.py
from django.shortcuts import render

def first_view(request):
    return render(request, 'first_template.html')

def second_view(request, num):
    return render(request, 'second_template.html', {
        'num': num
    })

def third_view(request, word):
    return render(request, 'third_template.html', {
        'word': word.reverse()
    })
```



## Template

```html
<h1>
    {% if word == 'apple' %}
        This is Apple
    {% else %}
        This is not Apple
    {% endif %}
</h1>

<ul>
    {% for num in numbers %}
  		<li>{{ num }}</li>
	{% endfor %}
</ul>
```






















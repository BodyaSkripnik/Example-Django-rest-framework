## Installation
  1. Open terminal in root directory of the project
  2. `git clone https://github.com/BodyaSkripnik/Example-Django-rest-framework`
  3. `python -m venv venv`
  4. `source venv/bin/activate`
  5. Fill the `.env` file in root folder with corresponding credentials
  6. `cd Example-Django-rest-framework`
  7. `pip install requirements.txt`
  8. `python manage.py migrate`

## Launching
  1. Open terminal in root directory of the project
  2. `source venv/bin/activate`
  3. `cd Example-Django-rest-framework`
  4. `python manage.py runserver`

## Routes

`GET /api/v1/comments/get/` <br />
**Search for comments with nested serializers**
```
REQUEST:
  headers => {
    'Content-Type: application/json'
  }
  params => id = id_8Yn8yQT2Mk 
RESPONSE:
  data => {
        id : 'id_8Yn8yQT2Mk',
        title : 'This comment',
        created_date : '2022-07-08T11:08:42.229618+03:00',
        participant: {
            id : 'id_3Q7AHGQYEE',
            created_date : '2022-07-08T11:08:27.258639+03:00',
            name : 'Skripnik Bogdan',
            photo : 'http://127.0.0.1:8000/media/media/111_zBEsYYm.jpg'
        },
        "project": {
            id : 'id_DdC4y2Vpne',
            created_date : '2022-07-08T11:08:16.685323+03:00',
            name : 'Project',
            photo : 'http://127.0.0.1:8000/media/media/orig.webp'
        }
    }
```

`POST /api/v1/comments/post/` <br />
**Create a new comment.**
```
REQUEST:
  headers => {
    'Authorization: Bearer 846cd...'
  }
  data => {
    title : 'New comment ',
    project : 'id_DdC4y2Vpne',
    participant : 'id_3Q7AHGQYEE'
  }

RESPONSE:
  data => {
        id : "id_KVDqFR3cTP",
        title : "This comment",
        created_date : "2022-07-08T11:28:31.855884+03:00",
        participant : "id_3Q7AHGQYEE",
        project : "id_DdC4y2Vpne"
    }
  ```

`PUT /api/v1/comments/update/<str:pk>/` <br />
**Сhange a Сomment.**
```
REQUEST:
  headers => {
    'Authorization: Bearer 846cd...'
    }
  params => id = id_KVDqFR3cTP
  data => {
        title : 'This comment new',
        project :  'id_DdC4y2Vpne',
        participant : 'id_3Q7AHGQYEE'
        }
RESPONSE:
  data => {
      id : 'id_KVDqFR3cTP',
      title : 'This comment new',
      created_date : '2022-07-08T11:28:31.855884+03:00',
      participant: 'id_3Q7AHGQYEE',
      project: 'id_DdC4y2Vpne'
    }
```


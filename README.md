
`POST /api/v1/comments/post/` <br />
**Create a new comment**

REQUEST:
  headers => {
    'Authorization: Token eyJ0e...'
  }

RESPONSE:
  {
        "title": "New comment ",
        "project":  "id_DdC4y2Vpne",
        "participant": "id_3Q7AHGQYEE"
    }


`GET /api/v1/comments/get/` <br />
**Search for comments with nested serializers**

RESPONSE:
    {
        "id": "id_8Yn8yQT2Mk",
        "title": "This comment",
        "created_date": "2022-07-08T11:08:42.229618+03:00",
        "participant": {
            "id": "id_3Q7AHGQYEE",
            "created_date": "2022-07-08T11:08:27.258639+03:00",
            "name": "Participant",
            "photo": "http://127.0.0.1:8000/media/media/111_zBEsYYm.jpg"
        },
        "project": {
            "id": "id_DdC4y2Vpne",
            "created_date": "2022-07-08T11:08:16.685323+03:00",
            "name": "Name Project",
            "photo": "http://127.0.0.1:8000/media/media/orig.webp"
        }
    }

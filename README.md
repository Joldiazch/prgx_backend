# Technical assessment backend
![enter image description here](https://i.ibb.co/ssdcqMf/Captura.png)

## Challenge description
Create two endpoints using python and the backend framework of your
choice:
#### Endpoint 1:
- Receive the path for one of the pdfs attached on the mail
```
http://127.0.0.1:8000/extract?doc_path=C%3A%5CUsers%5Ctmonto01%5CPycharmProjec
ts%5Ctech_assestment%5CDoc4.pdf'
```
#### Extract from the pdf file (images) the fields:
- Vendor Name
- Fiscal Number
- Contract Number
- Start Date
- End Date
- Comments paragraph
#### Store the extracted information in the database of your choice.
#### Returns:
- True if it was successfully added to the data base
- The data base id of the row.
- The extraction information.


#### Endpoint 2:
- Receive the name of the table where the extraction is stored
```
http://127.0.0.1:8000/db_data/?table_name=EXTRACTION
````
- Returns all the extractions ordered by the newest id to the oldest


## Solution
### tech stack:
- Python
- Django
- Docker
- Postgresql
- Pytesseract (Reelevant Python module)
- pdf2image (Reelevant Python module)
- React
- MaterialUI

The solution to the challenge consisted of reading the document in the specified path and then converting the pdf into an image that is then analyzed with Pytesseract, which is an OCR (Optical Character Recognition) tool that allows us to extract the text from the image. Then, using regular expressions, an analysis of the text is performed looking for matches for the values to be extracted previously described in the **Challenge description** section.

Using the ORM (Object relational mapping) of Django we create a model that allows us to store the information extracted from the analysis described above. Then we create the requested endpoints and an extra endpoint which allows us to connect to a React application where the user through the UI can select a PDF file from anywhere on your machine and do the analysis without having to know or copy its path. These endpoints are:

- [POST] http://localhost:8000/api/extract/?doc_path={{path to file}}
- [GET] http://localhost:8000/api/db_data/
- [POST] http://localhost:8000/api/extract/file

The third and last endpoint was not requested in the challenge, however by personal conviction I found its development useful as well as a basic UI built in react that makes use of it to perform the analysis of the document. Unlike the first endpoint, this one does not receive a path with the location of the file but the file itself to be able to do the analysis. 

## Run the project:
In the root folder run
```
$ docker-compose up
```
```
$ docker exec -it prgx_backend_web_1 python manage.py migrate
```
**Great, the project is ready to run.**
You can also run some test cases with the following command:
```
$ docker exec -it prgx_backend_web_1 python manage.py test apps
```

To run the react application go to the "react-app" folder:
```
$ npm install
```
```
$ cd react-app/
```
y luego ejecutamos 
```
$ npm run dev
```

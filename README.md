# alx_travel_app_0x01

## API for Travel Listings and Bookings

### Features

- CRUD API for Listings and Bookings
- RESTful routes under `/api/`
- Swagger documentation at `/swagger/`

### Endpoints

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | /api/listings/     | List all listings   |
| POST   | /api/listings/     | Create new listing  |
| PUT    | /api/listings/{id}/| Update listing      |
| DELETE | /api/listings/{id}/| Delete listing      |
| ...    | /api/bookings/...  | Booking operations  |

### Setup

```bash
git clone https://github.com/YOUR_USERNAME/alx_travel_app_0x01.git
cd alx_travel_app_0x01
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

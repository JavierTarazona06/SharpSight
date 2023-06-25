# SharpSight
This project aims to help buyers find their cell phones at the best prices by showing all the offers on the market.

# For running the project, open the terminal and run:

  python3 -m venv .env
  
  .env\Scripts\activate
  
  pip install -r requirements.txt 
  
  uvicorn main:app --reload


# For MAC:

python3 -m venv .env

source .env/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload

# To install local requirements:

pip freeze --local > requirements.txt 

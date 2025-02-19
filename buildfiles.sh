
echo " BUILD START"
python3.12  -m pip install -r requirements.txt
pytohn3.12 maange.py collectstatic --noinput --clear 
echo " BUILD END"
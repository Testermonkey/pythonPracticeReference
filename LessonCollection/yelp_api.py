import requests

API_KEY = "XAZucIpM4DuKyOc4S9ok32e0p3j1t7-8nWBanDvz5TWpuryDohJfH500ldWPh3JmCEnH56K0fYOcP-eD0W8k2Zri_kn8OL721JSVXXAPRo04mQAAgiRDLo7N5-_hZXYx"
CLIENT_ID = "LeQTeOOFtoX1RJVgOD48Fw"


url = "https://api.yelp.com/v3/businesses/search"
header = {'Authorization': f"Bearer {API_KEY}"}
headers
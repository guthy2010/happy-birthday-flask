import pytest, os

from app.happy_birthday.models import Users
from datetime import datetime,timedelta

# Add monitoring test data
@pytest.fixture()
def datacenter_monitoring(session):
    return Users(username='bob',dateOfBirth='1991-11-11T00:00:00')

#Test data for updating
@pytest.fixture()
def sample_post_data1():
  ret = {
	"dateOfBirth" : "1991-11-11"
  }
  return ret

@pytest.fixture()
def sample_happy_birthday():
  ret = {
    "dateOfBirth" : str(datetime.today().strftime('%Y-%m-%d'))
  }
  return ret
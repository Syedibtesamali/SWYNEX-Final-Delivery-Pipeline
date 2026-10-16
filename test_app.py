from app import get_status



def test_get_status():
    assert get_status() == "SWYNEX Final Delivery Pipeline is working!"

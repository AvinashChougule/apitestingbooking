# test_restfull_bookings.py
import restfullbooker
from assertpy import assert_that


def test_bookings_for_Avi():
    resp = restfullbooker.get_bookings('Avinash')
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    for booking in resp.json():
        assert_that(resp.ok, 'HTTP Request OK').is_true()
        resp2 = restfullbooker.describe_booking(booking['bookingid'])
        assert_that(resp2.json()["firstname"], 'Firstname').contains('Mark')


def test_addbooking():
    resp = restfullbooker.add_random_booking()
    print(resp.json())
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    # TODO construct a booking to create and assert created booking against it


def test_updatebooking():
    auth_token = restfullbooker.get_authtoken()
    new_booking = restfullbooker.add_random_booking().json()['bookingid']
    resp = restfullbooker.update_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_removebooking():
    auth_token = restfullbooker.get_authtoken()
    new_booking = restfullbooker.add_random_booking().json()['bookingid']
    resp = restfullbooker.remove_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()
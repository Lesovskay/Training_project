# Андрейченко Олеся, 24-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

def test_create_order():
    track_order = sender_stand_request.get_track()
    get_order = sender_stand_request.get_order_track(track_order)
    assert get_order.status_code == 200


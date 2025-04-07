import data
import sender_stand_request


def test_order_creation_and_retrieval():
    response = sender_stand_request.create_new_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер заказа:", track_number)

    order_response = sender_stand_request.get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from littlelemonAPI.models import MenuItem
from littlelemonAPI.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Crear algunas instancias de prueba
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=150, inventory=50)
        MenuItem.objects.create(title="Pasta", price=120, inventory=60)

        self.client = APIClient()

    def test_getall(self):
        # Recuperar todos los objetos
        response = self.client.get(reverse('menu-list'))  # Ajusta el nombre de la URL si es diferente

        # Obtener todos los objetos y serializarlos
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        # Comprobar la respuesta y los datos serializados
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

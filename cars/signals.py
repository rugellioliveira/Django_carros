from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio

'''
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ###')
    print(instance)
'''

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    
    '''
    if not instance.bio:
        ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        instance.bio = ai_bio
    '''

    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente!'

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
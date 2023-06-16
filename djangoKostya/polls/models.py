from django.db import models


class Employee(models.Model):
    fullname = models.CharField(max_length=128)
    password = models.CharField(max_length=50)
    permission = models.IntegerField()


class Pallet(models.Model):
    PALLET_FULLNESS = [
        (0, "Empty"),
        (1, "Filling"),
        (2, "Full"),
    ]
    PALLET_LOCATION = [
        (0, "Storage"),
        (1, "Moving"),
        (2, "Absent"),
    ]

    barcode = models.CharField(max_length=14, unique=True)
    state = models.IntegerField(choices=PALLET_FULLNESS)
    location = models.IntegerField(choices=PALLET_LOCATION)

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = str(self.pk).zfill(14)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.barcode


class StorageUnit(models.Model):
    STORAGE_STATE = [
        (0, "Empty"),
        (1, "Filling"),
        (2, "Full"),
    ]
    STORAGE_CONDITION = [
        (0, "Freezing"),
        (1, "Expensive"),
        (2, "Regular"),
    ]

    barcode = models.CharField(max_length=8, unique=True)
    state = models.IntegerField(choices=STORAGE_STATE)
    condition = models.IntegerField(choices=STORAGE_CONDITION)
    locationX = models.IntegerField()
    locationY = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = str(self.pk).zfill(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.barcode


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Product(models.Model):
    STORAGE_CONDITION = [
        (0, "Freezing"),
        (1, "Expensive"),
        (2, "Regular"),
    ]

    sku = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    description = models.TextField()
    condition = models.IntegerField(choices=STORAGE_CONDITION)
    expire_duration = models.DurationField()

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = str(self.pk).zfill(12)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.barcode


class PalletProductLink(models.Model):
    pallet = models.ForeignKey(Pallet, to_field='barcode', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField()


class StoragePalletLink(models.Model):
    storage = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, to_field='barcode', on_delete=models.CASCADE)


class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, to_field='barcode', on_delete=models.CASCADE)
    amount = models.IntegerField()
    update_time = models.DateTimeField()


class InventoryTransactions(models.Model):
    TRANSACTIONS_TYPES = [
        (0, "Load"),
        (1, "Unload"),
        (2, "Move"),
        (3, "Display"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TRANSACTIONS_TYPES)
    date = models.DateTimeField()

# class StorageUnit(models.Model):
#     STORAGE_FULLNESS = [
#         (0, "Empty"),
#         (1, "Filling"),
#         (2, "Full"),
#     ]
#
#     barcode = models.CharField(max_length=8, primary_key=True)
#     state = models.IntegerField(choices=STORAGE_FULLNESS)
#     location = models.IntegerField()
#
#     def save(self, *args, **kwargs):
#         if not self.barcode:
#             self.barcode = str(self.pk).zfill(8)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.barcode
#
#
# class Pallet(models.Model):
#     PALLET_FULLNESS = [
#         (0, "Empty"),
#         (1, "Filling"),
#         (2, "Full"),
#     ]
#
#     barcode = models.CharField(max_length=14, unique=True)
#     location = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
#     state = models.IntegerField(choices=PALLET_FULLNESS)
#
#     def __str__(self):
#         return self.barcode

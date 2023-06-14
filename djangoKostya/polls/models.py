from django.db import models


class StorageUnit(models.Model):
    STORAGE_FULLNESS = [
        (0, "Empty"),
        (1, "Filling"),
        (2, "Full"),
    ]

    barcode = models.CharField(max_length=8, primary_key=True)
    state = models.IntegerField(choices=STORAGE_FULLNESS)
    location = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = str(self.pk).zfill(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.barcode


class Pallet(models.Model):
    PALLET_FULLNESS = [
        (0, "Empty"),
        (1, "Filling"),
        (2, "Full"),
    ]

    barcode = models.CharField(max_length=14, unique=True)
    location = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    state = models.IntegerField(choices=PALLET_FULLNESS)

    def __str__(self):
        return self.barcode


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Product(models.Model):
    sku = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    expire_date = models.DurationField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = str(self.pk).zfill(12)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.barcode


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

    type = models.IntegerField(choices=TRANSACTIONS_TYPES)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    update_date = models.DateTimeField()


class StorageItemLink(models.Model):
    storage = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
